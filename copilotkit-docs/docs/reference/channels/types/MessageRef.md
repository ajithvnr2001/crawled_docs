---
url: https://docs.copilotkit.ai/reference/channels/types/MessageRef/
title: MessageRef
method: scrapling+scrapegraph
fetched_at: 2026-11-25T12:31:13.040816+00:00
---

# MessageRef

> Source: https://docs.copilotkit.ai/reference/channels/types/MessageRef/

Channels/Types

# MessageRef

The opaque provider message handle returned by post and supplied to managed interaction callbacks.

Copy MarkdownOpen

`MessageRef` identifies a provider message:

Copy Text
    
    
    interface MessageRef {
      id: string;
      [key: string]: unknown;
    }

Use a ref with `thread.update()` or `thread.delete()`:

Copy Text
    
    
    const ref = await thread.post("Working…");
    await thread.update(ref, "Done.");

## Managed lifetimeCopy Anchor Link

A ref returned by `thread.post()` carries routing for the current managed delivery. Do not persist it and assume it can be edited in a later delivery.

For a later component callback, use `ctx.message.ref`. Intelligence stamps the source provider message onto that interaction delivery when available:

Copy Text
    
    
    if (message.ref.id) {
      try {
        await thread.update(message.ref, "Updated");
      } catch {
        // Provider updates are best-effort.
      }
    }

Teams `Action.Submit` can arrive without `replyToId`, producing an empty ref. Slack and Teams delete capabilities also differ; see [`Thread`](https://docs.copilotkit.ai/reference/channels/classes/Thread).

How is this guide?

GoodBad

[Previous PageJSX callbacks](https://docs.copilotkit.ai/reference/channels/types/JSXCallbacks)[Next PageStateStore](https://docs.copilotkit.ai/reference/channels/types/StateStore)
