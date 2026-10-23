---
url: https://developers.cloudflare.com/workers/framework-guides/web-apps/foldkit/
title: Foldkit \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:57:11.703461+00:00
---

# Foldkit · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/framework-guides/web-apps/foldkit/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

Framework guides

  4. /Web applications
  5. /Foldkit



# Foldkit

Last updated Oct 13, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a Foldkit applicationConfigure your rendering mode SPA SSG SSRPreview and deploy

[Foldkit ↗︎](https://foldkit.dev/) supports single-page applications (SPA), static site generation (SSG), and server-side rendering (SSR). Each mode uses [Workers Assets](https://developers.cloudflare.com/workers/static-assets/) to serve browser files. SSR also runs a Worker `fetch` handler.

You need Node.js 22.22.2 or newer and a Cloudflare account.

## Create a Foldkit application

  1. Create a project with [`create-foldkit-app` ↗︎](https://www.npmjs.com/package/create-foldkit-app):

npm
         
         npx create-foldkit-app@latest --name my-foldkit-app

Choose a rendering mode when prompted. For SPA, choose the `routing` example. Select npm as the package manager.

  2. In the project directory, install Wrangler:
         
         cd my-foldkit-app

npm
         
         npm i -D wrangler




## Configure your rendering mode

In the project directory, create a `wrangler.jsonc` file with the configuration for your rendering mode.

### SPA

The SPA build writes `index.html` and browser assets to `dist`. The `single-page-application` setting serves `index.html` when a client-side route does not match an asset.
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "my-foldkit-app",
      // Set this to today's date
      "compatibility_date": "2026-10-14",
      "assets": {
        "directory": "./dist",
        "not_found_handling": "single-page-application"
      }
    }
    
    
    name = "my-foldkit-app"
    # Set this to today's date
    compatibility_date = "2026-10-14"
    
    [assets]
    directory = "./dist"
    not_found_handling = "single-page-application"

### SSG

The SSG build uses a server bundle to prerender routes, then writes HTML and browser assets to `dist/client`. Deploy only `dist/client` with Workers Assets.
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "my-foldkit-app",
      // Set this to today's date
      "compatibility_date": "2026-10-14",
      "assets": {
        "directory": "./dist/client"
      }
    }
    
    
    name = "my-foldkit-app"
    # Set this to today's date
    compatibility_date = "2026-10-14"
    
    [assets]
    directory = "./dist/client"

### SSR

The SSR build writes a Web `fetch` handler to `dist/server/fetch.js` and browser assets to `dist/client`. The Worker handles page requests, while Workers Assets serves the browser files.
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "my-foldkit-app",
      "main": "./dist/server/fetch.js",
      // Set this to today's date
      "compatibility_date": "2026-10-14",
      "assets": {
        "directory": "./dist/client"
      }
    }
    
    
    name = "my-foldkit-app"
    main = "./dist/server/fetch.js"
    # Set this to today's date
    compatibility_date = "2026-10-14"
    
    [assets]
    directory = "./dist/client"

## Preview and deploy

  1. Build the application:

npm
         
         npm run build

  2. Preview it in the Workers runtime:

npm
         
         npx wrangler dev

Open the local URL printed by Wrangler. For SPA, open `/people` and reload it. For SSG, visit `/about/`. For SSR, increment the counter and reload. Its cookie-backed value should persist.

  3. Build and deploy the application:

npm
         
         npm run build

npm
         
         npx wrangler deploy




Open the `workers.dev` URL printed by Wrangler to verify the deployed application. For more information about SSG and SSR builds, refer to [Foldkit's server rendering guide ↗︎](https://foldkit.dev/core/server-rendering).

[PreviousVike](https://developers.cloudflare.com/workers/framework-guides/web-apps/vike/)[Nextfate](https://developers.cloudflare.com/workers/framework-guides/web-apps/fate/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/framework-guides/web-apps/foldkit.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
