---
url: https://docs.copilotkit.ai/reference/channels/components/Message/
title: Message
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:23.873510+00:00
---

# Message

> Source: https://docs.copilotkit.ai/reference/channels/components/Message/

Channels/Components

# Message

Root container for portable Channels content and reaction behavior.

Copy MarkdownOpen

`Message` groups one portable message tree.

Copy Text
    
    
    import { Message, Section } from "@copilotkit/channels/ui";
    
    <Message>
      <Section>Checkout latency is above the SLO.</Section>
    </Message>;

## PropsCopy Anchor Link

Prop| Type| Description  
---|---|---  
`accent`| `string`| Optional renderer hint. Direct adapters may map it natively; the current managed Slack and Teams connectors ignore it.  
`fallbackText`| `string`| Plain-text notification and screen-reader summary for rich Slack output.  
`onReaction`| `MessageReactionHandler`| Handles an added or removed reaction on this posted message.  
`children`| `BotChildren`| Portable Channels content.  
  
`onReaction` receives the normalized emoji first and a reaction context second. The context contains `emoji`, `rawEmoji`, `added`, `user`, `actor`, `thread`, `messageId`, and `messageRef`. `actor` is the provider account that reacted. Use it when `user` is `null`.

Copy Text
    
    
    <Message
      onReaction={async (emoji, reaction) => {
        const marked = reaction.added && emoji === "eyes";
        await reaction.thread.post(
          marked ? "Marked for follow-up." : "Reaction update received.",
        );
      }}
    >
      <Section>React with 👀 to request follow-up.</Section>
    </Message>

Managed Slack routes reactions on bot-authored messages. Managed Teams routes delivered `messageReaction` activities. The bot can also add and remove its own reactions with `thread.react(ref, emoji)` and `thread.unreact(ref, emoji)`.

An output-free managed reaction callback is finalized and acknowledged. Silent audit-only work is supported, but make the side effect idempotent because managed delivery is at-least-once.

Register named components containing `onReaction` in `createChannel({ components })`. A reaction to an older message survives a process restart when the snapshot is in a durable `StateStore`: the default managed store, or your own `store.adapter`.

How is this guide?

GoodBad

[Previous PageMarkdown](https://docs.copilotkit.ai/reference/channels/components/Markdown)[Next PageModal](https://docs.copilotkit.ai/reference/channels/components/Modal)
