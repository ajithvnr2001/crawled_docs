---
url: https://docs.copilotkit.ai/reference/channels/components/Input/
title: Input
method: scrapling+scrapegraph
fetched_at: 2026-11-25T12:31:14.129210+00:00
---

# Input

> Source: https://docs.copilotkit.ai/reference/channels/components/Input/

Channels/Components

# Input

Render a portable text input and understand its current managed-provider callback limits.

Copy MarkdownOpen

`Input` describes a single- or multiline text field.

Copy Text
    
    
    import { Button, Input, Message } from "@copilotkit/channels/ui";
    
    <Message>
      <Input
        name="reason"
        placeholder="Why should this be approved?"
        multiline
        onSubmit={async (ctx) => {
          await ctx.thread.post(`Recorded: ${String(ctx.action.value)}`);
        }}
      />
      <Button
        value="approve"
        onClick={async (ctx) => {
          const reason = ctx.values?.reason;
          if (reason !== undefined) {
            await ctx.thread.post(`Recorded: ${String(reason)}`);
          }
        }}
      >
        Approve
      </Button>
    </Message>;

## PropsCopy Anchor Link

Prop| Type| Description  
---|---|---  
`name`| `string`| Logical field name.  
`placeholder`| `string`| Native placeholder or label text.  
`multiline`| `boolean`| Requests a multiline native input.  
`onSubmit`| `ClickHandler<string>`| Text submission callback where the provider dispatches it.  
  
Managed Slack renders a dispatching plain-text input block. Managed Teams renders `Input.Text`. Give the field a `name` and place it with a submitting `Button`; Teams sends the text to the Button callback in `ctx.values[name]`, while Slack invokes `Input.onSubmit` as soon as the input is dispatched. Teams does not dispatch `Input.onSubmit` independently.

How is this guide?

GoodBad

[Previous PageImage](https://docs.copilotkit.ai/reference/channels/components/Image)[Next PageMarkdown](https://docs.copilotkit.ai/reference/channels/components/Markdown)
