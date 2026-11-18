---
url: https://docs.copilotkit.ai/agent-spec/generative-ui/tool-rendering/
title: Tool Call Rendering
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:52.469648+00:00
---

# Tool Call Rendering

> Source: https://docs.copilotkit.ai/agent-spec/generative-ui/tool-rendering/

Controlled

# Tool Call Rendering

Render your agent's tool calls with custom UI components.

Copy MarkdownOpen

Not available for agent-spec yet

The code on this page comes from the showcase's `tool-rendering` demo, and agent-spec doesn't have it yet. See this page for [CopilotKit's Built-in Agent](https://docs.copilotkit.ai/generative-ui/tool-rendering), [LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/generative-ui/tool-rendering), [LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript/generative-ui/tool-rendering).

## What is this?Copy Anchor Link

Tools are how an LLM invokes predefined, typically-deterministic functions. Tool rendering lets you decide how each of those tool calls appears in the chat. By default, a tool call does not show in the chat. You register a React component that renders a branded card for the call (arguments, live status, and the eventual result). This is the **Generative UI** variant CopilotKit calls **tool rendering**.

## When should I use this?Copy Anchor Link

Render tool calls when you want to:

  * Show users exactly what tools the agent is invoking and with what arguments
  * Display live progress indicators while a tool executes
  * Render rich, polished results once a tool completes
  * Give tool-heavy agents a transparent, on-brand chat experience



## Default tool rendering (zero-config)Copy Anchor Link

The simplest entry point: call `useDefaultRenderTool()` with no arguments. CopilotKit registers its built-in `DefaultToolCallRenderer` as the `*` wildcard: every tool call renders as a tidy status card (tool name, live **Running → Done** pill, collapsible arguments/result) without you writing any UI. Calls the agent makes in a row are grouped into one card; see Grouping tool calls.

Without this hook, the chat has no `*` renderer, and tool calls without a named renderer are invisible. The user only sees the assistant's final text summary.

Not available for agent-spec yet

This sample comes from the showcase's `tool-rendering-default-catchall` demo, and agent-spec doesn't have it yet.

Here's what the built-in status card looks like for each tool call:

## Custom catch-allCopy Anchor Link

Once you want on-brand chrome, pass a `render` function to `useDefaultRenderTool`. It's a convenience wrapper around `useRenderTool({ name: "*", ... })`: one wildcard renderer handles every tool call, named or not:

Not available for agent-spec yet

This sample comes from the showcase's `tool-rendering-custom-catchall` demo, and agent-spec doesn't have it yet.

The catch-all component reads the tool `name`, `status`, `parameters`, and `result`. It uses the shadcn/ui `Card` and `Badge` components:

Not available for agent-spec yet

This sample comes from the showcase's `tool-rendering-custom-catchall` demo, and agent-spec doesn't have it yet.

Here's the branded catch-all in action, where every tool call gets the same on-brand card:

## Per-tool renderersCopy Anchor Link

The most expressive path is one renderer per tool name. The demo registers four per-tool renderers: `get_weather`, `search_flights`, `get_stock_price`, and `roll_d20`. Each renderer receives the tool's parsed arguments, a live `status`, and (once the agent returns) the `result`.

The frontend pattern is the same for every backend. This shared, docs-only example includes every component, type, and helper that its renderers use:

components/weather-card.tsx

Copy Text
    
    
    export interface WeatherCardProps {
      loading: boolean;
      location: string;
      temperature?: number;
      humidity?: number;
      windSpeed?: number;
      conditions?: string;
    }
    
    export function WeatherCard({
      loading,
      location,
      temperature,
      humidity,
      windSpeed,
      conditions,
    }: WeatherCardProps) {
      return (
        <article className="rounded-xl border p-4">
          <h3 className="font-semibold">{location || "Weather"}</h3>
          {loading ? (
            <p>Fetching weather...</p>
          ) : (
            <dl>
              <div>
                <dt>Conditions</dt>
                <dd>{conditions ?? "--"}</dd>
              </div>
              <div>
                <dt>Temperature</dt>
                <dd>{temperature ?? "--"}&deg;F</dd>
              </div>
              <div>
                <dt>Humidity</dt>
                <dd>{humidity ?? "--"}%</dd>
              </div>
              <div>
                <dt>Wind</dt>
                <dd>{windSpeed ?? "--"} mph</dd>
              </div>
            </dl>
          )}
        </article>
      );
    }

components/flight-list-card.tsx

Copy Text
    
    
    export interface Flight {
      airline?: string;
      flight?: string;
      depart?: string;
      arrive?: string;
      price_usd?: number;
    }
    
    export interface FlightListCardProps {
      loading: boolean;
      origin: string;
      destination: string;
      flights: Flight[];
    }
    
    export function FlightListCard({
      loading,
      origin,
      destination,
      flights,
    }: FlightListCardProps) {
      return (
        <article className="rounded-xl border p-4">
          <h3 className="font-semibold">
            {origin || "?"} → {destination || "?"}
          </h3>
          {loading ? (
            <p>Searching...</p>
          ) : (
            <ul>
              {flights.map((flight, index) => (
                <li key={`${flight.flight ?? "flight"}-${index}`}>
                  {flight.airline ?? "--"} {flight.flight ?? ""}:{" "}
                  {flight.depart ?? "?"} → {flight.arrive ?? "?"}
                  {flight.price_usd !== undefined ? ` ($${flight.price_usd})` : ""}
                </li>
              ))}
            </ul>
          )}
        </article>
      );
    }

lib/parse-json-result.ts

Copy Text
    
    
    export function parseJsonResult<T>(result: unknown): T {
      if (!result) return {} as T;
    
      try {
        return (typeof result === "string" ? JSON.parse(result) : result) as T;
      } catch {
        return {} as T;
      }
    }

app/tool-renderers.tsx

Copy Text
    
    
    "use client";
    
    import { useRenderTool } from "@copilotkit/react-core/v2";
    import { z } from "zod";
    import { WeatherCard } from "../components/weather-card";
    import { FlightListCard, type Flight } from "../components/flight-list-card";
    import { parseJsonResult } from "../lib/parse-json-result";
    
    interface WeatherResult {
      city?: string;
      temperature?: number;
      humidity?: number;
      wind_speed?: number;
      conditions?: string;
    }
    
    interface FlightSearchResult {
      origin?: string;
      destination?: string;
      flights?: Flight[];
    }
    
    export function ToolRenderers() {
      useRenderTool(
        {
          name: "get_weather",
          parameters: z.object({ location: z.string() }),
          render: ({ parameters, result, status }) => {
            const parsed = parseJsonResult<WeatherResult>(result);
            return (
              <WeatherCard
                loading={status !== "complete"}
                location={parameters?.location ?? parsed.city ?? ""}
                temperature={parsed.temperature}
                humidity={parsed.humidity}
                windSpeed={parsed.wind_speed}
                conditions={parsed.conditions}
              />
            );
          },
        },
        [],
      );
    
      useRenderTool(
        {
          name: "search_flights",
          parameters: z.object({
            origin: z.string(),
            destination: z.string(),
          }),
          render: ({ parameters, result, status }) => {
            const parsed = parseJsonResult<FlightSearchResult>(result);
            return (
              <FlightListCard
                loading={status !== "complete"}
                origin={parameters?.origin ?? parsed.origin ?? ""}
                destination={parameters?.destination ?? parsed.destination ?? ""}
                flights={parsed.flights ?? []}
              />
            );
          },
        },
        [],
      );
    
      return null;
    }

Mount the renderers anywhere beneath the same `CopilotKit` provider as your chat. The renderer component returns no layout of its own; it registers the two named renderers for tool calls in the chat:

app/page.tsx

Copy Text
    
    
    "use client";
    
    import { CopilotChat, CopilotKit } from "@copilotkit/react-core/v2";
    import { ToolRenderers } from "./tool-renderers";
    
    export default function Page() {
      return (
        // Use the agent name you registered on CopilotRuntime
        <CopilotKit runtimeUrl="/api/copilotkit" agent="default">
          <ToolRenderers />
          <CopilotChat agentId="default" />
        </CopilotKit>
      );
    }

The `name` you pass to `useRenderTool` must match the tool name the agent exposes. That is how the chat matches the call to your component.

Per-tool renderers compose with a catch-all: named renderers claim the "interesting" tools and a wildcard handles everything else. In the demo, the catch-all component from Custom catch-all handles every tool without a named renderer:

### Tool inputs and results are separateCopy Anchor Link

In `useRenderTool`, `parameters` contains the **inputs** the agent sent to the tool. It does not change into the tool's return value when `status` becomes `"complete"`. The completed output arrives separately as `result`, a string. For a tool that returns JSON, parse that string before reading its fields.

For example, `get_weather` might receive `{ "location": "Paris" }` and return `{ "temperature": 22 }`. Read `parameters.location` for the requested city and the parsed `result.temperature` for the temperature. Adding `temperature` to the renderer's `parameters` schema does not copy it from the result.

If a card says **complete** but still shows placeholder details, check whether those details come from `parameters` instead of the parsed `result`. Completion reports that the tool returned; it does not fill the card's props for you.

## The backend tool definitionCopy Anchor Link

The frontend renderer only sees what the agent sends down. Here's the matching backend definition for `get_weather`: expose a tool named `get_weather`, return structured data, and let the frontend renderer with the same name render the card.

### Give your Agent Spec agent a tool to callCopy Anchor Link

Open Agent Spec has no live demo on this page yet, so the backend code above does not show for it. In Agent Spec, a backend tool is a `ServerTool` in the agent config. `AgentSpecAgent` runs it through the Python function you register under the same name in `tool_registry`:

agent.py

Copy Text
    
    
    # Create the agent
    from pyagentspec.agent import Agent
    from pyagentspec.llms import OpenAiCompatibleConfig
    from pyagentspec.property import StringProperty
    from pyagentspec.tools import ServerTool
    from pyagentspec.serialization import AgentSpecSerializer
    
    llm = OpenAiCompatibleConfig(
        name="my_llm",
        model_id="gpt-6-luna",
        url="https://api.openai.com/v1",
    )
    weather_tool = ServerTool( # ServerTool are backend tools in Agent Spec
        name="get_weather",
        description="Get the weather for a given location.",
        inputs=[StringProperty(title="location", description="The location to get the weather forecast. Must be a city/town name.")],
        outputs=[StringProperty(title="weather_result")],
    )
    agent = Agent(
        name="my_agent",
        llm_config=llm,
        system_prompt="Based on the weather forecast result and the user input, write a response to the user",
        tools=[weather_tool],
        human_in_the_loop=True,
    )
    agentspec_json_config = AgentSpecSerializer().to_json(agent)
    
    async def get_weather(location: str = "Everywhere ever") -> str:
        """Get the weather for a given location. Ensure location is fully spelled out."""
        return f"The weather in {location} is sunny."
    
    # Start the server
    import uvicorn
    from fastapi import APIRouter, FastAPI
    from ag_ui_agentspec.agent import AgentSpecAgent
    from ag_ui_agentspec.endpoint import add_agentspec_fastapi_endpoint
    
    
    runtime = "langgraph" # you can also choose "wayflow"
    router = APIRouter()
    add_agentspec_fastapi_endpoint(
        app=router,
        agentspec_agent=AgentSpecAgent(
            agentspec_json_config,
            runtime=runtime,
            tool_registry={"get_weather": get_weather},
        ),
        path=f"/{runtime}/path_to_my_agent",
    )
    app = FastAPI(title="Agent-Spec x AG-UI Examples - Backend Tool")
    app.include_router(router)
    
    if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=8000)

Three names must match: the `ServerTool` name, the `tool_registry` key, and the `name` you pass to `useRenderTool` (`get_weather` here). A renderer with a different name never shows its card.

To check it, ask the agent for the weather in San Francisco. The `WeatherCard` renders with the temperature from `result`.

## Grouping tool callsCopy Anchor Link

Agents often call several tools in a row. By default, CopilotKit collapses each series of calls rendered by the built-in card from `useDefaultRenderTool()` into one card that reads "Used 3 tools". While a call runs, the card names it ("Running read_file src/app.ts"), and opening it shows a row per call. Calls rendered by your own renderers always show on their own and split the group around them, unless the renderer opts in with `group: true`:

page.tsx

Copy Text
    
    
    useDefaultRenderTool({ render: MyToolRow, group: true });

Pick how calls show with `toolCallDisplay` on the message view:

page.tsx

Copy Text
    
    
    // "grouped" (default) | "line" | "stacked" | "turn" | "separate"
    <CopilotChat messageView={{ toolCallDisplay: "line" }} />

Display| What the user sees  
---|---  
`"grouped"`| One card per series of calls, collapsed to "Used 3 tools". Opens to a row per call.  
`"line"`| The same grouping as a quiet line of text, like "Thought for 4 seconds".  
`"stacked"`| The latest call on top of a stack of the earlier ones. Opens into a card per call.  
`"turn"`| The agent works in the open, then everything before the reply folds into "Worked for 9s".  
`"separate"`| Every call gets its own card.  
  
To compare the displays side by side, run the [Tool call display stories](https://github.com/CopilotKit/CopilotKit/blob/main/examples/v2/react/storybook/stories/ToolCallDisplay.stories.tsx) in the React Storybook. They play a scripted run through the real message view, with a control to switch `toolCallDisplay`.

To restyle or replace the group, use the `group` slot of the tool-calls view (it applies to the grouped, line and stacked displays):

page.tsx

Copy Text
    
    
    // ToolTimeline: your component, given the group's `calls` and a `renderCall` function
    <CopilotChat
      messageView={{
        assistantMessage: { toolCallsView: { group: ToolTimeline } },
      }}
    />

See [`CopilotChatToolCallGroup`](https://docs.copilotkit.ai/reference/components/CopilotChatToolCallGroup) for its props and an example replacement.

**Free course:** See this pattern built end-to-end in [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/short-courses/build-interactive-agents-with-generative-ui/). This free DeepLearning.AI short course is taught by CopilotKit's CEO. It covers the full Generative UI spectrum (Controlled, Declarative, and Open-Ended).

How is this guide?

GoodBad

[Previous PageComponents as Tools](https://docs.copilotkit.ai/agent-spec/generative-ui/tool-based)[Next PageState Rendering](https://docs.copilotkit.ai/agent-spec/generative-ui/state-rendering)
