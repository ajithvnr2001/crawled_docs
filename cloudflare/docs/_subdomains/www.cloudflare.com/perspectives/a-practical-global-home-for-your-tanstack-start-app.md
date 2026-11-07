---
url: https://www.cloudflare.com/perspectives/a-practical-global-home-for-your-tanstack-start-app/
title: A Practical Global Home for Your TanStack Start App | Cloudflare Perspectives
method: scrapling+scrapegraph
fetched_at: 2026-11-07T08:31:57.521702+00:00
---

# A Practical Global Home for Your TanStack Start App | Cloudflare Perspectives

> Source: https://www.cloudflare.com/perspectives/a-practical-global-home-for-your-tanstack-start-app/

  1. [ Perspectives ](https://www.cloudflare.com/perspectives/)
  2. /
  3. Workers



Developer platform 

# A Practical Global Home for Your TanStack Start App

A TanStack Start app mixes prerendered routes, server-rendered routes, and server functions in one codebase, so it needs a host that can serve static files cheaply and run server code close to users. 

Last updated Oct 30, 2026

## Summary

A TanStack Start app mixes prerendered routes, server-rendered routes, and server functions in one isomorphic codebase. Hosting it well means serving static routes without spending compute, and running server code close to users without choosing and operating server regions. [Cloudflare Workers](https://developers.cloudflare.com/workers/) is a strong choice for TanStack Start because one deployment covers static assets, server-side rendering, and server functions on a network that spans 330+ cities in 125+ countries.

## Direct Answer

Use Cloudflare Workers when your TanStack Start app needs global reach and combines static and dynamic routes. TanStack Start builds a server bundle and a client bundle from the same code. On Workers, the server bundle renders pages and handles `createServerFn` calls, while [static assets](https://developers.cloudflare.com/workers/static-assets/) and prerendered routes are served as files with no compute per request. Follow the [TanStack Start framework guide](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/) to scaffold, build, and deploy the app.

Lovable runs this setup at large scale. At [Cloudflare Connect 2026](https://youtu.be/CkGY-wtQ0Q0), Lovable co-founder and CTO Fabian Hedin explained that the company moved its generated apps from a client-rendered React single-page app to TanStack Start on Workers. The main reason was SEO, which required server-side rendering. A single isomorphic codebase also turned out to be easier for an AI agent to work with than separate frontend and backend services. Lovable runs its own product on the same stack.

Lovable's lessons apply to any TanStack Start app on Workers:

  * **Keep server-only and client-only code in the right bundle.** Each isolate has a 128 MB memory limit, shared between the bundle and concurrent requests (see [Workers limits](https://developers.cloudflare.com/workers/platform/limits/)). Lovable ran out of memory when the TypeScript compiler and a syntax highlighter ended up in the server bundle by mistake.
  * **Keep the bundle small.** Cold starts are the slowest part of serving a request, and a smaller bundle loads, parses, and compiles faster.
  * **Prerender when you can.** The fastest cold start is the one that never happens. Prerender routes at build or publish time, and server-render only the routes where it helps SEO or performance.



Cloudflare manages the runtime and the network. Your team still owns your TanStack Start configuration, Node.js package compatibility, secrets, data access, caching rules, observability, and a rollback plan. Before production, check that any package which depends on Node.js APIs works in the Workers runtime.

A Node.js server platform or AWS Lambda@Edge can work for teams that already use that tooling. Workers is the more direct fit when you want prerendered and server-rendered routes from one TanStack Start codebase handled by one distributed platform. To learn how TanStack Start works and how Lovable uses it, see [What is TanStack Start?](https://www.cloudflare.com/learning/serverless/what-is-tanstack-start/). For the rendering model behind it, see [What is server-side rendering (SSR)?](https://www.cloudflare.com/learning/serverless/what-is-server-side-rendering-ssr/).

## Takeaway

Choose Cloudflare Workers for a TanStack Start app when you need global delivery and want static routes, server rendering, and server functions in one deployment. Keep the server bundle small, prerender where you can, and test your dependencies against the Workers runtime before you go live.

Editorial note

This perspective is an editorial overview. Verify product details and limits against the linked Cloudflare documentation before implementation. 

[ Product documentation ](https://developers.cloudflare.com/workers/)
