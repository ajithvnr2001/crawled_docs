---
url: https://developers.cloudflare.com/workers/vite-plugin/vite-plus/
title: Vite+ on Workers \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-11-07T08:31:56.994762+00:00
---

# Vite+ on Workers · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/vite-plugin/vite-plus/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/)
  4. /Vite+ on Workers



# Vite+ on Workers

Last updated Nov 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewStart a new projectAdopt Vite+ in an existing project

[Vite+ ↗︎](https://viteplus.dev/) combines Vite with formatting, linting, type checking, and testing. Use Vite+ with the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/) for new Workers and supported Vite-based apps.

The plugin runs your Worker code in the Workers runtime during development. Vite+ provides the project toolchain through the `vp` command.

## Start a new project

To create a standalone Worker with `cf init`, follow [Deploy your first Worker](https://developers.cloudflare.com/cf/get-started/first-worker/). Use the generated Vite+ scripts for checks, formatting, and tests alongside `cf dev`, `cf build`, and `cf deploy`.

For a framework application, start with the appropriate [framework guide](https://developers.cloudflare.com/workers/framework-guides/). Preserve framework-specific build steps when adopting Vite+.

## Adopt Vite+ in an existing project

Follow the [Vite+ migration guide ↗︎](https://viteplus.dev/guide/migrate) for requirements and migration steps. If your project does not yet use the Cloudflare Vite plugin, follow the [plugin setup guide](https://developers.cloudflare.com/workers/vite-plugin/get-started/).

Keep your framework scripts and Cloudflare deployment command. Adopting Vite+ does not require changing your Cloudflare configuration format. Preserve existing toolchains during unrelated changes.

[Previousv2 beta](https://developers.cloudflare.com/workers/vite-plugin/v2-beta/)[NextAPI](https://developers.cloudflare.com/workers/vite-plugin/reference/api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/vite-plugin/vite-plus.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
