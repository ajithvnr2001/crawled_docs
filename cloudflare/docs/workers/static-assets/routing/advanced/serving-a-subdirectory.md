---
url: https://developers.cloudflare.com/workers/static-assets/routing/advanced/serving-a-subdirectory/
title: Serving a subdirectory \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-29T08:14:04.212770+00:00
---

# Serving a subdirectory · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/static-assets/routing/advanced/serving-a-subdirectory/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Static Assets](https://developers.cloudflare.com/workers/static-assets/)Routing

  4. /Advanced
  5. /Serving a subdirectory



# Serving a subdirectory

Last updated Oct 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Set `assets.base_path` to serve static assets from a URL subpath. The files remain at the root of `assets.directory`.

Note

This option requires Wrangler 4.148.0 or later. With [`cloudflare.config.ts`](https://developers.cloudflare.com/cf/projects/cloudflare-config/), use `worker.assets.basePath` and `cf` 1.0.0-beta.13 or later. Your build configuration supplies the asset directory.

For example, use this asset directory to serve a blog:

  * dist 
    * index.html
    * posts 
      * post1.html
      * post2.html



Set `assets.base_path` to `/blog` in your Wrangler configuration file:
    
    
    {
    	"$schema": "./node_modules/wrangler/config-schema.json",
    	"name": "assets-on-a-path-example",
    	"main": "src/index.js",
    	"upload_source_maps": true,
    	"route": "example.com/blog/*",
    	"assets": {
    		"directory": "dist",
    		"base_path": "/blog"
    	}
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "assets-on-a-path-example"
    main = "src/index.js"
    upload_source_maps = true
    route = "example.com/blog/*"
    
    [assets]
    directory = "dist"
    base_path = "/blog"

Requests to `example.com/blog/` serve `dist/index.html`. Requests to `example.com/blog/posts/post1` serve `dist/posts/post1.html`.

Requests outside `/blog` do not resolve static assets. Requests made through the [assets binding](https://developers.cloudflare.com/workers/static-assets/binding/#binding) also use the mounted public path. Forwarding the original request works unchanged. When constructing a request, include `/blog` in its pathname, for example, `env.ASSETS.fetch("https://assets.local/blog/posts/post1")`.

Paths in `_headers`, `_redirects`, and `assets.run_worker_first` use the public URL path. Include `/blog` in those paths when they apply to this example.

[PreviousHTML handling](https://developers.cloudflare.com/workers/static-assets/routing/advanced/html-handling/)[NextHeaders](https://developers.cloudflare.com/workers/static-assets/headers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/static-assets/routing/advanced/serving-a-subdirectory.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
