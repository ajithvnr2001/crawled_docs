---
url: https://docs.copilotkit.ai/reference/channels/components/Context/
title: Context
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:37.860586+00:00
---

# Context

> Source: https://docs.copilotkit.ai/reference/channels/components/Context/

Channels/Components

# Context

Render muted metadata or footnote text in a portable Channels message.

Copy MarkdownOpen

`Context` renders secondary metadata below the main message content.

Copy Text
    
    
    import { Context, Message, Section } from "@copilotkit/channels/ui";
    
    <Message>
      <Section>Deployment completed.</Section>
      <Context>Production · commit 4f8a2d1</Context>
    </Message>;

Prop| Type| Description  
---|---|---  
`children`| `BotChildren`| Secondary text content.  
  
Managed Slack renders a context block. Managed Teams renders small, subtle, wrapping text. Do not place a required instruction only in `Context`, because native clients intentionally de-emphasize it.

How is this guide?

GoodBad

[Previous PageChart](https://docs.copilotkit.ai/reference/channels/components/Chart)[Next PageDivider](https://docs.copilotkit.ai/reference/channels/components/Divider)
