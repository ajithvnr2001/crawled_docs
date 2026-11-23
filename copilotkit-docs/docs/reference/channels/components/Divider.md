---
url: https://docs.copilotkit.ai/reference/channels/components/Divider/
title: Divider
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:23.802078+00:00
---

# Divider

> Source: https://docs.copilotkit.ai/reference/channels/components/Divider/

Channels/Components

# Divider

Add a portable visual separator to a rich Channels message.

Copy MarkdownOpen

`Divider` takes no props or children.

Copy Text
    
    
    import { Divider, Message, Section } from "@copilotkit/channels/ui";
    
    <Message>
      <Section>Summary</Section>
      <Divider />
      <Section>Next action</Section>
    </Message>;

Managed Slack renders a divider block. Adaptive Cards have no standalone rule element, so managed Teams renders an empty separated text block to create the visual boundary.

How is this guide?

GoodBad

[Previous PageContext](https://docs.copilotkit.ai/reference/channels/components/Context)[Next PageFields and Field](https://docs.copilotkit.ai/reference/channels/components/Fields)
