---
url: https://developers.cloudflare.com/changelog/post/2026-11-12-d1-data-source/
title: AI Search supports D1 databases as a data source (beta) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:04.745885+00:00
---

# AI Search supports D1 databases as a data source (beta) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-12-d1-data-source/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 12, 2026

## AI Search supports D1 databases as a data source (beta)

[AI Search](https://developers.cloudflare.com/ai-search/)[D1](https://developers.cloudflare.com/d1/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) can now use a [D1](https://developers.cloudflare.com/d1/) database as a data source. AI Search runs a read-only query that you provide and indexes each returned row as a separate document. Scheduled syncs keep the index current as rows are added, changed, or removed.

Create D1-backed instances from the dashboard, the REST API, or the Workers binding.

![Selecting a D1 database as the data source when creating an AI Search instance in the dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1964,height=1676,format=webp/_astro/d1-data-source-dashboard.DkeDgrZb.png)
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/default/instances" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      --data '{
        "id": "help-center",
        "type": "d1",
        "source": "<D1_DATABASE_ID>",
        "token_id": "<SERVICE_TOKEN_ID>",
        "source_params": {
          "d1": {
            "query": "SELECT article_id AS id, title, content, category AS meta_category\nFROM articles\nWHERE published = 1"
          }
        }
      }'

Learn more in [D1 data source](https://developers.cloudflare.com/ai-search/configuration/data-source/d1/).
