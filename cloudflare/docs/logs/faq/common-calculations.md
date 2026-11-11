---
url: https://developers.cloudflare.com/logs/faq/common-calculations/
title: Common calculations FAQ \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:01:01.494652+00:00
---

# Common calculations FAQ · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/faq/common-calculations/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /[FAQ](https://developers.cloudflare.com/logs/faq/)
  4. /Common calculations FAQ



# Common calculations FAQ

Last updated Nov 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview How can I calculate bytes served by the origin from Cloudflare Logs? How do I calculate bandwidth usage for my zone?

[❮ Back to FAQ](https://developers.cloudflare.com/logs/faq/)

### How can I calculate bytes served by the origin from Cloudflare Logs?

To approximate bytes served by the origin, use the `CacheResponseBytes` field in Cloudflare Logs, and filter only requests that come from the origin. Make sure to filter out `OriginResponseStatus` values `0` and `304`, which indicate a revalidated response.

`CacheResponseBytes` counts the response body as Cloudflare delivered it to the client, not as the origin sent it. The two can differ when Cloudflare changes the body encoding. For example, if the origin sends a gzip-compressed body and the client does not accept gzip, Cloudflare decompresses the body and `CacheResponseBytes` counts the uncompressed size. Refer to [edgeResponseBytes and cacheResponseBytes discrepancy](https://developers.cloudflare.com/cache/troubleshooting/edge-vs-cache-response-bytes/).

### How do I calculate bandwidth usage for my zone?

Bandwidth (or data transfer) can be calculated by adding the `EdgeResponseBytes` field in HTTP request logs. There are some types of requests that are not factored into bandwidth calculations. In order to only include relevant requests in calculations, add the filter `ClientRequestSource = 'eyeball'`.

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/faq/common-calculations.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
