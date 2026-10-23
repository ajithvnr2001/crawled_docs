---
url: https://developers.cloudflare.com/changelog/post/2026-08-04-agent-tracing/
title: Cloudflare Agents: trace every model call, tool run, and decision \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:38.592012+00:00
---

# Cloudflare Agents: trace every model call, tool run, and decision · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-04-agent-tracing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 4, 2026

## Cloudflare Agents: trace every model call, tool run, and decision

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Agents ↗︎](https://dash.cloudflare.com/?to=/:account/agents) now has a dedicated home in the Cloudflare dashboard that lists your traced agents and subagents.

Select an agent to inspect its traces in two ways:

**Replay a session** assembles the full conversation for a turn: system instructions, user messages, model reasoning, tool calls with arguments and results, and the final response.

![Session replay showing messages, reasoning, and subagent tool calls](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1980,height=1352,format=webp/_astro/agent_tracing_session_replay.uwseMu6e.png)

**View a trace** shows the execution timeline, connecting agent operations to Workers infrastructure so you can see where time was spent.

![Trace waterfall showing nested agent, model, tool, and D1 spans](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2832,height=1290,format=webp/_astro/agent_tracing_waterfall.Bw-JYiiV.png)

Enable tracing in your Wrangler configuration:
    
    
    {
    	"observability": {
    		"enabled": true,
    		"traces": {
    			"enabled": true
    		}
    	}
    }
    
    
    [observability]
    enabled = true
    
      [observability.traces]
      enabled = true

#### Framework support

Think and Flue agents are instrumented automatically. For direct AI SDK calls, wrap the namespace with [`wrapAISDK()`](https://developers.cloudflare.com/agents/runtime/operations/observability/tracing/#ai-sdk). Custom harnesses can use the [Workers custom spans API](https://developers.cloudflare.com/workers/observability/traces/custom-spans/) with [OpenTelemetry Generative AI semantic conventions ↗︎](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/).

#### Get Started

Check out the full blog post: [Introducing: Cloudflare Agents ↗︎](https://blog.cloudflare.com/agents-on-cloudflare).

For setup details, refer to the [Agent tracing documentation](https://developers.cloudflare.com/agents/runtime/operations/observability/tracing/).
