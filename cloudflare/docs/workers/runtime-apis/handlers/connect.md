---
url: https://developers.cloudflare.com/workers/runtime-apis/handlers/connect/
title: Connect handler \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-11-20T09:50:39.043905+00:00
---

# Connect handler · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/handlers/connect/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Handlers](https://developers.cloudflare.com/workers/runtime-apis/handlers/)
  5. /Connect handler



# Connect handler

Last updated Nov 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSyntaxLocal developmentExpose the Worker publicly

The `connect()` handler receives inbound TCP connections as a [`Socket`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/#socket). Use the socket's readable and writable streams to inspect data, implement a TCP protocol, or proxy the connection to another service.

Public beta

Inbound TCP connections to Workers are in public beta. Use a [Spectrum application with a Worker origin](https://developers.cloudflare.com/spectrum/how-to/route-tcp-traffic-to-a-worker/) to send public TCP connections to this handler. Sending an HTTP `CONNECT` request to a Worker's public URL does not invoke this handler.

## Syntax

src/index.jsjs
    
    
    export default {
    	async connect(socket, env, ctx) {
    		const { remoteAddress, localAddress } = await socket.opened;
    		console.log("TCP connection opened", {
    			remoteAddress,
    			localAddress,
    		});
    
    		await socket.readable.pipeTo(socket.writable);
    	},
    };

src/index.tsts
    
    
    export default {
    	async connect(
    		socket: Socket,
    		env: Env,
    		ctx: ExecutionContext,
    	): Promise<void> {
    		const { remoteAddress, localAddress } = await socket.opened;
    		console.log("TCP connection opened", {
    			remoteAddress,
    			localAddress,
    		});
    
    		await socket.readable.pipeTo(socket.writable);
    	},
    } satisfies ExportedHandler<Env>;

The example echoes each byte back to the client. Await all stream operations that must remain active for the connection. When the handler's returned promise settles, the inbound socket closes. A Worker without a `connect()` handler rejects forwarded TCP connections.

### Parameters

  * `socket` (`Socket`) — The established inbound connection. 
    * `socket.readable` contains bytes sent by the client.
    * `socket.writable` sends bytes to the client.
    * `socket.opened` resolves to [`SocketInfo`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/#socketinfo), which contains the connection addresses.
    * `socket.closed` settles when the connection closes.
  * `env` (`Env`) — The Worker's [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/).
  * `ctx` (`ExecutionContext`) — The handler's [execution context](https://developers.cloudflare.com/workers/runtime-apis/context/).



### Return value

The handler returns `void` or `Promise<void>`. Keep the returned promise pending while the Worker is processing the connection.

Inbound sockets preserve TCP half-closes. When a client closes its writable side, the Worker can continue sending data through `socket.writable`. Set `allowHalfOpen: true` on outbound sockets when a proxy must preserve this behavior.

## Connection addresses

For connections delivered by Spectrum, `remoteAddress` contains the original client's IP address and source port. Extract the IP address for client identification, such as rate limiting.

`localAddress` contains the destination IP address and Spectrum edge port. Use the port to identify which application port received the connection.

Addresses include the port, such as `203.0.113.7:12345`. IPv6 addresses use brackets, such as `[2001:db8::1]:12345`. `remoteAddress` is `undefined` when client address metadata is unavailable.

For [service bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/), `localAddress` contains the address the caller passed to `connect()`.

## TLS

Spectrum Enterprise can [terminate TLS before forwarding the connection](https://developers.cloudflare.com/spectrum/how-to/route-tcp-traffic-to-a-worker/#terminate-tls-with-spectrum-enterprise) to the Worker. Without Spectrum TLS termination, the Worker can proxy encrypted bytes to a backend service that terminates TLS.

Calling `socket.startTls()` on an inbound socket delivered by Spectrum is not supported, including when Spectrum TLS termination is turned off.

SMTP on port `587` and IMAP on port `143` can negotiate a TLS upgrade with STARTTLS. Proxy these connections to a backend that handles the upgrade and TLS handshake. Spectrum TLS termination expects TLS from the start of the connection.

## Deploy the Worker

The TCP `connect()` handler does not require a compatibility flag. Deploy the Worker before selecting it as a Spectrum origin.

## Forward connections between Workers

Another Worker can open a TCP connection through a [service binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/). This caller returns the bytes sent by the receiving Worker:

src/index.jsjs
    
    
    export default {
    	fetch(request, env) {
    		const socket = env.BACKEND.connect("backend:1234");
    		return new Response(socket.readable);
    	},
    };

src/index.tsts
    
    
    export default {
    	fetch(request, env) {
    		const socket = env.BACKEND.connect("backend:1234");
    		return new Response(socket.readable);
    	},
    } satisfies ExportedHandler<Env>;

The receiving Worker can export a `connect()` handler or implement it on a [`WorkerEntrypoint`](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc/) class. Configure the `BACKEND` binding to target this entrypoint:

src/index.jsjs
    
    
    import { WorkerEntrypoint } from "cloudflare:workers";
    
    export class Backend extends WorkerEntrypoint {
    	async connect(socket) {
    		const writer = socket.writable.getWriter();
    		await writer.write(new TextEncoder().encode("Hello from Worker B\n"));
    		await writer.close();
    	}
    }

src/index.tsts
    
    
    import { WorkerEntrypoint } from "cloudflare:workers";
    
    export class Backend extends WorkerEntrypoint {
    	async connect(socket: Socket): Promise<void> {
    		const writer = socket.writable.getWriter();
    		await writer.write(new TextEncoder().encode("Hello from Worker B\n"));
    		await writer.close();
    	}
    }

## Proxy a TCP connection

The following handler creates an outbound TCP socket and pipes data in both directions:

src/index.jsjs
    
    
    import { connect } from "cloudflare:sockets";
    
    export default {
    	async connect(socket) {
    		const upstream = connect(
    			{ hostname: "origin.example.com", port: 5432 },
    			{ allowHalfOpen: true },
    		);
    
    		try {
    			await upstream.opened;
    			await Promise.all([
    				socket.readable.pipeTo(upstream.writable),
    				upstream.readable.pipeTo(socket.writable),
    			]);
    		} finally {
    			await Promise.allSettled([socket.close(), upstream.close()]);
    		}
    	},
    };

src/index.tsts
    
    
    import { connect } from "cloudflare:sockets";
    
    export default {
    	async connect(socket: Socket): Promise<void> {
    		const upstream = connect(
    			{ hostname: "origin.example.com", port: 5432 },
    			{ allowHalfOpen: true },
    		);
    
    		try {
    			await upstream.opened;
    			await Promise.all([
    				socket.readable.pipeTo(upstream.writable),
    				upstream.readable.pipeTo(socket.writable),
    			]);
    		} finally {
    			await Promise.allSettled([socket.close(), upstream.close()]);
    		}
    	},
    } satisfies ExportedHandler;

Set `allowHalfOpen: true` on intermediate sockets when either side must continue sending after receiving an end-of-file signal.

Outbound TCP connections to Cloudflare IP addresses are blocked. Do not connect the Worker back to its own Spectrum hostname. Refer to [TCP socket considerations](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/#considerations).

## Local development

Configure a raw TCP listener in `wrangler.jsonc` for your `connect()` handler:
    
    
    {
    	"connect": [{ "protocol": "tcp", "port": 8788 }],
    }
    
    
    [[connect]]
    protocol = "tcp"
    port = 8_788

  1. Start local development:

npmyarnpnpm
         
         npx wrangler dev
         
         yarn wrangler dev
         
         pnpm wrangler dev

  2. Connect a TCP client to port `8788`:
         
         echo "Hello, Worker" | nc localhost 8788




Wrangler serves HTTP on port `8787` by default. The separate TCP port is set by the `connect` configuration; it does not follow the HTTP port automatically.

For example, to test a local gRPC client, connect it to `localhost:8788`. Refer to [Bidirectional gRPC with Workers and Containers](https://developers.cloudflare.com/containers/examples/bidirectional-grpc/) for a complete example.

## Expose the Worker publicly

Create a Spectrum application with the Worker as its origin. Spectrum accepts connections on the configured hostname and edge port, then invokes this handler.

Refer to [Route TCP traffic to a Worker](https://developers.cloudflare.com/spectrum/how-to/route-tcp-traffic-to-a-worker/) for dashboard, Cloudflare CLI, and REST API instructions.

[PreviousAlarm Handler ↗︎](https://developers.cloudflare.com/durable-objects/api/alarms/)[NextEmail Handler ↗︎](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/handlers/connect.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
