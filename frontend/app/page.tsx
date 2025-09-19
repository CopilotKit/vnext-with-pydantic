"use client";

import { CopilotChat, CopilotKitProvider } from "@copilotkitnext/react";
import { HttpAgent } from "@ag-ui/client";
import { WildCardRender } from "./WildCardRender";

export default function Home() {
  return (
    <CopilotKitProvider
      agents={{
        default: new HttpAgent({
          url: "http://localhost:8000",
        }),
      }}
      renderToolCalls={[WildCardRender]}
    >
      <div
        style={{ height: "100vh", margin: 0, padding: 0, overflow: "hidden" }}
      >
        <CopilotChat />
      </div>
    </CopilotKitProvider>
  );
}
