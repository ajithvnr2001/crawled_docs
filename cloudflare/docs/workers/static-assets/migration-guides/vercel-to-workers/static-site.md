---
url: https://developers.cloudflare.com/workers/static-assets/migration-guides/vercel-to-workers/static-site/
title: Migrate a static site or SPA from Vercel to Cloudflare Workers \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-11-06T09:03:45.107019+00:00
---

# Migrate a static site or SPA from Vercel to Cloudflare Workers · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/static-assets/migration-guides/vercel-to-workers/static-site/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Static Assets](https://developers.cloudflare.com/workers/static-assets/)Migration Guides

  4. /[Migrate from Vercel to Cloudflare Workers](https://developers.cloudflare.com/workers/static-assets/migration-guides/vercel-to-workers/)
  5. /Static site or SPA



# Migrate a static site or SPA from Vercel to Cloudflare Workers

Last updated Nov 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you beginMigrate your siteRelated resources

This guide moves a static site or single-page application (SPA) from Vercel to Cloudflare Workers. Use it if your project does not render pages on the server. [Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/) serves your build output, so you do not need a framework adapter.

## Before you begin

Review the steps in [Before you begin](https://developers.cloudflare.com/workers/static-assets/migration-guides/vercel-to-workers/#before-you-begin) that apply to every framework.

## Migrate your site

  1. In the Vercel dashboard, go to your project's **Settings** > **Build & Development settings**. Note the **Build Command** and **Output Directory** values.

![Finding the Build Command and Output Directory fields](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1848,height=1100,format=webp/_astro/vercel-deploy-1.DrHD4fam.png)
  2. In the root of your project, create a Wrangler configuration file. Replace `<your-project-name>` with your project name, and `<your-build-directory>` with the output directory, for example `./dist`.

For a static site:
         
         {
         	"name": "<your-project-name>",
         	// Set this to today's date
         	"compatibility_date": "2026-11-06",
         	"assets": {
         		"directory": "<your-build-directory>",
         	},
         }
         
         name = "<your-project-name>"
         # Set this to today's date
         compatibility_date = "2026-11-06"
         
         [assets]
         directory = "<your-build-directory>"

For a single-page application, add `not_found_handling`:
         
         {
         	"name": "<your-project-name>",
         	// Set this to today's date
         	"compatibility_date": "2026-11-06",
         	"assets": {
         		"directory": "<your-build-directory>",
         		"not_found_handling": "single-page-application",
         	},
         }
         
         name = "<your-project-name>"
         # Set this to today's date
         compatibility_date = "2026-11-06"
         
         [assets]
         directory = "<your-build-directory>"
         not_found_handling = "single-page-application"

  3. Build your project, then deploy it:

npmyarnpnpm
         
         npx wrangler deploy
         
         yarn wrangler deploy
         
         pnpm wrangler deploy

  4. To deploy on every push, [connect your repository to Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/#connect-a-new-worker). Use the same build command as on Vercel, and use `npx wrangler deploy` as the deploy command.




## Related resources

  * [Static Assets](https://developers.cloudflare.com/workers/static-assets/)
  * [Single-page application routing](https://developers.cloudflare.com/workers/static-assets/routing/single-page-application/)
  * [Migrate from Vercel to Workers](https://developers.cloudflare.com/workers/static-assets/migration-guides/vercel-to-workers/)



[PreviousTanStack Start](https://developers.cloudflare.com/workers/static-assets/migration-guides/vercel-to-workers/tanstack-start/)[NextMigrate from Pages to Workers](https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/static-assets/migration-guides/vercel-to-workers/static-site.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
