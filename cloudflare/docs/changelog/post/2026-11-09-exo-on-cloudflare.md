---
url: https://developers.cloudflare.com/changelog/post/2026-11-09-exo-on-cloudflare/
title: Run Exo agents on Cloudflare \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-10T09:28:45.534930+00:00
---

# Run Exo agents on Cloudflare · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-09-exo-on-cloudflare/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 9, 2026

## Run Exo agents on Cloudflare

[Workers](https://developers.cloudflare.com/workers/)[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now run [Exo](https://developers.cloudflare.com/agents/harnesses/exo/) agents on Cloudflare, with Durable Objects coordinating conversations and Cloudflare Sandboxes running Linux tools. Define an agent in Markdown, then use Exo's CLI or HTTP API to run it.

After [deploying the Cloudflare adapter and configuring your Exo provider ↗︎](https://github.com/exoharness/exo/tree/main/exoharness/cloudflare#authentication-and-cli), add an `openai` vault credential and save this definition as `agent.md`:
    
    
    ---
    harness: basic
    model:
      name: gpt-6.1-sol
      credential: openai
    ---
    
    Help the user with their task.

Run the agent against your Cloudflare deployment with Exo's CLI:
    
    
    exo --provider cloudflare agent run --agent-file agent.md

The Exo project maintains the Cloudflare adapter independently of Cloudflare. It does not require the Agents SDK.

Follow the [Exo guide](https://developers.cloudflare.com/agents/harnesses/exo/) for architecture, recovery behavior, and upstream setup instructions.
