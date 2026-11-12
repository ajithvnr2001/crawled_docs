---
url: https://docs.copilotkit.ai/openai-agents-python/multi-agent/subagents/
title: Sub-Agents
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:45.938884+00:00
---

# Sub-Agents

> Source: https://docs.copilotkit.ai/openai-agents-python/multi-agent/subagents/

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

Agent capabilities

# Sub-Agents

Decompose work across multiple specialized agents with a visible delegation log.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

subagents.py

page.tsx

delegation-log.tsx

route.ts
    
    
    """Sub-agents as tools, as in langgraph-python's subagents.py.The supervisor delegates to three Agents SDK agents (research, writing,critique). Each delegation tool runs its sub-agent with ``Runner.run`` (onemodel call, the task as the only user message), appends an entry to the``delegations`` slot of shared state and returns the sub-agent's output.``shared_state().update`` streams a STATE_SNAPSHOT as each delegation finishes, sothe page's delegation log fills in while the supervisor is still running,the same way the reference's ``Command(update={"delegations": [...]})``does.``Agent.as_tool()`` would run the sub-agents too, but it cannot record thedelegation, so the tools are spelled out."""import uuidfrom ag_ui_openai_agents import shared_statefrom agents import Agent, Runner, function_toolfrom demo_agents._common import MODEL, chat_settingsSUPERVISOR_PROMPT = (    "You are a supervisor. For research tasks call `research_agent`, for "    "drafting call `writing_agent`, for review call `critique_agent`. "    "Delegate step by step: research first, then write, then critique once, "    "then answer the user with the final draft.")SUB_AGENTS = {    "research_agent": Agent(        name="research_agent",        model=MODEL,        model_settings=chat_settings(),        instructions=(            "You are a research sub-agent. Given a topic, produce a concise "            "bulleted list of 3-5 key facts. No preamble, no closing."        ),    ),    "writing_agent": Agent(        name="writing_agent",        model=MODEL,        model_settings=chat_settings(),        instructions=(            "You are a writing sub-agent. Given a brief and optional source "            "facts, produce a polished 1-paragraph draft. Be clear and "            "concrete. No preamble."        ),    ),    "critique_agent": Agent(        name="critique_agent",        model=MODEL,        model_settings=chat_settings(),        instructions=(            "You are an editorial critique sub-agent. Given a draft, give 2-3 "            "crisp, actionable critiques. No preamble."        ),    ),}SUB_AGENT_EMPTY_SENTINEL = "<sub-agent produced no output>"async def _delegate(role: str, task: str) -> str:    result = await Runner.run(SUB_AGENTS[role], task)    output = str(result.final_output or "").strip() or SUB_AGENT_EMPTY_SENTINEL    # Read and write with no await in between, so delegations the model makes    # in parallel cannot drop each other's entry.    state = shared_state()    delegations = list(state.value.get("delegations") or [])    delegations.append(        {            "id": str(uuid.uuid4()),            "sub_agent": role,            "task": task,            "status": "completed",            "result": output,        }    )    state.update(delegations=delegations)    return output@function_toolasync def research_agent(task: str) -> str:    """Delegate a research task; returns 3-5 key facts."""    return await _delegate("research_agent", task)@function_toolasync def writing_agent(task: str) -> str:    """Delegate a drafting task; returns a one-paragraph draft."""    return await _delegate("writing_agent", task)@function_toolasync def critique_agent(task: str) -> str:    """Delegate a review task; returns 2-3 critiques."""    return await _delegate("critique_agent", task)subagents_agent = Agent(    name="supervisor",    instructions=SUPERVISOR_PROMPT,    model=MODEL,    # Research, then write, then critique: one delegation per model call.    model_settings=chat_settings(parallel_tool_calls=False),    tools=[research_agent, writing_agent, critique_agent],)

## What is this?#

Sub-agents are the canonical multi-agent pattern: a top-level **supervisor** LLM orchestrates one or more specialized **sub-agents** by exposing each of them as a tool. The supervisor decides what to delegate, the sub-agents do their narrow job, and their results flow back up to the supervisor's next step.

This is fundamentally the same shape as tool-calling, but each "tool" is itself a full-blown agent with its own system prompt and (often) its own tools, memory, and model.

## When should I use this?#

Reach for sub-agents when a task has distinct specialized sub-tasks that each benefit from their own focus:

  * **Research → Write → Critique** pipelines, where each stage needs a different system prompt and temperature.
  * **Router + specialists** , where one agent classifies the request and dispatches to the right expert.
  * **Divide-and-conquer** — any problem that fits cleanly into parallel or sequential sub-problems.



The example below uses the Research → Write → Critique shape as the canonical example.

## Setting up sub-agents#

### Install the OpenAI Agents AG-UI adapter
    
    
    pip install ag-ui-openai-agents openai-agents

### Give the supervisor one tool per sub-agent

Each sub-agent is its own SDK `Agent` with a role prompt. The supervisor reaches it through an `async` function tool that runs the sub-agent with `Runner.run` and returns its final output. The supervisor's instructions decide the order. Every delegation is an ordinary tool call, so the adapter streams the `TOOL_CALL_*` events the UI renders its per-delegation cards from.

subagents.py
    
    
    import uuid
    
    from ag_ui_openai_agents import shared_state
    from agents import Agent, Runner, function_tool
    
    from demo_agents._common import MODEL, chat_settings
    
    SUPERVISOR_PROMPT = (
        "You are a supervisor. For research tasks call `research_agent`, for "
        "drafting call `writing_agent`, for review call `critique_agent`. "
        "Delegate step by step: research first, then write, then critique once, "
        "then answer the user with the final draft."
    )
    
    SUB_AGENTS = {
        "research_agent": Agent(
            name="research_agent",
            model=MODEL,
            model_settings=chat_settings(),
            instructions=(
                "You are a research sub-agent. Given a topic, produce a concise "
                "bulleted list of 3-5 key facts. No preamble, no closing."
            ),
        ),
        "writing_agent": Agent(
            name="writing_agent",
            model=MODEL,
            model_settings=chat_settings(),
            instructions=(
                "You are a writing sub-agent. Given a brief and optional source "
                "facts, produce a polished 1-paragraph draft. Be clear and "
                "concrete. No preamble."
            ),
        ),
        "critique_agent": Agent(
            name="critique_agent",
            model=MODEL,
            model_settings=chat_settings(),
            instructions=(
                "You are an editorial critique sub-agent. Given a draft, give 2-3 "
                "crisp, actionable critiques. No preamble."
            ),
        ),
    }
    
    SUB_AGENT_EMPTY_SENTINEL = "<sub-agent produced no output>"
    
    
    async def _delegate(role: str, task: str) -> str:
        result = await Runner.run(SUB_AGENTS[role], task)
        output = str(result.final_output or "").strip() or SUB_AGENT_EMPTY_SENTINEL
        # Read and write with no await in between, so delegations the model makes
        # in parallel cannot drop each other's entry.
        state = shared_state()
        delegations = list(state.value.get("delegations") or [])
        delegations.append(
            {
                "id": str(uuid.uuid4()),
                "sub_agent": role,
                "task": task,
                "status": "completed",
                "result": output,
            }
        )
        state.update(delegations=delegations)
        return output
    
    
    @function_tool
    async def research_agent(task: str) -> str:
        """Delegate a research task; returns 3-5 key facts."""
        return await _delegate("research_agent", task)
    
    
    @function_tool
    async def writing_agent(task: str) -> str:
        """Delegate a drafting task; returns a one-paragraph draft."""
        return await _delegate("writing_agent", task)
    
    
    @function_tool
    async def critique_agent(task: str) -> str:
        """Delegate a review task; returns 2-3 critiques."""
        return await _delegate("critique_agent", task)
    
    
    
    
    subagents_agent = Agent(
        name="supervisor",
        instructions=SUPERVISOR_PROMPT,
        model=MODEL,
        # Research, then write, then critique: one delegation per model call.
        model_settings=chat_settings(parallel_tool_calls=False),
        tools=[research_agent, writing_agent, critique_agent],
    )
    
    

Each delegation also appends an entry to the `delegations` slot of shared state with `shared_state().update(...)`, which streams a `STATE_SNAPSHOT` as the tool finishes, so the UI's delegation log fills in while the supervisor is still running.

Handoffs and agents as tools

The SDK's other multi-agent tools work through the adapter too, with two limits. An agent reached by `handoffs` keeps its own tools and instructions, so it does not get the page's frontend tools or the `useAgentContext` entries. Give it what it needs through its own dynamic instructions, for example by reading `shared_state()`. A tool marked `needs_approval=True` inside an agent used through `Agent.as_tool()` cannot be resumed, because it pauses inside the sub-agent's own run. Gate the agent tool itself (`as_tool(..., needs_approval=True)`) or reach the sub-agent by handoff.

Each sub-agent is an isolated agent call with its own model, system prompt, and optional tools. They don't share memory or tools with the supervisor; the supervisor only ever sees what the sub-agent returns.

subagents.py
    
    
    import uuidfrom ag_ui_openai_agents import shared_statefrom agents import Agent, Runner, function_toolfrom demo_agents._common import MODEL, chat_settingsSUPERVISOR_PROMPT = (    "You are a supervisor. For research tasks call `research_agent`, for "    "drafting call `writing_agent`, for review call `critique_agent`. "    "Delegate step by step: research first, then write, then critique once, "    "then answer the user with the final draft.")SUB_AGENTS = {    "research_agent": Agent(        name="research_agent",        model=MODEL,        model_settings=chat_settings(),        instructions=(            "You are a research sub-agent. Given a topic, produce a concise "            "bulleted list of 3-5 key facts. No preamble, no closing."        ),    ),    "writing_agent": Agent(        name="writing_agent",        model=MODEL,        model_settings=chat_settings(),        instructions=(            "You are a writing sub-agent. Given a brief and optional source "            "facts, produce a polished 1-paragraph draft. Be clear and "            "concrete. No preamble."        ),    ),    "critique_agent": Agent(        name="critique_agent",        model=MODEL,        model_settings=chat_settings(),        instructions=(            "You are an editorial critique sub-agent. Given a draft, give 2-3 "            "crisp, actionable critiques. No preamble."        ),    ),}SUB_AGENT_EMPTY_SENTINEL = "<sub-agent produced no output>"async def _delegate(role: str, task: str) -> str:    result = await Runner.run(SUB_AGENTS[role], task)    output = str(result.final_output or "").strip() or SUB_AGENT_EMPTY_SENTINEL    # Read and write with no await in between, so delegations the model makes    # in parallel cannot drop each other's entry.    state = shared_state()    delegations = list(state.value.get("delegations") or [])    delegations.append(        {            "id": str(uuid.uuid4()),            "sub_agent": role,            "task": task,            "status": "completed",            "result": output,        }    )    state.update(delegations=delegations)    return output@function_toolasync def research_agent(task: str) -> str:    """Delegate a research task; returns 3-5 key facts."""    return await _delegate("research_agent", task)@function_toolasync def writing_agent(task: str) -> str:    """Delegate a drafting task; returns a one-paragraph draft."""    return await _delegate("writing_agent", task)@function_toolasync def critique_agent(task: str) -> str:    """Delegate a review task; returns 2-3 critiques."""    return await _delegate("critique_agent", task)subagents_agent = Agent(    name="supervisor",    instructions=SUPERVISOR_PROMPT,    model=MODEL,    # Research, then write, then critique: one delegation per model call.    model_settings=chat_settings(parallel_tool_calls=False),    tools=[research_agent, writing_agent, critique_agent],)

Keep sub-agent system prompts narrow and focused. The point of this pattern is that each one does one thing well. If a sub-agent needs to know the whole user context to do its job, that's a signal the boundary is wrong.

## Exposing sub-agents as tools#

The supervisor delegates by calling tools. Each delegation tool is a thin wrapper around a specialized agent call that:

  1. Runs the sub-agent on the supplied `task` string.
  2. Records the delegation into a `delegations` slot in shared agent state (so the UI can render a live log).
  3. Returns the sub-agent's final message as the tool result, which the supervisor sees on its next turn.



subagents.py
    
    
    @function_toolasync def research_agent(task: str) -> str:    """Delegate a research task; returns 3-5 key facts."""    return await _delegate("research_agent", task)@function_toolasync def writing_agent(task: str) -> str:    """Delegate a drafting task; returns a one-paragraph draft."""    return await _delegate("writing_agent", task)@function_toolasync def critique_agent(task: str) -> str:    """Delegate a review task; returns 2-3 critiques."""    return await _delegate("critique_agent", task)

This is where CopilotKit's shared-state channel earns its keep: the supervisor's tool calls mutate `delegations` as they happen, and the frontend renders every new entry live.

Give every delegation a stable `id` and merge new entries by that `id`. The client sends its copy of shared state back as run input on every run, so a slot that blindly appends whatever it receives — a LangGraph `Annotated[list, operator.add]` reducer, for example — concatenates the entries the client just echoed onto the ones the agent already has, and the log doubles when a thread is continued.

## Rendering a live delegation log#

On the frontend, the delegation log is a reactive render of the `delegations` slot.

Subscribe with `useAgent({ updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged] })`, read `agent.state.delegations`, and render one card per entry.

delegation-log.tsx
    
    
    /** * Live delegation log — renders the `delegations` slot of agent state. * * Each entry corresponds to one invocation of a sub-agent. The list * grows in real time as the supervisor fans work out to its children. * The parent header shows how many sub-agents have been called and * whether the supervisor is still running. */// Fixed list of the three sub-agent roles the supervisor can call.// Rendered as always-visible indicator chips at the top of the log// (regardless of whether the supervisor has delegated yet) so the user// — and the e2e suite — can see at a glance which sub-agents exist and// which are currently active.const INDICATOR_ROLES: ReadonlyArray<{  role: "researcher" | "writer" | "critic";  subAgent: SubAgentName;}> = [  { role: "researcher", subAgent: "research_agent" },  { role: "writer", subAgent: "writing_agent" },  { role: "critic", subAgent: "critique_agent" },];export function DelegationLog({ delegations, isRunning }: DelegationLogProps) {  const calledRoles = new Set<SubAgentName>(    delegations.map((d) => d.sub_agent),  );  return (    <div      data-testid="delegation-log"      className="w-full h-full flex flex-col bg-white rounded-2xl shadow-sm border border-[#DBDBE5] overflow-hidden dark:bg-card dark:border-border"    >      <div className="flex items-center justify-between px-6 py-3 border-b border-[#E9E9EF] bg-[#FAFAFC] dark:border-border dark:bg-muted">        <div className="flex items-center gap-3">          <span className="text-lg font-semibold text-[#010507] dark:text-foreground">            Sub-agent delegations          </span>          {isRunning && (            <span              data-testid="supervisor-running"              className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full border border-[#BEC2FF] bg-[#BEC2FF1A] text-[#010507] text-[10px] font-semibold uppercase tracking-[0.12em] dark:text-foreground"            >              <span className="w-1.5 h-1.5 rounded-full bg-[#010507] animate-pulse dark:bg-foreground" />              Supervisor running            </span>          )}        </div>        <span          data-testid="delegation-count"          className="text-xs font-mono text-[#838389] dark:text-muted-foreground"        >          {delegations.length} calls        </span>      </div>      <div        data-testid="subagent-indicators"        className="flex items-center gap-2 border-b border-[#E9E9EF] bg-white px-6 py-2 dark:border-border dark:bg-card"      >        {INDICATOR_ROLES.map(({ role, subAgent }) => {          const style = SUB_AGENT_STYLE[subAgent];          const fired = calledRoles.has(subAgent);          return (            <span              key={role}              data-testid={`subagent-indicator-${role}`}              data-role={role}              data-fired={fired ? "true" : "false"}              className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold uppercase tracking-[0.1em] border ${style.color} ${                fired ? "" : "opacity-60"              }`}            >              <span aria-hidden>{style.emoji}</span>              <span>{style.label}</span>            </span>          );        })}      </div>      <div className="flex-1 overflow-y-auto p-4 space-y-3">        {delegations.length === 0 ? (          <p className="text-[#838389] italic text-sm dark:text-muted-foreground">            Ask the supervisor to complete a task. Every sub-agent it calls will            appear here.          </p>        ) : (          delegations.map((d, idx) => {            const style = SUB_AGENT_STYLE[d.sub_agent];            return (              <div                key={d.id}                data-testid="delegation-entry"                className="border border-[#E9E9EF] rounded-xl p-3 bg-[#FAFAFC] dark:border-border dark:bg-muted"              >                <div className="flex items-center justify-between mb-2">                  <div className="flex items-center gap-2">                    <span className="text-xs font-mono text-[#AFAFB7] dark:text-muted-foreground">                      #{idx + 1}                    </span>                    <span                      className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold uppercase tracking-[0.1em] border ${style.color}`}                    >                      <span>{style.emoji}</span>                      <span>{style.label}</span>                    </span>                  </div>                  <span className="text-[10px] uppercase tracking-[0.12em] font-semibold text-[#189370] dark:text-[#85ECCE]">                    {d.status}                  </span>                </div>                <div className="text-xs text-[#57575B] mb-2 dark:text-muted-foreground">                  <span className="font-semibold text-[#010507] dark:text-foreground">                    Task:{" "}                  </span>                  {d.task}                </div>                <div className="text-sm text-[#010507] whitespace-pre-wrap bg-white rounded-lg p-2.5 border border-[#E9E9EF] dark:text-foreground dark:bg-card dark:border-border">                  {d.result}                </div>              </div>            );          })        )}      </div>    </div>  );}

The result: as the supervisor fans work out to its sub-agents, the log grows in real time, giving the user visibility into a process that would otherwise be a long opaque spinner.

## Related#

  * **[Shared State](https://docs.copilotkit.ai/openai-agents-python/shared-state)** — the channel that makes the delegation log live.
  * **[State streaming](https://docs.copilotkit.ai/openai-agents-python/shared-state/streaming)** — stream _individual_ sub-agent outputs token-by-token inside each log entry.


