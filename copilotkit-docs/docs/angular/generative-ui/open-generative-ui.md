---
url: https://docs.copilotkit.ai/angular/generative-ui/open-generative-ui/
title: Open Generative UI
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:52.962576+00:00
---

# Open Generative UI

> Source: https://docs.copilotkit.ai/angular/generative-ui/open-generative-ui/

Open-ended

# Open Generative UI

Let the agent stream sandboxed HTML, CSS, and script into Angular chat, with narrow host functions.

Copy MarkdownOpen

An `openGenerativeUI` object opts the frontend into the built-in sandboxed renderer. Expose narrow host functions when generated UI must ask the application to act.

src/app/app.config.ts

Copy Text
    
    
    import { ApplicationConfig } from "@angular/core";
    import {
      provideCopilotKit,
      type SandboxFunction,
    } from "@copilotkit/angular";
    import { z } from "zod";
    
    const dashboardFilterParameters = z.object({ filter: z.string() });
    
    const setDashboardFilter: SandboxFunction = {
      name: "setDashboardFilter",
      description: "Set the active dashboard filter",
      parameters: dashboardFilterParameters,
      handler: async (args) => {
        const { filter } = dashboardFilterParameters.parse(args);
        sessionStorage.setItem("dashboard-filter", filter);
        return { applied: filter };
      },
    };
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({
          runtimeUrl: "/api/copilotkit",
          openGenerativeUI: {
            sandboxFunctions: [setDashboardFilter],
          },
        }),
      ],
    };

Generated code runs in a sandboxed iframe without same-origin access. It calls only the host functions you list in `sandboxFunctions`.

## Next stepsCopy Anchor Link

  * [Other generative UI paths](https://docs.copilotkit.ai/angular/generative-ui)



How is this guide?

GoodBad

[Previous PageMCP Apps](https://docs.copilotkit.ai/angular/generative-ui/mcp-apps)[Next PageShared State](https://docs.copilotkit.ai/angular/shared-state)
