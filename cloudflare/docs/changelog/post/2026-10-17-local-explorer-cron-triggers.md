---
url: https://developers.cloudflare.com/changelog/post/2026-10-17-local-explorer-cron-triggers/
title: Test Cron Triggers with Local Explorer \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:09:47.516407+00:00
---

# Test Cron Triggers with Local Explorer · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-17-local-explorer-cron-triggers/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 17, 2026

## Test Cron Triggers with Local Explorer

[Workers](https://developers.cloudflare.com/workers/)[Cloudflare CLI](https://developers.cloudflare.com/cf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Local Explorer can now send one-off Cron Trigger invocations to a Worker's `scheduled()` handler during local development. This removes the need to construct request URLs when testing handler behavior.

Start your local development server with [`cf dev`](https://developers.cloudflare.com/cf/projects/#start-development), [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev), or the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/). Open `/cdn-cgi/local/explorer` on the server URL and select **Cron Triggers**.

The browser interface supports the following tasks:

  * Invoke configured cron expressions
  * Build ad hoc expressions
  * Set reusable scheduled times
  * Inspect outcomes and `noRetry()` status



Ad hoc triggers and scheduled time presets stay in your browser. They do not change `cloudflare.config.ts`, your Wrangler configuration, or deployed Cron Triggers. Local development does not run cron schedules automatically.

Full logs and traces are available in the development session that owns the Worker when that session has **Observability** turned on.

The following example uses port `8787`. Replace it with your development server port, such as `5173` for Vite.

The Local Explorer API exposes the same operation for tools and AI agents. The request targets an exact Worker name and accepts a cron expression and optional scheduled time:
    
    
    curl -X POST \
      "http://localhost:8787/cdn-cgi/local/explorer/api/local/scheduled?worker=my-worker" \
      -H "Content-Type: application/json" \
      --data '{"cron":"0 * * * *","scheduled_time":1745856238000}'

For more details, refer to [Test Cron Triggers with Local Explorer](https://developers.cloudflare.com/workers/local-development/local-explorer/#test-cron-triggers).
