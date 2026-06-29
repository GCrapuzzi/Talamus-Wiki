import { useState } from "react";
import {
  api,
  IngestPreview,
  IngestRunResult,
  ScanActionResult,
  ScanPreview,
} from "../api";

type Mode = "source" | "text" | "folder";

const MODES: { id: Mode; label: string; hint: string }[] = [
  { id: "source", label: "File / URL", hint: "Path to a file, or a URL" },
  { id: "text", label: "Paste text", hint: "Paste anything worth remembering…" },
  { id: "folder", label: "Folder", hint: "Path to a folder to scan" },
];

const panel: React.CSSProperties = {
  background: "var(--surface)",
  border: "1px solid var(--border)",
  borderRadius: "var(--radius)",
  padding: 16,
};

function Section({ children }: { children: React.ReactNode }) {
  return (
    <div
      style={{
        color: "var(--accent-2)",
        fontSize: 11,
        fontWeight: 600,
        letterSpacing: 0.8,
        textTransform: "uppercase",
        marginBottom: 8,
      }}
    >
      {children}
    </div>
  );
}

function Stat({ value, label }: { value: string; label: string }) {
  return (
    <div>
      <div style={{ fontSize: 18, fontWeight: 500 }}>{value}</div>
      <div style={{ color: "var(--muted)", fontSize: 12 }}>{label}</div>
    </div>
  );
}

function fmtBytes(n: number): string {
  if (!n) return "0 B";
  if (n < 1024) return `${n} B`;
  if (n < 1024 * 1024) return `${(n / 1024).toFixed(1)} KB`;
  return `${(n / 1024 / 1024).toFixed(1)} MB`;
}

export function Import() {
  const [mode, setMode] = useState<Mode>("source");
  const [target, setTarget] = useState("");
  const [text, setText] = useState("");
  const [ingest, setIngest] = useState<IngestPreview | null>(null);
  const [scan, setScan] = useState<ScanPreview | null>(null);
  const [result, setResult] = useState<IngestRunResult | ScanActionResult | null>(null);
  const [allowSecrets, setAllowSecrets] = useState(false);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const reset = () => {
    setIngest(null);
    setScan(null);
    setResult(null);
    setError(null);
    setAllowSecrets(false);
  };

  const pickMode = (m: Mode) => {
    setMode(m);
    reset();
  };

  const analyze = async () => {
    if (!target.trim() || busy) return;
    setBusy(true);
    reset();
    try {
      if (mode === "folder") {
        const r = await api.scanPreview(target.trim());
        if (r.success && r.data) setScan(r.data as ScanPreview);
        else setError(r.message ?? "Could not read that folder.");
      } else {
        const r = await api.importPreview(target.trim());
        if (r.success && r.data) setIngest(r.data as IngestPreview);
        else setError(r.message ?? "Could not read that source.");
      }
    } catch {
      setError("Could not reach the brain.");
    } finally {
      setBusy(false);
    }
  };

  const run = async () => {
    if (busy) return;
    setBusy(true);
    setError(null);
    try {
      if (mode === "text") {
        if (!text.trim()) return;
        const r = await api.importText(text.trim());
        if (r.success && r.data) setResult(r.data);
        else setError(r.message ?? "Import failed.");
      } else if (mode === "folder") {
        const r = await api.scanRun(target.trim(), true, allowSecrets);
        if (r.code === "scan_secrets_blocked") {
          setError(r.message ?? "Likely secrets detected — confirm to allow them.");
        } else if (r.success && r.data && "notes_written" in r.data) {
          setResult(r.data as ScanActionResult);
        } else {
          setError(r.message ?? "Scan failed.");
        }
      } else {
        const r = await api.importRun(target.trim(), true);
        if (r.success && r.data && "notes_written" in r.data) {
          setResult(r.data as IngestRunResult);
        } else {
          setError(r.message ?? "Import failed.");
        }
      }
    } catch {
      setError("Could not reach the brain.");
    } finally {
      setBusy(false);
    }
  };

  const activeHint = MODES.find((m) => m.id === mode)!.hint;

  return (
    <div style={{ maxWidth: 760 }}>
      <h2 style={{ marginTop: 0 }}>Import</h2>
      <div style={{ color: "var(--muted)", fontSize: 13, margin: "6px 0 16px" }}>
        Bring documents into your brain. Preview the cost first — nothing is written until you
        confirm.
      </div>

      <div style={{ display: "flex", gap: 6, marginBottom: 14 }}>
        {MODES.map((m) => (
          <button
            key={m.id}
            className="btn"
            onClick={() => pickMode(m.id)}
            style={{
              background: mode === m.id ? "var(--surface-2)" : "transparent",
              borderColor: mode === m.id ? "var(--accent)" : "var(--border)",
              color: mode === m.id ? "var(--text)" : "var(--muted)",
            }}
          >
            {m.label}
          </button>
        ))}
      </div>

      <div style={{ ...panel, padding: 12 }}>
        {mode === "text" ? (
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder={activeHint}
            rows={5}
            style={{
              width: "100%",
              resize: "vertical",
              background: "var(--bg)",
              color: "var(--text)",
              border: "1px solid var(--border)",
              borderRadius: 8,
              padding: "10px 12px",
              font: "inherit",
              fontSize: 14,
              lineHeight: 1.6,
            }}
          />
        ) : (
          <input
            value={target}
            onChange={(e) => setTarget(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && analyze()}
            placeholder={activeHint}
            style={{
              width: "100%",
              background: "var(--bg)",
              color: "var(--text)",
              border: "1px solid var(--border)",
              borderRadius: 8,
              padding: "10px 12px",
              font: "inherit",
              fontSize: 14,
            }}
          />
        )}
        <div style={{ marginTop: 10 }}>
          {mode === "text" ? (
            <button className="btn btn-primary" onClick={run} disabled={busy || !text.trim()}>
              {busy ? "Importing…" : "Import"}
            </button>
          ) : (
            <button className="btn btn-primary" onClick={analyze} disabled={busy || !target.trim()}>
              {busy ? "Analyzing…" : "Analyze"}
            </button>
          )}
        </div>
      </div>

      {ingest ? (
        <div style={{ ...panel, borderLeft: "3px solid var(--accent)", marginTop: 14 }}>
          <Section>Cost preview</Section>
          <div style={{ display: "flex", gap: 28, flexWrap: "wrap" }}>
            <Stat value={ingest.target_type} label="source type" />
            <Stat value={`${ingest.chunks}`} label="chunks" />
            <Stat value={`~${ingest.est_llm_calls}`} label="LLM calls" />
            <Stat value={`~${ingest.est_input_tokens.toLocaleString()}`} label="input tokens" />
          </div>
          <div style={{ color: "var(--muted)", fontSize: 13, margin: "12px 0" }}>
            Confirm to compile this source into reviewed notes. This runs the engine.
          </div>
          <button className="btn btn-primary" onClick={run} disabled={busy}>
            {busy ? "Importing…" : "Import"}
          </button>
        </div>
      ) : null}

      {scan ? (
        <div style={{ ...panel, borderLeft: "3px solid var(--accent)", marginTop: 14 }}>
          <Section>Scan preview — {scan.target_root}</Section>
          <div style={{ display: "flex", gap: 28, flexWrap: "wrap" }}>
            <Stat value={`${scan.files}`} label="files" />
            <Stat value={`${scan.skipped}`} label="skipped" />
            <Stat value={fmtBytes(scan.total_bytes)} label="size" />
            <Stat value={`~${scan.est_llm_calls}`} label="LLM calls" />
            <Stat value={`~${scan.est_tokens.toLocaleString()}`} label="tokens" />
          </div>
          {scan.secret_files.length ? (
            <div
              style={{
                ...panel,
                borderColor: "var(--danger)",
                marginTop: 12,
                padding: 12,
              }}
            >
              <div style={{ color: "var(--danger)", fontWeight: 500, fontSize: 13 }}>
                ⚠ {scan.secret_files.length} file(s) look like they contain secrets
              </div>
              <div style={{ color: "var(--muted)", fontSize: 12, marginTop: 4, wordBreak: "break-all" }}>
                {scan.secret_files.slice(0, 4).join(", ")}
              </div>
              <label style={{ display: "flex", gap: 8, alignItems: "center", marginTop: 8, fontSize: 13 }}>
                <input
                  type="checkbox"
                  checked={allowSecrets}
                  onChange={(e) => setAllowSecrets(e.target.checked)}
                />
                Import anyway (I understand these may contain secrets)
              </label>
            </div>
          ) : null}
          <div style={{ color: "var(--muted)", fontSize: 13, margin: "12px 0" }}>
            Confirm to compile {scan.files} file(s) into reviewed notes. This runs the engine.
          </div>
          <button
            className="btn btn-primary"
            onClick={run}
            disabled={busy || (scan.secret_files.length > 0 && !allowSecrets) || scan.files === 0}
          >
            {busy ? "Importing…" : `Import ${scan.files} file${scan.files === 1 ? "" : "s"}`}
          </button>
        </div>
      ) : null}

      {error ? (
        <div
          style={{ ...panel, borderColor: "var(--danger)", color: "var(--danger)", fontSize: 13, marginTop: 14 }}
        >
          {error}
        </div>
      ) : null}

      {result ? (
        <div style={{ ...panel, borderLeft: "3px solid var(--ok)", marginTop: 14 }}>
          <div style={{ color: "var(--ok)", fontWeight: 500, marginBottom: 8 }}>✓ Imported</div>
          <div style={{ display: "flex", gap: 28, flexWrap: "wrap" }}>
            <Stat value={`${result.notes_written}`} label="notes written" />
            {"files" in result && result.files != null ? (
              <Stat value={`${result.files}`} label="files" />
            ) : null}
            {"chunks" in result && result.chunks != null ? (
              <Stat value={`${result.chunks}`} label="chunks" />
            ) : null}
          </div>
          <div style={{ color: "var(--muted)", fontSize: 12.5, marginTop: 10 }}>
            New notes land in your brain — uncertain ones wait in Review.
          </div>
        </div>
      ) : null}
    </div>
  );
}
