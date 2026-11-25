---
url: https://developers.cloudflare.com/changelog/post/2026-11-24-range-requests-content-encoding/
title: Range requests respect client Accept-Encoding \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-25T10:59:48.356486+00:00
---

# Range requests respect client Accept-Encoding · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-24-range-requests-content-encoding/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 24, 2026

## Range requests respect client Accept-Encoding

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare updated how range requests handle content encoding for both cached files and uncached `GET` requests over HTTPS.

#### Cached encoded files

A byte range of a cached file encoded with gzip or Brotli (`br`) counts bytes of the encoded file, not of the decompressed content ([RFC 9110, section 14.1.2 ↗︎](https://www.rfc-editor.org/rfc/rfc9110.html#section-14.1.2)). Cloudflare now serves that range only if the client's `Accept-Encoding` header explicitly lists the encoding without `q=0` (and over HTTPS for Brotli). Otherwise, Cloudflare ignores `Range` ([RFC 9110, section 14.2 ↗︎](https://www.rfc-editor.org/rfc/rfc9110.html#section-14.2)) and sends the complete file as `200 OK` using normal content negotiation. Cloudflare always sends the complete `200 OK` file for a cached file encoded with Zstandard (`zstd`) or `deflate`.

Previously, a client that did not accept the encoding could receive a `206 Partial Content` response whose bytes did not match its `Content-Range` header.

#### Uncached range requests

If caching is bypassed or the request is not eligible for caching, Cloudflare forwards the client's `Range` header to your origin. For `GET` requests over HTTPS, Cloudflare now also forwards the client's own `Accept-Encoding` header instead of Cloudflare's default `gzip, br` header. Previously, Cloudflare passed your origin's byte-range `206 Partial Content` response to the client without decoding it, so a client could receive a range in an encoding it did not accept.

If a client sends no `Accept-Encoding` header (on Orange-to-Orange requests), or sends only stripped dictionary encodings (`dcb` or `dcz`), your origin can receive an empty `Accept-Encoding` header. Under [RFC 9110, section 12.5.3 ↗︎](https://www.rfc-editor.org/rfc/rfc9110.html#section-12.5.3), an empty `Accept-Encoding` header means the client accepts no encoding, so your origin should answer it with an unencoded response rather than `406 Not Acceptable`.

Range requests that Cloudflare serves from cache, or fetches with Origin Range Requests, still send Cloudflare's own `Accept-Encoding` header to your origin.

For more information, refer to [Range request behavior](https://developers.cloudflare.com/cache/reference/range-requests/).
