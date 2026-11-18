---
url: https://docs.copilotkit.ai/reference/v1/hooks/useCopilotAction/
title: useCopilotAction
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:59.788466+00:00
---

# useCopilotAction

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useCopilotAction/

React/v1

# useCopilotAction

The useCopilotAction hook allows your copilot to take action in the app.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

`useCopilotAction` is still supported, but we recommend migrating to [`useFrontendTool`](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool) from the v2 API.

![](https://cdn.copilotkit.ai/docs/copilotkit/images/use-copilot-action/useCopilotAction.gif)

`useCopilotAction` is a React hook that registers an action that the agent can call during a chat.

Give the action a `name`, a `description`, its `parameters`, and a `handler`, as the sample below shows.

## UsageCopy Anchor Link

### Simple UsageCopy Anchor Link

Copy Text
    
    
    useCopilotAction({
      name: "sayHello",
      description: "Say hello to someone.",
      parameters: [
        {
          name: "name",
          type: "string",
          description: "name of the person to say greet",
        },
      ],
      handler: async ({ name }) => {
        alert(`Hello, ${name}!`);
      },
    });

## Generative UICopy Anchor Link

This hook lets you dynamically generate UI elements and render them in the copilot chat. For more information, check out the [Generative UI](https://docs.copilotkit.ai/generative-ui/display) page.

## ParametersCopy Anchor Link

Prop

Type

`action`Action

`dependencies?`any[]

How is this guide?

GoodBad

[Previous PageuseLangGraphInterrupt](https://docs.copilotkit.ai/reference/v1/hooks/useLangGraphInterrupt)[Next PageCopilotRuntime](https://docs.copilotkit.ai/reference/v1/classes/CopilotRuntime)
