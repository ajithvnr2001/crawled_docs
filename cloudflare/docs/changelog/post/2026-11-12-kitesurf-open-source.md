---
url: https://developers.cloudflare.com/changelog/post/2026-11-12-kitesurf-open-source/
title: Kitesurf is now open source \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:05.033020+00:00
---

# Kitesurf is now open source · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-12-kitesurf-open-source/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 12, 2026

## Kitesurf is now open source

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Kitesurf ↗︎](https://kitesurf.dev/), Cloudflare's browser engine for AI agents, is now [open source on GitHub ↗︎](https://github.com/cloudflare/kitesurf) under the Apache 2.0 license. You can inspect the source, run it locally, and deploy your own instance to your Cloudflare account.

Kitesurf runs entirely on Cloudflare Workers. It parses HTML, applies CSS, executes page JavaScript, and renders screenshots without a browser container. It supports the Chrome DevTools Protocol (CDP), so you can connect clients such as Puppeteer.

Kitesurf is still **experimental and under heavy development**. The team continues to improve web standards support, rendering fidelity, and performance.

#### Run locally or deploy to your account

Developers can run Kitesurf locally with Wrangler. After following the [build requirements and setup instructions ↗︎](https://github.com/cloudflare/kitesurf#build-and-run-locally), run `pnpm run dev`. This builds the engine and starts `wrangler dev`.

To run your own instance on Cloudflare, follow the [deployment instructions ↗︎](https://github.com/cloudflare/kitesurf#cloudflare-deployment). Protect your deployment with Cloudflare Access or another authentication layer. Kitesurf does not provide built-in authentication.

Important

Kitesurf requires [Cloudflare Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/) to create isolated Workers for pages. Dynamic Workers are part of the [Workers Paid plan](https://developers.cloudflare.com/dynamic-workers/pricing/). A Workers Paid plan is required to run Kitesurf on Cloudflare. Local development uses `wrangler dev`.

#### Contribute and follow progress

Contributions and pull requests are welcome. The team remains focused on compatibility, reliability, and performance, with limited review capacity. Keep changes focused and follow the [contribution guidelines ↗︎](https://github.com/cloudflare/kitesurf/blob/main/CONTRIBUTING.md), including opening an issue and getting vouched by a maintainer before submitting a pull request.

Visit [kitesurf.dev ↗︎](https://kitesurf.dev/), the main Kitesurf website and playground. Track [Web Platform Tests (WPT) progress ↗︎](https://kitesurf.dev/wpt) and [performance benchmarks ↗︎](https://kitesurf.dev/benchmarks) as development continues.

For background and technical details, refer to the [introductory blog post ↗︎](https://blog.cloudflare.com/kitesurf/) and the [Kitesurf update ↗︎](https://blog.cloudflare.com/kitesurf-update/). To use Kitesurf through Browser Run, refer to the [Kitesurf documentation](https://developers.cloudflare.com/browser-run/kitesurf/).
