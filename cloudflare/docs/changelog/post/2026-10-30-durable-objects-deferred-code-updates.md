---
url: https://developers.cloudflare.com/changelog/post/2026-10-30-durable-objects-deferred-code-updates/
title: Durable Objects now defer code updates by default \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:17.337877+00:00
---

# Durable Objects now defer code updates by default · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-30-durable-objects-deferred-code-updates/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 30, 2026

## Durable Objects now defer code updates by default

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Durable Objects can stay active across requests, allowing you to run long-running [agents](https://developers.cloudflare.com/agents/), maintain [long-lived WebSocket connections](https://developers.cloudflare.com/durable-objects/best-practices/websockets/) and coordinate state across many clients. This is possible because each Durable Object is globally unique, and this means it must run only one version of your code at a time. Previously, when you deployed a change to your Durable Objects code, that change would be applied immediately, which could interrupt in-flight work and terminate open connections.

Durable Objects now defer code updates by default. When you deploy, an active Durable Object can keep running its current code for up to 5 minutes (300 seconds) while it waits to hibernate. This gives in-flight work time to finish. WebSocket connections that use the [Hibernation API](https://developers.cloudflare.com/durable-objects/examples/websocket-hibernation-server/) remain connected when an object adopts new code after hibernating.

For an active Durable Object, a code update follows this flow:
    
    
    flowchart TD
        accTitle: Code updates for an active Durable Object
        accDescr: By default, an active object can keep running its current code until it hibernates or the delay ends. After hibernating, it starts on new code on the next request. If the delay ends first, or immediate mode is selected, it resets and adopts the new code. Deferral is best effort.
        A["You deploy new code"] -->|"Default: deferred"| B["The object can keep running<br/>its current code"]
        B --> C{"Hibernates before<br/>the delay ends?"}
        C -->|Yes| D["Starts on the new code<br/>on the next request"]
        C -->|No| E["The object resets<br/>and adopts the new code"]
        A -.->|"Override: immediate"| E
    

To change the delay, add `code_update_strategy` to `durable_objects` in your Wrangler configuration:
    
    
    {
    	"durable_objects": {
    		"bindings": [
    			{
    				"name": "CHAT_ROOM",
    				"class_name": "ChatRoom",
    			},
    		],
    		"code_update_strategy": {
    			"mode": "deferred",
    			"max_delay": 60,
    		},
    	},
    }
    
    
    [[durable_objects.bindings]]
    name = "CHAT_ROOM"
    class_name = "ChatRoom"
    
    [durable_objects.code_update_strategy]
    mode = "deferred"
    max_delay = 60

`max_delay` is in seconds, from `0` to `86400` (24 hours), with millisecond precision. Omit it to use the default of `300` seconds.

To set the strategy for a single deployment, pass `--durable-objects-code-update-mode` with `immediate` or `deferred <duration>`. For example, apply an update right away during an incident, or when your deployment tooling calls a Durable Object right after deploying and needs the new code:

npmyarnpnpm
    
    
    npx wrangler versions deploy <VERSION_ID>@100% --durable-objects-code-update-mode immediate
    
    
    yarn wrangler versions deploy <VERSION_ID>@100% --durable-objects-code-update-mode immediate
    
    
    pnpm wrangler versions deploy <VERSION_ID>@100% --durable-objects-code-update-mode immediate

A `deferred` code update is best effort and does not guarantee that every operation finishes. The object can still reset before `max_delay` is reached, for example during a Cloudflare runtime update.

For more information, including how this interacts with gradual deployments and the REST API, refer to [Durable Objects code updates](https://developers.cloudflare.com/durable-objects/deployments/durable-objects-code-updates/).
