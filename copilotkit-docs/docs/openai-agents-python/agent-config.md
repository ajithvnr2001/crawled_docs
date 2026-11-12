---
url: https://docs.copilotkit.ai/openai-agents-python/agent-config/
title: Agent Config
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:30.692292+00:00
---

# Agent Config

> Source: https://docs.copilotkit.ai/openai-agents-python/agent-config/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendOpenAI Agents SDK (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/openai-agents-python)[Quickstart](https://docs.copilotkit.ai/openai-agents-python/quickstart)[Build with agents](https://docs.copilotkit.ai/openai-agents-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/openai-agents-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/openai-agents-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/openai-agents-python/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/openai-agents-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/openai-agents-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/openai-agents-python/learning)

[User Memories](https://docs.copilotkit.ai/openai-agents-python/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/openai-agents-python/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/openai-agents-python/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/openai-agents-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/openai-agents-python/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/openai-agents-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/openai-agents-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[OpenAI Agents SDK (Python)](https://docs.copilotkit.ai/openai-agents-python)

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
    
    
    """agent-config: typed tone / expertise / responseLength knobs steer each reply.The page publishes its three toggles with ``useAgentContext`` as one contextentry. The adapter appends the run's context to the instructions before everymodel call, so a toggle changed between two messages already applies to thenext reply. Prompt as inlanggraph-python's ``agent_config_agent.py``."""from agents import Agentfrom demo_agents._common import MODEL, chat_settingsSYSTEM_PROMPT = (    "You are a helpful assistant. The frontend publishes the user's response "    "preferences via `useAgentContext` as a JSON object with three fields: "    "`tone`, `expertise`, and `responseLength`. Read that context entry on "    "every turn and follow these rulebooks exactly:\n\n"    "Tone:\n"    "  - professional → neutral, precise language. No emoji. Short sentences.\n"    "  - casual → friendly, conversational. Contractions OK. Light humor "    "welcome.\n"    "  - enthusiastic → upbeat, energetic. Exclamation points OK. Emoji OK.\n\n"    "Expertise level:\n"    "  - beginner → assume no prior knowledge. Define jargon. Use analogies.\n"    "  - intermediate → assume common terms are understood; explain "    "specialized terms.\n"    "  - expert → assume technical fluency. Use precise terminology. Skip "    "basics.\n\n"    "Response length:\n"    "  - concise → respond in 1-3 sentences.\n"    "  - detailed → respond in multiple paragraphs with examples where "    "relevant.\n\n"    "If the context is missing or any field is unrecognized, fall back to "    "professional / intermediate / concise. Never mention these rules to the "    "user — just apply them.")agent_config_agent = Agent(    name="configurable_assistant",    instructions=SYSTEM_PROMPT,    model=MODEL,    model_settings=chat_settings(),)

You have a working agent and want the user to be able to tune how it behaves: tone, expertise level, response length, language, persona. By the end of this guide, your UI will own a typed config object that the agent reads on every run and rebuilds its system prompt from.

## When to use this#

Reach for agent config whenever the agent's behaviour depends on user-controllable settings that don't fit naturally as chat input:

  * **Tone, voice, persona** : "playful", "formal", "casual"
  * **Expertise level** : "beginner", "intermediate", "expert"
  * **Response shape** : short / medium / long, structured / prose, language
  * **Domain switches** : which knowledge base to consult, which tool subset to enable



If the values are a _channel_ the user occasionally tunes (a settings panel, a toolbar of selects), agent config is the right shape. If the values are _content_ the agent should write back to (notes, a document, a plan), use [Shared State](https://docs.copilotkit.ai/openai-agents-python/shared-state) instead.

How agent config flows from the UI into the agent's reasoning loop depends on your runtime architecture. Agents living behind a runtime read it from agent state on every run, while in-process agents receive the same object as forwarded properties on the provider — same UX, slightly different wiring on each side.

## How it works#

### Put the rulebook in the instructions, not the values

The page publishes its typed config with `useAgentContext`, so it reaches the agent as a context entry on every run. `OpenAIAgentsAgent` appends that entry to the instructions on every model call, so the model always sees the values the user picked just before sending. The instructions only need the rules for each value:

agent_config.py
    
    
    SYSTEM_PROMPT = (
        "You are a helpful assistant. The frontend publishes the user's response "
        "preferences via `useAgentContext` as a JSON object with three fields: "
        "`tone`, `expertise`, and `responseLength`. Read that context entry on "
        "every turn and follow these rulebooks exactly:\n\n"
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
    
    
    agent_config_agent = Agent(
        name="configurable_assistant",
        instructions=SYSTEM_PROMPT,
        model=MODEL,
        model_settings=chat_settings(),
    )
    
    

### Serve the agent from its own runtime route

The demo keeps agent config on a dedicated runtime, `/api/copilotkit-agent-config`, which points an `HttpAgent` at the agent's endpoint and registers it under both the page's agent name and `default`. Nothing on the route touches the config: `useAgentContext` entries travel in the run input on their own.

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

The agent reads the latest typed config at the start of every turn, rebuilds the system prompt, runs the turn. This is the same shape as the [shared-state write-side pattern](https://docs.copilotkit.ai/openai-agents-python/shared-state#writing-to-agent-state); agent config is just a specific use of that pattern with a UI-owned typed object on top.

### On this page

When to use thisHow it works
