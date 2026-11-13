---
url: https://developers.cloudflare.com/ai-search/get-started/dashboard/
title: Dashboard \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:09.254782+00:00
---

# Dashboard · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/get-started/dashboard/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /Get started
  4. /Dashboard



# Dashboard

Last updated Nov 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate an AI Search instanceUpload contentTry it outAdd to your application

This guide walks you through creating an AI Search instance using the Cloudflare dashboard.

## Create an AI Search instance

  1. Go to **AI Search** in the Cloudflare dashboard.

[ Go to **AI Search** ↗ ](https://dash.cloudflare.com/?to=/:account/ai/ai-search)
  2. Select **Create Instance**.

  3. Name your AI Search instance.

  4. Optionally connect a [data source](https://developers.cloudflare.com/ai-search/configuration/data-source/) such as a website you own, an R2 bucket, or a D1 database.

To connect a [D1 database](https://developers.cloudflare.com/ai-search/configuration/data-source/d1/), select **D1 Database** , choose the database, write the **SQL query** , and choose a document template. Select **Test query** to check the query before you continue.

  5. Review your configurations.

  6. Select **Create**.




## Upload content

Once an instance has been created, you can upload files directly from the dashboard.

  1. Go to **AI Search** in the Cloudflare dashboard.

[ Go to **AI Search** ↗ ](https://dash.cloudflare.com/?to=/:account/ai/ai-search)
  2. Select your instance.

  3. Select the **Items** tab.

  4. Upload your files. AI Search indexes them automatically.




## Try it out

Once your content is indexed, you can run your first query.

  1. Go to your AI Search instance.
  2. Select the **Playground** tab.
  3. Select **Chat** or **Search**.
  4. Enter a query to test the response.



## Add to your application

There are multiple ways you can connect AI Search to your application:

### [Workers Binding](https://developers.cloudflare.com/ai-search/api/search/workers-binding/)

Query AI Search directly from your Workers code.

### [REST API](https://developers.cloudflare.com/ai-search/api/search/rest-api/)

Query AI Search using HTTP requests.

[PreviousCLI](https://developers.cloudflare.com/ai-search/get-started/wrangler/)[NextPython SDK](https://developers.cloudflare.com/ai-search/get-started/python/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/get-started/dashboard.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
