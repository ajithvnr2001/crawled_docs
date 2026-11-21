---
url: https://docs.copilotkit.ai/reference/channels/components/Markdown/
title: Markdown
method: scrapling+scrapegraph
fetched_at: 2026-11-21T10:52:47.857074+00:00
---

# Markdown

> Source: https://docs.copilotkit.ai/reference/channels/components/Markdown/

Channels/Components

# Markdown

Render an explicit portable Markdown text block.

Copy MarkdownOpen

`Markdown` is an explicit body-text block for formatted content.

Copy Text
    
    
    import { Markdown, Message } from "@copilotkit/channels/ui";
    
    <Message>
      <Markdown>{"**Owner:** Payments\n\n`p95 = 1.8s`"}</Markdown>
    </Message>;

Prop| Type| Description  
---|---|---  
`children`| `BotChildren`| Markdown text and portable child content.  
  
It currently maps to the same provider primitives as [`Section`](https://docs.copilotkit.ai/reference/channels/components/Section): Slack `mrkdwn` and a wrapping Teams `TextBlock`. Use it when the semantic intent of the source is formatted text.

How is this guide?

GoodBad

[Previous PageInput](https://docs.copilotkit.ai/reference/channels/components/Input)[Next PageMessage](https://docs.copilotkit.ai/reference/channels/components/Message)
