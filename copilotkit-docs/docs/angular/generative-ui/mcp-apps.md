---
url: https://docs.copilotkit.ai/angular/generative-ui/mcp-apps/
title: MCP Apps
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.087666+00:00
---

# MCP Apps

> Source: https://docs.copilotkit.ai/angular/generative-ui/mcp-apps/

Open-ended

# MCP Apps

Render the interactive app resources an MCP server returns in Angular chat.

Copy MarkdownOpen

Add `provideMCPApps()` from `@copilotkit/angular/mcp-apps` when an MCP server returns an interactive app resource.

src/app/app.config.ts

Copy Text
    
    
    import { ApplicationConfig } from "@angular/core";
    import { provideCopilotKit } from "@copilotkit/angular";
    import { provideMCPApps } from "@copilotkit/angular/mcp-apps";
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({ runtimeUrl: "/api/copilotkit" }),
        provideMCPApps(),
      ],
    };

MCP resource and tool requests travel through the selected AG-UI agent. The browser provider does not take a server URL.

## Next stepsCopy Anchor Link

  * [Other generative UI paths](https://docs.copilotkit.ai/angular/generative-ui)



How is this guide?

GoodBad

[Previous PageA2UI](https://docs.copilotkit.ai/angular/generative-ui/a2ui)[Next PageOpen Generative UI](https://docs.copilotkit.ai/angular/generative-ui/open-generative-ui)
