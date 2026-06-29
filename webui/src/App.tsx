import "./theme.css";
import { useEffect, useState } from "react";
import { api, ActiveBrain, ServiceResult } from "./api";
import { Shell } from "./shell/Shell";
import { Inspector } from "./shell/Inspector";
import { Home } from "./views/Home";
import { Ask } from "./views/Ask";
import { Graph } from "./views/Graph";
import { Library } from "./views/Library";
import { Import } from "./views/Import";
import { Ontology } from "./views/Ontology";
import { Review } from "./views/Review";
import { Brains } from "./views/Brains";
import { System } from "./views/System";

export default function App() {
  const [note, setNote] = useState<string | null>(null);
  const [active, setActive] = useState<ActiveBrain | null>(null);

  useEffect(() => {
    api
      .getActive()
      .then((r) => setActive(r.data))
      .catch(() => setActive(null));
  }, []);

  const switchBrain = async (
    body: { name?: string; path?: string },
  ): Promise<ServiceResult<ActiveBrain>> => {
    const r = await api.setActiveBrain(body);
    if (r.success) window.location.reload(); // re-point every view at the new brain
    return r;
  };

  return (
    <Shell
      activeBrain={active}
      views={{
        home: <Home />,
        ask: <Ask onOpenNote={setNote} />,
        graph: <Graph onOpenNote={setNote} />,
        library: <Library />,
        import: <Import />,
        ontology: <Ontology />,
        review: <Review onOpenNote={setNote} />,
        brains: <Brains active={active} onSwitch={switchBrain} />,
        system: <System />,
      }}
      inspector={note ? <Inspector title={note} onClose={() => setNote(null)} /> : null}
    />
  );
}
