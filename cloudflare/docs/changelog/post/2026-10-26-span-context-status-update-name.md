---
url: https://developers.cloudflare.com/changelog/post/2026-10-26-span-context-status-update-name/
title: Workers tracing \u2014 new spanContext(), setStatus(), and updateName() APIs \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-27T07:31:30.277508+00:00
---

# Workers tracing — new spanContext(), setStatus(), and updateName() APIs · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-26-span-context-status-update-name/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 26, 2026

## Workers tracing — new spanContext(), setStatus(), and updateName() APIs

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Custom spans](https://developers.cloudflare.com/workers/observability/traces/custom-spans/) in Workers now support three more methods from the OpenTelemetry span API.

  * **`span.spanContext()`** returns the span's `traceId`, `spanId`, and `traceFlags`. The IDs match the trace and span IDs in Workers Observability and in exported traces, so you can log them or return them to clients to correlate a request with its trace.
  * **`span.setStatus(status)`** sets the span status to `"unset"`, `"ok"`, or `"error"`, with an optional message for errors. Span status is included in traces exported to [OpenTelemetry destinations](https://developers.cloudflare.com/workers/observability/opentelemetry-export/). The Workers Observability dashboard does not display it yet.
  * **`span.updateName(name)`** renames a span after it starts, such as once you know which route a request matched. You can also rename the invocation's root span returned by `tracing.getActiveSpan()`.



src/index.jsjs
    
    
    import { tracing } from "cloudflare:workers";
    
    export default {
    	async fetch(request, env) {
    		const root = tracing.getActiveSpan();
    		const route = router.match(request);
    		root?.updateName(`${request.method} ${route.pattern}`);
    
    		return tracing.startActiveSpan("handle", async (span) => {
    			try {
    				const response = await route.handler(request, env);
    				span.setStatus({ code: "ok" });
    				return response;
    			} catch (err) {
    				span.recordException(err);
    				span.setStatus({ code: "error", message: "Route handler failed" });
    				return Response.json(
    					{ error: "Internal error", traceId: root?.spanContext().traceId },
    					{ status: 500 },
    				);
    			} finally {
    				span.end();
    			}
    		});
    	},
    };

src/index.tsts
    
    
    import { tracing } from "cloudflare:workers";
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const root = tracing.getActiveSpan();
    		const route = router.match(request);
    		root?.updateName(`${request.method} ${route.pattern}`);
    
    		return tracing.startActiveSpan("handle", async (span) => {
    			try {
    				const response = await route.handler(request, env);
    				span.setStatus({ code: "ok" });
    				return response;
    			} catch (err) {
    				span.recordException(err as Error);
    				span.setStatus({ code: "error", message: "Route handler failed" });
    				return Response.json(
    					{ error: "Internal error", traceId: root?.spanContext().traceId },
    					{ status: 500 },
    				);
    			} finally {
    				span.end();
    			}
    		});
    	},
    };

For more details, refer to the [custom spans documentation](https://developers.cloudflare.com/workers/observability/traces/custom-spans/).
