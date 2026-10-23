---
url: https://developers.cloudflare.com/changelog/post/2026-08-18-connect-handler/
title: Connect handler no longer requires an experimental flag \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:35.307163+00:00
---

# Connect handler no longer requires an experimental flag · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-18-connect-handler/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 18, 2026

## Connect handler no longer requires an experimental flag

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers can now export a [`connect()` handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/connect/) without enabling any [compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/). Previously, using a `connect()` handler required the `experimental` compatibility flag, which cannot be enabled in production.

A `connect()` handler lets a Worker accept a TCP connection forwarded from another Worker over a [service binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/), and read and write raw bytes on it using a [`Socket`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/#socket) object:

backend-worker.jsjs
    
    
    export default {
    	async connect(socket, env, ctx) {
    		const writer = socket.writable.getWriter();
    		await writer.write(new TextEncoder().encode("hello"));
    		await writer.close();
    	},
    };

Another Worker forwards a connection to it by calling `connect()` on the service binding:

frontend-worker.jsjs
    
    
    export default {
    	async fetch(request, env) {
    		const socket = env.BACKEND.connect("example.com:1234");
    		return new Response(socket.readable);
    	},
    };

On the `connect()` handler side, `socket.opened` resolves with `localAddress` set to the address the caller passed to `connect()`.

Direct inbound TCP connections remain unsupported at present.

For more information, refer to the [connect handler documentation](https://developers.cloudflare.com/workers/runtime-apis/handlers/connect/).
