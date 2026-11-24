---
url: https://docs.copilotkit.ai/reference/v1/classes/CopilotTask/
title: CopilotTask
method: scrapling+scrapegraph
fetched_at: 2026-11-24T13:30:50.004531+00:00
---

# CopilotTask

> Source: https://docs.copilotkit.ai/reference/v1/classes/CopilotTask/

React/v1

# CopilotTask

CopilotTask is used to execute one-off tasks, for example on button click.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

`CopilotTask` has no direct v2 replacement. See the [v1 to v2 export map](https://docs.copilotkit.ai/reference/v1/export-map).

This class is used to execute one-off tasks, for example on button press. It can use the context available via [useCopilotReadable](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotReadable) and the actions provided by [useCopilotAction](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotAction), or you can provide your own context and actions.

## ExampleCopy Anchor Link

In the simplest case, use CopilotTask in the context of your app by giving it instructions on what to do.

Copy Text
    
    
    import { useState } from "react";
    import { CopilotTask, useCopilotContext } from "@copilotkit/react-core";
    
    export function MyComponent() {
      const context = useCopilotContext();
      const [message, setMessage] = useState("");
    
      const task = new CopilotTask({
        instructions: "Set a random message",
        actions: [
          {
            name: "setMessage",
            description: "Set the message.",
            parameters: [
              {
                name: "message",
                type: "string",
                description: "A message to display.",
                required: true,
              },
            ],
            handler: ({ message }) => setMessage(message),
          },
        ],
      });
    
      const executeTask = async () => {
        await task.run(context);
      };
    
      return (
        <>
          <button onClick={executeTask}>Execute task</button>
          <p>{message}</p>
        </>
      );
    }

Have a look at the [Presentation Example App](https://github.com/CopilotKit/CopilotKit/blob/main/examples/v1/next-openai/src/app/presentation/page.tsx) for a more complete example.

## Constructor ParametersCopy Anchor Link

Prop

Type

`instructions`string

`actions?`FrontendAction<any>[]

`includeCopilotReadable?`boolean

`includeCopilotActions?`boolean

`forwardedParameters?`ForwardedParametersInput

`run?`context: CopilotContextParams, data?: T

How is this guide?

GoodBad

[Previous PageGoogleGenerativeAIAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/GoogleGenerativeAIAdapter)[Next PageRemote Endpoints](https://docs.copilotkit.ai/reference/v1/sdk/python/RemoteEndpoints)
