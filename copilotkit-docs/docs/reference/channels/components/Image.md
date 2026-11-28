---
url: https://docs.copilotkit.ai/reference/channels/components/Image/
title: Image
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:16.545638+00:00
---

# Image

> Source: https://docs.copilotkit.ai/reference/channels/components/Image/

Channels/Components

# Image

Render an image URL inside a portable Slack or Microsoft Teams message.

Copy MarkdownOpen

`Image` adds an externally reachable image to a rich message.

Copy Text
    
    
    import { Image, Message } from "@copilotkit/channels/ui";
    
    <Message>
      <Image
        url="https://example.com/status.png"
        alt="Checkout latency over the last hour"
      />
    </Message>;

Prop| Type| Description  
---|---|---  
`url`| `string`| Required image URL.  
`alt`| `string`| Accessible alternative text.  
  
Managed Slack renders an image block. Managed Teams renders an Adaptive Card image. The provider client must be able to fetch the URL without your application's private cookies or headers. Use `thread.postFile()` when the image must be uploaded as bytes.

How is this guide?

GoodBad

[Previous PageHeader](https://docs.copilotkit.ai/reference/channels/components/Header)[Next PageInput](https://docs.copilotkit.ai/reference/channels/components/Input)
