---
url: https://developers.cloudflare.com/changelog/post/2026-10-21-basin-sql-offset/
title: Basin SQL supports OFFSET \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:48.362986+00:00
---

# Basin SQL supports OFFSET · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-21-basin-sql-offset/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 21, 2026

## Basin SQL supports OFFSET

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-21-basin-sql-offset/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Basin SQL](https://developers.cloudflare.com/basin-sql/) is a serverless, distributed SQL engine for querying Apache Iceberg tables in Basin Catalog. It now supports `OFFSET`, which lets you skip a specified number of rows when retrieving query results.

Use `LIMIT` to set the page size and `OFFSET` to skip earlier rows. With a page size of 100, use `OFFSET 0` for the first page, `OFFSET 100` for the second, and increase the offset by 100 for each later page. Add `ORDER BY` on a unique column to keep the row order consistent.

For example, this query returns the second page of 100 rows:
    
    
    SELECT sale_id, total_amount
    FROM my_namespace.sales_data
    ORDER BY sale_id
    LIMIT 100 OFFSET 100

For syntax and examples, refer to the [OFFSET clause](https://developers.cloudflare.com/basin-sql/sql-reference/#offset-clause) in the Basin SQL reference.
