---
url: https://docs.copilotkit.ai/angular/google-antigravity/quickstart/
title: Angular quickstart
method: scrapling+scrapegraph
fetched_at: 2026-11-04T10:45:55.411866+00:00
---

# Angular quickstart

> Source: https://docs.copilotkit.ai/angular/google-antigravity/quickstart/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngular![](https://docs.copilotkit.ai/logos/google-antigravity.svg)Agent backendGoogle Antigravity

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular/google-antigravity)[Quickstart](https://docs.copilotkit.ai/angular/google-antigravity/quickstart)[Build with agents](https://docs.copilotkit.ai/angular/google-antigravity/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/google-antigravity/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/google-antigravity/webmcp)

Agent capabilities

Angular Guides

[Sub-agents](https://docs.copilotkit.ai/angular/google-antigravity/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/google-antigravity/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/google-antigravity/learning)

[User Memories](https://docs.copilotkit.ai/angular/google-antigravity/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/angular/google-antigravity/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/angular/google-antigravity/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/angular/google-antigravity/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/google-antigravity/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

Concepts

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/google-antigravity/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/google-antigravity/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

# Angular

Connect an Angular app to Copilot Runtime with CopilotKit.

`@copilotkit/angular` provides Angular components, directives, and services for CopilotKit. This guide gets you to a working Angular app with a chat UI backed by [Copilot Runtime](https://docs.copilotkit.ai/angular/google-antigravity/backend/copilot-runtime). When you select an agent backend in the sidebar, the backend step below changes with it; without a selection, the guide uses CopilotKit's `BuiltInAgent`.

The runtime runs on your server, keeps model credentials out of the browser, and exposes the `default` agent that `CopilotChat` uses automatically.

[Take your Angular copilot from local to productionAdd threads, inspection, and cloud-hosted or self-hosted CopilotKit Intelligence without changing the Angular frontend APIs in this guide.Get CopilotKit Intelligence free](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs%3Aangular%2Fquickstart%3Aproduction&utm_frontend=angular&utm_backend=google-antigravity)

## Start with your coding agent#

Use this prompt to connect your Angular app to Copilot Runtime with the selected agent backend, then verify a working conversation. You can also follow the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is CopilotKit for Angular?#

CopilotKit for Angular is the first-party, signal-based Angular frontend for AG-UI agents and Copilot Runtime. It provides complete chat surfaces and headless APIs, and it supports zoneless applications.

## Prerequisites#

  * An OpenAI API key (or another model provider supported by [Model Selection](https://docs.copilotkit.ai/angular/model-selection))
  * Angular 22
  * Node.js 22



## Getting started#

### Create your Angular app#

If you don't have one already, pin the CLI to the supported major:
    
    
    npx @angular/cli@22 new my-copilot-app
    cd my-copilot-app

### Install CopilotKit#

Install the Angular frontend package, `@angular/cdk`, and `@copilotkit/runtime` for your local Copilot Runtime server:

npmpnpmyarn
    
    
    npm install @copilotkit/angular @angular/cdk @copilotkit/runtime
    npm install -D tsx typescript @types/node
    
    
    pnpm add @copilotkit/angular @angular/cdk @copilotkit/runtime
    pnpm add -D tsx typescript @types/node
    
    
    yarn add @copilotkit/angular @angular/cdk @copilotkit/runtime
    yarn add -D tsx typescript @types/node

Match @angular/cdk to your Angular version

`@angular/cdk` must share your Angular major version. Most package managers resolve this for you, but if you hit a peer-dependency error, pin it explicitly (for example `@angular/cdk@^22`).

### Connect the selected agent backend#

This URL keeps the agent backend selected. The Angular setup remains shared; the backend setup below comes from that integration's canonical showcase source.

An Antigravity agent is an `AntigravityAgent` from `ag_ui_antigravity`. You give it a Gemini model and its API key, the `workspaces` it may touch on disk, and a `save_dir` for its conversation trajectories. To send the model calls somewhere other than Google's API, pass an `endpoint`: the SDK's `GeminiAPIEndpoint(base_url=..., http_headers=...)`. The showcase does that to replay aimock fixtures, and the headers ride on every call the harness makes. Antigravity is session-based rather than a stateless graph — the SDK drives a bundled Go `localharness` subprocess — so the session knobs belong here too.

_common.py
    
    
    def api_key() -> str | None:
        """The Gemini API key.
    
        ``GEMINI_API_KEY`` is the only name the Antigravity SDK reads. The showcase
        fleet exports ``GOOGLE_API_KEY`` for its Gemini integrations, so accept
        that too rather than fail on the first model call.
        """
        return os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    
    
    def gemini_base_url() -> str | None:
        """The Gemini-compatible server to call instead of Google's API.
    
        Showcase compose sets ``GOOGLE_GEMINI_BASE_URL=http://aimock:4010``, the
        same variable the google-adk integration reads.
        """
        return os.environ.get("GOOGLE_GEMINI_BASE_URL", "").rstrip("/") or None
    
    
    def aimock_headers() -> dict[str, str]:
        """Headers for a model call: the package's fixture context plus the
        current request's mock and diagnostic headers.
    
        ``X-AIMock-Context`` is fixed: it selects this package's fixtures whatever
        the request says. The rest comes from the inbound request (captured by
        ``HeaderForwardingHTTPMiddleware``) and is forwarded only when present, so
        ordinary demo traffic is never forced into strict mode.
        """
        forwarded = {
            k: v
            for k, v in get_forwarded_headers().items()
            if k.startswith(_FORWARDED_PREFIXES)
        }
        return {**forwarded, "x-aimock-context": SLUG}
    
    
    def endpoint() -> GeminiAPIEndpoint | None:
        """Where every model call goes: aimock under compose, Google's API otherwise.
    
        Passed to the adapter as a callable, so it runs each time a session is
        built, inside that conversation's first request. The harness makes the
        model calls itself, so headers can only reach them on the endpoint: the
        request's ``X-AIMock-Strict`` and ``x-test-id``/``x-diag-*`` ride along
        from here (PNI-576). They are fixed per conversation, because the SDK
        sets a conversation's model configuration when it starts.
        """
        base_url = gemini_base_url()
        if base_url is None:
            return None
        return GeminiAPIEndpoint(
            base_url=base_url,
            api_key=api_key(),
            http_headers=aimock_headers(),
        )
    
    
    def chat_only_capabilities() -> CapabilitiesConfig:
        """Only ``finish`` stays enabled.
    
        ``search_web`` returns an empty summary without Google credentials and the
        model retries it forever; ``ask_question`` would park on an interrupt the
        CopilotKit demos never answer. ``finish`` is how the harness ends a turn.
        """
        return CapabilitiesConfig(
            enabled_tools=[BuiltinTools.FINISH], enable_subagents=False
        )
    
    
    _DIRS_READY = False
    
    
    def _ensure_dirs() -> None:
        """Creates the workspace / save_dir once, on first agent construction.
    
        Deliberately NOT done at import time: the defaults live under ``/data``,
        which only exists inside the container image, so an import-time
        ``os.makedirs`` blows up on a developer machine (read-only ``/`` on macOS)
        and takes every ``import agent_server`` — including the package's pytest
        suite — down with it.
        """
        global _DIRS_READY
        if _DIRS_READY:
            return
        os.makedirs(WORKSPACE, exist_ok=True)
        os.makedirs(SAVE_DIR, exist_ok=True)
        _DIRS_READY = True
    
    
    _POOL = None
    
    
    def shared_pool():
        """One HarnessPool for the whole server: one Go process, not one per agent."""
        global _POOL
        if _POOL is None:
            from ag_ui_antigravity.harness_pool import HarnessPool
    
            _POOL = HarnessPool()
        return _POOL
    
    
    def build(**kwargs):
        """Creates an AntigravityAgent with the package defaults applied."""
        from ag_ui_antigravity import AntigravityAgent
    
        _ensure_dirs()
    
        defaults = dict(
            model=MODEL,
            api_key=api_key(),
            endpoint=endpoint,
            workspaces=[WORKSPACE],
            save_dir=SAVE_DIR,
            harness_pool=shared_pool(),
            capabilities=chat_only_capabilities(),
            session_timeout_seconds=SESSION_TIMEOUT_SECONDS,
            max_sessions=MAX_SESSIONS,
            max_tool_calls_per_turn=MAX_TOOL_CALLS_PER_TURN,
        )
        defaults.update(kwargs)
        return AntigravityAgent(**defaults)
    
    

Nothing about CopilotKit is configured on the agent: every tool the browser registers arrives with each run in `RunAgentInput.tools`, and the adapter rebuilds those as custom Antigravity tools for that turn, so a call the browser has to answer parks as an awaited coroutine until the answer arrives on a later run. Handing every agent the same `harness_pool` **and** the same `save_dir` is what keeps one Go harness process behind the whole server instead of one per agent — `save_dir` is half the pool's partition key, so passing the pool alone changes nothing.

`create_antigravity_app` (also from `ag_ui_antigravity`) turns a `{name: agent}` mapping into a FastAPI app with one AG-UI endpoint per name, mounted at `/<name>`:

agent_server.py
    
    
    AGENT_REGISTRY = build_registry()
    app = create_antigravity_app(AGENT_REGISTRY)
    app.title = "Google Antigravity Agent Server"

Pass a single agent instead of a mapping to mount it at `/`. Then point Copilot Runtime at `http://localhost:8000/<agent name>`.

Install the SDK
    
    
    pip install ag-ui-antigravity google-antigravity

`google-antigravity` ships platform wheels that bundle the `localharness` binary, so there is no separate download step.

Expose the selected backend through Copilot Runtime

Configure Copilot Runtime to register this backend as the `default` agent at `/api/copilotkit`. Continue with the selected backend's [Copilot Runtime guide](https://docs.copilotkit.ai/backend/copilot-runtime) for its runtime adapter, credentials, and server command. Do not replace it with the `BuiltInAgent` server from the standalone Angular path.

### Import the styles#

Add the package stylesheet to your global styles. It's self-contained, so the chat renders without any other CSS.

src/styles.css
    
    
    @import "@copilotkit/angular/styles.css"; 

### Connect to Copilot Runtime#

Point `provideCopilotKit` at the runtime endpoint. The chat uses the agent that your runtime registers as `default`.

src/app/app.config.ts
    
    
    import { ApplicationConfig } from "@angular/core";
    import { provideCopilotKit } from "@copilotkit/angular"; 
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({
          runtimeUrl: "http://localhost:8200/api/copilotkit",
        }),
      ],
    };

### Add the chat UI#

Import the `CopilotChat` component into your root component and drop it into the template.

src/app/app.ts
    
    
    import { Component } from "@angular/core";
    import { CopilotChat } from "@copilotkit/angular"; 
    
    @Component({
      selector: "app-root",
      imports: [CopilotChat], 
      template: `
        <div style="height: 100vh">
          <copilot-chat />
        </div>
      `,
    })
    export class App {}

### Run the backend, runtime, and Angular app#

Start the selected agent backend and Copilot Runtime with the commands from its runtime guide. Confirm `http://localhost:8200/api/copilotkit/info` reports the `default` agent, then start Angular:
    
    
    npm start

Open the Angular CLI URL (usually `http://localhost:4200`) and send a message. The request now follows the selected path end to end: Angular → Copilot Runtime → your selected agent backend.

### Open Inspector and confirm setup#

On localhost, click the Inspector button in the corner of the app.

  1. Open **Agents** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Agents** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with Enable Intelligence (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/angular/google-antigravity/inspector).

## Next steps#

  * [Runtime and backend docs](https://docs.copilotkit.ai/backend/copilot-runtime): configure the server, secure requests, and deploy without leaving the selected Angular surface.
  * [CopilotKit Intelligence](https://docs.copilotkit.ai/intelligence/overview): add threads, inspection, and cloud-hosted or self-hosted operations.
  * [Angular task guides](https://docs.copilotkit.ai/guides/chat-ui): build chat UI, tools, generative UI, interrupts, shared state, threads, memory, attachments, and headless UI.
  * [Angular feature examples](https://docs.copilotkit.ai/features): find runnable examples and canonical shared Angular source for each supported feature.
  * [Angular API reference](https://docs.copilotkit.ai/reference/angular): use components, signals, tools, context, and runtime services.
  * [Production and lifecycle](https://docs.copilotkit.ai/reference/angular/production-lifecycle): handle cleanup, errors, server rendering, hydration, zoneless Angular, and browser-only features.


