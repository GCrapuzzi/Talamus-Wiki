import { useEffect, useState } from "react";
import { Info, X } from "@phosphor-icons/react";
import { api } from "../api";

// split YAML frontmatter (metadata) from the note body
function splitNote(md: string): { meta: string; body: string } {
  const m = md.match(/^---\n([\s\S]*?)\n---\n?/);
  if (m) return { meta: m[1].trim(), body: md.slice(m[0].length).trim() };
  return { meta: "", body: md.trim() };
}

export function Inspector({ title, onClose }: { title: string; onClose: () => void }) {
  const [md, setMd] = useState<string | null>(null);
  const [missing, setMissing] = useState(false);
  const [showMeta, setShowMeta] = useState(false);

  useEffect(() => {
    setMd(null);
    setMissing(false);
    setShowMeta(false);
    api
      .note(title)
      .then((r) => {
        if (r.data.found && r.data.markdown) setMd(r.data.markdown);
        else setMissing(true);
      })
      .catch(() => setMissing(true));
  }, [title]);

  const parsed = md ? splitNote(md) : null;
  const hasMeta = !!parsed?.meta;

  return (
    <div style={{ display: "flex", flexDirection: "column", height: "100%" }}>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 8,
          padding: "10px 12px 10px 14px",
          borderBottom: "1px solid var(--border)",
        }}
      >
        <span style={{ fontWeight: 600, flex: 1, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
          {title}
        </span>
        {hasMeta ? (
          <button
            onClick={() => setShowMeta((v) => !v)}
            title={showMeta ? "Hide metadata" : "Details / metadata"}
            aria-pressed={showMeta}
            className="icon-btn"
            style={{ color: showMeta ? "var(--accent-1)" : "var(--muted)" }}
          >
            <Info size={17} weight={showMeta ? "fill" : "regular"} />
          </button>
        ) : null}
        <button onClick={onClose} aria-label="Close" className="icon-btn" style={{ color: "var(--muted)" }}>
          <X size={16} />
        </button>
      </div>

      <div style={{ flex: 1, overflow: "auto", padding: 14, minHeight: 0 }}>
        {md === null && !missing ? (
          <div style={{ color: "var(--muted)" }}>Loading…</div>
        ) : missing ? (
          <div style={{ color: "var(--muted)" }}>Note not found.</div>
        ) : (
          <>
            {showMeta && hasMeta ? (
              <pre
                style={{
                  whiteSpace: "pre-wrap",
                  wordBreak: "break-word",
                  fontFamily: "ui-monospace, monospace",
                  fontSize: 12,
                  lineHeight: 1.55,
                  margin: "0 0 14px",
                  padding: 12,
                  color: "var(--muted)",
                  background: "var(--surface-2)",
                  border: "1px solid var(--border)",
                  borderRadius: "var(--r-sm)",
                }}
              >
                {parsed!.meta}
              </pre>
            ) : null}
            <pre
              style={{
                whiteSpace: "pre-wrap",
                wordBreak: "break-word",
                fontFamily: "inherit",
                fontSize: 13.5,
                lineHeight: 1.65,
                margin: 0,
                color: "var(--text)",
              }}
            >
              {parsed!.body || "(no content)"}
            </pre>
          </>
        )}
      </div>
    </div>
  );
}
