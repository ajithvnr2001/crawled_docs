---
url: https://docs.copilotkit.ai/reference/channels/types/InteractionContext/
title: InteractionContext
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:15.828699+00:00
---

# InteractionContext

> Source: https://docs.copilotkit.ai/reference/channels/types/InteractionContext/

Channels/Types

# InteractionContext

The thread, message reference, typed action value, user, and capabilities passed to a component callback.

Copy MarkdownOpen

Buttons, selects, and inputs receive an `InteractionContext<TValue>`.

## ShapeCopy Anchor Link

Copy Text
    
    
    interface InteractionContext<TValue = unknown> {
      thread: Thread;
      message: IncomingMessage;
      action: {
        id: string;
        value?: TValue;
      };
      values: Record<string, unknown>;
      user: ApplicationUser | null;
      actor: ProviderActor;
      platform: string;
      openModal?(view: ModalView): Promise<{ ok: boolean; error?: string }>;
    }

Field| Notes  
---|---  
`thread`| Post, update, or resume the current conversation.  
`message`| Message containing the control. Check `message.ref.id` before updating it.  
`action.id`| Opaque SDK action id.  
`action.value`| Round-tripped `Button.value`, selected value, or submitted text. Guard `undefined`.  
`values`| Other submitted form values. Teams `Action.Submit` callbacks include named Adaptive Card input values.  
`user`| Nullable application user selected by `identifyUser`.  
`actor`| Provider account that caused the interaction.  
`platform`| Native provider; managed callbacks report `"slack"` or `"teams"`.  
`openModal`| Capability-gated and omitted on the managed Slack and Teams path.  
  
Copy Text
    
    
    <Button
      value={{ approved: true }}
      onClick={async ({ thread, message, action }) => {
        if (action.value === undefined) return;
    
        await thread.assertCanResume();
    
        if (message.ref.id) {
          try {
            await thread.update(message.ref, "Approved");
          } catch {
            // Best-effort visual update.
          }
        }
    
        await thread.resume(action.value);
      }}
    >
      Approve
    </Button>

Managed interactions arrive as a later delivery. Return after posting the original control and use `resume()` in its callback; do not block with `awaitChoice()`.

How is this guide?

GoodBad

[Previous PageIncomingMessage](https://docs.copilotkit.ai/reference/channels/types/IncomingMessage)[Next PageJSX callbacks](https://docs.copilotkit.ai/reference/channels/types/JSXCallbacks)
