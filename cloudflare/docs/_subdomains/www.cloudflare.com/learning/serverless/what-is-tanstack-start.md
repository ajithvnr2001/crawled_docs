---
url: https://www.cloudflare.com/learning/serverless/what-is-tanstack-start/
title: What is TanStack Start? | Full-stack React framework
method: scrapling+scrapegraph
fetched_at: 2026-11-26T10:37:14.781710+00:00
---

# What is TanStack Start? | Full-stack React framework

> Source: https://www.cloudflare.com/learning/serverless/what-is-tanstack-start/

[ Learning Center ](https://www.cloudflare.com/learning/) / serverless

##  What is TanStack Start? 

TanStack Start is an open-source, full-stack web framework for React and Solid. It is built on TanStack Router and adds server-side rendering (SSR), streaming, type-safe server functions, server routes, and middleware. Start apps can be deployed to any JavaScript runtime, such as Cloudflare Workers. TanStack Start reached version 1.0 on October 13, 2026. 

[Learning Center](https://www.cloudflare.com/learning)/serverless/[What is BaaS? | Backend-as-a-Service vs. serverless](https://www.cloudflare.com/learning/serverless/glossary/backend-as-a-service-baas/)[What do client side and server side mean? | Client side vs. server side](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/)[What is Function-as-a-Service (FaaS)?](https://www.cloudflare.com/learning/serverless/glossary/function-as-a-service-faas/)[Can mobile applications use a serverless architecture?](https://www.cloudflare.com/learning/serverless/glossary/mobile-apps-serverless-backend/)[What is Platform-as-a-Service (PaaS)?](https://www.cloudflare.com/learning/serverless/glossary/platform-as-a-service-paas/)[The Serverless Framework and Cloudflare Workers | What is the Serverless Framework?](https://www.cloudflare.com/learning/serverless/glossary/serverless-and-cloudflare-workers/)[What is a serverless microservice? | Serverless microservices explained](https://www.cloudflare.com/learning/serverless/glossary/serverless-microservice/)[How are serverless computing and Platform-as-a-Service different?](https://www.cloudflare.com/learning/serverless/glossary/serverless-vs-paas/)[What is Chrome V8?](https://www.cloudflare.com/learning/serverless/glossary/what-is-chrome-v8/)[What is continuous integration and continuous delivery (CI/CD)?](https://www.cloudflare.com/learning/serverless/glossary/what-is-ci-cd/)[What is edge computing?](https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/)[How to build and deploy your web app fast](https://www.cloudflare.com/learning/serverless/how-to-deploy-app-or-website/)[How does serverless JavaScript work? | Service workers and Cloudflare Workers](https://www.cloudflare.com/learning/serverless/serverless-javascript/)[How can serverless computing improve performance? | Lambda performance](https://www.cloudflare.com/learning/serverless/serverless-performance/)[Serverless computing vs. containers | How to choose](https://www.cloudflare.com/learning/serverless/serverless-vs-containers/)[What is server-side rendering (SSR)?](https://www.cloudflare.com/learning/serverless/what-is-server-side-rendering/)[What is serverless computing?](https://www.cloudflare.com/learning/serverless/what-is-serverless/)[What is TanStack Start?](https://www.cloudflare.com/learning/serverless/what-is-tanstack-start/)[Why use serverless?](https://www.cloudflare.com/learning/serverless/why-use-serverless/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define TanStack Start and explain how it relates to TanStack Router 
  * Describe its core features: SSR, streaming, server functions, server routes, and middleware 
  * Understand what changed in TanStack Start 1.0 
  * Explain how a TanStack Start application runs on a serverless platform like Cloudflare Workers 



Related content  [ What is serverless computing? ](https://www.cloudflare.com/learning/serverless/what-is-serverless/)[ How to build and deploy your web app fast ](https://www.cloudflare.com/learning/serverless/how-to-deploy-app-or-website/)[ How does serverless JavaScript work? | Service workers and Cloudflare Workers ](https://www.cloudflare.com/learning/serverless/serverless-javascript/)

On this page

  * What is TanStack Start?

  * How does TanStack Start work?

  * What are the key features of TanStack Start?

  * What is new in TanStack Start 1.0?

  * TanStack Start vs. other full-stack frameworks

  * Who uses TanStack Start in production?

  * How Lovable migrated their 70 million apps platform from Next.js to TanStack Start on Workers

  * How do you deploy TanStack Start to Cloudflare?

  * FAQs

    * What is TanStack Start used for?

    * Is TanStack Start production-ready?

    * Which companies use TanStack Start?

    * What is the difference between TanStack Router and TanStack Start?

    * What are TanStack Start server functions?

    * Does TanStack Start support React Server Components?

    * Can TanStack Start run on Cloudflare Workers?

    * Why is TanStack Start good for AI coding agents?

    * Is TanStack Start free?

    * How does TanStack Start compare to Next.js?




## What is TanStack Start?

TanStack Start is a full-stack framework. That means one codebase can render pages on the [server](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/), hydrate them in the browser, and run backend logic, such as database queries, authentication, and API calls, in the same project.

Start is made by TanStack, the open-source team behind TanStack Query, TanStack Table, and TanStack Router. Routing does most of the work in any web framework, and Start uses TanStack Router for all of its routing. Start then adds the server and builds layers around that router.

TanStack calls Start **"client-first, server-capable."** Developers write a normal React (or Solid) application with type-safe routes. They add server code only where they need it, and server boundaries are explicit in the code. This is the main difference from frameworks that render on the server by default.

## How does TanStack Start work?

A TanStack Start application has three main parts:

  1. **Routes.** Each route is a file that declares its URL path, its URL parameters, a schema for its search parameters, a data `loader`, and the component it renders. TanStack Router generates TypeScript types from these files. This means links, parameters, and loader data are all type-checked.
  2. **Server functions.** A server function is created with `createServerFn()`. It always runs on the server, but it can be called from anywhere in the app: a route loader, a component, or an event handler. TanStack Start compiles each call into a type-safe remote procedure call (RPC), so you never write a fetch request or an API route by hand.
  3. **A build tool.** Start uses a build tool such as [Vite](https://vite.dev/) to produce two builds: one for the browser and one for the server. The server build exposes a single standard `fetch(request) => Response` handler. Any runtime that supports the Fetch API can run it.



When a user requests a page, the server runs the matching route loaders, renders the HTML, and streams it to the browser. React then hydrates the page. Later navigations happen on the client, and data comes from the same loaders and server functions over RPC.
    
    
    // src/routes/index.tsx
    import { createFileRoute } from "@tanstack/react-router";
    import { createServerFn } from "@tanstack/react-start";
    
    // Runs only on the server, but is fully typed on the client
    const getGreeting = createServerFn()
      .validator((name: string) => name)
      .handler(async ({ data: name }) => {
    return { message: `Hello, ${name}!` };
      });
    
    export const Route = createFileRoute("/")({
      loader: () => getGreeting({ data: "world" }),
      component: Home,
    });
    
    function Home() {
      const { message } = Route.useLoaderData(); // typed as { message: string }
      return <h1>{message}</h1>;
    }
    

## What are the key features of TanStack Start?

  * **Full-document SSR and streaming.** The server renders complete HTML for fast first loads and search engine indexing, and streams slower data to the browser as it becomes ready.
  * **Selective SSR.** Each route can choose full SSR, data-only SSR, or client-only rendering.
  * **Static prerendering.** Pages can be rendered to static HTML at build time and served from a CDN.
  * **Server functions.** Type-safe RPCs with input validation, used for reads and mutations.
  * **Server routes.** Raw HTTP endpoints (for example, `/api/webhooks`) for callers outside the app, such as webhooks, mobile clients, or third-party services.
  * **Middleware and context.** Composable middleware for authentication, logging, and access policy. It runs on both requests and server functions.
  * **Import protection.** The compiler stops server-only code, like secrets or database clients, from being bundled into the browser build.
  * **End-to-end type safety.** TypeScript types flow from routes to loaders to server functions to components. The route tree types are generated automatically during development.
  * **Built for AI coding agents.** End-to-end types give agents a compiler feedback loop that catches anything a change breaks. TanStack Start also ships agent skills inside its npm packages through [TanStack Intent](https://tanstack.com/intent/latest), so coding agents learn the framework's best practices, not just its APIs.
  * **Deploy anywhere.** Swapping hosting providers changes the build configuration, not your routes or application code.
  * **Experimental features.** React Server Components and HTTP 103 Early Hints are available behind experimental APIs.



You can find details on each of these and more on the official [TanStack Start website](https://tanstack.com/start/latest/docs/framework/react/overview).

## What is new in TanStack Start 1.0?

TanStack Start entered Release Candidate (RC) status in September 2025. At that point, its API was declared feature-complete and stable. According to TanStack, enterprise teams and Fortune 500 companies were already running it in production, many of them since the beta. Version 1.0 makes that stability official, so teams can now rely on semantic versioning for upgrades. Notable changes during the RC period include:

  * **`validator()` replaces `inputValidator()`** as the standard way to validate server function and middleware input. The old method still works but triggers a compiler warning.
  * **Rsbuild support** joins Vite as a first-class build tool, including experimental React Server Components support.
  * **Vite 7+ baseline** , with support for Vite's bundled development mode.
  * **Hosting through build plugins.** Each hosting provider plugs in as a build plugin, such as `@cloudflare/vite-plugin`. On Cloudflare, the Worker entrypoint is now `@tanstack/react-start/server-entry` instead of a generated `.output/` directory.
  * **Faster server rendering.** In TanStack's own SSR benchmark, throughput improved about [5.5×](https://tanstack.com/blog/tanstack-start-5x-ssr-throughput) after a series of profiling-driven optimizations.
  * **Agent skills.** Start's npm packages ship `SKILL.md` files for topics like server functions, middleware, and deployment. Coding agents can discover them with TanStack Intent.
  * **Security hardening.** This includes stricter server-function input and response validation, shipped as part of the CVE-2026-102989 fix.



## TanStack Start vs. other full-stack frameworks

TanStack Start covers the same ground as frameworks like Next.js, Remix/React Router, and SvelteKit. Several design choices set it apart:

| TanStack Start | Typical server-first framework  
---|---|---  
Default rendering model | Client-first app, server where you opt in | Server-rendered by default  
Routing | TanStack Router: fully type-safe paths, params, and search params | File-based, types usually partial or generated  
Backend calls | Typed server functions (RPC) and server routes | API routes, server actions, or loaders  
Build tool | Vite or Rsbuild | Often framework-specific  
Hosting | Any Fetch-API runtime through adapters | Often optimized for one platform  
  
Start is a good fit for highly interactive applications, such as dashboards, SaaS products, and internal tools. It also suits teams that already use TanStack Query or TanStack Router, and projects that need strong type safety throughout. For a mostly static content site, a static site generator may be simpler.

## Who uses TanStack Start in production?

Teams of all sizes run TanStack Start in production. One of the largest deployments is [Lovable](https://lovable.dev/), an AI app builder that generates full-stack web applications from a chat prompt and hosts them on Cloudflare Workers.

In 2026, Lovable made TanStack Start the default framework for every new app it generates. At Cloudflare Connect 2026, Lovable co-founder and CTO Fabian Hedin explained why:

  * **Server-side rendering for SEO.** Lovable apps were originally client-rendered React single-page apps. Moving to TanStack Start gave every generated app [server-side rendering](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/), so search engines can index their full content.
  * **One codebase for the AI to work with.** TanStack Start's isomorphic model, with one codebase compiled into a server build and a browser build, is simpler for an AI agent to edit than a separate frontend and backend.
  * **Static where possible.** Each route can be prerendered or server-rendered, so apps keep fast static delivery for pages that do not need per-request data.



Lovable runs at a large scale: more than 70 million apps created, about 1 million new apps a week, and about 7 billion Workers requests a day. Server-rendered apps run in [Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/), which load each app's code on demand and start in under one second.

## How Lovable migrated their 70 million apps platform from Next.js to TanStack Start on Workers

## How do you deploy TanStack Start to Cloudflare?

The server build of a TanStack Start app is a standard `fetch` handler. That is the same interface used by [Cloudflare Workers](https://www.cloudflare.com/developer-platform/products/workers/), so a Start app runs on Workers without changes. Cloudflare is an Official Hosting Partner of TanStack Start.

Running on Workers means:

  * **Rendering close to users.** SSR and server functions run in Cloudflare data centers in [330+ cities](https://www.cloudflare.com/network/), with no regions to choose and no servers to manage.
  * **Direct access to the platform.** Server functions can read and write [D1](https://www.cloudflare.com/developer-platform/products/d1/) (SQL), KV, [R2](https://www.cloudflare.com/developer-platform/products/r2/) (object storage), Durable Objects, Queues, Workflows, and [Workers AI](https://www.cloudflare.com/developer-platform/products/workers-ai/) through bindings. This requires no API keys or network round trips to another cloud.
  * **The same runtime locally and in production.** The Cloudflare Vite plugin runs your app inside `workerd`, the open-source Workers runtime, during `vite dev`.



**Create a new project:**
    
    
    npm create cloudflare@latest -- my-app --framework=tanstack-start
    

**Deploy an existing project:** Run `npx wrangler deploy` in a TanStack Start project. Wrangler detects the framework, generates the configuration, and deploys. You can also set it up manually by adding the Cloudflare plugin to `vite.config.ts`:
    
    
    import { defineConfig } from "vite";
    import { tanstackStart } from "@tanstack/react-start/plugin/vite";
    import { cloudflare } from "@cloudflare/vite-plugin";
    import react from "@vitejs/plugin-react";
    
    export default defineConfig({
      plugins: [
    cloudflare({ viteEnvironment: { name: "ssr" } }),
    tanstackStart(),
    react(),
      ],
    });
    

**Use Cloudflare bindings in a server function:**
    
    
    import { createServerFn } from "@tanstack/react-start";
    import { env } from "cloudflare:workers";
    
    export const getPost = createServerFn()
      .validator((id: string) => id)
      .handler(async ({ data: id }) => {
    return env.DB.prepare("SELECT * FROM posts WHERE id = ?").bind(id).first();
      });
    

The full guide covers custom entrypoints for Queues, Cron Triggers, Durable Objects, and Workflows, as well as static prerendering. See the [TanStack Start framework guide in the Cloudflare Workers docs](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/).

* * *

## FAQs

#### What is TanStack Start used for?

TanStack Start is used to build full-stack web applications with React or Solid. It handles routing, server-side rendering, streaming, data loading, and backend logic, using server functions and server routes, in a single type-safe codebase.

#### Is TanStack Start production-ready?

Yes. TanStack Start 1.0 was released on October 13, 2026, after a Release Candidate period that began in September 2025. According to the TanStack team, enterprise teams and Fortune 500 companies already run it in production, many since the beta. The AI app builder Lovable uses TanStack Start as the default framework for every app it generates.

#### Which companies use TanStack Start?

TanStack Start is used in production by enterprise teams and startups. One of the largest deployments is Lovable, an AI app builder that uses TanStack Start for every new app it generates. Lovable hosts more than 70 million apps on Cloudflare Workers, and its CTO explained the setup in a talk at Cloudflare Connect 2026.

#### What is the difference between TanStack Router and TanStack Start?

TanStack Router is a type-safe client-side router. TanStack Start is a full-stack framework built on top of TanStack Router. Start adds server-side rendering, streaming, server functions, server routes, middleware, and production server builds. If an application does not need a server, TanStack Router alone may be enough.

#### What are TanStack Start server functions?

Server functions are functions created with `createServerFn()` that always execute on the server but can be called from client code. TanStack Start turns each call into a type-safe RPC, validates input with `.validator()`, and keeps server-only code out of the browser bundle.

#### Does TanStack Start support React Server Components?

Yes, as an experimental feature. React Server Components are available in TanStack Start for both Vite and Rsbuild builds, but the API may change.

#### Can TanStack Start run on Cloudflare Workers?

Yes. Cloudflare is an Official Hosting Partner of TanStack Start. Use `@cloudflare/vite-plugin` and deploy with `wrangler deploy`. Server functions can access Cloudflare bindings like D1, KV, R2, Durable Objects, and Workers AI through `import { env } from "cloudflare:workers"`.

#### Why is TanStack Start good for AI coding agents?

TanStack Start's end-to-end type safety means that when an AI coding agent makes a change, the TypeScript compiler catches anything it breaks. TanStack Start also ships agent skills inside its npm packages through TanStack Intent, so agents learn the framework's recommended patterns, not just its API surface.

#### Is TanStack Start free?

Yes. TanStack Start is 100% open source under the MIT license. Cloudflare Workers also has a free plan that can host TanStack Start applications.

#### How does TanStack Start compare to Next.js?

Both are full-stack React frameworks with SSR, streaming, and server-side data access. TanStack Start is client-first and has end-to-end type-safe routing through TanStack Router. It uses Vite or Rsbuild and is designed to deploy to many hosting providers through adapters. Next.js is server-first by default and uses its own build tooling.
