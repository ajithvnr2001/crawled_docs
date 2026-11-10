---
url: https://developers.cloudflare.com/changelog/post/2026-11-09-nanocode-on-workers/
title: Run the Nanocode agent harness in Cloudflare Durable Objects \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-10T09:28:45.667194+00:00
---

# Run the Nanocode agent harness in Cloudflare Durable Objects · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-09-nanocode-on-workers/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 9, 2026

## Run the Nanocode agent harness in Cloudflare Durable Objects

[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now run [Nanocode ↗︎](https://github.com/gakonst/nanocode) coding agents in [Cloudflare Durable Objects](https://developers.cloudflare.com/durable-objects/), with persistent session history and recovery after interruptions.

Nanocode's Rust engine runs as WebAssembly and implements Codex and Claude Code prompt and tool conventions. Its Cloudflare host saves turn progress and tool results in SQLite and uses alarms to resume pending work. The Nanocode project maintains the host independently of Cloudflare; it does not require the Agents SDK.

Start with the [reference Worker ↗︎](https://github.com/gakonst/nanocode-cloudflare-durable) and follow [Nanocode on Workers](https://developers.cloudflare.com/agents/harnesses/nanocode/) for setup, models, and recovery limits.
