"use client";

import { CopilotChat, CopilotKitProvider } from "@copilotkitnext/react";
import { PydanticAIAgent } from "@ag-ui/pydantic-ai";
import { WildCardRender } from "./WildCardRender";

export default function Home() {
  const agentUrl =
    typeof window === "undefined" ? "/api" : `${window.location.origin}/api`;

  return (
    <CopilotKitProvider
      agents={{
        default: new PydanticAIAgent({
          url: agentUrl,
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
