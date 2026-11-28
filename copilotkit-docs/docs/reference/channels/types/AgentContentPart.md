---
url: https://docs.copilotkit.ai/reference/channels/types/AgentContentPart/
title: AgentContentPart
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:15.915710+00:00
---

# AgentContentPart

> Source: https://docs.copilotkit.ai/reference/channels/types/AgentContentPart/

Channels/Types

# AgentContentPart

Provider-neutral text, image, audio, video, and document content passed from Channel attachments to an agent.

Copy MarkdownOpen

`AgentContentPart` is the multimodal prompt union used by Channels.

Copy Text
    
    
    type MediaDataSource = {
      type: "data";
      value: string;
      mimeType: string;
    };
    
    type AgentContentPart =
      | { type: "text"; text: string }
      | { type: "image"; source: MediaDataSource }
      | { type: "audio"; source: MediaDataSource }
      | { type: "video"; source: MediaDataSource }
      | { type: "document"; source: MediaDataSource };

Binary `value` is base64. Managed ingress maps image, audio, video, and PDF files to binary parts, decodes `text/*` as text, and represents other binary types with a text note.

Pass parts through `thread.runAgent({ prompt })`. The selected agent framework and model decide which media kinds they can consume.

See [Files and multimodal input](https://docs.copilotkit.ai/slack/files-and-multimodality).

How is this guide?

GoodBad

[Previous PageActionStore](https://docs.copilotkit.ai/reference/channels/types/ActionStore)[Next PageChannelNode](https://docs.copilotkit.ai/reference/channels/types/ChannelNode)
