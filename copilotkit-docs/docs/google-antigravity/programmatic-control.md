---
url: https://docs.copilotkit.ai/google-antigravity/programmatic-control/
title: Programmatic Control
method: scrapling+scrapegraph
fetched_at: 2026-11-04T10:46:25.863207+00:00
---

# Programmatic Control

> Source: https://docs.copilotkit.ai/google-antigravity/programmatic-control/

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

[Google Antigravity](https://docs.copilotkit.ai/google-antigravity)

# Programmatic Control

Drive agent runs directly from code — no chat UI required.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Programmatic control is what you reach for when you want to drive an agent run from code rather than from a chat composer: a button, a form, a cron job, a keyboard shortcut, a graph callback. CopilotKit exposes three primitives that cover every triggering pattern:

  * `agent.addMessage(...)` — append a message to the conversation without running the agent. Pair with `copilotkit.runAgent({ agent })` when you want the appended message to kick off a turn.
  * `copilotkit.runAgent({ agent })` — the same entry point `<CopilotChat />` calls under the hood. Orchestrates frontend tools, follow-up runs, and the subscriber lifecycle.
  * `agent.subscribe(subscriber)` — low-level AG-UI event subscription (`onCustomEvent`, `onRunStartedEvent`, `onRunFinalized`, `onRunFailed`, …). Pairs with `copilotkit.runAgent({ agent, resume })` for standard AG-UI interrupts, or `copilotkit.runAgent({ agent, forwardedProps: { command: { resume, interruptEvent } } })` for legacy `on_interrupt` custom events, to drive interrupt resolution from arbitrary UI.



The send-and-stop example below is intentionally self-contained. The later subscription and interrupt examples are pulled from the live `interrupt-headless` cell.

## When should I use this?#

Use programmatic control when you want to:

  * Trigger agent runs from buttons, forms, or other UI elements
  * Execute specific tools directly from UI interactions (without an LLM turn)
  * Build agent features without a chat window
  * Access agent state and results programmatically
  * Create fully custom agent-driven workflows



## Sending a message from code#

### Install the Antigravity AG-UI adapter
    
    
    pip install ag-ui-antigravity google-antigravity

### Wire the agent once — chat and code share it

`copilotkit.runAgent`, `agent.subscribe` and `agent.addMessage` drive runs against the same AG-UI endpoint your chat UI posts to, so there is no second backend to set up: build the `AntigravityAgent` the way any chat demo does and every entry point sees the same model, tools and session.

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
    
    

Sessions are keyed by `thread_id` inside the agent, so a headless run that reuses a thread continues that conversation, and a fresh `thread_id` starts a new one.

Headless interrupts come from server tools

The headless interrupt-resolver pattern — read the interrupt off the agent, answer it with a `resume` — works when a Python server tool pauses with the adapter's `experimental_interrupt()` (see the human-in-the-loop setup). The harness's own `ask_question` built-in, which would also park on an interrupt, is disabled in this showcase. For asking the user from code without a backend tool, use the frontend-tool Promise pattern: register the tool with `useFrontendTool` and an `async` handler, and resolve its promise when your own UI has the answer.

The canonical pattern is to append a user message with `agent.addMessage`, then call `copilotkit.runAgent({ agent })`. Use `copilotkit.stopAgent({ agent })` to cancel an in-flight run.

frontend/src/app/agent-trigger.tsx
    
    
    "use client";
    
    import { useAgent, useCopilotKit } from "@copilotkit/react-core/v2";
    
    export function AgentTrigger({ agentId }: { agentId: string }) {
      const { agent } = useAgent({ agentId });
      const { copilotkit } = useCopilotKit();
    
      const run = async () => {
        if (agent.isRunning) return;
    
        agent.addMessage({
          id: crypto.randomUUID(),
          role: "user",
          content: "Summarize the latest sales data",
        });
    
        try {
          await copilotkit.runAgent({ agent });
        } catch (error) {
          console.error("CopilotKit runAgent failed:", error);
        }
      };
    
      return (
        <>
          <button onClick={run} disabled={agent.isRunning}>
            Run agent
          </button>
          <button
            onClick={() => copilotkit.stopAgent({ agent })}
            disabled={!agent.isRunning}
          >
            Stop
          </button>
        </>
      );
    }

### `copilotkit.runAgent()` vs `agent.runAgent()`#

Both methods trigger the agent, but they operate at different levels:

  * **`copilotkit.runAgent({ agent })`** — the recommended default. Orchestrates the full lifecycle: executes frontend tools, handles follow-up runs, and routes errors through the subscriber system.
  * **`agent.runAgent(options)`** — low-level method on the agent instance. Sends the request to the runtime but does **not** execute frontend tools or chain follow-ups. Reach for this only when you need direct control. (For the interrupt-resume case, use `copilotkit.runAgent({ agent, resume })` for standard AG-UI interrupts, or `copilotkit.runAgent({ agent, forwardedProps: { command: { resume, interruptEvent } } })` for legacy `on_interrupt` custom events — the snippet below shows the legacy form — so the subscriber lifecycle still wraps the resumed run.)



## Subscribing to agent events#

`agent.subscribe(subscriber)` returns `{ unsubscribe }`. The subscriber object accepts every AG-UI lifecycle callback: `onCustomEvent`, `onRunStartedEvent`, `onRunFinalized`, `onRunFailed`, and the streaming deltas. Use it to drive custom progress UI, forward events to analytics, or catch framework pause/resume events and resolve them with a payload (the pattern below).

## Resolving a frontend tool call from a button#

For promise-based integrations there is no native interrupt primitive — the demo uses `useFrontendTool` with a Promise-based handler instead. The handler stages its `resolve` callback and pending payload via React state, the app surface renders the picker outside the chat, and the user's pick resolves the Promise that the agent's tool call is awaiting. Same UX, different mechanism — the agent never knows it's talking to a button grid instead of a chat picker:

Not supported on Google Antigravity

Google Antigravity doesn't support Human in the Loop: Headless Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

The resulting `{ pending, resolveActive }` pair is pure data; any UI can drive it. The cell itself renders a simple button grid, but the same pattern would power a modal, a toast, a sidebar form, or a voice UI.

## See also#

  * [Headless UI](https://docs.copilotkit.ai/headless) — the full `useRenderedMessages` composition that mirrors `<CopilotChatMessageView>` line-for-line.
  * [Human-in-the-Loop](https://docs.copilotkit.ai/human-in-the-loop) — the `useHumanInTheLoop` and `useInterrupt` hooks with their render-prop contracts, for the "paused mid-chat" pattern this page's headless variant replaces.


