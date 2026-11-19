---
url: https://docs.copilotkit.ai/reference/channels/types/ActionStore/
title: ActionStore
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:33.029532+00:00
---

# ActionStore

> Source: https://docs.copilotkit.ai/reference/channels/types/ActionStore/

Channels/Types

# ActionStore

Deprecated callback snapshot store and migration path to the current StateStore configuration.

Copy MarkdownOpen

`ActionStore` and `InMemoryActionStore` remain exported for compatibility, but both are deprecated. New Channels code should configure `createChannel({ store: { adapter } })`; callback snapshots use the `StateStore.kv` facet.

channel.ts

Copy Text
    
    
    import { createChannel } from "@copilotkit/channels";
    import { durableStateStore } from "./state-store.js";
    
    const channel = createChannel({
      name: required("CHANNEL_CODE"),
      identifyUser: "platform",
      agent: makeAgent,
      components: [ApprovalCard],
      store: { adapter: durableStateStore },
    });

The same Channel declaration receives managed Slack and Teams deliveries. The registered component lets the SDK rebuild its callback, while the durable store preserves the snapshot across process restarts.

## Deprecated contractCopy Anchor Link

Copy Text
    
    
    interface ActionStore {
      put(id: string, snapshot: ActionSnapshot, ttlMs?: number): Promise<void>;
      get(id: string): Promise<ActionSnapshot | undefined>;
      consume(id: string): Promise<ActionSnapshot | undefined>;
      delete(id: string): Promise<void>;
    }

`consume` must atomically return and delete one snapshot so a HITL continuation can start at most one resumed run.

`InMemoryActionStore` never survives a process restart. Do not introduce it in new managed Slack or Teams runners. See [`StateStore`](https://docs.copilotkit.ai/reference/channels/types/StateStore) and [persistence and scaling](https://docs.copilotkit.ai/slack/persistence-and-scaling).

How is this guide?

GoodBad

[Previous PageDirect provider adapters](https://docs.copilotkit.ai/reference/channels/sdk/direct-adapters)[Next PageAgentContentPart](https://docs.copilotkit.ai/reference/channels/types/AgentContentPart)
