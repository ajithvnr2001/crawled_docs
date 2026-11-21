---
url: https://docs.copilotkit.ai/reference/channels/components/Button/
title: Button
method: scrapling+scrapegraph
fetched_at: 2026-11-21T10:52:48.220212+00:00
---

# Button

> Source: https://docs.copilotkit.ai/reference/channels/components/Button/

Channels/Components

# Button

Post a portable callback or link button in Slack and Microsoft Teams.

Copy MarkdownOpen

`Button` creates the most portable managed interaction control.

Copy Text
    
    
    import { Actions, Button } from "@copilotkit/channels/ui";
    
    <Actions>
      <Button
        value={{ approved: true }}
        style="primary"
        onClick={async ({ action, thread }) => {
          if (action.value) await thread.resume(action.value);
        }}
      >
        Approve
      </Button>
    </Actions>;

## PropsCopy Anchor Link

Prop| Type| Description  
---|---|---  
`value`| `TValue`| JSON-serializable value returned as `ctx.action.value`. It also infers the callback value type.  
`onClick`| `ClickHandler<TValue>`| Callback for a native button submission.  
`url`| `string`| Creates a native link button. When set, `onClick` and `value` are ignored.  
`style`| `"primary" | "danger"`| Maps to the closest provider emphasis.  
`children`| `BotChildren`| Button label.  
  
Managed Slack renders a Block Kit button. Managed Teams renders `Action.Submit`, or `Action.OpenUrl` when `url` is set. A Teams submission can arrive without a source message reference, so only call `thread.update()` when `ctx.message.ref.id` is non-empty.

Register the named component that owns `onClick`. Buttons stay usable across a runner restart when the snapshot is in a durable `StateStore`: the default managed store, or your own `store.adapter`.

How is this guide?

GoodBad

[Previous PageActions](https://docs.copilotkit.ai/reference/channels/components/Actions)[Next PageChart](https://docs.copilotkit.ai/reference/channels/components/Chart)
