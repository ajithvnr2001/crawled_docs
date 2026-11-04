---
url: https://docs.copilotkit.ai/google-antigravity/generative-ui/mcp-apps/
title: MCP Apps
method: scrapling+scrapegraph
fetched_at: 2026-11-04T10:46:15.343817+00:00
---

# MCP Apps

> Source: https://docs.copilotkit.ai/google-antigravity/generative-ui/mcp-apps/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReact![](https://docs.copilotkit.ai/logos/google-antigravity.svg)Agent backendGoogle Antigravity

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-antigravity)[Quickstart](https://docs.copilotkit.ai/google-antigravity/quickstart)[Build with agents](https://docs.copilotkit.ai/google-antigravity/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-antigravity/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-antigravity/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

[MCP Apps](https://docs.copilotkit.ai/google-antigravity/generative-ui/mcp-apps)[Open Generative UI](https://docs.copilotkit.ai/google-antigravity/generative-ui/open-generative-ui)

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/google-antigravity/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/google-antigravity/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-antigravity/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/google-antigravity/learning)

[User Memories](https://docs.copilotkit.ai/google-antigravity/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/google-antigravity/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/google-antigravity/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/google-antigravity/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-antigravity/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/google-antigravity/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-antigravity/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

MCP Apps

Generative UIOpen-ended

# MCP Apps

Render interactive UI components from MCP servers directly in your chat interface.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

mcp_apps.py

page.tsx

route.ts
    
    
    """MCP Apps demo: the runtime supplies the Excalidraw MCP tools."""from agents._common import buildSYSTEM_PROMPT = """\You draw simple diagrams in Excalidraw via the MCP tool.SPEED MATTERS. Produce a correct-enough diagram fast; do not optimizefor polish. Target: one tool call, done in seconds.When the user asks for a diagram:1. Call `create_view` ONCE with 3-5 elements total: shapes + arrows +   an optional title text.2. Use straightforward shapes (rectangle, ellipse, diamond) with plain   `label` fields (`{"text": "...", "fontSize": 18}`) on them.3. Connect with arrows. Endpoints can be element centers or simple   coordinates — you don't need edge anchors / fixedPoint bindings.4. Include ONE `cameraUpdate` at the END of the elements array that   frames the whole diagram. Use an approved 4:3 size (600x450 or   800x600). No opening camera needed.5. Reply with ONE short sentence describing what you drew.Every element needs a unique string `id` (e.g. `"b1"`, `"a1"`,`"title"`). Standard sizes: rectangles 160x70, ellipses/diamonds120x80, 40-80px gap between shapes.Do NOT:- Call `read_me`. You already know the basic shape API.- Make multiple `create_view` calls.- Iterate or refine. Ship on the first shot.- Add decorative colors / fills / zone backgrounds unless the user  explicitly asks for them.- Add labels on arrows unless crucial.If the user asks for something specific (colors, more elements,particular layout), follow their lead — but still in ONE call."""def mcp_apps_agent():    return build(system_instructions=SYSTEM_PROMPT)

## What is this?#

MCP Apps are MCP servers that expose tools with associated UI resources. When the agent calls one of these tools, CopilotKit automatically fetches the resource and renders the UI component in the chat; no additional frontend code required.

**Free course:** See this pattern built end-to-end in [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/short-courses/build-interactive-agents-with-generative-ui/) — a free DeepLearning.AI short course taught by CopilotKit's CEO covering the full Generative UI spectrum (Controlled, Declarative, and Open-Ended).

Key benefits:

  * **Zero frontend code** — UI components are served by the MCP server
  * **Full interactivity** — components can use HTML, CSS, and JavaScript
  * **Secure sandboxing** — content runs in isolated iframes
  * **Thread persistence** — MCP Apps are stored in conversation history and restored on reconnect



## Wire the runtime to your MCP server(s)#

A single `mcpApps.servers` entry on the runtime is all it takes. The runtime auto-applies the MCP Apps middleware to every registered agent: each time an agent calls a tool backed by an MCP UI resource, the middleware fetches the resource and emits an `activity` event that the built-in `MCPAppsActivityRenderer` renders inline in the chat as a sandboxed iframe.

route.ts
    
    
        // The `mcpApps.servers` config is all you need server-side. The runtime    // auto-applies the MCP Apps middleware to every registered agent: on each    // MCP tool call it fetches the associated UI resource and emits an    // `activity` event that the built-in `MCPAppsActivityRenderer` renders    // inline in the chat.    const runtime = new CopilotRuntime({      agents: {        "mcp-apps": mcpAppsAgent,        "headless-complete": headlessCompleteAgent,      },      mcpApps: {        servers: [          {            type: "http",            url: process.env.MCP_SERVER_URL || "https://mcp.excalidraw.com/mcp",            // Always pin a stable `serverId`. Without it CopilotKit hashes the            // URL, and a URL change silently breaks restoration of persisted            // MCP Apps in prior conversation threads.            serverId: "excalidraw",          },        ],      },    });

Always pin a serverId

In production, always provide a stable `serverId`. Without it, CopilotKit hashes the server URL, and a URL change (for example between environments) silently breaks restoration of MCP Apps persisted in earlier conversation threads.

## MCP Apps with Intelligence#

The `mcpApps` option works the same way on a runtime connected to [Intelligence](https://docs.copilotkit.ai/google-antigravity/intelligence/quickstart). The two options do different jobs:

  * `mcpApps` configures the agent side. On every run, the runtime attaches the MCP Apps middleware to the agent.
  * `intelligence` replaces the runner. Intelligence stores the threads and runs, so the MCP Apps in a conversation are restored when the thread is loaded.



To move an existing MCP Apps runtime to Intelligence, keep `mcpApps` as it is. Remove `runner`, then add `intelligence` and `identifyUser`:

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import {
      BuiltInAgent,
      CopilotKitIntelligence,
      CopilotRuntime,
      createCopilotRuntimeHandler,
    } from "@copilotkit/runtime/v2";
    
    const agent = new BuiltInAgent({
      model: "openai/gpt-5.4",
      prompt: "You are a helpful assistant.",
    });
    
    const runtime = new CopilotRuntime({
      agents: { default: agent },
      // Intelligence stores threads and runs. Do not pass `runner` as well.
      intelligence: new CopilotKitIntelligence({
        apiKey: process.env.CPK_INTELLIGENCE_API_KEY!,
      }),
      // Replace this fixed user with the user from your verified session.
      identifyUser: () => ({ id: "demo-user", name: "Demo User" }),
      // Unchanged from the in-memory setup.
      mcpApps: {
        servers: [
          {
            type: "http",
            url: "https://mcp.excalidraw.com/mcp",
            serverId: "excalidraw",
          },
        ],
      },
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    export const GET = handler;
    export const POST = handler;
    export const PATCH = handler;
    export const DELETE = handler;

Keep the same `serverId` values when you move to Intelligence. The stored MCP Apps in a thread refer to the server by that ID.

To give a server to one agent only, add `agentId` to its entry in `mcpApps.servers`. On an Intelligence runtime, prefer this to attaching `MCPAppsMiddleware` to the agent yourself: the runtime then checks each request from an MCP App against the servers of that agent.

For the API key, user identity, and route protection, follow the [Intelligence quickstart](https://docs.copilotkit.ai/google-antigravity/intelligence/quickstart).

## No frontend renderer needed#

Unlike custom activity types, the MCP Apps renderer is already registered by `CopilotKit` out of the box. A plain `<CopilotChat />` is enough; no `renderActivityMessages` prop, no manual `useRenderActivityMessage` wiring.

page.tsx
    
    
      // No `renderActivityMessages`, no `useRenderActivityMessage` — the  // CopilotKitProvider auto-registers the built-in `MCPAppsActivityRenderer`  // for the "mcp-apps" activity type. A plain <CopilotChat /> is enough.  return (    <CopilotKit runtimeUrl="/api/copilotkit-mcp-apps" agent="mcp-apps">      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );

## Sandbox and widget storage#

Each MCP App runs in a sandboxed iframe with an opaque origin. A widget can't read your page's cookies, storage or DOM. It can't read responses from your APIs either, unless an API allows cross-origin requests (for example with `Access-Control-Allow-Origin: *`). It can still send requests, though, so protect state-changing endpoints against cross-site request forgery as you would for any other site. The trade-off is that the widget can't use `localStorage`, `sessionStorage`, `IndexedDB` or cookies of its own either.

Requests a widget makes that need CORS, such as `<script type="module">` and `fetch`, are sent with `Origin: null`. Serve public widget assets with `Access-Control-Allow-Origin: *`. Classic `<script src>` tags don't need CORS. To avoid CORS entirely, bundle the widget into a single HTML file, as the [ext-apps examples](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples) do with `vite-plugin-singlefile`.

The MCP Apps spec pairs `allow-same-origin` with a sandbox served from a separate origin. CopilotKit loads the sandbox inline, so it leaves `allow-same-origin` off rather than give widgets your page's origin.

If you wrote a widget yourself and it needs storage, you can restore `allow-same-origin`:
    
    
    <CopilotKit runtimeUrl="/api/copilotkit" mcpApps={{ allowSameOriginFallback: true }}>
      {children}
    </CopilotKit>

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

## Example MCP servers#

Try these open-source MCP Apps servers to get started:

  * [Excalidraw](https://mcp.excalidraw.com) — collaborative whiteboard rendered in-chat
  * [modelcontextprotocol/ext-apps](https://github.com/modelcontextprotocol/ext-apps) — canonical reference implementations



### On this page

What is this?Wire the runtime to your MCP server(s)MCP Apps with IntelligenceNo frontend renderer neededSandbox and widget storageTransport typesHTTPSSEExample MCP servers
