---
url: https://developers.cloudflare.com/workflows/reference/data-location/
title: Data location \u00b7 Cloudflare Workflows docs
method: scrapling+scrapegraph
fetched_at: 2026-10-28T08:03:53.701048+00:00
---

# Data location · Cloudflare Workflows docs

> Source: https://developers.cloudflare.com/workflows/reference/data-location/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workflows](https://developers.cloudflare.com/workflows/)
  3. /Platform
  4. /Data location



# Data location

Last updated Oct 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRestrict Workflows to a jurisdiction Supported locations

## Restrict Workflows to a jurisdiction

Jurisdictions are used to create Workflows whose instances only run and store data within a region to comply with data localization regulations such as [GDPR ↗︎](https://gdpr-info.eu/) or [FedRAMP ↗︎](https://blog.cloudflare.com/cloudflare-achieves-fedramp-authorization/).

Workers can still create and manage instances of a Workflow restricted to a jurisdiction from anywhere in the world. The jurisdiction constraint only controls where the Workflow instances themselves run and persist data. Consider using [Regional Services](https://developers.cloudflare.com/data-localization/regional-services/) to control the regions from which Cloudflare responds to requests.

Settings

A Workflow's settings are stored outside of the specified jurisdiction.

To restrict a Workflow to a jurisdiction, set `jurisdiction` on its `workflows` binding in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/#workflows):
    
    
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

You can also set `jurisdiction` on a Workflow declared in [`exports`](https://developers.cloudflare.com/workflows/build/workers-api/#declare-workflows-in-exports). When you run `wrangler deploy`, Wrangler creates the Workflow in that jurisdiction. Setting a jurisdiction requires Wrangler 4.152.0 or above.

  * A Workflow's jurisdiction is set when the Workflow is created, and cannot be changed afterwards. If an existing Workflow has a different jurisdiction, `wrangler deploy` and `wrangler versions upload` stop before uploading your Worker.
  * To use a different jurisdiction, give the Workflow a new name, or delete the existing Workflow first. Deleting a Workflow also deletes its instances.
  * If you remove `jurisdiction` from your configuration, the Workflow keeps its existing jurisdiction.
  * `jurisdiction` cannot be combined with `script_name`. To bind to a Workflow defined in another Worker, set `jurisdiction` on the Worker that defines the Workflow.
  * [Local development](https://developers.cloudflare.com/workflows/build/local-development/) ignores `jurisdiction`.
  * [`wrangler workflows describe`](https://developers.cloudflare.com/workers/wrangler/commands/workflows/#workflows-describe) shows the jurisdiction of a Workflow.



### Supported locations

The following jurisdictions are supported:

Parameter | Location  
---|---  
eu | The European Union  
us | The United States  
fedramp | FedRAMP-Moderate data centers  
  
[PreviousLimits](https://developers.cloudflare.com/workflows/reference/limits/)[NextEvent subscriptions](https://developers.cloudflare.com/workflows/reference/event-subscriptions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workflows/reference/data-location.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
