---
url: https://developers.cloudflare.com/changelog/post/2026-10-22-pi-harness-pi-1-4/
title: Agents SDK now supports the latest Pi 1.4 release \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:48.814927+00:00
---

# Agents SDK now supports the latest Pi 1.4 release · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-22-pi-harness-pi-1-4/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 22, 2026

## Agents SDK now supports the latest Pi 1.4 release

[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-22-pi-harness-pi-1-4/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Agents SDK v0.30.0 runs [`PiHarness`](https://developers.cloudflare.com/agents/harnesses/pi/) on [Pi 1.4 ↗︎](https://github.com/earendil-works/pi/blob/v1.4.0/packages/durable/CHANGELOG.md#140---2026-10-21), and makes it recover more reliably from evictions, crashes, and storage errors.

  * **Hibernation while Pi's tasks sleep.** `PiHarness` passes Pi's new `onWake` callback to your harness factory. While a task sleeps, such as during a model retry backoff, the Durable Object can hibernate until the task is due instead of staying in memory.
  * **Parked tasks.** Pi 1.4 parks a task that keeps crashing the object instead of restarting it forever. Parked operations show as `parked` in `pending()`, and `session.retry()` runs them again.
  * **Recovery from storage errors.** `PiHarness` reopens Pi after a storage error instead of failing every call until the object restarts. Its wake-up job retries failed steps with a backoff instead of being dropped.
  * **Retried model streams.** `agents/models/pi-ai` reports a cut-off or idle model stream as a transient error, so Pi retries the turn instead of failing it.



#### Upgrade

The [Agents SDK v0.30.0 changelog ↗︎](https://github.com/cloudflare/agents/blob/main/packages/agents/CHANGELOG.md#0300) has step-by-step upgrade instructions. Point your coding agent at them and upgrade today:

![](https://developers.cloudflare.com/icons/agents/claude/light.svg)![](https://developers.cloudflare.com/icons/agents/claude/dark.svg)![](https://developers.cloudflare.com/icons/agents/codex/light.svg)![](https://developers.cloudflare.com/icons/agents/codex/dark.svg)![](https://developers.cloudflare.com/icons/agents/cursor/light.svg)![](https://developers.cloudflare.com/icons/agents/cursor/dark.svg)![](https://developers.cloudflare.com/icons/agents/opencode/light.svg)![](https://developers.cloudflare.com/icons/agents/opencode/dark.svg)Copy promptPrompt copied!

Pi 1.4 migrates the session storage in the object's SQLite database to a schema that Pi 1.3 cannot open, so a deployment cannot roll back past this upgrade. Refer to the [Pi Durable 1.4.0 changelog ↗︎](https://github.com/earendil-works/pi/blob/v1.4.0/packages/durable/CHANGELOG.md#140---2026-10-21) for Pi's own breaking changes.
