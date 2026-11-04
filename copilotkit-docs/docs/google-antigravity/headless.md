---
url: https://docs.copilotkit.ai/google-antigravity/headless/
title: Headless UI
method: scrapling+scrapegraph
fetched_at: 2026-11-04T10:46:17.175231+00:00
---

# Headless UI

> Source: https://docs.copilotkit.ai/google-antigravity/headless/

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

# Headless UI

Build fully custom chat interfaces with complete rendering control via hooks.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Full rendering control via hooks#

CopilotKit's headless hooks give you complete control over the chat experience: you compose messages, streaming, and tool-call surfaces yourself with zero UI opinions. Bring your own design system and render everything your way.

There are two live cells on this page. Start with **Minimal** for the smallest possible custom chat on `useAgent` \+ `useCopilotKit`, then jump to **Complete** to see the full generative-UI composition (tool calls, reasoning, activity messages, custom before/after slots) rebuilt by hand from the low-level hooks.

## When should I use this?#

Use headless UI when you want to:

  * Build a completely custom chat interface with your own design system
  * Integrate agent chat into existing UI patterns
  * Have full control over message rendering and interaction
  * Drop generative UI primitives (`useRenderToolCall`, `useRenderActivityMessage`, `useRenderCustomMessages`) into a layout that isn't a chat at all



## Minimal (`headless-simple`)#

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

The bare minimum: three hooks do the heavy lifting.

  * `useAgent({ agentId })` exposes the current conversation (`messages`, `isRunning`) and the run-state object.
  * `useCopilotKit()` returns the runtime handle you call `runAgent({ agent })` on (the same entry point `<CopilotChat />` uses internally).
  * `useComponent(...)` (sugar over `useFrontendTool`) lets you register a React component the agent can render by invoking a named tool call. `useRenderToolCall()` then returns a function that paints any tool call inline.



chat.tsx
    
    
      const { agent } = useAgent({ agentId: "headless-simple" });  const { copilotkit } = useCopilotKit();  const [input, setInput] = useState("");  const send = (text: string) => {    const trimmed = text.trim();    if (!trimmed || agent.isRunning) return;    agent.addMessage({      id: crypto.randomUUID(),      role: "user",      content: trimmed,    });    setInput("");    void copilotkit.runAgent({ agent }).catch((err) => {      // The Headless Simple demo is the canonical "two hooks, your      // design system" example users copy-paste as a starting point.      // Silently swallowing errors here would model broken practice;      // log so a network failure / runtime error / transport disconnect      // surfaces in the console for the developer.      console.error("[langgraph-python:headless-simple] runAgent failed", err);    });  };

The message list is a plain `.map()` over `agent.messages`: user messages render as right-aligned bubbles, assistant messages render any streamed text plus inline tool calls via `renderToolCall({ toolCall })`:

chat.tsx
    
    
                    {visible.map((m) =>                  m.role === "user" ? (                    <UserBubble key={m.id} content={m.content} />                  ) : (                    <AssistantBubble key={m.id} content={m.content} />                  ),                )}

That's it: no `<CopilotChat />`, no `<CopilotChatMessageView>`, no slots. The downside: you only get text + tool calls. Reasoning messages, activity messages (A2UI, MCP Apps), and custom before/after slots won't show up unless you wire them in yourself, which is exactly what the next section covers.

## Complete (`headless-complete`)#

This is the heart of the page. The `headless-complete` cell rebuilds the **full** generative-UI weave (text, tool calls via `useRenderTool` / `useDefaultRenderTool` / `useComponent` / `useFrontendTool`, reasoning cards, A2UI + MCP Apps activity messages, and custom before/after message slots) from the low-level hooks directly, without importing `<CopilotChatMessageView>` or `<CopilotChatAssistantMessage>`.

### The `useRenderedMessages` hook#

The cell's central piece is a hand-rolled `useRenderedMessages(messages, isRunning)` that returns the same flat list of messages, each augmented with a `renderedContent: ReactNode` field. This hook is a **manual recreation of what`<CopilotChatMessageView>` does**; compare it line-for-line against the `renderMessageBlock` helper inside the canonical primitive: [`packages/react-core/src/v2/components/chat/CopilotChatMessageView.tsx:542-612`](https://github.com/CopilotKit/CopilotKit/blob/main/packages/react-core/src/v2/components/chat/CopilotChatMessageView.tsx#L542-L612).

message-list.tsx
    
    
      const renderToolCall = useRenderToolCall();  const { renderActivityMessage } = useRenderActivityMessage();  // Index tool results by their originating tool-call id so each tool-call  // card can hand the matching ToolMessage to `useRenderToolCall`.  // Without this the renderer can't see a result and the card stays in the  // "in-progress" state forever.  const toolMessagesByCallId = useMemo(() => {    const map = new Map<string, ToolMessage>();    for (const m of messages) {      if (m.role === "tool" && "toolCallId" in m && m.toolCallId) {        map.set(m.toolCallId, m as ToolMessage);      }    }    return map;  }, [messages]);

Three low-level hooks feed it:

  * `useRenderToolCall()` — returns the renderer for any registered tool call (per-tool via `useRenderTool` / `useComponent`, plus the wildcard from `useDefaultRenderTool`).
  * `useRenderActivityMessage()` — renders A2UI + MCP Apps activity messages for the current agent scope.
  * `useRenderCustomMessages()` — invokes `renderCustomMessage` hooks registered against the active `CopilotChatConfigurationProvider`, emitting `"before"` and `"after"` slots around every message.



### Per-role dispatch#

Inside `renderMessageContent` the role-switch mirrors `CopilotChatMessageView`'s `renderMessageBlock` exactly: assistant bodies get text + tool calls, user bodies get their text content, reasoning messages go through the `<CopilotChatReasoningMessage>` leaf component, and activity messages route through `renderActivityMessage`:

message-list.tsx
    
    
          {messages.map((m) => {        if (m.role === "user") {          // Cast through the local input shape — UserBubble accepts a          // simplified version of the ag-ui content union.          return (            <UserBubble              key={m.id}              content={m.content as Parameters<typeof UserBubble>[0]["content"]}            />          );        }        if (m.role === "assistant") {          const toolCalls =            "toolCalls" in m && Array.isArray(m.toolCalls) ? m.toolCalls : [];          return (            <AssistantBubble              key={m.id}              content={typeof m.content === "string" ? m.content : undefined}            >              {toolCalls.map((tc) => {                const toolMessage = toolMessagesByCallId.get(tc.id);                const node = renderToolCall({                  toolCall: tc,                  toolMessage,                });                return node ? <div key={tc.id}>{node}</div> : null;              })}            </AssistantBubble>          );        }        if (m.role === "activity") {          const node = renderActivityMessage(m);          if (!node) return null;          return <ActivityWrapper key={m.id}>{node}</ActivityWrapper>;        }        return null;      })}

### Tool-call composition#

For each `toolCall` on an assistant message, we look up the sibling `tool`-role message (keyed by `toolCallId`) and hand both to `renderToolCall`. This mirrors `CopilotChatToolCallsView` exactly:

message-list.tsx
    
    
                  {toolCalls.map((tc) => {                const toolMessage = toolMessagesByCallId.get(tc.id);                const node = renderToolCall({                  toolCall: tc,                  toolMessage,                });                return node ? <div key={tc.id}>{node}</div> : null;              })}

### Bubble chrome#

The `UserBubble` and `AssistantBubble` components are **pure chrome** : they receive the pre-rendered node from `useRenderedMessages` and drop it into a styled container. No chat primitives are imported here:

message-assistant.tsx
    
    
    export function AssistantBubble({  content,  children,}: {  content?: string;  children?: React.ReactNode;}) {  const hasText = typeof content === "string" && content.trim().length > 0;  const hasChildren = React.Children.count(children) > 0;  if (!hasText && !hasChildren) return null;  return (    <div      data-testid="headless-message-assistant"      data-message-role="assistant"      className="flex w-full items-start gap-3"    >      <Avatar className="h-8 w-8 shrink-0 border bg-muted text-muted-foreground">        <AvatarFallback className="bg-muted text-muted-foreground">          <Bot className="h-4 w-4" />        </AvatarFallback>      </Avatar>      <div className="flex max-w-[calc(100%-2.75rem)] flex-1 flex-col items-start gap-2">        {hasText && (          <div            className={cn(              "max-w-[90%] rounded-2xl rounded-tl-sm px-4 py-2.5 text-sm leading-relaxed shadow-sm",              "bg-muted text-foreground",            )}          >            <ReactMarkdown              remarkPlugins={[remarkGfm]}              components={{                p: ({ children }) => (                  <p className="my-1 first:mt-0 last:mb-0">{children}</p>                ),                ul: ({ children }) => (                  <ul className="my-1 list-disc pl-5">{children}</ul>                ),                ol: ({ children }) => (                  <ol className="my-1 list-decimal pl-5">{children}</ol>                ),                li: ({ children }) => <li className="my-0.5">{children}</li>,                code: ({ children, className }) => {                  const isBlock = (className ?? "").includes("language-");                  if (isBlock) {                    return <code className={className}>{children}</code>;                  }                  return (                    <code className="rounded bg-background px-1 py-0.5 font-mono text-[0.85em]">                      {children}                    </code>                  );                },                pre: ({ children }) => (                  <pre className="my-2 overflow-x-auto rounded-md bg-background p-3 font-mono text-xs">                    {children}                  </pre>                ),                a: ({ children, href }) => (                  <a                    href={href}                    target="_blank"                    rel="noreferrer noopener"                    className="text-primary underline underline-offset-2 hover:opacity-80"                  >                    {children}                  </a>                ),                strong: ({ children }) => (                  <strong className="font-semibold">{children}</strong>                ),                h1: ({ children }) => (                  <h1 className="my-2 text-base font-semibold">{children}</h1>                ),                h2: ({ children }) => (                  <h2 className="my-2 text-base font-semibold">{children}</h2>                ),                h3: ({ children }) => (                  <h3 className="my-2 text-sm font-semibold">{children}</h3>                ),                blockquote: ({ children }) => (                  <blockquote className="my-2 border-l-2 border-border pl-3 italic text-muted-foreground">                    {children}                  </blockquote>                ),              }}            >              {content as string}            </ReactMarkdown>          </div>        )}        {hasChildren && (          <div className="flex w-full max-w-full flex-col gap-2">            {children}          </div>        )}      </div>    </div>  );}export function UserBubble({  content,}: {  content: string | MultimodalPart[];}) {  const { text, attachments } = splitContent(content);  const hasText = text.trim().length > 0;  const hasAttachments = attachments.length > 0;  if (!hasText && !hasAttachments) return null;  return (    <div      data-testid="headless-message-user"      data-message-role="user"      className="flex w-full items-start gap-3 flex-row-reverse"    >      <Avatar className="h-8 w-8 shrink-0 border bg-primary text-primary-foreground">        <AvatarFallback className="bg-primary text-primary-foreground">          <User className="h-4 w-4" />        </AvatarFallback>      </Avatar>      <div className="flex max-w-[80%] flex-col items-end gap-2">        {hasAttachments && (          <div className="flex flex-wrap justify-end gap-2">            {attachments.map((a) => (              <AttachmentChip key={a.id} attachment={a} />            ))}          </div>        )}        {hasText && (          <div            className={cn(              "rounded-2xl rounded-tr-sm px-4 py-2.5 text-sm leading-relaxed shadow-sm",              "bg-primary text-primary-foreground",            )}          >            <p className="whitespace-pre-wrap break-words">{text}</p>          </div>        )}      </div>    </div>  );}function splitContent(content: string | MultimodalPart[]): {  text: string;  attachments: Attachment[];} {  if (typeof content === "string") {    return { text: content, attachments: [] };  }  let text = "";  const attachments: Attachment[] = [];  let i = 0;  for (const part of content) {    if (part.type === "text") {      text += part.text;      continue;    }    const meta = (part.metadata ?? {}) as {      filename?: string;      size?: number;    };    attachments.push({      id: `${part.type}-${i++}`,      type: part.type,      source: part.source,      filename: meta.filename,      size: meta.size,      status: "ready",    });  }  return { text, attachments };}
