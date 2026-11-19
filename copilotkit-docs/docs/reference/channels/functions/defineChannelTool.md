---
url: https://docs.copilotkit.ai/reference/channels/functions/defineChannelTool/
title: defineChannelTool
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:33.197999+00:00
---

# defineChannelTool

> Source: https://docs.copilotkit.ai/reference/channels/functions/defineChannelTool/

Channels/Functions

# defineChannelTool

Define a Standard Schema-validated tool with inferred arguments and Channels thread context.

Copy MarkdownOpen

`defineChannelTool` preserves a tool definition while inferring the handler argument type from its Standard Schema.

## SignatureCopy Anchor Link

Copy Text
    
    
    function defineChannelTool<Schema extends ObjectSchema>(
      tool: ChannelTool<Schema>,
    ): ChannelTool<Schema>;

Copy Text
    
    
    interface ChannelTool<Schema extends ObjectSchema> {
      name: string;
      description: string;
      parameters: Schema;
      handler(
        args: InferSchemaOutput<Schema>,
        context: ChannelToolContext,
      ): unknown | Promise<unknown>;
    }

## ExampleCopy Anchor Link

tools.ts

Copy Text
    
    
    import { defineChannelTool } from "@copilotkit/channels";
    import { z } from "zod";
    
    export const getIncident = defineChannelTool({
      name: "get_incident",
      description: "Read an incident by id.",
      parameters: z.object({
        incidentId: z.string(),
      }),
      async handler({ incidentId }) {
        const incident = await incidents.get(incidentId);
        return incident;
      },
    });

Register tools in `createChannel({ tools })`, add one with `channel.tool(tool)` before startup, or pass turn-scoped tools to `thread.runAgent({ tools })`.

## Handler contextCopy Anchor Link

Field| Type| Managed behavior  
---|---|---  
`thread`| `Thread`| Current conversation handle.  
`message`| `IncomingMessage | undefined`| Current inbound message when the run began from a message trigger.  
`user`| `ApplicationUser | null`| Application user selected for this event.  
`actor`| `ProviderActor`| Provider account that caused this event.  
`signal`| `AbortSignal | undefined`| Reserved optional field; the current SDK tool runner leaves it undefined.  
`platform`| `string`| Normalized source provider, such as `"slack"` or `"teams"`.  
  
Return raw objects or arrays for data. The SDK JSON-serializes non-string results for the model. A tool that already posted UI should return a short natural-language confirmation so the model does not repeat the card.

See [Tools and context](https://docs.copilotkit.ai/slack/tools) for a complete managed example.

How is this guide?

GoodBad

[Previous PagedefineChannelCommand](https://docs.copilotkit.ai/reference/channels/functions/defineChannelCommand)[Next PagerenderToIR](https://docs.copilotkit.ai/reference/channels/functions/renderToIR)
