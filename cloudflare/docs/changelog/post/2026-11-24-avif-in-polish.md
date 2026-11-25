---
url: https://developers.cloudflare.com/changelog/post/2026-11-24-avif-in-polish/
title: Automatic AVIF conversion with Polish \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-25T10:59:48.275835+00:00
---

# Automatic AVIF conversion with Polish · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-24-avif-in-polish/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 24, 2026

## Automatic AVIF conversion with Polish

[Cloudflare Images](https://developers.cloudflare.com/images/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Polish](https://developers.cloudflare.com/images/polish/) can now create AVIF versions of JPEG and PNG images served from your origin, alongside its existing WebP conversion. AVIF often produces smaller files than WebP, reducing transfer sizes and improving load times for image-heavy sites such as product catalogs, photo galleries, and news publications.

Polish automatically optimizes images on your zone that are served from your origin server. It strips metadata, applies compression, and can convert JPEG and PNG files to more efficient image formats.

[Configure Polish](https://developers.cloudflare.com/images/polish/configure-polish/) with AVIF through the [Cloudflare CLI](https://developers.cloudflare.com/images/polish/configure-polish/#cloudflare-cli), [dashboard](https://developers.cloudflare.com/images/polish/configure-polish/#dashboard), or [REST API](https://developers.cloudflare.com/images/polish/configure-polish/#rest-api):
    
    
    cf zones settings edit polish --zone example.com --body '{"value":"lossy"}'
    cf zones settings edit avif --zone example.com --body '{"value":"on"}'
    cf zones settings edit webp --zone example.com --body '{"value":"on"}'

AVIF and WebP can be enabled at the same time. When both formats are enabled, Polish selects an output based on browser support, file size, and image quality:

  * The browser must advertise AVIF support in its `Accept` header.
  * Polish serves AVIF only if the converted image is smaller than the original.
  * If the browser supports both AVIF and WebP, then Polish prefers AVIF.
  * Browsers without AVIF support continue to receive WebP or the optimized original format.



Refer to [Configure Polish](https://developers.cloudflare.com/images/polish/configure-polish/#avif-and-webp) and [AVIF may be skipped](https://developers.cloudflare.com/images/polish/no-avif/) for format selection and fallback behavior.
