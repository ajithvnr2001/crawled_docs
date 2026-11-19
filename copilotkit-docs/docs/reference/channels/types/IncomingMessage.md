---
url: https://docs.copilotkit.ai/reference/channels/types/IncomingMessage/
title: IncomingMessage
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:32.986335+00:00
---

# IncomingMessage

> Source: https://docs.copilotkit.ai/reference/channels/types/IncomingMessage/

Channels/Types

# IncomingMessage

The normalized provider message passed to Channels handlers, including user, multimodal parts, and managed correlation ids.

Copy MarkdownOpen

`IncomingMessage` is the normalized inbound turn passed to `onMessage`, `onMention`, tools, and interaction contexts.

## ShapeCopy Anchor Link

Copy Text
    
    
    interface IncomingMessage {
      text: string;
      user: ApplicationUser | null;
      actor: ProviderActor;
      ref: MessageRef;
      platform: string;
      operation?: MessageOperation;
      contentParts?: AgentContentPart[];
      eventId?: string;
      turnId?: string;
      deliveryId?: string;
    }

Field| Managed Slack and Teams behavior  
---|---  
`text`| Provider text after ingress normalization.  
`user`| Nullable application user returned by the Channel's `identifyUser` policy.  
`actor`| Provider account that caused the event. It includes a required actor kind.  
`ref`| In ordinary message handlers this may have an empty id; do not assume every inbound turn can be edited.  
`platform`| Native source: `"slack"` or `"teams"` for message deliveries.  
`operation`| Present on `onMessage` and `onMention` turns: `kind` (`"created"`, `"updated"`, or `"deleted"`), `logicalMessageId`, `revisionId`, and `mentioned`. Edits and deletes also reach these handlers, so check `kind` before you run the agent.  
`contentParts`| Hydrated file/media parts when attachments were retrieved.  
`eventId`| Stable provider-event id for application idempotency.  
`turnId`| Managed turn correlation id.  
`deliveryId`| Managed lease/delivery correlation id.  
  
## Multimodal promptCopy Anchor Link

Copy Text
    
    
    const prompt = message.contentParts?.length
      ? [
          ...(message.text ? [{ type: "text" as const, text: message.text }] : []),
          ...message.contentParts,
        ]
      : message.text;
    
    await thread.runAgent({ prompt });

Managed history excludes the current inbound turn. `runAgent()` injects the message automatically when `prompt` is omitted; use the explicit combined prompt above when a turn can contain both text and attachments. See [Files and multimodal input](https://docs.copilotkit.ai/slack/files-and-multimodality).

How is this guide?

GoodBad

[Previous PageChannelNode](https://docs.copilotkit.ai/reference/channels/types/ChannelNode)[Next PageInteractionContext](https://docs.copilotkit.ai/reference/channels/types/InteractionContext)
