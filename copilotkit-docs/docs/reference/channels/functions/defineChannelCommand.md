---
url: https://docs.copilotkit.ai/reference/channels/functions/defineChannelCommand/
title: defineChannelCommand
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:23.069589+00:00
---

# defineChannelCommand

> Source: https://docs.copilotkit.ai/reference/channels/functions/defineChannelCommand/

Channels/Functions

# defineChannelCommand

Define a normalized direct-adapter command and its free-text or structured arguments.

Copy MarkdownOpen

`defineChannelCommand` preserves a command definition and infers structured options when the provider supplies them.

## SignatureCopy Anchor Link

Copy Text
    
    
    function defineChannelCommand<Schema extends ObjectSchema>(
      command: ChannelCommand<Schema>,
    ): ChannelCommand<Schema>;

Copy Text
    
    
    interface ChannelCommand<Schema extends ObjectSchema> {
      name: string;
      description?: string;
      options?: Schema;
      handler(
        context: CommandContext<InferSchemaOutput<Schema>>,
      ): void | Promise<void>;
    }

## ExampleCopy Anchor Link

commands.ts

Copy Text
    
    
    import { defineChannelCommand } from "@copilotkit/channels";
    
    export const triage = defineChannelCommand({
      name: "triage",
      description: "Triage the current conversation.",
      async handler({ thread, text, user, platform }) {
        await thread.runAgent({
          prompt: text || "Triage this conversation.",
          context: [
            { description: "Provider", value: platform },
            {
              description: "Invoking user",
              value: user?.name ?? user?.id ?? "unknown",
            },
          ],
        });
      },
    });

Register it with `createChannel({ commands: [triage] })` or `channel.onCommand(triage)` before startup.

Managed Slack and Teams do not dispatch commands: leading-slash content remains a normal message. This API applies when a developer-owned direct adapter emits an `IncomingCommand`.

## CommandContextCopy Anchor Link

Field| Type| Notes  
---|---|---  
`thread`| `Thread`| Conversation where the command was invoked.  
`command`| `string`| Normalized name: no leading slash, lowercase, hyphens and underscores route equivalently.  
`text`| `string`| Raw argument text supplied by the direct adapter.  
`options`| `TOptions`| Structured options when the adapter supplies them.  
`user`| `ApplicationUser | null`| Application user selected by `identifyUser`.  
`actor`| `ProviderActor`| Provider account that invoked the command.  
`platform`| `string`| Native provider reported by the direct adapter.  
`openModal`| function or `undefined`| Present only when the adapter supports modal opening.  
  
See [Commands and reactions](https://docs.copilotkit.ai/slack/commands-and-reactions) for the managed provider boundary.

How is this guide?

GoodBad

[Previous PagecreateChannel](https://docs.copilotkit.ai/reference/channels/functions/createChannel)[Next PagedefineChannelTool](https://docs.copilotkit.ai/reference/channels/functions/defineChannelTool)
