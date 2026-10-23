---
url: https://developers.cloudflare.com/workers/framework-guides/web-apps/sveltekit/
title: SvelteKit \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-12T08:23:32.498469+00:00
---

# SvelteKit · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/framework-guides/web-apps/sveltekit/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

Framework guides

  4. /Web applications
  5. /SvelteKit



# SvelteKit

Last updated Oct 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Set up a new project2\. Develop locally3\. Deploy your ProjectBindings

In this guide, you will create a new [SvelteKit ↗︎](https://svelte.dev/docs/kit/introduction) application and deploy to Cloudflare Workers.

Already have a SvelteKit project?

Run `wrangler deploy` in a project without a Wrangler configuration file and Wrangler will automatically detect SvelteKit, generate the necessary configuration, and deploy your project.

npmyarnpnpm
    
    
    npx wrangler deploy
    
    
    yarn wrangler deploy
    
    
    pnpm wrangler deploy

Learn more about [automatic project configuration](https://developers.cloudflare.com/workers/framework-guides/automatic-configuration/).

First deploy fails with `Types file not found`

When Wrangler configures an existing SvelteKit project, it runs the Svelte CLI (`sv add`) to install the Cloudflare adapter. This adds `wrangler types --check` to the `build` script in your `package.json`. The types file does not exist yet, so the first build fails with the following error:
    
    
    ✘ [ERROR] Types file not found at worker-configuration.d.ts.

To fix this, generate the types file, then deploy again:

npmyarnpnpm
    
    
    npx wrangler types
    
    
    yarn wrangler types
    
    
    pnpm wrangler types

npmyarnpnpm
    
    
    npx wrangler deploy
    
    
    yarn wrangler deploy
    
    
    pnpm wrangler deploy

You only need to do this once. Wrangler has already created your Wrangler configuration file, so the second deploy skips project setup.

SvelteKitDetected

Generated configuration

wrangler.jsonc

main:.svelte-kit/cloudflare/_worker.js

wrangler.jsonc

assets:directory: .svelte-kit/cloudflare

wrangler.jsonc

compatibility_flags:nodejs_compat

wrangler.jsonc

observability:enabled: true

svelte.config.js

adapter:@sveltejs/adapter-cloudflare

WorkersDeployed

Wrangler handles configuration automatically

## 1\. Set up a new project

Use the [`create-cloudflare` ↗︎](https://www.npmjs.com/package/create-cloudflare) CLI (C3) to set up a new project. C3 will create a new project directory, initiate SvelteKit's official setup tool, and provide the option to deploy instantly.

To use `create-cloudflare` to create a new SvelteKit project with Workers Assets, run the following command:

npmyarnpnpm
    
    
    npm create cloudflare@latest -- my-svelte-app --framework=svelte
    
    
    yarn create cloudflare my-svelte-app --framework=svelte
    
    
    pnpm create cloudflare@latest my-svelte-app --framework=svelte

After setting up your project, change your directory by running the following command:
    
    
    cd my-svelte-app

## 2\. Develop locally

After you have created your project, run the following command in the project directory to start a local server. This will allow you to preview your project locally during development.

npmyarnpnpm
    
    
    npm run dev
    
    
    yarn run dev
    
    
    pnpm run dev

## 3\. Deploy your Project

Your project can be deployed to a `*.workers.dev` subdomain or a [Custom Domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/), from your own machine or from any CI/CD system, including [Cloudflare's own](https://developers.cloudflare.com/workers/ci-cd/builds/).

The following command will build and deploy your project. If you're using CI, ensure you update your ["deploy command"](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#build-settings) configuration appropriately.

npmyarnpnpm
    
    
    npm run deploy
    
    
    yarn run deploy
    
    
    pnpm run deploy

* * *

## Bindings

Your SvelteKit application can be fully integrated with the Cloudflare Developer Platform, in both local development and in production, by using product bindings. The [SvelteKit documentation ↗︎](https://kit.svelte.dev/docs/adapter-cloudflare#runtime-apis) provides information about configuring bindings and how you can access them in your SvelteKit hooks and endpoints.

With bindings, your application can be fully integrated with the Cloudflare Developer Platform, giving you access to compute, storage, AI and more.

### [Bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/)

Access to compute, storage, AI and more.

[PreviousMicrofrontends](https://developers.cloudflare.com/workers/framework-guides/web-apps/microfrontends/)[NextVike](https://developers.cloudflare.com/workers/framework-guides/web-apps/vike/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/framework-guides/web-apps/sveltekit.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
