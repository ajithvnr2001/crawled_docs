---
url: https://docs.copilotkit.ai/reference/v1/hooks/useCopilotAdditionalInstructions/
title: useCopilotAdditionalInstructions
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:59.754642+00:00
---

# useCopilotAdditionalInstructions

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useCopilotAdditionalInstructions/

React/v1

# useCopilotAdditionalInstructions

The useCopilotAdditionalInstructions hook gives additional instructions to the agent.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

In v2, use [`useAgentContext`](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext) from `@copilotkit/react-core/v2`.

`useCopilotAdditionalInstructions` is a React hook that provides additional instructions to the Copilot.

## UsageCopy Anchor Link

### Simple UsageCopy Anchor Link

Pass the instructions in the `instructions` field of the options object.

Copy Text
    
    
    import { useCopilotAdditionalInstructions } from "@copilotkit/react-core";
    
    export function MyComponent() {
      useCopilotAdditionalInstructions({
        instructions: "Do not answer questions about the weather.",
      });
    }

### Conditional UsageCopy Anchor Link

You can also conditionally add instructions based on the state of your app.

Copy Text
    
    
    import { useCopilotAdditionalInstructions } from "@copilotkit/react-core";
    
    export function MyComponent() {
      const [showInstructions, setShowInstructions] = useState(false);
    
      useCopilotAdditionalInstructions({
        available: showInstructions ? "enabled" : "disabled",
        instructions: "Do not answer questions about the weather.",
      });
    }

## ParametersCopy Anchor Link

Prop

Type

`instructions`string

`available?`'enabled' | 'disabled'

`dependencies?`any[]

How is this guide?

GoodBad

[Previous PageuseCopilotReadable](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotReadable)[Next PageuseCopilotChat](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChat)
