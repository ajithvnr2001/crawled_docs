---
url: https://docs.copilotkit.ai/reference/channels/classes/MemoryStore/
title: MemoryStore
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:16.904961+00:00
---

# MemoryStore

> Source: https://docs.copilotkit.ai/reference/channels/classes/MemoryStore/

Channels/Classes

# MemoryStore

The built-in process-local StateStore used when a Channel has no explicit persistence adapter.

Copy MarkdownOpen

`MemoryStore` implements the complete `StateStore` interface in one Node process.

Copy Text
    
    
    import { MemoryStore } from "@copilotkit/channels";
    
    const store = new MemoryStore();
    
    const channel = createChannel({
      name: "support-slack",
      identifyUser: "platform",
      agent: makeAgent,
      store: { adapter: store },
    });

It supports key/value TTLs, lists, locks, deduplication, and queues. It is also the SDK default when no explicit or adapter-provided store exists.

Process-local only

Values disappear on restart and are not shared between replicas. Do not use MemoryStore for restart-safe approvals, durable workflow state, or cross-process locking.

MemoryStore preserves JavaScript values by reference, while a remote `StateStore` must round-trip JSON. Test application state with the production backend so a `Date`, `Map`, or class instance does not pass locally and fail after deployment.

See [`StateStore`](https://docs.copilotkit.ai/reference/channels/types/StateStore) and [Persistence and scaling](https://docs.copilotkit.ai/slack/persistence-and-scaling).

How is this guide?

GoodBad

[Previous PageChannel](https://docs.copilotkit.ai/reference/channels/classes/Channel)[Next PageThread](https://docs.copilotkit.ai/reference/channels/classes/Thread)
