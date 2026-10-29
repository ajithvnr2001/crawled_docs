---
url: https://developers.cloudflare.com/changelog/post/2026-10-28-static-assets-base-path/
title: Serve Workers Static Assets from a URL path prefix \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-29T08:13:59.276360+00:00
---

# Serve Workers Static Assets from a URL path prefix · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-28-static-assets-base-path/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 28, 2026

## Serve Workers Static Assets from a URL path prefix

[Workers](https://developers.cloudflare.com/workers/)[Cloudflare CLI](https://developers.cloudflare.com/cf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers Static Assets can now serve assets from a URL path prefix without changing their directory structure. Set `assets.base_path` in Wrangler, or `worker.assets.basePath` in `cloudflare.config.ts`.

Use [Wrangler 4.148.0 ↗︎](https://github.com/cloudflare/workers-sdk/releases/tag/wrangler%404.148.0) or later. With `cloudflare.config.ts`, use [`cf` 1.0.0-beta.13 ↗︎](https://github.com/cloudflare/cf/releases/tag/cf%401.0.0-beta.13) or later.

For example, this configuration serves your built assets from `/blog/`:

Select your preferred CLI

WranglerCF

Changes examples on this page to use the selected CLI.
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "assets": {
        "directory": "./dist",
        "base_path": "/blog"
      }
    }
    
    
    [assets]
    directory = "./dist"
    base_path = "/blog"

cloudflare.config.tsts
    
    
    import { defineConfig } from "cf/config";
    
    export default defineConfig({
    worker: {
      name: "blog",
      // Set this to today's date
      compatibilityDate: "2026-10-29",
      assets: {
        basePath: "/blog",
      },
    },
    });

With Wrangler, `assets.directory` selects the directory to serve. With [`cloudflare.config.ts`](https://developers.cloudflare.com/cf/projects/cloudflare-config/), your build configuration supplies the assets.

To configure the option, refer to [Serving a subdirectory](https://developers.cloudflare.com/workers/static-assets/routing/advanced/serving-a-subdirectory/).
