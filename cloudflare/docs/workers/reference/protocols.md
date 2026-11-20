---
url: https://developers.cloudflare.com/workers/reference/protocols/
title: Protocols \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-11-20T09:50:39.312930+00:00
---

# Protocols · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/reference/protocols/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /Reference
  4. /Protocols



# Protocols

Last updated Nov 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Workers support the following protocols and interfaces:

Protocol | Inbound | Outbound  
---|---|---  
**HTTP / HTTPS** | Handle incoming HTTP requests using the [`fetch()` handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/). | Make HTTP subrequests using the [`fetch()` API](https://developers.cloudflare.com/workers/runtime-apis/fetch/).  
**Direct TCP sockets** | Handle TCP connections forwarded over a [service binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) or through a [Spectrum application](https://developers.cloudflare.com/spectrum/how-to/route-tcp-traffic-to-a-worker/) using the [`connect()` handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/connect/) (public beta). | Create outbound TCP connections using the [`connect()` API](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/).  
**gRPC** | Route gRPC, including bidirectional streams, through Spectrum to a Worker and [Cloudflare Container](https://developers.cloudflare.com/containers/examples/bidirectional-grpc/) (public beta). | —  
**WebSockets** | Accept incoming WebSocket connections using the [`WebSocket` API](https://developers.cloudflare.com/workers/runtime-apis/websockets/). | —  
**HTTP/3 (QUIC)** | Accept inbound requests over [HTTP/3 ↗︎](https://www.cloudflare.com/learning/performance/what-is-http3/) by enabling it on your [zone](https://developers.cloudflare.com/fundamentals/concepts/accounts-and-zones/#zones) in **Speed** > **Settings** > **Protocol Optimization** in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/). | —  
**SMTP** | Use [Email Workers](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/) to process and forward email without managing TCP connections to SMTP email servers. | Use [Email Workers](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/).  
  
For gRPC, the Worker receives the connection as a raw TCP byte stream. In this path, the Worker does not parse gRPC or HTTP/2 frames. It forwards the stream to a gRPC server running in a Container. Refer to [Bidirectional gRPC with Workers and Containers](https://developers.cloudflare.com/containers/examples/bidirectional-grpc/) for a complete example.

[PreviousMigrate from Service Workers to ES Modules](https://developers.cloudflare.com/workers/reference/migrate-to-module-workers/)[NextSecurity model](https://developers.cloudflare.com/workers/reference/security-model/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/reference/protocols.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
