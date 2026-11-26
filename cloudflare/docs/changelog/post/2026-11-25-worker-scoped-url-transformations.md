---
url: https://developers.cloudflare.com/changelog/post/2026-11-25-worker-scoped-url-transformations/
title: URL-based image optimization in Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-26T10:37:13.861624+00:00
---

# URL-based image optimization in Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-25-worker-scoped-url-transformations/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 25, 2026

## URL-based image optimization in Workers

[Cloudflare Images](https://developers.cloudflare.com/images/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

In [Images](https://developers.cloudflare.com/images/), you can add [optimization parameters](https://developers.cloudflare.com/images/optimization/features/) directly to [transformation URL requests](https://developers.cloudflare.com/images/optimization/features/#url-interface) to optimize images from any origin.

[Workers](https://developers.cloudflare.com/workers/) now supports the Images [URL interface](https://developers.cloudflare.com/images/optimization/features/#url-interface) directly on `workers.dev` subdomains through new Worker-scoped configuration. For example, a Worker can serve this transformation URL without connecting a custom domain:
    
    
    https://example-app.<YOUR_SUBDOMAIN>.workers.dev/cdn-cgi/image/format=auto,width=400/image.png

Previously, transformation URLs were not available on `workers.dev` subdomains or during local development. A Worker could serve transformation URLs only through a connected custom domain when the URL interface was enabled for that zone.

The new Worker-scoped settings apply to deployed Workers and during local development. On connected custom domains, they override the zone-scoped settings.

Configure the settings in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) or in [`cloudflare.config.ts`](https://developers.cloudflare.com/cf/projects/cloudflare-config/) for [Cloudflare CLI](https://developers.cloudflare.com/cf/):

The following content appears twice: first for the Cloudflare CLI (`cf`), then for Wrangler. Use `cf` for new projects. In an existing project, use the CLI that the project already uses.

Cloudflare CLI

cloudflare.config.tsts
    
    
    import { defineConfig } from "cf/config";
    
    export default defineConfig({
    worker: {
      name: "image-app",
      // Set this to today's date
      compatibilityDate: "2026-11-26",
      images: {
        urlTransformations: {
          enabled: true,
          allowedOrigins: [
            "images.example.com",
            "image-app.<YOUR_SUBDOMAIN>.workers.dev",
          ],
        },
      },
    },
    });

Wrangler
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "images": {
        "url_transformations": {
          "enabled": true,
          "allowed_origins": [
            "images.example.com",
            "image-app.<YOUR_SUBDOMAIN>.workers.dev"
          ]
        }
      }
    }
    
    
    [images.url_transformations]
    enabled = true
    allowed_origins = [
      "images.example.com",
      "image-app.<YOUR_SUBDOMAIN>.workers.dev",
    ]

Set `enabled` to `true` to turn on transformation URLs.

By default, Workers accepts source images only from the same zone as the transformation URL. To use external source images, specify up to 10 [hostnames](https://developers.cloudflare.com/images/optimization/transformations/sources/#how-it-works) using `allowed_origins` in Wrangler or `allowedOrigins` in `cloudflare.config.ts`.

Deployed settings remain active if you remove the configuration. To disable transformation URLs on a Worker, deploy with `enabled` set to `false`. Named Wrangler environments require their own configuration, and [Version URLs](https://developers.cloudflare.com/workers/versions-and-deployments/version-urls/) support transformation URLs using the Worker's deployed settings.

`wrangler deploy` and `cf deploy` apply the same settings to the Worker, while `wrangler dev` and `cf dev` use them locally.

Transformation URLs do not require an [`IMAGES` binding](https://developers.cloudflare.com/images/optimization/binding/). Transformed results are automatically cached in production.

Refer to [Transform via URL](https://developers.cloudflare.com/images/optimization/transformations/url/) for URL syntax and configuration methods.
