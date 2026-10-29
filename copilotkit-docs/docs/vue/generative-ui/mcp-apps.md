---
url: https://docs.copilotkit.ai/vue/generative-ui/mcp-apps/
title: MCP Apps
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:22.991667+00:00
---

# MCP Apps

> Source: https://docs.copilotkit.ai/vue/generative-ui/mcp-apps/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendVueAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Quickstart](https://docs.copilotkit.ai/vue)[Using these docs](https://docs.copilotkit.ai/vue/using-these-docs)[Build with agents](https://docs.copilotkit.ai/vue/build-with-agents)[Intelligence](https://docs.copilotkit.ai/vue/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/vue/frontend-tools)

Generative UI

Controlled

Open-ended

[MCP Apps](https://docs.copilotkit.ai/vue/generative-ui/mcp-apps)

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/vue/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/vue/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/vue/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/vue/learning)

[User Memories](https://docs.copilotkit.ai/vue/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/vue/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/vue/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/vue/intelligence/analytics)[Channels](https://docs.copilotkit.ai/vue/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

Other

Troubleshooting

[Community frameworks](https://docs.copilotkit.ai/vue/community-frameworks)[Reference docs](https://docs.copilotkit.ai/reference/vue)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

MCP Apps

Generative UIOpen-ended

# MCP Apps

Render interactive UI components from MCP servers directly in your chat interface.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

MCP Apps are MCP servers that expose tools with associated UI resources. When the agent calls one of these tools, CopilotKit automatically fetches the resource and renders the UI component in the chat; no additional frontend code required.

**Free course:** See this pattern built end-to-end in [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/short-courses/build-interactive-agents-with-generative-ui/) — a free DeepLearning.AI short course taught by CopilotKit's CEO covering the full Generative UI spectrum (Controlled, Declarative, and Open-Ended).

Key benefits:

  * **Zero frontend code** — UI components are served by the MCP server
  * **Full interactivity** — components can use HTML, CSS, and JavaScript
  * **Secure sandboxing** — content runs in isolated iframes
  * **Thread persistence** — MCP Apps are stored in conversation history and restored on reconnect



## Wire the runtime to your MCP server(s)#

A single `mcpApps.servers` entry on the runtime is all it takes. The runtime auto-applies the MCP Apps middleware to every registered agent: each time an agent calls a tool backed by an MCP UI resource, the middleware fetches the resource and emits an `activity` event that Vue's built-in `MCPAppsActivityRenderer` renders inline in the chat as a sandboxed iframe.

server.ts
    
    
    import { CopilotRuntime } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: { default: agent },
      mcpApps: {
        servers: [
          {
            type: "http",
            url: "https://mcp.example.com/mcp",
            serverId: "support-tools",
          },
        ],
      },
    });

Always pin a serverId

In production, always provide a stable `serverId`. Without it, CopilotKit hashes the server URL, and a URL change (for example between environments) silently breaks restoration of MCP Apps persisted in earlier conversation threads.

## No frontend renderer needed#

Unlike custom activity types, the MCP Apps renderer is already registered by `CopilotKitProvider` out of the box. A plain `<CopilotChat />` is enough; no manual renderer wiring is required.

src/App.vue
    
    
    <script setup lang="ts">
    import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <main style="height: 100dvh"><CopilotChat /></main>
      </CopilotKitProvider>
    </template>

## Sandbox and widget storage#

Each MCP App runs in a sandboxed iframe with an opaque origin. A widget can't read your page's cookies, storage or DOM. It can't read responses from your APIs either, unless an API allows cross-origin requests, for example with `Access-Control-Allow-Origin: *`. It can still send requests, so protect state-changing endpoints against cross-site request forgery as you would for any other site. The trade-off is that the widget can't use `localStorage`, `sessionStorage`, `IndexedDB` or cookies of its own either.

Requests a widget makes that need CORS, such as `<script type="module">` and `fetch`, are sent with `Origin: null`. Serve public widget assets with `Access-Control-Allow-Origin: *`. Classic `<script src>` tags don't need CORS. To avoid CORS entirely, bundle the widget into a single HTML file, as the [ext-apps examples](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples) do with `vite-plugin-singlefile`.

The MCP Apps spec pairs `allow-same-origin` with a sandbox served from a separate origin. CopilotKit loads the sandbox inline, so it leaves `allow-same-origin` off rather than give widgets your page's origin.

If you wrote a widget yourself and it needs storage, you can restore `allow-same-origin`:

Trusted widget configuration
    
    
    <script setup lang="ts">
    import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotKitProvider
        runtime-url="/api/copilotkit"
        :mcp-apps="{ allowSameOriginFallback: true }"
      >
        <CopilotChat />
      </CopilotKitProvider>
    </template>

Only for widgets you trust

With `allowSameOriginFallback`, every MCP App runs with your page's origin. Any connected MCP server's widget can then read your cookies and storage and act as the signed-in user. Don't enable it if you connect third-party MCP servers.

## Transport types#

The middleware supports two transport types:

### HTTP#

Use this format to connect to an MCP server that accepts standard HTTP requests:
    
    
    {
      type: "http",
      url: "http://localhost:3101/mcp",
      serverId: "my-http-server"
    }

### SSE#

Use this format to connect to an MCP server that streams events over a persistent connection:
    
    
    {
      type: "sse",
      url: "https://mcp.example.com/sse",
      headers: {
        "Authorization": "Bearer token"
      },
      serverId: "my-sse-server"
    }

Keep credentials on the runtime; do not expose private MCP tokens in Vue code.

## Example MCP servers#

Try these open-source MCP Apps servers to get started:

  * [Excalidraw](https://mcp.excalidraw.com) — collaborative whiteboard rendered in-chat
  * [modelcontextprotocol/ext-apps](https://github.com/modelcontextprotocol/ext-apps) — canonical reference implementations



## Choose your AI backend

See [Integrations](https://ssr-placeholder.invalid//integrations) for all available frameworks (generative-ui/mcp-apps).

### On this page

What is this?Wire the runtime to your MCP server(s)No frontend renderer neededSandbox and widget storageTransport typesHTTPSSEExample MCP servers
