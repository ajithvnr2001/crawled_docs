---
url: https://developers.cloudflare.com/pages/configuration/api/
title: REST API \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:32.350364+00:00
---

# REST API · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/configuration/api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /Configuration
  4. /REST API



# REST API

Last updated Nov 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow to use the API Get an API token Make requestsExamples Trigger a new build every hour Delete old deployments after a week Share project informationRelated resources

The [Pages API](https://developers.cloudflare.com/api/resources/pages/subresources/projects/methods/list/) allows you to build automations and integrate Pages with your development workflow. At a high level, the API endpoints let you manage deployments and builds and configure projects. Cloudflare supports [Deploy Hooks](https://developers.cloudflare.com/pages/configuration/deploy-hooks/) for headless CMS deployments. Refer to the [API documentation](https://developers.cloudflare.com/api/) for a full breakdown of object types and endpoints.

For programmatic build and deployment automation on Cloudflare Workers, refer to the [Workers Builds API](https://developers.cloudflare.com/workers/ci-cd/builds/api-reference/).

## How to use the API

### Get an API token

To create an API token:

  1. In the Cloudflare dashboard, go to the **Account API tokens** page.

[ Go to **Account API tokens** ↗ ](https://dash.cloudflare.com/?to=/:account/api-tokens)
  2. Select **Create Token**.

  3. Select **Create Custom Token** > **Get started** , and add the **Cloudflare Pages** permission with **Edit** access (or **Read** access for read-only requests).




### Make requests

After creating your token, you can authenticate and make requests to the API using your API token in the request headers. For example, here is an API request to get all deployments in a project.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Pages Read`
  * `Pages Write`

List Pages deploymentsbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/pages/projects/$PROJECT_NAME/deployments" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Try it with one of your projects by replacing `{account_id}`, `{project_name}`, and `<API_TOKEN>`. Refer to [Find your account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) for more information.

## Examples

The API is even more powerful when combined with Cloudflare Workers: the easiest way to deploy serverless functions on Cloudflare's global network. The following section includes three code examples on how to use the Pages API. To build and deploy these samples, refer to the [Get started guide](https://developers.cloudflare.com/workers/get-started/guide/).

### Trigger a new build every hour

Suppose you have a CMS that pulls data from live sources to compile a static output. You can keep the static content current by triggering new builds periodically using the API.
    
    
    const endpoint =
    	"https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/{project_name}/deployments";
    
    export default {
    	async scheduled(_, env) {
    		const init = {
    			method: "POST",
    			headers: {
    				"Content-Type": "application/json;charset=UTF-8",
    				// Store the API token as a secret using the Workers dashboard or Wrangler:
    				// /workers/wrangler/commands/workers/#secret
    				Authorization: `Bearer ${env.API_TOKEN}`,
    			},
    		};
    
    		await fetch(endpoint, init);
    	},
    };

After you have deployed the JavaScript Worker, set a cron trigger in your Worker to run this script periodically. Refer to [Cron Triggers](https://developers.cloudflare.com/workers/configuration/cron-triggers/) for more details.

### Delete old deployments after a week

Cloudflare Pages hosts and serves project deployments on preview links. Pages automatically deletes deployments older than 30 days (except your 100 most recent deployments and current production deployment; refer to [Deployment limits](https://developers.cloudflare.com/pages/platform/limits/#deployments)). If you want to delete older preview deployments sooner — for example, after seven days — you can use the API. The latest deployment for a branch cannot be deleted.

Note

To delete individual deployments from the command line, you can use [`wrangler pages deployment delete`](https://developers.cloudflare.com/workers/wrangler/commands/pages/#pages-deployment-delete).
    
    
    const endpoint =
    	"https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/{project_name}/deployments";
    const expirationDays = 7;
    
    export default {
    	async scheduled(_, env) {
    		const init = {
    			headers: {
    				"Content-Type": "application/json;charset=UTF-8",
    				// Store the API token as a secret using the Workers dashboard or Wrangler:
    				// /workers/wrangler/commands/workers/#secret
    				Authorization: `Bearer ${env.API_TOKEN}`,
    			},
    		};
    
    		const response = await fetch(endpoint, init);
    		const deployments = await response.json();
    
    		for (const deployment of deployments.result) {
    			// Skip production deployments so the live deployment is never deleted
    			if (deployment.environment === "production") {
    				continue;
    			}
    
    			// Check if the preview deployment is older than `expirationDays`
    			if (
    				(Date.now() - new Date(deployment.created_on)) / 86400000 >
    				expirationDays
    			) {
    				// Delete the preview deployment (`force=true` also deletes aliased preview deployments)
    				await fetch(`${endpoint}/${deployment.id}?force=true`, {
    					method: "DELETE",
    					headers: {
    						"Content-Type": "application/json;charset=UTF-8",
    						Authorization: `Bearer ${env.API_TOKEN}`,
    					},
    				});
    			}
    		}
    	},
    };

After you have deployed the JavaScript Worker, you can set a cron trigger in your Worker to run this script periodically. Refer to the [Cron Triggers guide](https://developers.cloudflare.com/workers/configuration/cron-triggers/) for more details.

### Share project information

Imagine you are working on a development team using Pages to build your websites. You might want an easy way to share deployment preview links and build status without having to share Cloudflare accounts. Using the API, you can share project information, including deployment status and preview links, and serve this content as HTML from a Cloudflare Worker.
    
    
    const deploymentsEndpoint =
    	"https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/{project_name}/deployments";
    const projectEndpoint =
    	"https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/{project_name}";
    
    export default {
    	async fetch(request, env) {
    		const init = {
    			headers: {
    				"content-type": "application/json;charset=UTF-8",
    				// Store the API token as a secret using the Workers dashboard or Wrangler:
    				// /workers/wrangler/commands/workers/#secret
    				Authorization: `Bearer ${env.API_TOKEN}`,
    			},
    		};
    
    		const style = `body { padding: 6em; font-family: sans-serif; } h2 { color: #f6821f }`;
    		let content = "<h2>Project</h2>";
    
    		let response = await fetch(projectEndpoint, init);
    		const projectResponse = await response.json();
    		content += `<p>Project Name: ${projectResponse.result.name}</p>`;
    		content += `<p>Project ID: ${projectResponse.result.id}</p>`;
    		content += `<p>Pages Subdomain: ${projectResponse.result.subdomain}</p>`;
    		content += `<p>Domains: ${projectResponse.result.domains.join(", ")}</p>`;
    		content += `<a href="${projectResponse.result.canonical_deployment.url}"><p>Production deployment: ${projectResponse.result.canonical_deployment.url}</p></a>`;
    
    		content += `<h2>Deployments</h2>`;
    		response = await fetch(deploymentsEndpoint, init);
    		const deploymentsResponse = await response.json();
    
    		for (const deployment of deploymentsResponse.result) {
    			content += `<a href="${deployment.url}"><p>Deployment: ${deployment.id}</p></a>`;
    		}
    
    		let html = `
          <!DOCTYPE html>
          <html>
            <head>
              <title>Example Pages Project</title>
            </head>
            <body>
              <style>${style}</style>
              <div id="container">
                ${content}
              </div>
            </body>
          </html>`;
    
    		return new Response(html, {
    			headers: {
    				"Content-Type": "text/html;charset=UTF-8",
    			},
    		});
    	},
    };

## Related resources

  * [Pages API Docs](https://developers.cloudflare.com/api/resources/pages/subresources/projects/methods/list/)
  * [Workers Getting Started Guide](https://developers.cloudflare.com/workers/get-started/guide/)
  * [Workers Cron Triggers](https://developers.cloudflare.com/workers/configuration/cron-triggers/)



[PreviousRedirects](https://developers.cloudflare.com/pages/configuration/redirects/)[NextRollbacks](https://developers.cloudflare.com/pages/configuration/rollbacks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/configuration/api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
