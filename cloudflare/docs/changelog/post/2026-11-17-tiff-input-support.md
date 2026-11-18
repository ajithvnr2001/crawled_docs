---
url: https://developers.cloudflare.com/changelog/post/2026-11-17-tiff-input-support/
title: Optimize original TIFF files with Images \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:17.031130+00:00
---

# Optimize original TIFF files with Images · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-17-tiff-input-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 17, 2026

## Optimize original TIFF files with Images

[Cloudflare Images](https://developers.cloudflare.com/images/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Images](https://developers.cloudflare.com/images/) lets you optimize images for web delivery while storing only the original, high-resolution version. With Images, you can dynamically serve compressed and resized versions in the [most efficient format](https://developers.cloudflare.com/images/optimization/features/#format) for the requesting browser.

Starting today, Images accepts TIFF as an [input format](https://developers.cloudflare.com/images/get-started/limits/#input-formats).

In publishing and e-commerce, TIFF is widely deployed as a master format for product photography, high-resolution scans, print assets, and archival collections. TIFF is a mature format, but it has limited support in modern browsers and tends to produce larger files than formats optimized for web delivery.

You can dynamically transcode original TIFF files to formats such as WebP or AVIF. These formats offer more efficient compression, which can reduce file sizes and improve page load performance. You can also resize each output without converting or modifying your original image.

For multi-page TIFF files, Images decodes only the first page. For supported formats and limits, refer to [Limits and formats](https://developers.cloudflare.com/images/get-started/limits/).
