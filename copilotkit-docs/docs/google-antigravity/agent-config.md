---
url: https://docs.copilotkit.ai/google-antigravity/agent-config/
title: Agent Config
method: scrapling+scrapegraph
fetched_at: 2026-11-04T10:45:55.475108+00:00
---

# Agent Config

> Source: https://docs.copilotkit.ai/google-antigravity/agent-config/

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

On this page

[Google Antigravity](https://docs.copilotkit.ai/google-antigravity)

# Agent Config

Forward typed configuration from your UI into the agent's reasoning loop.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent_config.py

page.tsx

config-card.tsx

use-agent-config.ts

config-types.ts

route.ts
    
    
    """agent-config: typed tone / expertise / responseLength knobs steer each reply.The page publishes its three toggles with ``useAgentContext`` as one contextentry, which reaches the agent as ``RunAgentInput.context``. langgraph-pythonlets ``CopilotKitMiddleware`` fold that entry into the prompt on every turn.Antigravity fixes the instructions when the harness session starts, and theadapter forwards only user messages, so the rulebook below is static and themodel reads the current values itself through the adapter's silent built-in``get_app_context()`` tool. The user can change a toggle between any twomessages, which is why the prompt asks for a fresh read every turn."""from agents._common import build# Rulebooks as in langgraph-python's agent_config_agent.py; only the first# sentence differs, because the model has to ask for the context.SYSTEM_PROMPT = (    "You are a helpful assistant. The app publishes the user's response "    "preferences as a JSON object with three fields: `tone`, `expertise`, "    "and `responseLength`. Call `get_app_context` at the start of EVERY turn "    "to read the current values (the user can change them between "    "messages), then follow these rulebooks exactly:\n\n"    "Tone:\n"    "  - professional → neutral, precise language. No emoji. Short sentences.\n"    "  - casual → friendly, conversational. Contractions OK. Light humor "    "welcome.\n"    "  - enthusiastic → upbeat, energetic. Exclamation points OK. Emoji OK.\n\n"    "Expertise level:\n"    "  - beginner → assume no prior knowledge. Define jargon. Use analogies.\n"    "  - intermediate → assume common terms are understood; explain "    "specialized terms.\n"    "  - expert → assume technical fluency. Use precise terminology. Skip "    "basics.\n\n"    "Response length:\n"    "  - concise → respond in 1-3 sentences.\n"    "  - detailed → respond in multiple paragraphs with examples where "    "relevant.\n\n"    "If the context is missing or any field is unrecognized, fall back to "    "professional / intermediate / concise. Never mention these rules to the "    "user — just apply them.")def agent_config_agent():    return build(system_instructions=SYSTEM_PROMPT, experimental_app_context=True)

You have a working agent and want the user to be able to tune how it behaves: tone, expertise level, response length, language, persona. By the end of this guide, your UI will own a typed config object that the agent reads on every run and rebuilds its system prompt from.

## When to use this#

Reach for agent config whenever the agent's behaviour depends on user-controllable settings that don't fit naturally as chat input:

  * **Tone, voice, persona** : "playful", "formal", "casual"
  * **Expertise level** : "beginner", "intermediate", "expert"
  * **Response shape** : short / medium / long, structured / prose, language
  * **Domain switches** : which knowledge base to consult, which tool subset to enable



If the values are a _channel_ the user occasionally tunes (a settings panel, a toolbar of selects), agent config is the right shape. If the values are _content_ the agent should write back to (notes, a document, a plan), use [Shared State](https://docs.copilotkit.ai/google-antigravity/shared-state) instead.

How agent config flows from the UI into the agent's reasoning loop depends on your runtime architecture. Agents living behind a runtime read it from agent state on every run, while in-process agents receive the same object as forwarded properties on the provider — same UX, slightly different wiring on each side.

## How it works#

### Put the rulebook in the instructions, not the values

The page publishes its typed config with `useAgentContext`, so it reaches the agent as a context entry on every run. Antigravity sets an agent's instructions once, when the harness session starts, so the system prompt cannot be rebuilt from the config on each turn. Write one static prompt that covers every value instead, and have the model read the current values itself through the adapter's built-in `get_app_context()` tool, which `experimental_app_context=True` turns on:

agent_config.py
    
    
    SYSTEM_PROMPT = (
        "You are a helpful assistant. The app publishes the user's response "
        "preferences as a JSON object with three fields: `tone`, `expertise`, "
        "and `responseLength`. Call `get_app_context` at the start of EVERY turn "
        "to read the current values (the user can change them between "
        "messages), then follow these rulebooks exactly:\n\n"
        "Tone:\n"
        "  - professional → neutral, precise language. No emoji. Short sentences.\n"
        "  - casual → friendly, conversational. Contractions OK. Light humor "
        "welcome.\n"
        "  - enthusiastic → upbeat, energetic. Exclamation points OK. Emoji OK.\n\n"
        "Expertise level:\n"
        "  - beginner → assume no prior knowledge. Define jargon. Use analogies.\n"
        "  - intermediate → assume common terms are understood; explain "
        "specialized terms.\n"
        "  - expert → assume technical fluency. Use precise terminology. Skip "
        "basics.\n\n"
        "Response length:\n"
        "  - concise → respond in 1-3 sentences.\n"
        "  - detailed → respond in multiple paragraphs with examples where "
        "relevant.\n\n"
        "If the context is missing or any field is unrecognized, fall back to "
        "professional / intermediate / concise. Never mention these rules to the "
        "user — just apply them."
    )
    
    
    def agent_config_agent():
        return build(system_instructions=SYSTEM_PROMPT, experimental_app_context=True)
    
    

`get_app_context()` returns the current run's context entries as `{"description", "value"}` objects, so the model sees the value the user selected just before sending. The tool is silent: no tool card appears in the chat.

### Serve the agent from its own runtime route

The demo keeps agent config on a dedicated runtime, `/api/copilotkit-agent-config`, that points an `HttpAgent` at the agent's endpoint and registers it under both the page's agent name and `default`. Nothing on the route touches the config: `useAgentContext` entries travel in the run input on their own.

Ask for a fresh read every turn

The user can change a setting between any two messages. Tell the model to call `get_app_context` at the start of every turn, not once per conversation. Otherwise it keeps applying the values it read first.

Agent config is a typed object the frontend owns and publishes to the agent as runtime context. The backend reads that context entry and turns it into a system prompt.

Hold the typed config in React state, then mirror every change into the agent through `useAgentContext`:

frontend/src/app/page.tsx — UI publishes the typed config
    
    
    function ConfigContextRelay({ config }: { config: AgentConfig }) {
      useAgentContext({
        description: "Agent response preferences",
        value: {
          tone: config.tone,
          expertise: config.expertise,
          responseLength: config.responseLength,
        },
      });
      return null;
    }

The framework setup above shows the exact backend bridge for the selected agent. In every framework, the flow is the same: read the latest valid context from the current run and use it to build the system prompt for that turn.

Backend flow
    
    
    config = latestValidConfig(currentRun.context)
    systemPrompt = buildSystemPrompt(config)
    model.invoke(systemPrompt, currentUserRequest)

The agent reads the latest typed config at the start of every turn, rebuilds the system prompt, runs the turn. This is the same shape as the [shared-state write-side pattern](https://docs.copilotkit.ai/google-antigravity/shared-state#writing-to-agent-state); agent config is just a specific use of that pattern with a UI-owned typed object on top.

### On this page

When to use thisHow it works
