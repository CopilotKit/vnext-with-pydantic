"use client";

import { CopilotChat, CopilotKitProvider } from "@copilotkitnext/react";
import { PydanticAIAgent } from "@ag-ui/pydantic-ai";
import { WildCardRender } from "./WildCardRender";

export default function Home() {
  return (
    <CopilotKitProvider
      agents={{
        default: new PydanticAIAgent({
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
