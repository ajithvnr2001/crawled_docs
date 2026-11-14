---
url: https://developers.cloudflare.com/changelog/post/2026-11-13-quick-actions-local-dev/
title: Browser Run Quick Actions now work in local development \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-14T08:45:52.196517+00:00
---

# Browser Run Quick Actions now work in local development · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-13-quick-actions-local-dev/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 13, 2026

## Browser Run Quick Actions now work in local development

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now test [Browser Run Quick Actions](https://developers.cloudflare.com/browser-run/quick-actions/) locally. Under `npx wrangler dev`, the browser binding's `.quickAction()` method runs against a Chrome instance on your machine. Before, `.quickAction()` worked only in remote mode, and local calls failed with `The RPC receiver does not implement the method "quickAction"`.

Note

There are currently two limitations in the local simulation:

  * The `json` action is emulated. It requires an AI model to extract data, and the model is not available locally, so the action returns placeholder data that matches your schema.
  * The [Kitesurf](https://developers.cloudflare.com/browser-run/kitesurf/) browser is not supported yet.



For details, refer to [Test Quick Actions locally](https://developers.cloudflare.com/browser-run/quick-actions/#test-quick-actions-locally).
