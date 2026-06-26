import { useEffect, useRef, useState } from "react";
import { api, GraphData } from "../api";

export function Graph({ onOpenNote }: { onOpenNote?: (title: string) => void }) {
  const ref = useRef<HTMLCanvasElement>(null);
  const [g, setG] = useState<GraphData | null>(null);
  const view = useRef({ scale: 1, ox: 0, oy: 0, drag: false, px: 0, py: 0, moved: 0 });

  useEffect(() => {
    api
      .graph()
      .then((r) => setG(r.data))
      .catch(() => setG({ nodes: [], edges: [], width: 900, height: 600 }));
  }, []);

  useEffect(() => {
    const canvas = ref.current;
    if (!canvas || !g) return;
    const ctx = canvas.getContext("2d")!;
    const byId = new Map(g.nodes.map((n) => [n.id, n]));
    const xs = g.nodes.map((n) => n.x);
    const ys = g.nodes.map((n) => n.y);
    const cx = xs.length ? (Math.min(...xs) + Math.max(...xs)) / 2 : g.width / 2;
    const cy = ys.length ? (Math.min(...ys) + Math.max(...ys)) / 2 : g.height / 2;
    const tx = () => view.current.ox + canvas.width / 2 - cx * view.current.scale;
    const ty = () => view.current.oy + canvas.height / 2 - cy * view.current.scale;

    const draw = () => {
      const { scale } = view.current;
      canvas.width = canvas.clientWidth;
      canvas.height = canvas.clientHeight;
      ctx.fillStyle = "#0A0E14";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.save();
      ctx.translate(tx(), ty());
      ctx.scale(scale, scale);
      for (const e of g.edges) {
        const a = byId.get(e.source);
        const b = byId.get(e.target);
        if (!a || !b) continue;
        ctx.strokeStyle = e.typed ? "rgba(110,91,255,0.55)" : "rgba(110,91,255,0.25)";
        ctx.lineWidth = e.typed ? 1.4 : 1;
        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.lineTo(b.x, b.y);
        ctx.stroke();
      }
      for (const n of g.nodes) {
        ctx.beginPath();
        ctx.fillStyle = "rgba(110,91,255,0.18)";
        ctx.arc(n.x, n.y, n.r + 6, 0, Math.PI * 2);
        ctx.fill();
        ctx.beginPath();
        ctx.fillStyle = n.degree > 2 ? "#B7ADFF" : "#8B7BFF";
        ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = "#C9D2E0";
        ctx.font = "11px sans-serif";
        ctx.fillText(n.label, n.x + n.r + 4, n.y + 3);
      }
      ctx.restore();
    };

    const hit = (sx: number, sy: number) => {
      const wx = (sx - tx()) / view.current.scale;
      const wy = (sy - ty()) / view.current.scale;
      for (const n of g.nodes) {
        const dx = wx - n.x;
        const dy = wy - n.y;
        if (dx * dx + dy * dy <= (n.r + 6) * (n.r + 6)) return n.id;
      }
      return null;
    };

    draw();
    const ro = new ResizeObserver(() => draw());
    ro.observe(canvas);

    const onWheel = (ev: WheelEvent) => {
      ev.preventDefault();
      view.current.scale = Math.min(3, Math.max(0.3, view.current.scale * (ev.deltaY < 0 ? 1.1 : 0.9)));
      draw();
    };
    const onDown = (ev: MouseEvent) => {
      view.current.drag = true;
      view.current.moved = 0;
      view.current.px = ev.clientX;
      view.current.py = ev.clientY;
    };
    const onMove = (ev: MouseEvent) => {
      if (!view.current.drag) return;
      const dx = ev.clientX - view.current.px;
      const dy = ev.clientY - view.current.py;
      view.current.moved += Math.abs(dx) + Math.abs(dy);
      view.current.ox += dx;
      view.current.oy += dy;
      view.current.px = ev.clientX;
      view.current.py = ev.clientY;
      draw();
    };
    const onUp = (ev: MouseEvent) => {
      const wasClick = view.current.drag && view.current.moved < 5;
      view.current.drag = false;
      if (wasClick && onOpenNote) {
        const rect = canvas.getBoundingClientRect();
        const node = hit(ev.clientX - rect.left, ev.clientY - rect.top);
        if (node) onOpenNote(node);
      }
    };
    canvas.addEventListener("wheel", onWheel, { passive: false });
    canvas.addEventListener("mousedown", onDown);
    window.addEventListener("mousemove", onMove);
    window.addEventListener("mouseup", onUp);
    return () => {
      ro.disconnect();
      canvas.removeEventListener("wheel", onWheel);
      canvas.removeEventListener("mousedown", onDown);
      window.removeEventListener("mousemove", onMove);
      window.removeEventListener("mouseup", onUp);
    };
  }, [g, onOpenNote]);

  return (
    <div style={{ height: "100%", display: "flex", flexDirection: "column" }}>
      <h2 style={{ marginTop: 0 }}>Graph</h2>
      <div style={{ color: "var(--muted)", fontSize: 13, marginBottom: 10 }}>
        the most connected notes — drag to pan, wheel to zoom, click a node to open it
      </div>
      <canvas
        ref={ref}
        style={{
          flex: 1,
          width: "100%",
          border: "1px solid var(--border)",
          borderRadius: "var(--radius)",
          cursor: "grab",
          display: "block",
        }}
      />
    </div>
  );
}
