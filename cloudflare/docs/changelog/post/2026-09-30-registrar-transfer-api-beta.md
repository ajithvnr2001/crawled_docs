---
url: https://developers.cloudflare.com/changelog/post/2026-09-30-registrar-transfer-api-beta/
title: Cloudflare Registrar API beta now supports domain transfers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-27T07:31:30.297636+00:00
---

# Cloudflare Registrar API beta now supports domain transfers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-30-registrar-transfer-api-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 30, 2026

## Cloudflare Registrar API beta now supports domain transfers

[Registrar](https://developers.cloudflare.com/registrar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Registrar API beta now supports domain transfers.

You can now use the Cloudflare API to:

  * Initiate a supported domain transfer into Cloudflare Registrar.
  * Poll transfer status through a dedicated status endpoint.



Before starting a transfer, the domain must already have a zone in your Cloudflare account, DNSSEC must be disabled, and most extensions require an authorization or EPP code from the current registrar.

Transfers are asynchronous and typically take 1 to 10 days to complete, so clients should poll the transfer status endpoint to track workflow progress.

For transfer initiation and status details, refer to:

  * [Initiate Transfer API reference ↗︎](https://developers.cloudflare.com/api/resources/registrar/subresources/transfer_in/methods/create/)
  * [Get Transfer Status API reference ↗︎](https://developers.cloudflare.com/api/resources/registrar/subresources/transfer_in_status/methods/get/)


