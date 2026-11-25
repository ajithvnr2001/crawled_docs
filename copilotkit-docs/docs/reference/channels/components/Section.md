---
url: https://docs.copilotkit.ai/reference/channels/components/Section/
title: Section
method: scrapling+scrapegraph
fetched_at: 2026-11-25T12:31:13.951770+00:00
---

# Section

> Source: https://docs.copilotkit.ai/reference/channels/components/Section/

Channels/Components

# Section

Render a portable body-text section in Slack or Microsoft Teams.

Copy MarkdownOpen

`Section` renders the main body text of a rich message.

Copy Text
    
    
    import { Message, Section } from "@copilotkit/channels/ui";
    
    <Message>
      <Section>Checkout latency is **above the SLO**.</Section>
    </Message>;

Prop| Type| Description  
---|---|---  
`children`| `BotChildren`| Text and nested portable content.  
  
Managed Slack converts GitHub-flavored Markdown to Slack `mrkdwn`. Managed Teams renders a wrapping Adaptive Card `TextBlock`. Provider Markdown dialects are not identical, so verify complex tables, mentions, and links in both clients.

How is this guide?

GoodBad

[Previous PageModal](https://docs.copilotkit.ai/reference/channels/components/Modal)[Next PageSelect](https://docs.copilotkit.ai/reference/channels/components/Select)
