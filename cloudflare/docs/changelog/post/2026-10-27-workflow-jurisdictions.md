---
url: https://developers.cloudflare.com/changelog/post/2026-10-27-workflow-jurisdictions/
title: Restrict Workflows to a jurisdiction \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-28T08:03:52.902837+00:00
---

# Restrict Workflows to a jurisdiction · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-27-workflow-jurisdictions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 27, 2026

## Restrict Workflows to a jurisdiction

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now restrict a Workflow to a [jurisdiction](https://developers.cloudflare.com/workflows/reference/data-location/). Its instances only run and store data within that jurisdiction, which helps you comply with data localization regulations such as [GDPR ↗︎](https://gdpr-info.eu/) or [FedRAMP ↗︎](https://blog.cloudflare.com/cloudflare-achieves-fedramp-authorization/).

Set `jurisdiction` on a `workflows` binding, or on a Workflow declared in [`exports`](https://developers.cloudflare.com/workflows/build/workers-api/#declare-workflows-in-exports):
    
    
    {
    	"workflows": [
    		{
    			"name": "my-workflow",
    			"binding": "MY_WORKFLOW",
    			"class_name": "MyWorkflow",
    			"jurisdiction": "eu",
    		},
    	],
    }
    
    
    [[workflows]]
    name = "my-workflow"
    binding = "MY_WORKFLOW"
    class_name = "MyWorkflow"
    jurisdiction = "eu"

The supported jurisdictions are `eu` (the European Union), `us` (the United States), and `fedramp` (FedRAMP-Moderate data centers).

A Workflow's jurisdiction is set when the Workflow is created, and cannot be changed afterwards. If an existing Workflow has a different jurisdiction, `wrangler deploy` and `wrangler versions upload` stop before uploading your Worker.

Workflow jurisdictions require Wrangler 4.152.0 or above.

For more information, refer to [Data location](https://developers.cloudflare.com/workflows/reference/data-location/).
