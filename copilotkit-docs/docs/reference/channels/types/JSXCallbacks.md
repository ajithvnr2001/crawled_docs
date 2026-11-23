---
url: https://docs.copilotkit.ai/reference/channels/types/JSXCallbacks/
title: JSX callbacks
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:22.435793+00:00
---

# JSX callbacks

> Source: https://docs.copilotkit.ai/reference/channels/types/JSXCallbacks/

Channels/Types

# JSX callbacks

Reference for portable component handlers and their managed Slack and Teams interaction context.

Copy MarkdownOpen

Portable Channels components can carry callbacks. Slack and Teams receive opaque action ids; the SDK resolves the original handler when the interaction returns.

Slack renders the controls as Block Kit. With Slack app Interactivity enabled, clicks arrive as `block_actions` through the signed managed webhook.

Teams renders the controls in Adaptive Cards. Buttons use `Action.Submit`, and clicks return through the managed connection as message activities. A Teams `Action.Submit` activity can arrive without a source message ref; in that case, `message.ref.id` is empty.

## Callback propsCopy Anchor Link

Component| Prop| Handler value  
---|---|---  
`Button`| `onClick`| `InteractionContext<TValue>`; read the Button's `value` from `action.value`  
`Select`| `onSelect`| `InteractionContext<string | string[]>`; arrays are used when `multi` is set  
`Input`| `onSubmit`| `InteractionContext<string>` containing the submitted text  
`Message`| `onReaction`| `(emoji, reaction)`  
  
Managed Teams control boundary

Managed Teams dispatches `Button` submissions. Named `Select` and `Input` fields from the same Adaptive Card are available on that Button callback as `ctx.values`, but Teams does not dispatch their `onSelect` or `onSubmit` callbacks independently.

## Portable component propsCopy Anchor Link

Import these components from `@copilotkit/channels/ui`. Renderers may simplify or omit a component when the native provider has no equivalent.

Component| Key props  
---|---  
`Message`| `accent?`, `fallbackText?`, `onReaction?`, `children?`  
`Header`, `Section`, `Markdown`, `Context`, `Actions`| `children?`  
`Fields` / `Field`| `children?`; `Field` also accepts `label?`  
`Button`| `value?`, `onClick?`, `url?`, `style?: "primary" | "danger"`, `children?`  
`Select`| `name?`, `options`, `placeholder?`, `multi?`, `onSelect?`  
`Input`| `name?`, `placeholder?`, `multiline?`, `onSubmit?`  
`Image`| `url`, `alt?`  
`Render`| `alt`, `width?`, `height?`, `children?`  
`Carousel` / `CarouselCard`| `children?`  
`Divider`| No props or children  
`Table` / `Row` / `Cell`| `Table.columns?`; nested rows and cells are children  
`Chart`| `data`, plus optional `type`, `title`, `xAxisTitle`, and `yAxisTitle`  
  
`Button.url` creates a link button and ignores `value` and `onClick`. `Select.options` is an array of `{ label, value }`. `Chart.data` is an array of `{ label, value }`; unsupported native chart surfaces omit the chart.

## InteractionContextCopy Anchor Link

`Button`, `Select`, and `Input` callbacks receive:

Field| Type| Description  
---|---|---  
`thread`| `Thread`| Post, update, run, or resume the conversation.  
`message`| `IncomingMessage`| Message containing the control. Its ref is updateable only when the interaction carries a non-empty `message.ref.id`.  
`action.id`| `string`| Opaque action identifier.  
`action.value`| `TValue | undefined`| The control's round-tripped value. Guard it before use even when the component declares `value`.  
`values`| `Record<string, unknown>`| Submitted form values.  
`user`| `ApplicationUser | null`| Application user selected by `identifyUser`.  
`actor`| `ProviderActor`| Provider account that caused the interaction.  
`platform`| `string`| Normalized source provider, such as `"slack"` or `"teams"`.  
`openModal`| function or `undefined`| Capability-gated modal opener. Not part of the managed Slack/Teams realtime path.  
  
decision.tsx

Copy Text
    
    
    import { Actions, Button, Message, Section } from "@copilotkit/channels/ui";
    
    export function Decision({ id }: { id: string }) {
      return (
        <Message>
          <Section>{`Approve ${id}?`}</Section>
          <Actions>
            <Button
              value={{ id, approved: true }}
              onClick={async ({ thread, message, action }) => {
                const value = action.value;
                if (value === undefined) return;
    
                if (message.ref.id) {
                  try {
                    await thread.update(message.ref, `Approved ${value.id}.`);
                  } catch {
                    // Updating the card is best-effort; always resume the agent.
                  }
                }
                await thread.resume(value);
              }}
            >
              Approve
            </Button>
          </Actions>
        </Message>
      );
    }

An interaction ref is updateable only when `message.ref.id` is non-empty. Always resume outside the update guard and error handler so an omitted ref or failed card update cannot strand the interrupted run.

## Reaction callbackCopy Anchor Link

`Message.onReaction` receives `(emoji, reaction)`. The reaction contains `emoji`, `rawEmoji`, `added`, `user`, `actor`, `messageId`, `messageRef`, and `thread`. Managed reaction delivery is provider-dependent; do not require it for a cross-platform approval. A managed callback that posts nothing is still finalized and acknowledged. Managed delivery is at-least-once, so keep application side effects idempotent.

## Registration and persistenceCopy Anchor Link

Register every named component that carries a callback:

channel.tsx

Copy Text
    
    
    import { createChannel } from "@copilotkit/channels";
    import { makeAgent } from "./agent.js";
    import { Decision } from "./decision.js";
    import { durableStateStore } from "./state-store.js";
    
    function required(name: string): string {
      const value = process.env[name];
      if (!value) throw new Error(`Missing ${name}`);
      return value;
    }
    
    const channel = createChannel({
      name: required("CHANNEL_CODE"),
      identifyUser: "platform",
      agent: makeAgent,
      components: [Decision],
      store: { adapter: durableStateStore },
    });

The same Channel declaration handles managed Slack and Teams deliveries.

Registration allows the action registry to rebuild the callback from the component name and serializable props. Clicks on messages posted before a process restart need a durable `StateStore`: the default managed store, or your own `store.adapter`.

See the interactive messages and approvals guide for [Slack](https://docs.copilotkit.ai/slack/interactive) or [Teams](https://docs.copilotkit.ai/teams/interactive) for the full post-and-resume flow.

How is this guide?

GoodBad

[Previous PageInteractionContext](https://docs.copilotkit.ai/reference/channels/types/InteractionContext)[Next PageMessageRef](https://docs.copilotkit.ai/reference/channels/types/MessageRef)
