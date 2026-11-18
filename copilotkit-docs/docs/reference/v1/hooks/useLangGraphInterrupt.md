---
url: https://docs.copilotkit.ai/reference/v1/hooks/useLangGraphInterrupt/
title: useLangGraphInterrupt
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:59.222286+00:00
---

# useLangGraphInterrupt

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useLangGraphInterrupt/

React/v1

# useLangGraphInterrupt

The useLangGraphInterrupt hook allows setting the generative UI to be displayed on LangGraph's Interrupt event.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

  


`useLangGraphInterrupt` is still supported, but we recommend migrating to [`useInterrupt`](https://docs.copilotkit.ai/reference/v2/hooks/useInterrupt) from the v2 API. `useInterrupt` uses the same `render: ({ event, resolve }) => ...` pattern to render UI for an interrupt and resume the agent with the user's response. In v2, `event.value` can arrive as a JSON string. Parse it before you read its fields.

`useLangGraphInterrupt` is a React hook that you can use in your application to provide custom UI to be rendered when using `interrupt` by LangGraph. When LangGraph emits an interrupt, the hook renders your component. The user answers in it, and `resolve` sends the answer back to the agent.

## UsageCopy Anchor Link

### Simple UsageCopy Anchor Link

app/page.tsx

Copy Text
    
    
    import { useLangGraphInterrupt } from "@copilotkit/react-core";
    // ...
    
    const YourMainContent = () => {
      // ...
      // styles omitted for brevity
      useLangGraphInterrupt<string>({
        render: ({ event, resolve }) => (
          <div>
            <p>{event.value}</p>
            <form onSubmit={(e) => {
              e.preventDefault();
              resolve((e.target as HTMLFormElement).response.value);
            }}>
              <input type="text" name="response" placeholder="Enter your response" />
              <button type="submit">Submit</button>
            </form>
          </div>
        )
      });
      // ...
    
      return <div>{/* ... */}</div>
    }

## ParametersCopy Anchor Link

Prop

Type

`action`Omit<LangGraphInterruptRender<TEventValue>, "id">

`dependencies?`any[]

How is this guide?

GoodBad

[Previous PageuseCoAgentStateRender](https://docs.copilotkit.ai/reference/v1/hooks/useCoAgentStateRender)[Next PageuseCopilotAction](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotAction)
