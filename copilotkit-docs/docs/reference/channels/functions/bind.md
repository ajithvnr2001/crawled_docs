---
url: https://docs.copilotkit.ai/reference/channels/functions/bind/
title: bind
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:33.357429+00:00
---

# bind

> Source: https://docs.copilotkit.ai/reference/channels/functions/bind/

Channels/Functions

# bind

Reuse a Channels interaction handler while binding a serializable value into action.value.

Copy MarkdownOpen

`bind(handler, args)` returns a click handler that replaces `ctx.action.value` with `args`.

## SignatureCopy Anchor Link

Copy Text
    
    
    function bind(handler: ClickHandler, args: unknown): ClickHandler;

issue-actions.tsx

Copy Text
    
    
    import { Actions, Button, bind } from "@copilotkit/channels/ui";
    import type { InteractionContext } from "@copilotkit/channels/ui";
    
    async function assign({ thread, action }: InteractionContext) {
      if (typeof action.value !== "string") return;
      await assignments.assign(action.value);
      await thread.post(`Assigned ${action.value}.`);
    }
    
    export function IssueActions({ issueId }: { issueId: string }) {
      return (
        <Actions>
          <Button onClick={bind(assign, issueId)}>Assign to me</Button>
        </Actions>
      );
    }

For a one-off button, the `value` prop is usually clearer:

Copy Text
    
    
    <Button value={issueId} onClick={assign}>
      Assign to me
    </Button>

Bound values and registered component props must be JSON-serializable if the callback must survive a restart. Register the named component. The snapshot must be in a durable `StateStore`: the default managed store, or your own `store.adapter`.

How is this guide?

GoodBad

[Previous PageTable, Row, and Cell](https://docs.copilotkit.ai/reference/channels/components/Table)[Next PagecreateChannel](https://docs.copilotkit.ai/reference/channels/functions/createChannel)
