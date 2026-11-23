---
url: https://docs.copilotkit.ai/reference/channels/classes/Transcripts/
title: Transcripts
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:24.308720+00:00
---

# Transcripts

> Source: https://docs.copilotkit.ai/reference/channels/classes/Transcripts/

Channels/Classes

# Transcripts

Append, query, retain, and delete an application-owned transcript keyed by a stable user identity.

Copy MarkdownOpen

`Transcripts` stores an optional SDK-owned record on the Channel's `StateStore`. Configure top-level `identifyUser` and `store.transcripts`.

## ConfigurationCopy Anchor Link

Copy Text
    
    
    const channel = createChannel({
      name: "support-slack",
      identifyUser: ({ actor }) => accounts.resolveApplicationUser(actor.id),
      agent: makeAgent,
      store: {
        adapter: durableStateStore,
        transcripts: {
          retention: "30d",
          maxPerUser: 500,
        },
      },
    });

`retention` accepts milliseconds or a duration string. Entries are stored on the `list` facet, so that facet must be durable for production transcripts.

## appendCopy Anchor Link

Copy Text
    
    
    await channel.transcripts.append(
      thread,
      {
        role: "assistant",
        text: "The incident owner is Payments.",
      },
      { userId: "usr_123" },
    );

Append silently does nothing when `userId` is `null`.

## listCopy Anchor Link

Copy Text
    
    
    const entries = await channel.transcripts.list({
      userId: "usr_123",
      limit: 20,
      roles: ["user", "assistant"],
    });

Entries are oldest-first. Filter them with `platforms` (for example `["slack"]`), `threadId`, or `roles`. Each entry has `role`, `text`, `platform`, `threadId`, `userId`, and `ts`. On managed Channels, `platform` is the native provider (`"slack"` or `"teams"`). Use the stable application `userId` to carry context between providers, and filter by platform only when you want one provider's entries.

## deleteCopy Anchor Link

Copy Text
    
    
    const { deleted } = await channel.transcripts.delete({
      userId: "usr_123",
    });

This deletes only the SDK-owned transcript. It does not delete provider history or a separate Intelligence record.

## Automatic bridgeCopy Anchor Link

`thread.runAgent({ transcript: true })` injects prior entries, appends the current user turn, runs the agent, and appends its response. Do not manually append those same turns.

`channel.transcripts` becomes available after the runtime starts the Channel. See [History and transcripts](https://docs.copilotkit.ai/slack/history-and-transcripts).

How is this guide?

GoodBad

[Previous PageThread](https://docs.copilotkit.ai/reference/channels/classes/Thread)[Next PageActions](https://docs.copilotkit.ai/reference/channels/components/Actions)
