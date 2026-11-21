---
url: https://docs.copilotkit.ai/reference/channels/components/Select/
title: Select
method: scrapling+scrapegraph
fetched_at: 2026-11-21T10:52:47.501685+00:00
---

# Select

> Source: https://docs.copilotkit.ai/reference/channels/components/Select/

Channels/Components

# Select

Render a portable single- or multi-select control and understand its current managed-provider limits.

Copy MarkdownOpen

`Select` describes a list of string choices.

Copy Text
    
    
    import { Actions, Button, Select } from "@copilotkit/channels/ui";
    
    <Actions>
      <Select
        name="owner"
        placeholder="Choose an owner"
        options={[
          { label: "Payments", value: "payments" },
          { label: "Identity", value: "identity" },
        ]}
        onSelect={async (ctx) => {
          await ctx.thread.post(`Selected ${String(ctx.action.value)}.`);
        }}
      />
      <Button
        value="assign"
        onClick={async (ctx) => {
          const owner = ctx.values?.owner;
          if (owner !== undefined) {
            await ctx.thread.post(`Selected ${String(owner)}.`);
          }
        }}
      >
        Assign
      </Button>
    </Actions>;

## PropsCopy Anchor Link

Prop| Type| Description  
---|---|---  
`name`| `string`| Stable field key used in Teams `ctx.values` when a Button submits the card.  
`options`| `{ label: string; value: string }[]`| Required choices.  
`placeholder`| `string`| Native placeholder text.  
`multi`| `boolean`| Allows multiple selections where the provider supports them.  
`onSelect`| `ClickHandler<string | string[]>`| Selection callback. `multi` selections use a string array.  
  
Managed Slack emits a dispatching static select; `multi` becomes a `multi_static_select` input block. Managed Teams renders an Adaptive Card `Input.ChoiceSet`. Slack invokes `Select.onSelect` when the selection is dispatched; Teams sends the selected field to the submitting Button in `ctx.values[name]`. Teams does not dispatch `Select.onSelect` independently.

How is this guide?

GoodBad

[Previous PageSection](https://docs.copilotkit.ai/reference/channels/components/Section)[Next PageTable, Row, and Cell](https://docs.copilotkit.ai/reference/channels/components/Table)
