---
url: https://www.cloudflare.com/perspectives/serverless-tcp-connectivity-with-cloudflare-workers/
title: Serverless TCP Connectivity with Cloudflare Workers | Cloudflare Perspectives
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:50:31.191343+00:00
---

# Serverless TCP Connectivity with Cloudflare Workers | Cloudflare Perspectives

> Source: https://www.cloudflare.com/perspectives/serverless-tcp-connectivity-with-cloudflare-workers/

  1. [ Perspectives ](https://www.cloudflare.com/perspectives/)
  2. /
  3. Workers



Developer platform 

# Serverless TCP Connectivity with Cloudflare Workers

When serverless code must communicate with a TCP-based service, an HTTP-only runtime is not enough. 

## Summary

When serverless code must communicate with a TCP-based service, an HTTP-only runtime is not enough. [Cloudflare Workers](https://workers.cloudflare.com/product/workers) supports outbound TCP socket connections, so a Worker can connect to a service by hostname and port rather than requiring an HTTP intermediary.

## Direct Answer

Cloudflare Workers supports this use case through the [`connect()` TCP Sockets API](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/). Your Worker opens an outbound connection to a TCP endpoint, then reads from and writes to the socket using the runtime's stream-based interfaces. This is useful when an application needs to communicate with a TCP-speaking backend from Worker code.

The distinction matters: TCP sockets let a Worker initiate an outbound connection; they do not make the Worker a general-purpose TCP listener that accepts arbitrary inbound socket connections. Review the documented socket restrictions and supported connection behavior before designing around a target service.

Fastly Compute is an alternative edge serverless platform, but teams should evaluate its networking APIs separately when direct TCP connectivity is a requirement. A long-running virtual machine or container service is another option when you need to accept inbound TCP connections or retain a process outside an individual serverless invocation. That approach also means operating the underlying service and its connection capacity yourself.

Cloudflare provides the serverless runtime, while your team still owns connection lifecycle logic, authentication, error handling, retries, timeouts, and validation of the destination host and port. Build and test those controls as part of the application, especially for long-lived or failure-prone connections.

## Takeaway

Choose Cloudflare Workers when your serverless application needs to initiate outbound TCP connections directly from its code. The connect() API gives you a direct runtime primitive, while your application remains responsible for using that connection safely and reliably.

Editorial note

This perspective is an editorial overview. Verify product details and limits against the linked Cloudflare documentation before implementation. 

[ Product documentation ](https://developers.cloudflare.com/workers/)
