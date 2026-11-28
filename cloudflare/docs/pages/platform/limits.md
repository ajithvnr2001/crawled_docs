---
url: https://developers.cloudflare.com/pages/platform/limits/
title: Limits \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:31.660581+00:00
---

# Limits · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/platform/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /Platform
  4. /Limits



# Limits

Last updated Nov 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBuildsCustom domainsDeploymentsFilesFile sizeFunctionsHeadersPreview deploymentsRedirectsUsersProjects

The following limits apply to Cloudflare Pages by plan type. For more details on plans, refer to the [Cloudflare plans ↗︎](https://www.cloudflare.com/plans/) page.

Need a higher limit?

To request an adjustment to a limit, complete the [Limit Increase Request Form ↗︎](https://forms.gle/eX6pXvit1wBv77Yw5). If the limit can be increased, Cloudflare will contact you with next steps.

## Builds

Each time you push new code to your Git repository, Pages builds and deploys your site. Build limits depend on your plan:

| Free | Pro | Business  
---|---|---|---  
Builds | 1 build at a time | 5 concurrent builds | 20 concurrent builds  
Builds per month | 500 | 5,000 | 20,000  
  
Builds time out after 20 minutes. Concurrent builds are counted per account. For Enterprise build limits, contact your account team.

## Custom domains

Based on your Cloudflare plan type, a Pages project is limited to a specific number of custom domains. This limit is on a per-project basis.

Free | Pro | Business | Enterprise  
---|---|---|---  
100 | 250 | 500 | 5001  
  
## Deployments

Limit | Value  
---|---  
Deployment retention | 30 days  
Deployments always kept | 100 most recent, plus your current production deployment  
  
Deployments are kept for 30 days. After 30 days, a deployment is deleted unless:

  * It is one of the project's 100 most recent deployments. Both production and preview deployments count.
  * It is your current production deployment.



For example, a project has 250 deployments. Its 100 most recent deployments are always kept. Of the other 150, deployments created in the last 30 days are kept, and older ones are deleted unless one of them is your current production deployment.

When a deployment is deleted:

  * It no longer appears in your project's deployment list in the dashboard or API.
  * Its unique preview URL, such as `<hash>.<project>.pages.dev`, stops working.
  * You cannot [roll back](https://developers.cloudflare.com/pages/configuration/rollbacks/) to it.



## Files

Pages uploads each file on your site to Cloudflare's globally distributed network to deliver a low latency experience to every user that visits your site. Cloudflare Pages sites can contain up to 20,000 files on the Free plan.

Paid plans (such as Pro, Business, and Enterprise plans) can have up to 100,000 files per site. To enable this increased limit, set the environment variable `PAGES_WRANGLER_MAJOR_VERSION=4` in your Pages project settings.

## File size

The maximum file size for a single Cloudflare Pages site asset is 25 MiB.

Larger Files

To serve larger files, consider uploading them to [R2](https://developers.cloudflare.com/r2/) and utilizing the [public bucket](https://developers.cloudflare.com/r2/buckets/public-buckets/) feature. You can also use [custom domains](https://developers.cloudflare.com/r2/buckets/public-buckets/#connect-a-bucket-to-a-custom-domain), such as `static.example.com`, for serving these files.

## Functions

Requests to [Pages Functions](https://developers.cloudflare.com/pages/functions/) count toward your Workers plan request quota and CPU limits. Subrequests from a Function to bindings such as KV or Durable Objects do not count as additional Workers requests, though each bound service has its own usage quotas and pricing.

Pages supports the [Workers Standard usage model](https://developers.cloudflare.com/workers/platform/pricing/#workers).

## Headers

A `_headers` file can have a maximum of 100 header rules.

Each header line in a `_headers` file can have a maximum of 2,000 characters. For managing larger headers, use [Pages Functions](https://developers.cloudflare.com/pages/functions/).

## Preview deployments

Preview deployments count toward the deployments that Cloudflare keeps for each project. Preview deployments older than 30 days are deleted, unless they are one of the project's 100 most recent deployments. For more information, refer to Deployments.

## Redirects

A `_redirects` file can have a maximum of 2,000 static redirects and 100 dynamic redirects, for a combined total of 2,100 redirects, with a 1,000-character limit per rule. Use [Bulk Redirects](https://developers.cloudflare.com/pages/configuration/redirects/#surpass-_redirects-limits) when you need more rules than `_redirects` supports.

## Users

Your Pages site can be managed by an unlimited number of users via the Cloudflare dashboard. This does not correlate with your Git project — you can manage both public and private repositories, open issues, and accept pull requests without impacting your Pages site.

## Projects

Cloudflare Pages has a limit of 100 projects2 per account. This limit is not routinely increased.

If you need to host more than 100 sites, use one of these products designed for scale:

  * **[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)** — Deploy sites and applications at scale with no project limit. Supports [static assets](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/).
  * **[Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/)** — Deploy static sites as individual Workers. Paid plans support up to 500 Workers per account, each serving up to 100,000 static asset files.



Note

The Workers project limit (100 on Free, 500 on paid plans) is separate from the Pages project limit. Refer to [Workers limits](https://developers.cloudflare.com/workers/platform/limits/#number-of-workers) for details.

In order to protect against abuse of the service, Cloudflare limits the number of new Pages projects you can create within your first 48 hours of using the service. If you are temporarily blocked from creating new projects, this restriction will automatically lift once the initial 48-hour window has passed.

## Footnotes

  1. If you need more custom domains, contact your account team. ↩

  2. If you need a higher project limit, use [Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/). ↩




[PreviousUse Pages Functions for A/B testing](https://developers.cloudflare.com/pages/how-to/use-worker-for-ab-testing-in-pages/)[NextChoose a data or storage product ↗︎](https://developers.cloudflare.com/workers/platform/storage-options/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/platform/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
