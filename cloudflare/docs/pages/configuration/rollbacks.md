---
url: https://developers.cloudflare.com/pages/configuration/rollbacks/
title: Rollbacks \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:31.758501+00:00
---

# Rollbacks · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/configuration/rollbacks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /Configuration
  4. /Rollbacks



# Rollbacks

Last updated Nov 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRelated resources

Rollbacks allow you to instantly revert your project to a previous production deployment. For rollbacks and gradual deployments on Cloudflare Workers, refer to [Workers Rollbacks](https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/).

Any production deployment that has been successfully built, and has not been deleted, is a valid rollback target. Deployments older than 30 days are deleted, except your 100 most recent and your current production deployment, and you cannot roll back to a deleted deployment. For more information, refer to [Deployments limits](https://developers.cloudflare.com/pages/platform/limits/#deployments). When your project has rolled back to a previous deployment, you may still roll back to deployments that are newer than your current version. Note that preview deployments are not valid rollback targets.

To perform a rollback:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select your Pages project and go to **Deployments**.

  3. Browse the **All deployments** list, select the three-dot actions menu for the desired target, and select **Rollback to this deployment**.

  4. Confirm in the dialog window to update your production deployment.




![Deployments for your Pages project that can be used for rollbacks](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2144,height=662,format=webp/_astro/rollbacks.DNHeRPOm.png)

## Related resources

  * [Preview Deployments](https://developers.cloudflare.com/pages/configuration/preview-deployments/)
  * [Branch deployment controls](https://developers.cloudflare.com/pages/configuration/branch-build-controls/)
  * [Workers Rollbacks](https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/)



[PreviousREST API](https://developers.cloudflare.com/pages/configuration/api/)[NextServing Pages](https://developers.cloudflare.com/pages/configuration/serving-pages/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/configuration/rollbacks.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
