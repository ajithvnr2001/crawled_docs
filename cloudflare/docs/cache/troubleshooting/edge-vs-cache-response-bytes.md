---
url: https://developers.cloudflare.com/cache/troubleshooting/edge-vs-cache-response-bytes/
title: edgeResponseBytes and cacheResponseBytes discrepancy \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:01:01.968188+00:00
---

# edgeResponseBytes and cacheResponseBytes discrepancy · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/troubleshooting/edge-vs-cache-response-bytes/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /Troubleshooting
  4. /edgeResponseBytes and cacheResponseBytes discrepancy



# edgeResponseBytes and cacheResponseBytes discrepancy

Last updated Nov 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

In [HTTP request logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/), `cacheResponseBytes` and `edgeResponseBytes` both count the response body as Cloudflare delivered it to the client. They differ only in which response headers they count:

  * `cacheResponseBytes`: the response headers Cloudflare received from cache or origin, plus the response body as delivered to the client.
  * `edgeResponseBytes`: the response headers sent to the client, after any header modifications, plus the response body as delivered to the client.



Neither field records the body size as received from the origin. If the origin sends a pre-compressed body (for example, `Content-Encoding: gzip` or `br`) and the client accepts that encoding, both fields count the compressed body. If Cloudflare decompresses the body, for example because the client does not accept the encoding or a feature needs to modify the HTML, both fields count the body as delivered: uncompressed, or re-compressed.

Because both fields count the same body, any difference between `edgeResponseBytes` and `cacheResponseBytes` comes from response headers. The header size counted in `cacheResponseBytes` can be larger than the headers your origin sent.

[PreviousBot Management cookie causes cache bypass in O2O setups](https://developers.cloudflare.com/cache/troubleshooting/bot-management-o2o-cache-bypass/)[NextAlways Online](https://developers.cloudflare.com/cache/troubleshooting/always-online/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/troubleshooting/edge-vs-cache-response-bytes.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
