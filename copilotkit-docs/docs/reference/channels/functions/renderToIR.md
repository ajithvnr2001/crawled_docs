---
url: https://docs.copilotkit.ai/reference/channels/functions/renderToIR/
title: renderToIR
method: scrapling+scrapegraph
fetched_at: 2026-11-25T12:31:13.477763+00:00
---

# renderToIR

> Source: https://docs.copilotkit.ai/reference/channels/functions/renderToIR/

Channels/Functions

# renderToIR

Lower Channels JSX or text into the serializable ChannelNode intermediate representation.

Copy MarkdownOpen

`renderToIR(renderable)` expands fragments and function components into an array of intrinsic `ChannelNode` values.

## SignatureCopy Anchor Link

Copy Text
    
    
    function renderToIR(ui: Renderable): ChannelNode[];

Copy Text
    
    
    type Renderable =
      | string
      | ChannelNode
      | ChannelNode[]
      | { raw: unknown; provider?: "slack" | "teams" };

## ExampleCopy Anchor Link

Copy Text
    
    
    import { Header, Message, renderToIR } from "@copilotkit/channels/ui";
    
    const ir = renderToIR(
      <Message>
        <Header>Incident update</Header>
      </Message>,
    );

The runtime calls this automatically before binding callbacks and rendering a message. Use it directly for component tests or a custom adapter.

Strings and numbers used as component children become `text` nodes. `false`, `null`, and `undefined` render nothing. Function components are evaluated immediately, so keep them pure and free of provider side effects.

The `{ raw, provider }` escape hatch produces a provider-specific `raw` node. Use `provider: "slack"` for native blocks and `provider: "teams"` for one Adaptive Card object. Omitting `provider` defaults to Slack. A raw node sent through the wrong active provider fails explicitly before that effect reaches the provider; it is never translated or silently dropped.

How is this guide?

GoodBad

[Previous PagedefineChannelTool](https://docs.copilotkit.ai/reference/channels/functions/defineChannelTool)[Next PageDirect provider adapters](https://docs.copilotkit.ai/reference/channels/sdk/direct-adapters)
