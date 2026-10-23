---
url: https://developers.cloudflare.com/changelog/post/2026-08-19-spec-compliant-dispatch-exceptions/
title: Spec-compliant dispatchEvent() exception handling \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:47.976236+00:00
---

# Spec-compliant dispatchEvent() exception handling · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-19-spec-compliant-dispatch-exceptions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 19, 2026

## Spec-compliant dispatchEvent() exception handling

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-19-spec-compliant-dispatch-exceptions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new compatibility flag, `spec_compliant_dispatch_exceptions`, aligns the Workers runtime's event dispatch behavior with the [DOM specification ↗︎](https://dom.spec.whatwg.org/#dispatching-events). This flag becomes the default for all Workers with a compatibility date of `2026-09-15` or later.

Previously, when an event listener threw an exception during `dispatchEvent()`, the runtime propagated the exception immediately and skipped all remaining listeners for that event. The spec instead requires that listener exceptions are reported (via the global `error` event and the console) without interrupting the dispatch — remaining listeners still run.

This change affects the JS-visible `dispatchEvent()`, `AbortSignal` abort dispatch, and runtime-fired events on `WebSocket`, `EventSource`, and `MessagePort`. Top-level event delivery for legacy Service Worker syntax entry points (such as `addEventListener("fetch", ...)`) is not affected.

To opt in before the default date, add `spec_compliant_dispatch_exceptions` to your `compatibility_flags`. To preserve the old behavior after the default date, use `no_spec_compliant_dispatch_exceptions`.

For more details, refer to the [compatibility flags documentation](https://developers.cloudflare.com/workers/configuration/compatibility-flags/).
