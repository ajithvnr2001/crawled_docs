---
url: https://developers.cloudflare.com/workers/runtime-apis/handlers/connect/
title: Connect Handler \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:57:11.634834+00:00
---

# Connect Handler · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/handlers/connect/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Handlers](https://developers.cloudflare.com/workers/runtime-apis/handlers/)
  5. /Connect Handler



# Connect Handler

Last updated Oct 13, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBackgroundSyntax ParametersRelated resources

## Background

Export a `connect()` handler to let a Worker accept an inbound TCP connection and read and write raw bytes on it. The handler receives a [`Socket`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/#socket) object, the same type returned by [`connect()` from `cloudflare:sockets`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/) for outbound connections.

A Worker receives a connection in its `connect()` handler when another Worker forwards a TCP connection to it over a [service binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/), by calling `connect()` on the binding:
    
    
    // Worker A forwards a TCP connection to Worker B over a service binding
    export default {
    	async fetch(request, env) {
    		const socket = env.BACKEND.connect("example.com:1234");
    		// Read from and write to socket.readable / socket.writable
    		return new Response(socket.readable);
    	},
    };

Note

Direct inbound TCP connections from the public Internet, for example by using the HTTP `CONNECT` method against a Worker's public URL, are not supported at present. A `connect()` handler only receives connections forwarded from another Worker over a service binding.

## Syntax
    
    
    export default {
    	async connect(socket, env, ctx) {
    		const writer = socket.writable.getWriter();
    		await writer.write(new TextEncoder().encode("hello"));
    		await writer.close();
    	},
    };
    
    
    interface Env {}
    
    export default {
    	async connect(socket: Socket, env: Env, ctx: ExecutionContext) {
    		const writer = socket.writable.getWriter();
    		await writer.write(new TextEncoder().encode("hello"));
    		await writer.close();
    	},
    } satisfies ExportedHandler<Env>;

You can also implement `connect()` as a method on a [`WorkerEntrypoint`](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc/) class, which lets a single Worker expose a `connect()` handler alongside other RPC methods:
    
    
    import { WorkerEntrypoint } from "cloudflare:workers";
    
    export class Backend extends WorkerEntrypoint {
    	async connect(socket) {
    		const writer = socket.writable.getWriter();
    		await writer.write(new TextEncoder().encode("hello"));
    		await writer.close();
    	}
    }

### Parameters

  * `socket` Socket 
    * The inbound [`Socket`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/#socket) used to read and write raw bytes on the connection.
    * [`socket.opened`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/#socket) resolves with a [`SocketInfo`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/#socketinfo) object. On a `connect()` handler, `localAddress` is set to the address the caller passed to `connect()` on the service binding.
  * `env` object 
    * The [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) available to the Worker.
  * `ctx` object 
    * The context associated with the Worker, containing [`waitUntil()`](https://developers.cloudflare.com/workers/runtime-apis/context/#waituntil) and [`passThroughOnException()`](https://developers.cloudflare.com/workers/runtime-apis/context/#passthroughonexception).



A Worker that does not export a `connect()` handler rejects any connection forwarded to it.

## Related resources

  * [TCP sockets](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/) — Create outbound TCP connections and work with the `Socket` API.
  * [Service bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) — Call one Worker from another, including forwarding TCP connections with `connect()`.



[PreviousAlarm Handler ↗︎](https://developers.cloudflare.com/durable-objects/api/alarms/)[NextEmail Handler ↗︎](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/handlers/connect.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
