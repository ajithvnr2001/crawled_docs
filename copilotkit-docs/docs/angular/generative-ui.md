---
url: https://docs.copilotkit.ai/angular/generative-ui/
title: Generative UI
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.154884+00:00
---

# Generative UI

> Source: https://docs.copilotkit.ai/angular/generative-ui/

# Generative UI

Choose how your Angular app renders agent-driven UI, from your own components to A2UI, Open Generative UI, and MCP Apps.

Copy MarkdownOpen

Generative UI lets an agent show UI in chat, not only text. Angular supports several paths. Pick the one that fits your agent, then follow its page.

## Choose a generative UI pathCopy Anchor Link

Path| Best fit| Angular setup  
---|---|---  
[Your components, display only](https://docs.copilotkit.ai/angular/generative-ui/tool-based)| The agent should show a component and nothing else runs| `registerComponent`  
[Your components](https://docs.copilotkit.ai/angular/generative-ui/tool-rendering)| Known data shapes and application actions| `registerFrontendTool` or `registerRenderToolCall` with a component  
[A2UI](https://docs.copilotkit.ai/angular/generative-ui/a2ui)| A server emits A2UI operations or snapshots| Set `a2ui.catalog` in `provideCopilotKit` to turn on the built-in renderer; without a catalog A2UI stays off  
[Open Generative UI](https://docs.copilotkit.ai/angular/generative-ui/open-generative-ui)| The agent produces streamed HTML, CSS, and script expressions| Set `openGenerativeUI` in `provideCopilotKit`  
[MCP Apps](https://docs.copilotkit.ai/angular/generative-ui/mcp-apps)| An MCP server returns an interactive app resource| Add `provideMCPApps()` from `@copilotkit/angular/mcp-apps`  
  
## Next stepsCopy Anchor Link

  * [Activity renderers](https://docs.copilotkit.ai/reference/angular/functions/registerRenderActivityMessage)



How is this guide?

GoodBad

[Previous PageFrontend Tools](https://docs.copilotkit.ai/angular/frontend-tools)[Next PageComponents as Tools](https://docs.copilotkit.ai/angular/generative-ui/tool-based)
