---
url: https://docs.copilotkit.ai/reference/v1/hooks/useHumanInTheLoop/
title: useHumanInTheLoop
method: scrapling+scrapegraph
fetched_at: 2026-11-27T11:59:06.945755+00:00
---

# useHumanInTheLoop

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useHumanInTheLoop/

React/v1

# useHumanInTheLoop

The useHumanInTheLoop hook enables human approval and interaction workflows.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

This is the v1 `useHumanInTheLoop`, which takes an array of parameter definitions. It is still supported, but we recommend migrating to the [v2 `useHumanInTheLoop`](https://docs.copilotkit.ai/reference/v2/hooks/useHumanInTheLoop) (from `@copilotkit/react-core/v2`), which uses Zod schemas for parameters.

`useHumanInTheLoop` pauses the agent to request human input or approval. When the agent calls this tool, it stops and waits for the user to respond through your custom UI before continuing. This is essential for sensitive operations, confirmations, or collecting information that only the user can provide.

Unlike `useFrontendTool`, there's no handler function. Instead, your render function receives a `respond` callback that sends the user's input back to the agent. The agent remains paused until `respond` is called, making this a true blocking interaction.

## UsageCopy Anchor Link

### Simple Confirmation ExampleCopy Anchor Link

Copy Text
    
    
    import { useHumanInTheLoop } from "@copilotkit/react-core";
    
    useHumanInTheLoop({
      name: "confirmDeletion",
      description: "Ask user to confirm before deleting items",
      parameters: [
        {
          name: "itemName",
          type: "string",
          description: "Name of the item to delete",
          required: true,
        },
        {
          name: "itemCount",
          type: "number",
          description: "Number of items to delete",
          required: true,
        },
      ],
      render: ({ args, status, respond, result }) => {
        if (status === "executing" && respond) {
          return (
            <div className="p-4 border rounded">
              <p>Are you sure you want to delete {args.itemCount} {args.itemName}(s)?</p>
              <div className="flex gap-2 mt-4">
                <button
                  onClick={() => respond({ confirmed: true })}
                  className="bg-red-500 text-white px-4 py-2 rounded"
                >
                  Delete
                </button>
                <button
                  onClick={() => respond({ confirmed: false })}
                  className="bg-gray-300 px-4 py-2 rounded"
                >
                  Cancel
                </button>
              </div>
            </div>
          );
        }
    
        if (status === "complete" && result) {
          return (
            <div className="p-2 text-sm text-gray-600">
              {result.confirmed ? "Items deleted" : "Deletion cancelled"}
            </div>
          );
        }
    
        return null;
      },
    });

### Complex Input Collection ExampleCopy Anchor Link

Copy Text
    
    
    import { useHumanInTheLoop } from "@copilotkit/react-core";
    import { useState } from "react";
    
    useHumanInTheLoop({
      name: "collectUserPreferences",
      description: "Collect detailed preferences from the user",
      parameters: [
        {
          name: "context",
          type: "string",
          description: "Context for why preferences are needed",
          required: true,
        },
        {
          name: "requiredFields",
          type: "string[]",
          description: "Fields to collect",
          required: true,
        },
      ],
      render: ({ args, status, respond }) => {
        const [preferences, setPreferences] = useState({
          theme: "light",
          notifications: true,
          language: "en",
        });
    
        if (status === "executing" && respond) {
          return (
            <div className="p-4 border rounded">
              <h3 className="font-bold mb-2">{args.context}</h3>
              <form onSubmit={(e) => {
                e.preventDefault();
                respond(preferences);
              }}>
                <button
                  type="submit"
                  className="bg-blue-500 text-white px-4 py-2 rounded"
                >
                  Save Preferences
                </button>
              </form>
            </div>
          );
        }
    
        return null;
      },
    });

## Best PracticesCopy Anchor Link

  1. Always check for the `respond` function before rendering interactive elements
  2. Handle all status states to provide good user feedback
  3. Validate user input before calling `respond`
  4. Provide clear instructions in your UI about what input is expected
  5. Consider timeout scenarios for time-sensitive operations



## Migration from useCopilotActionCopy Anchor Link

If you're migrating from `useCopilotAction` with `renderAndWaitForResponse`:

Copy Text
    
    
    // Before with useCopilotAction
    useCopilotAction({
      name: "confirmAction",
      parameters: [
        { name: "message", type: "string", required: true },
      ],
      renderAndWaitForResponse: ({ args, respond, status }) => {
        return (
          <ConfirmDialog
            message={args.message}
            onConfirm={() => respond(true)}
            onCancel={() => respond(false)}
            isActive={status === "executing"}
          />
        );
      },
    });
    
    // After with useHumanInTheLoop
    useHumanInTheLoop({
      name: "confirmAction",
      parameters: [
        {
          name: "message",
          type: "string",
          description: "The message to display",
          required: true,
        },
      ],
      render: ({ args, respond, status }) => {
        if (status === "executing" && respond) {
          return (
            <ConfirmDialog
              message={args.message}
              onConfirm={() => respond(true)}
              onCancel={() => respond(false)}
              isActive={true}
            />
          );
        }
        return null;
      },
    });

The main differences are:

  1. The property is called `render` instead of `renderAndWaitForResponse`
  2. You need to check for the `respond` function's existence



## ParametersCopy Anchor Link

Prop

Type

`name`string

`description?`string

`parameters?`T

`render`FrontendAction<T>['renderAndWaitForResponse']

`available?`'disabled' | 'enabled'

`followUp?`boolean

`dependencies?`any[]

How is this guide?

GoodBad

[Previous PageuseRenderToolCall](https://docs.copilotkit.ai/reference/v1/hooks/useRenderToolCall)[Next PageuseCopilotReadable](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotReadable)
