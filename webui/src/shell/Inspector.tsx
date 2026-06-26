import { useEffect, useState } from "react";
import { api } from "../api";

export function Inspector({ title, onClose }: { title: string; onClose: () => void }) {
  const [md, setMd] = useState<string | null>(null);
  const [missing, setMissing] = useState(false);
  useEffect(() => {
    setMd(null);
    setMissing(false);
    api
      .note(title)
      .then((r) => {
        if (r.data.found && r.data.markdown) setMd(r.data.markdown);
        else setMissing(true);
      })
      .catch(() => setMissing(true));
  }, [title]);
  return (
    <div style={{ display: "flex", flexDirection: "column", height: "100%" }}>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          padding: "10px 14px",
          borderBottom: "1px solid var(--border)",
        }}
      >
        <span style={{ fontWeight: 500 }}>{title}</span>
        <button
          onClick={onClose}
          aria-label="Close"
          style={{
            background: "transparent",
            color: "var(--muted)",
            border: "none",
            cursor: "pointer",
            fontSize: 16,
          }}
        >
          ✕
        </button>
      </div>
      <div style={{ flex: 1, overflow: "auto", padding: 14 }}>
        {md === null && !missing ? (
          <div style={{ color: "var(--muted)" }}>Loading…</div>
        ) : missing ? (
          <div style={{ color: "var(--muted)" }}>Note not found.</div>
        ) : (
          <pre
            style={{
              whiteSpace: "pre-wrap",
              wordBreak: "break-word",
              fontFamily: "inherit",
              fontSize: 13,
              lineHeight: 1.6,
              margin: 0,
              color: "var(--text)",
            }}
          >
            {md}
          </pre>
        )}
      </div>
    </div>
  );
}
