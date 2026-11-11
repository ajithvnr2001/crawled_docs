---
url: https://developers.cloudflare.com/changelog/post/2026-11-10-per-workflow-concurrency-limits/
title: Set a concurrency limit for each Workflow \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:00:58.562352+00:00
---

# Set a concurrency limit for each Workflow · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-10-per-workflow-concurrency-limits/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 10, 2026

## Set a concurrency limit for each Workflow

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now set a [concurrency limit](https://developers.cloudflare.com/workflows/build/concurrency-limits/#per-workflow-concurrency-limits) on an individual Workflow to cap how many of its instances run at the same time. Use it to protect a database or third-party API that slows down or rejects requests past a certain number of concurrent connections, or to distribute load more evenly across your Workflows so that one high-volume Workflow does not use all of your account's concurrency.

For example, to allow only 10 instances of a Workflow to run at a time, set `concurrency.limit` on its `workflows` binding and redeploy:
    
    
    {
    	"workflows": [
    		{
    			"name": "my-workflow",
    			"binding": "MY_WORKFLOW",
    			"class_name": "MyWorkflow",
    			"concurrency": {
    				"limit": 10,
    			},
    		},
    	],
    }
    
    
    [[workflows]]
    name = "my-workflow"
    binding = "MY_WORKFLOW"
    class_name = "MyWorkflow"
    
      [workflows.concurrency]
      limit = 10

You can also set `concurrency` on a Workflow declared in [`exports`](https://developers.cloudflare.com/workflows/build/workers-api/#declare-workflows-in-exports), or with `exports.workflow()` in [`@cloudflare/config`](https://developers.cloudflare.com/cf/projects/cloudflare-config/).

Instances above the limit are not rejected. They are queued and start automatically as running instances finish or move to the `waiting` state.

The limit must be a positive integer, and cannot be higher than your account's [concurrency limit](https://developers.cloudflare.com/workflows/reference/limits/) (100 on Workers Free, 50,000 on Workers Paid). Lowering the limit does not stop instances that are already running. Workflows without a concurrency limit can still use up to your account's full concurrency limit.

Caution

Set `concurrency.limit` in your configuration on every deploy. If you deploy without it, the Workflow's concurrency limit is removed.

Per-Workflow concurrency limits require Wrangler 4.127.0 or above.

For more information, refer to [Concurrency limits](https://developers.cloudflare.com/workflows/build/concurrency-limits/#per-workflow-concurrency-limits).
