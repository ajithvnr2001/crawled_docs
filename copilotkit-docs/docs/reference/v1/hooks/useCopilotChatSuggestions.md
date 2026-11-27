---
url: https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChatSuggestions/
title: useCopilotChatSuggestions
method: scrapling+scrapegraph
fetched_at: 2026-11-27T11:59:07.336508+00:00
---

# useCopilotChatSuggestions

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChatSuggestions/

React/v1

# useCopilotChatSuggestions

The useCopilotChatSuggestions hook generates suggestions in the chat window based on real-time app state.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

In v2, use [`useConfigureSuggestions`](https://docs.copilotkit.ai/reference/v2/hooks/useConfigureSuggestions) from `@copilotkit/react-core/v2`.

`useCopilotChatSuggestions` generates suggestions in the chat from your instructions and app state.

  
![](https://cdn.copilotkit.ai/docs/copilotkit/images/use-copilot-chat-suggestions/use-copilot-chat-suggestions.gif)

## UsageCopy Anchor Link

### Install DependenciesCopy Anchor Link

This component is part of the [@copilotkit/react-ui](https://npmjs.com/package/@copilotkit/react-ui) package.

Copy Text
    
    
    npm install @copilotkit/react-core @copilotkit/react-ui

### Simple UsageCopy Anchor Link

Copy Text
    
    
    import { useCopilotChatSuggestions } from "@copilotkit/react-ui";
    
    export function MyComponent() {
      const [employees, setEmployees] = useState([]);
    
      useCopilotChatSuggestions({
        instructions: `The following employees are on duty: ${JSON.stringify(employees)}`,
      });
    }

### Dependency ManagementCopy Anchor Link

Copy Text
    
    
    import { useCopilotChatSuggestions } from "@copilotkit/react-ui";
    
    export function MyComponent() {
      useCopilotChatSuggestions(
        {
          instructions: "Suggest the most relevant next actions.",
        },
        [appState],
      );
    }

In the example above, the suggestions are generated based on the given instructions. The hook monitors `appState`, and updates suggestions accordingly whenever it changes.

### Behavior and LifecycleCopy Anchor Link

The hook registers the configuration with the chat context upon component mount and removes it on unmount.

## ParametersCopy Anchor Link

Pass either the instructions to generate suggestions, or a static list of suggestions.

Prop

Type

`instructions`string

`minSuggestions?`number

`maxSuggestions?`number

`available?`'enabled' | 'disabled' | 'always' | 'before-first-message' | 'after-first-message'

`className?`string

`suggestions?`{ title: string; message: string }[]

`dependencies?`any[]

How is this guide?

GoodBad

[Previous PageuseCopilotChatHeadless_c](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChatHeadless_c)[Next PageuseCoAgent](https://docs.copilotkit.ai/reference/v1/hooks/useCoAgent)
