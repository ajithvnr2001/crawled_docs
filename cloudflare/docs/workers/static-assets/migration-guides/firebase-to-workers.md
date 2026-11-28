---
url: https://developers.cloudflare.com/workers/static-assets/migration-guides/firebase-to-workers/
title: Migrate from Firebase Hosting to Workers \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:27.697537+00:00
---

# Migrate from Firebase Hosting to Workers · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/static-assets/migration-guides/firebase-to-workers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Static Assets](https://developers.cloudflare.com/workers/static-assets/)

  4. /Migration Guides
  5. /Migrate from Firebase Hosting to Workers



# Migrate from Firebase Hosting to Workers

Last updated Nov 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFrameworks1\. Find your build command and output directory2\. Create a Wrangler configuration file3\. Connect and deploy with Workers Builds4\. Switch your custom domainRelated resources

This guide walks you through migrating an existing static site or single-page application (SPA) from Firebase Hosting to Cloudflare Workers with [Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/).

## Frameworks

If your Firebase Hosting project uses a supported web framework, review the [Workers framework guides](https://developers.cloudflare.com/workers/framework-guides/) or run [`wrangler deploy`](https://developers.cloudflare.com/workers/framework-guides/automatic-configuration/) to automatically detect your framework and generate a Workers configuration. Otherwise, continue with the steps below.

## 1\. Find your build command and output directory

Check your `firebase.json` file for the `hosting.public` field, which specifies the build output directory Firebase deploys:

firebase.jsonjson
    
    
    {
    	"hosting": {
    		"public": "dist",
    		"rewrites": [
    			{
    				"source": "**",
    				"destination": "/index.html"
    			}
    		]
    	}
    }

Identify your project's build command in `package.json` (typically `npm run build` or a framework-specific command such as `ng build`). If `firebase.json` includes a catch-all rewrite to `/index.html`, your app is configured as a Single Page Application (SPA).

## 2\. Create a Wrangler configuration file

In the root of your project, create a `wrangler.jsonc` file. Replace `<your-project-name>` with your Worker name and `<your-build-directory>` with the `public` directory from `firebase.json`.

For a static site ([Static Site Generation](https://developers.cloudflare.com/workers/static-assets/routing/static-site-generation/)):
    
    
    {
    	"name": "<your-project-name>",
    	// Set this to today's date
    	"compatibility_date": "2026-11-28",
    	"assets": {
    		"directory": "<your-build-directory>"
    	}
    }
    
    
    name = "<your-project-name>"
    # Set this to today's date
    compatibility_date = "2026-11-28"
    
    [assets]
    directory = "<your-build-directory>"

For a [Single Page Application](https://developers.cloudflare.com/workers/static-assets/routing/single-page-application/) (matching a Firebase `**` → `/index.html` rewrite):
    
    
    {
    	"name": "<your-project-name>",
    	// Set this to today's date
    	"compatibility_date": "2026-11-28",
    	"assets": {
    		"directory": "<your-build-directory>",
    		"not_found_handling": "single-page-application"
    	}
    }
    
    
    name = "<your-project-name>"
    # Set this to today's date
    compatibility_date = "2026-11-28"
    
    [assets]
    directory = "<your-build-directory>"
    not_found_handling = "single-page-application"

If your `firebase.json` defines custom HTTP headers or URL redirects, move them into [`_headers`](https://developers.cloudflare.com/workers/static-assets/headers/) and [`_redirects`](https://developers.cloudflare.com/workers/static-assets/redirects/) files inside your static asset output directory.

## 3\. Connect and deploy with Workers Builds

  1. Push your updated repository (including `wrangler.jsonc`) to GitHub or GitLab.
  2. Follow [Connect a new Worker](https://developers.cloudflare.com/workers/ci-cd/builds/#connect-a-new-worker) to link your repository to Workers Builds.
  3. Set your **Build command** (for example, `npm run build`) and keep the default **Deploy command** (`npx wrangler deploy`).



Alternatively, deploy directly from your terminal with `npx wrangler deploy`.

## 4\. Switch your custom domain

Workers [Custom Domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/) support domains whose DNS is managed by Cloudflare.

  1. Verify your deployed Worker on its `*.workers.dev` subdomain.
  2. In your domain's **DNS** > **Records** page, remove any Firebase Hosting `A`, `AAAA`, or `CNAME` records for the hostname you are migrating.
  3. Follow [Add a Custom Domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/#add-a-custom-domain) to attach the domain to your Worker.
  4. Once traffic is serving from Workers, remove the old site from Firebase Hosting.



## Related resources

  * [Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/)
  * [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/)
  * [Migrate from Pages to Workers](https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/)



[PreviousMigrate from Pages to Workers](https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/)[NextMigrate from GitHub Pages to Workers](https://developers.cloudflare.com/workers/static-assets/migration-guides/github-pages-to-workers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/static-assets/migration-guides/firebase-to-workers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
