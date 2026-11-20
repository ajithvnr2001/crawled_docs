---
url: https://docs.copilotkit.ai/reference/v1/hooks/useCopilotReadable/
title: useCopilotReadable
method: scrapling+scrapegraph
fetched_at: 2026-11-20T11:16:26.870496+00:00
---

# useCopilotReadable

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useCopilotReadable/

React/v1

# useCopilotReadable

The useCopilotReadable hook gives your copilot knowledge (e.g. application state).

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

In v2, use [`useAgentContext`](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext) from `@copilotkit/react-core/v2`.

`useCopilotReadable` is a React hook that provides app-state and other information to the Copilot.

## UsageCopy Anchor Link

### Simple UsageCopy Anchor Link

Pass a `description` and a `value`. The hook adds them to the context that the Copilot reads when it answers.

Copy Text
    
    
    import { useCopilotReadable } from "@copilotkit/react-core";
    
    export function MyComponent() {
      const [employees, setEmployees] = useState([]);
    
      useCopilotReadable({
        description: "The list of employees",
        value: employees,
      });
    }

### Custom SerializationCopy Anchor Link

By default the value is serialized with `JSON.stringify`. Pass `convert` to control the string the Copilot sees. It is called with the description and the value, in that order:

Copy Text
    
    
    useCopilotReadable({
      description: "The current user",
      value: user,
      convert: (description, value) => `${description}: ${value.firstName} ${value.lastName}`,
    });

### Conditional UsageCopy Anchor Link

Toggle `available` to add or remove the context as your app state changes. Switching to `"disabled"` removes the entry from the Copilot context; switching back to `"enabled"` re-adds it.

Copy Text
    
    
    useCopilotReadable({
      description: "The list of employees",
      value: employees,
      available: showEmployees ? "enabled" : "disabled",
    });

### Re-running on Custom DependenciesCopy Anchor Link

The context is refreshed whenever `description`, `value`, `convert` or `available` change. Pass a second argument to add your own dependencies:

Copy Text
    
    
    useCopilotReadable(
      {
        description: "The selected employee",
        value: employee,
      },
      [departmentId],
    );

## Return ValueCopy Anchor Link

`string | undefined`: the id of the context entry. It is `undefined` on the first render and while `available` is `"disabled"`.

## ParametersCopy Anchor Link

Prop

Type

`description`string

`value`any

`available?`'enabled' | 'disabled'

`convert?`(description: string, value: any) => string

How is this guide?

GoodBad

[Previous PageuseHumanInTheLoop](https://docs.copilotkit.ai/reference/v1/hooks/useHumanInTheLoop)[Next PageuseCopilotAdditionalInstructions](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotAdditionalInstructions)
