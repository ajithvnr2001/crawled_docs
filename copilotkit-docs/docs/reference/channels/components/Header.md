---
url: https://docs.copilotkit.ai/reference/channels/components/Header/
title: Header
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:37.705969+00:00
---

# Header

> Source: https://docs.copilotkit.ai/reference/channels/components/Header/

Channels/Components

# Header

Render a portable title row in a Slack Block Kit message or Teams Adaptive Card.

Copy MarkdownOpen

`Header` renders prominent text near the top of a message.

Copy Text
    
    
    import { Header, Message } from "@copilotkit/channels/ui";
    
    <Message>
      <Header>INC-421 · Investigating</Header>
    </Message>;

Prop| Type| Description  
---|---|---  
`children`| `BotChildren`| Text and nested portable content.  
  
Managed Slack renders a plain-text header block. Managed Teams renders a large, bold, wrapping `TextBlock`. Keep the header short; each provider clamps text to its native payload budget.

How is this guide?

GoodBad

[Previous PageFields and Field](https://docs.copilotkit.ai/reference/channels/components/Fields)[Next PageImage](https://docs.copilotkit.ai/reference/channels/components/Image)
