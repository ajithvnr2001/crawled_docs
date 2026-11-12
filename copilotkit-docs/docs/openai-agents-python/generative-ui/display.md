---
url: https://docs.copilotkit.ai/openai-agents-python/generative-ui/display/
title: Display components
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:41.254006+00:00
---

# Display components

> Source: https://docs.copilotkit.ai/openai-agents-python/generative-ui/display/

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

[OpenAI Agents SDK (Python)](https://docs.copilotkit.ai/openai-agents-python)[Build Generative UI](https://docs.copilotkit.ai/openai-agents-python/generative-ui)

# Display components

Register React components that your agent can render in the chat.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

gen_ui_tool_based.py

page.tsx

bar-chart.tsx

route.ts
    
    
    """Tool-based generative UI: the frontend registers the render tools."""from agents import Agentfrom demo_agents._common import MODEL, chat_settingsSYSTEM_PROMPT = """You are a data visualization assistant.When the user asks for a chart, call `render_bar_chart` or `render_pie_chart`with a concise title, short description, and a `data` array of`{label, value}` items. Pick bar for comparisons over a small set ofcategories; pick pie for composition / share-of-whole.If the user names a chart subject but does NOT supply concrete numbers(e.g. "show me a pie chart of website traffic by source"), do NOT askthem for data. Invent plausible illustrative sample values yourself,call the appropriate `render_*` tool immediately, and briefly note inthe follow-up that the values are illustrative samples. Always renderthe chart on the first turn -- never reply with a clarifying questionasking for the data.Keep chat responses brief -- let the chart do the talking."""gen_ui_tool_based_agent = Agent(    name="chart_assistant",    instructions=SYSTEM_PROMPT,    model=MODEL,    model_settings=chat_settings(),)

## What is this?#

Render-only generative UI lets you register React components as tools your agent can invoke. When the agent calls the tool, CopilotKit renders your component directly in the chat with the tool's arguments as props; no handler logic or user interaction required.

page.tsxchart.tsx
    
    
    useComponent({
    name: "showChart",
    description: "Populate data and show the user a chart",
    parameters: ChartProps,
    render: Chart
    });
    
    
    
    export const ChartProps = z.object({
      title: z.string(),
      data: z.array(z.object({ label: z.string(), value: z.number() })),
    });
    
    export function Chart({ title, data }: z.infer<typeof ChartProps>) {
      return (
        <div>
          <h3>{title}</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={data}>
              <XAxis dataKey="label" /><YAxis /><Tooltip />
              <Bar dataKey="value" fill="#6366f1" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      );
    }

## When should I use this?#

Use render-only generative UI when you want to:

  * Display rich UI (cards, charts, tables) inline in the chat
  * Show structured data from agent responses
  * Render previews, status indicators, or visual feedback
  * Let the agent present information beyond plain text



## How it works in code#

### Nothing to wire on the agent

On every run, the OpenAI Agents AG-UI adapter adds each tool the frontend registered to a per-request copy of the agent, so the agent declares no tools of its own for this. When the model calls one, the run stops there, because the browser owns that call. The browser runs the handler, and the next request carries the result as a tool message, which the model sees as the call's output before it continues.

If a frontend tool has the same name as one of the agent's own tools, the agent's tool wins and the frontend one is ignored.

### Tell the model when to call it

This is the part that is easy to miss. The tool arrives on every run, but a model with no instruction about it will answer in prose and never call it. Name the tool in the instructions and say what it is for.

gen_ui_tool_based.py
    
    
    from agents import Agent
    
    from demo_agents._common import MODEL, chat_settings
    
    SYSTEM_PROMPT = """You are a data visualization assistant.
    
    When the user asks for a chart, call `render_bar_chart` or `render_pie_chart`
    with a concise title, short description, and a `data` array of
    `{label, value}` items. Pick bar for comparisons over a small set of
    categories; pick pie for composition / share-of-whole.
    
    If the user names a chart subject but does NOT supply concrete numbers
    (e.g. "show me a pie chart of website traffic by source"), do NOT ask
    them for data. Invent plausible illustrative sample values yourself,
    call the appropriate `render_*` tool immediately, and briefly note in
    the follow-up that the values are illustrative samples. Always render
    the chart on the first turn -- never reply with a clarifying question
    asking for the data.
    
    Keep chat responses brief -- let the chart do the talking."""
    
    
    gen_ui_tool_based_agent = Agent(
        name="chart_assistant",
        instructions=SYSTEM_PROMPT,
        model=MODEL,
        model_settings=chat_settings(),
    )
    
    

Backend tools in the same turn

A frontend tool call ends the run as soon as the model makes it. A backend tool the model called in the same turn and that has not finished is cancelled, and the next request answers it as not having run. Where that matters, turn off parallel tool calls on the agent with `ModelSettings(parallel_tool_calls=False)`.

The renderer component receives the tool's arguments as typed props and mounts inline in the chat. Below is the chart renderer wired up in the canonical demo — the agent emits the data, the component draws it.

page.tsx
    
    
      useComponent({    name: "render_bar_chart",    description: "Display a bar chart with labeled numeric values.",    parameters: barChartPropsSchema,    render: BarChart,  });
