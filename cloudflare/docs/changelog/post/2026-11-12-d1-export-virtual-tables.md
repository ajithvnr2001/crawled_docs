---
url: https://developers.cloudflare.com/changelog/post/2026-11-12-d1-export-virtual-tables/
title: Export D1 databases with virtual tables \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:04.926857+00:00
---

# Export D1 databases with virtual tables · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-12-d1-export-virtual-tables/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 12, 2026

## Export D1 databases with virtual tables

[D1](https://developers.cloudflare.com/d1/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now export a D1 database that contains virtual tables, such as full-text search tables using SQLite's [FTS5 module ↗︎](https://www.sqlite.org/fts5.html) or spatial index tables using the `R*Tree` module. Previously, export failed for any database containing virtual tables.

To include virtual tables in the dump, set `dump_options.compatibility` to `sqlite3_cli_only` on the [D1 export API](https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/export/). The same option is available as the `--compatibility` flag on `wrangler d1 export`.

Import is not supported

This dump targets the SQLite CLI only. You cannot import it back into D1. Use the standard export for databases without virtual tables.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/d1/database/$DATABASE_ID/export" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"output_format": "polling",
    		"dump_options": {
    			"compatibility": "sqlite3_cli_only"
    		}
    	}'

For more information, refer to [Export a D1 database with virtual tables](https://developers.cloudflare.com/d1/best-practices/import-export-data/#export-a-d1-database-with-virtual-tables).
