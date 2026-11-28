---
url: https://docs.copilotkit.ai/reference/channels/components/Fields/
title: Fields and Field
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:16.574831+00:00
---

# Fields and Field

> Source: https://docs.copilotkit.ai/reference/channels/components/Fields/

Channels/Components

# Fields and Field

Render compact label-value facts in Slack and Microsoft Teams.

Copy MarkdownOpen

`Fields` groups `Field` values into a compact fact layout.

Copy Text
    
    
    import { Field, Fields, Message } from "@copilotkit/channels/ui";
    
    <Message>
      <Fields>
        <Field>Owner: Payments</Field>
        <Field>Status: Investigating</Field>
      </Fields>
    </Message>;

## PropsCopy Anchor Link

Component| Prop| Type| Description  
---|---|---|---  
`Fields`| `children`| `BotChildren`| `Field` children.  
`Field`| `label`| `string`| Optional provider label. Managed Slack renders it in bold.  
`Field`| `children`| `BotChildren`| Field value.  
  
Managed Slack creates section fields and honors the `label` prop. Managed Teams creates an Adaptive Card `FactSet` by splitting each field's text at the first colon; it does not currently read the `label` prop. Use `Label: value` text, as in the example, when the same component must preserve labels in both providers.

How is this guide?

GoodBad

[Previous PageDivider](https://docs.copilotkit.ai/reference/channels/components/Divider)[Next PageHeader](https://docs.copilotkit.ai/reference/channels/components/Header)
