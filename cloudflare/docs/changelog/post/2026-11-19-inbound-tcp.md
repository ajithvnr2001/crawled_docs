---
url: https://developers.cloudflare.com/changelog/post/2026-11-19-inbound-tcp/
title: Inbound TCP and gRPC for Workers and Containers now in public beta \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-20T09:50:37.560654+00:00
---

# Inbound TCP and gRPC for Workers and Containers now in public beta · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-19-inbound-tcp/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 19, 2026

## Inbound TCP and gRPC for Workers and Containers now in public beta

[Spectrum](https://developers.cloudflare.com/spectrum/)[Containers](https://developers.cloudflare.com/containers/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Inbound TCP connections to Workers and bidirectional gRPC in Containers are now in public beta.

Worker-origin Spectrum applications are available on Pro and Business zones, and on Enterprise zones with Spectrum Enterprise enabled. Without Spectrum Enterprise, Pro and Business zones support one Worker-origin application per zone, on one TCP port.
    
    
    flowchart LR
        Client[TCP client] <--> Spectrum
        Spectrum <--> Worker["Worker connect()<br/>Handle or forward bytes"]
        Worker <--> DO["Durable Object<br/>connect()"]
        DO <--> Container["Container<br/>gRPC or other TCP server"]
    

#### Forward a Worker socket to a Durable Object

Spectrum sends public TCP connections to your Worker's `connect()` handler. The Worker opens a socket to the `GrpcContainer` Durable Object and pipes bytes in both directions:

src/index.jsjs
    
    
    export default {
    	async connect(socket, env) {
    		const container = env.GRPC_CONTAINER.getByName("grpc-demo");
    		const durableObjectSocket = container.connect("grpc-container:50051", {
    			allowHalfOpen: true,
    			secureTransport: "off",
    		});
    
    		try {
    			await durableObjectSocket.opened;
    			await Promise.all([
    				socket.readable.pipeTo(durableObjectSocket.writable),
    				durableObjectSocket.readable.pipeTo(socket.writable),
    			]);
    		} finally {
    			await Promise.allSettled([socket.close(), durableObjectSocket.close()]);
    		}
    	},
    };

src/index.tsts
    
    
    export default {
    	async connect(socket: Socket, env: Env): Promise<void> {
    		const container = env.GRPC_CONTAINER.getByName("grpc-demo");
    		const durableObjectSocket = container.connect("grpc-container:50051", {
    			allowHalfOpen: true,
    			secureTransport: "off",
    		});
    
    		try {
    			await durableObjectSocket.opened;
    			await Promise.all([
    				socket.readable.pipeTo(durableObjectSocket.writable),
    				durableObjectSocket.readable.pipeTo(socket.writable),
    			]);
    		} finally {
    			await Promise.allSettled([socket.close(), durableObjectSocket.close()]);
    		}
    	},
    } satisfies ExportedHandler<Env>;

#### Forward the Durable Object socket to its Container

The Durable Object receives the connection in its own `connect()` handler. Once its Container is running, `getTcpPort(50051).connect()` opens a socket to the gRPC server inside it:

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class GrpcContainer extends DurableObject {
    	async connect(socket) {
    		const containerSocket = this.ctx.container
    			.getTcpPort(50051)
    			.connect("10.0.0.1:50051", {
    				allowHalfOpen: true,
    				secureTransport: "off",
    			});
    
    		try {
    			await containerSocket.opened;
    			await Promise.all([
    				socket.readable.pipeTo(containerSocket.writable),
    				containerSocket.readable.pipeTo(socket.writable),
    			]);
    		} finally {
    			await Promise.allSettled([socket.close(), containerSocket.close()]);
    		}
    	}
    }

src/index.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class GrpcContainer extends DurableObject<Env> {
    	async connect(socket: Socket): Promise<void> {
    		const containerSocket = this.ctx
    			.container!.getTcpPort(50051)
    			.connect("10.0.0.1:50051", {
    				allowHalfOpen: true,
    				secureTransport: "off",
    			});
    
    		try {
    			await containerSocket.opened;
    			await Promise.all([
    				socket.readable.pipeTo(containerSocket.writable),
    				containerSocket.readable.pipeTo(socket.writable),
    			]);
    		} finally {
    			await Promise.allSettled([socket.close(), containerSocket.close()]);
    		}
    	}
    }

`allowHalfOpen: true` preserves TCP half-closes. The Worker and Durable Object forward encrypted bytes; the Container terminates TLS and handles HTTP/2 and gRPC.

#### Run bidirectional gRPC in the Container

Run an existing gRPC server in any language, including services for real-time voice applications. This Node.js snippet shows the streaming handler and service registration. It sends a greeting, echoes incoming messages, and sends a final response when the client finishes:

container/server.jsjs
    
    
    const path = require("node:path");
    const grpc = require("@grpc/grpc-js");
    const protoLoader = require("@grpc/proto-loader");
    
    const definition = protoLoader.loadSync(
    	path.resolve(__dirname, "../proto/bytes.proto"),
    );
    const proto = grpc.loadPackageDefinition(definition).cloudflare.grpcdemo;
    
    function chat(call) {
    	let count = 0;
    	call.write({
    		payload: Buffer.from("hello from the container gRPC server\n"),
    	});
    	call.on("data", ({ payload }) => {
    		count += 1;
    		call.write({
    			payload: Buffer.concat([
    				Buffer.from(`container echo ${count}: `),
    				payload,
    			]),
    		});
    	});
    	call.on("end", () => {
    		call.write({
    			payload: Buffer.from("goodbye from the container gRPC server\n"),
    		});
    		call.end();
    	});
    	call.on("error", (error) => console.error("gRPC stream error", error));
    }
    
    const server = new grpc.Server();
    server.addService(proto.ByteStream.service, { Chat: chat });

Follow the [complete gRPC example](https://developers.cloudflare.com/containers/examples/bidirectional-grpc/) for the protobuf definition, bindings, Spectrum routing, Secrets Store TLS credentials, and Container startup and readiness checks.
