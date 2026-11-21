---
url: https://docs.copilotkit.ai/reference/channels/types/ChannelNode/
title: ChannelNode
method: scrapling+scrapegraph
fetched_at: 2026-11-21T10:52:47.062166+00:00
---

# ChannelNode

> Source: https://docs.copilotkit.ai/reference/channels/types/ChannelNode/

Channels/Types

# ChannelNode

The serializable intermediate representation between Channels JSX and native provider renderers.

Copy MarkdownOpen

`ChannelNode` is the intermediate representation produced by Channels JSX.

Copy Text
    
    
    interface ChannelNode {
      type: string | ComponentFn | symbol;
      props: Record<string, unknown>;
      key?: string | number;
    }
    
    type Renderable =
      | string
      | ChannelNode
      | ChannelNode[]
      | { raw: unknown; provider?: "slack" | "teams" };

Before `renderToIR`, `type` can be a named component or Fragment. After expansion, intrinsic string types such as `message`, `section`, and `button` remain. Strings and numbers become `text` nodes.

Callbacks stay in the tree until the action registry replaces them with opaque ids. Provider credentials and handler source are never embedded in the native message.

Most applications should use components rather than constructing nodes directly. Reach for `ChannelNode` when writing component tests, a custom renderer, or a direct platform adapter.

See [`renderToIR`](https://docs.copilotkit.ai/reference/channels/functions/renderToIR).

How is this guide?

GoodBad

[Previous PageAgentContentPart](https://docs.copilotkit.ai/reference/channels/types/AgentContentPart)[Next PageIncomingMessage](https://docs.copilotkit.ai/reference/channels/types/IncomingMessage)
