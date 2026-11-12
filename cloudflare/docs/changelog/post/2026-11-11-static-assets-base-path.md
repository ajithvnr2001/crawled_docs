---
url: https://developers.cloudflare.com/changelog/post/2026-11-11-static-assets-base-path/
title: Serve a Worker's static assets from a URL path like /blog/ \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-12T09:30:22.885334+00:00
---

# Serve a Worker's static assets from a URL path like /blog/ · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-11-static-assets-base-path/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 11, 2026

## Serve a Worker's static assets from a URL path like /blog/

[Workers](https://developers.cloudflare.com/workers/)[Cloudflare CLI](https://developers.cloudflare.com/cf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now serve your Worker's [static assets](https://developers.cloudflare.com/workers/static-assets/) from a URL path prefix, such as `example.com/blog/`, without changing your build output.

Previously, to serve assets from `/blog/`, you had to nest your files in a matching `blog` directory. Now, set `assets.base_path` in your Wrangler configuration file, or `worker.assets.basePath` in [`cloudflare.config.ts`](https://developers.cloudflare.com/cf/projects/cloudflare-config/), and keep your files at the root of your asset directory.

Use [Wrangler 4.148.0 ↗︎](https://github.com/cloudflare/workers-sdk/releases/tag/wrangler%404.148.0) or later. With `cloudflare.config.ts`, use [`cf` 1.0.0-beta.13 ↗︎](https://github.com/cloudflare/cf/releases/tag/cf%401.0.0-beta.13) or later.

For example, this configuration serves your built assets from `/blog/`:

The following content appears twice: first for the Cloudflare CLI (`cf`), then for Wrangler. Use `cf` for new projects. In an existing project, use the CLI that the project already uses.

Cloudflare CLI

cloudflare.config.tsts
    
    
    import { defineConfig } from "cf/config";
    
    export default defineConfig({
    worker: {
      name: "blog",
      // Set this to today's date
      compatibilityDate: "2026-11-12",
      assets: {
        basePath: "/blog",
      },
    },
    });

Wrangler
    
    
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

Requests to `/blog/` serve `dist/index.html`, and requests to `/blog/posts/post1` serve `dist/posts/post1.html`. Requests outside `/blog/` do not match your static assets and run your Worker, if it has one.

Paths in `_headers`, `_redirects`, and `run_worker_first` use the full public path, including `/blog`. If you build with the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/), also set Vite's `base` option to `/blog/`.

For more information, refer to [Serving a subdirectory](https://developers.cloudflare.com/workers/static-assets/routing/advanced/serving-a-subdirectory/).
