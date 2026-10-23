---
url: https://developers.cloudflare.com/changelog/post/2026-07-07-warning-attributes/
title: Workers Observability now surfaces warning attributes on spans for non-fatal errors \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:39.624664+00:00
---

# Workers Observability now surfaces warning attributes on spans for non-fatal errors · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-07-warning-attributes/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 7, 2026

## Workers Observability now surfaces warning attributes on spans for non-fatal errors

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers Observability now attaches warning attributes to spans for non-fatal telemetry issues. These attributes help you identify instrumentation issues.

When a warning is present, both attributes are set together:

  * `cloudflare.warning.type` — An identifier indicating the type of warning condition.
  * `cloudflare.warning.message` — A free-form, human-readable explanation of the warning condition.



For example, recording an entire webhook payload as a span attribute can exceed the span data limit:
    
    
    export default {
    	async fetch(request, env, ctx) {
    		const payload = await request.text();
    
    		return ctx.tracing.enterSpan("receive-webhook", (span) => {
    			span.setAttribute("webhook.payload", payload);
    			return new Response("Accepted", { status: 202 });
    		});
    	},
    };
    
    
    export default {
      async fetch(request: Request, env: Env, ctx: ExecutionContext) {
        const payload = await request.text();
    
        return ctx.tracing.enterSpan("receive-webhook", (span) => {
          span.setAttribute("webhook.payload", payload);
          return new Response("Accepted", { status: 202 });
        });
      },
    };

The Worker still returns `202 Accepted`, but tracing drops the oversized attribute. The span includes `cloudflare.warning.type` set to `span_data_limit_exceeded` and a `cloudflare.warning.message` identifying the rejected attribute and its size.

For more information, refer to [Warning attributes](https://developers.cloudflare.com/workers/observability/traces/spans-and-attributes/#warning-attributes).
