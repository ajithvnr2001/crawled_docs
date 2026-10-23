---
url: https://developers.cloudflare.com/changelog/post/2026-10-20-source-maps-on-by-default/
title: Wrangler and cf now upload source maps by default \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:51:29.350768+00:00
---

# Wrangler and cf now upload source maps by default · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-20-source-maps-on-by-default/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 20, 2026

## Wrangler and cf now upload source maps by default

[Workers](https://developers.cloudflare.com/workers/)[Cloudflare CLI](https://developers.cloudflare.com/cf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

From Wrangler 4.150.0, [`wrangler deploy`](https://developers.cloudflare.com/workers/wrangler/commands/general/#deploy), [`wrangler versions upload`](https://developers.cloudflare.com/workers/wrangler/commands/general/#versions-upload), and [`wrangler preview`](https://developers.cloudflare.com/workers/wrangler/commands/workers/#preview) generate and upload [source maps](https://developers.cloudflare.com/workers/observability/source-maps/) by default. You no longer need to set `upload_source_maps` to get stack traces with your original file names and line numbers.

[`cf deploy`](https://developers.cloudflare.com/cf/) also uploads source maps by default. With the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/) 1.64.0 or later, Worker builds generate source maps by default, and `cf deploy` uploads every source map in the build output.

![Stack Trace with Source Map remapping](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1850,height=238,format=webp/_astro/with-source-map.PipytmVe.png)

Remapped stack traces show up in [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/), [real-time logs](https://developers.cloudflare.com/workers/observability/logs/real-time-logs/), [Tail Workers](https://developers.cloudflare.com/workers/observability/logs/tail-workers/), and [Workers Issues](https://developers.cloudflare.com/workers/observability/issues/). Source maps are applied after your Worker runs, so they don't affect CPU time, bundle size, or cold starts.

If your Worker uses a custom build, Wrangler uploads any external source maps it finds. Maps it can't resolve, such as inline `data:` source maps, are skipped instead of failing the upload. Set `upload_source_maps` to `true` if you'd prefer the upload to fail.

To opt out with Wrangler, set `upload_source_maps` to `false`:
    
    
    {
    	"upload_source_maps": false
    }
    
    
    upload_source_maps = false

To opt out with `cf` or the Cloudflare Vite plugin, set `build.sourcemap` to `false` for your Worker's Vite environment. Refer to [Disable source maps](https://developers.cloudflare.com/workers/observability/source-maps/#disable-source-maps).
