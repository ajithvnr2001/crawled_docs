---
url: https://developers.cloudflare.com/changelog/post/2026-11-02-local-flag-store/
title: Evaluate Flagship flags locally \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-04T08:48:16.505150+00:00
---

# Evaluate Flagship flags locally · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-02-local-flag-store/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 2, 2026

## Evaluate Flagship flags locally

[Flagship](https://developers.cloudflare.com/flagship/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Flagship](https://developers.cloudflare.com/flagship/) bindings now evaluate flags against a local flag store during local development, instead of calling your remote app. You can develop offline and test flag changes without affecting production. This applies to [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev), the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/), the [Vitest integration](https://developers.cloudflare.com/workers/testing/vitest-integration/), and [`cf dev`](https://developers.cloudflare.com/cf/projects/#start-development).

The local store starts empty, so evaluations return the default value you pass in code. Add and manage local flags in any of these ways:

  * **Wrangler** — Add `--local` to `wrangler flagship flags` commands, such as `create`, `update`, and `evaluate`. To copy all flags from your remote app, run `npx wrangler flagship flags pull <APP_ID>`.
  * **Local Explorer** — Create, edit, toggle, and evaluate flags in [Local Explorer](https://developers.cloudflare.com/workers/local-development/local-explorer/) while your dev server runs.
  * **`cf` CLI** — Add `--local` to [`cf flagship` commands](https://developers.cloudflare.com/flagship/configuration/#use-the-cf-cli).



To keep evaluating against your remote app instead, set [`remote: true`](https://developers.cloudflare.com/flagship/configuration/#use-the-remote-app-instead) on the binding.

The local flag store requires Wrangler v4.135.0 or `@cloudflare/vite-plugin` v1.56.0 or later. Flagship in Local Explorer requires Wrangler v4.148.0 or `@cloudflare/vite-plugin` v1.63.0 or later.

Refer to [Flagship local development](https://developers.cloudflare.com/flagship/configuration/#local-development) for details.
