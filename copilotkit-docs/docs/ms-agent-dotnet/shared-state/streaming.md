---
url: https://docs.copilotkit.ai/ms-agent-dotnet/shared-state/streaming/
title: State Streaming
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:23.077808+00:00
---

# State Streaming

> Source: https://docs.copilotkit.ai/ms-agent-dotnet/shared-state/streaming/

Shared state

# State Streaming

Stream partial agent state updates to the UI while a tool call is still running.

Copy MarkdownOpen

State Streaming

DemoCode

[](https://showcase-ms-agent-dotnet-production.up.railway.app/demos/shared-state-streaming "Open in a new tab")[](https://github.com/CopilotKit/CopilotKit/tree/main/showcase/integrations/ms-agent-dotnet/src/app/demos/shared-state-streaming "View the code on GitHub")

Waking up the demo

## What is this?Copy Anchor Link

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call (writing a full document, drafting an email) appears to the UI as one big burst at the end. For agent-native apps, that feels broken: users expect to watch the output materialise.

**State streaming** copies one tool argument into an agent state key while the model writes the argument. The UI, subscribed via `useAgent`, re-renders every token.

## When should I use this?Copy Anchor Link

Use state streaming whenever a tool's output is long-form text or a growing structured value and you want the user to see it assemble in real time. Common shapes:

  * A collaborative writing agent that emits a document
  * A research agent that accumulates a list of findings
  * A planning agent that builds up a step-by-step plan



## The backend: one streaming state mappingCopy Anchor Link

### Map the tool call to a state snapshotCopy Anchor Link

`AGUIStreamOptions.MapCall` maps a tool call to AG-UI events. Return a `StateSnapshotEvent` built from the tool's arguments, and attach the options to the endpoint with `WithMetadata`:

Program.cs

Copy Text
    
    
    using System.ComponentModel;
    using System.Text.Json;
    using AGUI.Abstractions;
    using AGUI.Server;
    #pragma warning disable OPENAI001
    using Microsoft.Extensions.AI;
    using Microsoft.Agents.AI;
    using Microsoft.Agents.AI.Hosting.AGUI.AspNetCore;
    using Microsoft.Extensions.AI;
    using OpenAI;
    using OpenAI.Chat;
    
    var builder = WebApplication.CreateBuilder(args);
    builder.Services.AddAGUIServer();
    var app = builder.Build();
    
    string openAiApiKey = builder.Configuration["OPENAI_API_KEY"]
        ?? throw new InvalidOperationException("Set OPENAI_API_KEY");
    
    // Define a tool the LLM may call to report its progress
    [Description("Report current step progress.")]
    static string StepProgress([Description("Steps completed so far")] string[] steps)
        => "Progress received.";
    
    AITool stepProgress = AIFunctionFactory.Create(StepProgress, name: "step_progress");
    var agent = new OpenAIClient(openAiApiKey)
        .GetChatClient("gpt-6-luna")
        .AsIChatClient().AsBuilder()
        .ConfigureOptions(options => options.RawRepresentationFactory = _ =>
            new OpenAI.Chat.ChatCompletionOptions { ReasoningEffortLevel = new("none") })
        .Build()
        .AsAIAgent(
            name: "AGUIAssistant",
            instructions: "You are a helpful assistant that may call the 'step_progress' tool to report intermediate steps.",
            tools: [stepProgress]);
    
    // Map the completed tool arguments to a shared-state snapshot
    AGUIStreamOptions streamOptions = new AGUIStreamOptions()
        .MapCall("step_progress", call =>
        {
            if (call.Arguments?.TryGetValue("steps", out object? steps) is not true)
            {
                return [];
            }
    
            JsonElement snapshot = JsonSerializer.SerializeToElement(
                new { observed_steps = steps });
            return [new StateSnapshotEvent { Snapshot = snapshot }];
        });
    
    app.MapAGUIServer("/", agent).WithMetadata(streamOptions);
    await app.RunAsync();

### Know what streams and what does notCopy Anchor Link

`MapCall` runs on the completed `FunctionCallContent`, so the state key updates once, when the tool call finishes. It does not grow token by token while the model writes the arguments. To stream partial arguments into state, register a provider-specific extractor with `MapStreamingToolCallArguments`.

The backend pattern is always the same: map one streaming tool argument to one shared-state key. Each framework does this in its own way:

  * LangGraph Python: `StateStreamingMiddleware` with `StateItem(...)` entries.
  * LangGraph TypeScript: `copilotkitCustomizeConfig` with an `emitIntermediateState` mapping.
  * Direct SDK adapters: parse partial tool arguments in the streaming loop, and emit `STATE_SNAPSHOT` whenever the mapped value changes.
  * LlamaIndex and Pydantic AI: there is no per-token mapping. A backend tool sends a state snapshot after each step or tool call instead (see the setup above).



When the LLM streams that argument, CopilotKit writes every partial value into shared state before the tool even finishes executing.

Missing snippet

Region `state-streaming-middleware` not found in `ms-agent-dotnet::shared-state-streaming`. Tag the source lines with `// @region[state-streaming-middleware]` / `// @endregion[state-streaming-middleware]`.Available: frontend-use-coagent-state

A few things to note:

  * The state key must exist in your agent state (`document` in this demo).
  * The tool and argument names must match the exact LLM-facing tool call you want to forward (`write_document.document` here).
  * Streamed values are previews. When the step ends, the state the agent saves replaces them, so save the final value when the tool finishes. On CrewAI, LlamaIndex and Pydantic AI, write the final value to the agent state yourself, or it is overwritten when the step returns.



## The frontend: useAgent + OnStateChangedCopy Anchor Link

The UI side is the same as any other [shared-state](https://docs.copilotkit.ai/ms-agent-dotnet/shared-state) subscription: `useAgent` with `OnStateChanged` gives you a reactive `agent.state`. Add `OnRunStatusChanged` if you want a "LIVE" / "done" indicator.

page.tsx

Copy Text
    
    
      // Subscribe to BOTH state changes and run-status changes. The former
      // drives the per-token document rerender; the latter toggles the
      // "LIVE" badge when the agent starts / stops.
      const { agent } = useAgent({
        agentId: "shared-state-streaming",
        updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged],
      });

From there, `agent.state.document` is just a string that grows on every token, and `agent.isRunning` tells you whether to show a streaming indicator.

## Try itCopy Anchor Link

Ask the agent to write a short poem. The `document` text grows in your UI while the agent writes. When the run ends, `agent.isRunning` is `false`, so your streaming indicator turns off.

How is this guide?

GoodBad

[Previous PageRender agent state in your app](https://docs.copilotkit.ai/ms-agent-dotnet/shared-state/rendering-in-app)[Next PageAgent Read-Only Context](https://docs.copilotkit.ai/ms-agent-dotnet/shared-state/agent-readonly)
