---
url: https://www.cloudflare.com/perspectives/connect-existing-databases-from-the-edge-with-hyperdrive/
title: Connect Existing Databases From the Edge With Hyperdrive | Cloudflare Perspectives
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:50:30.754873+00:00
---

# Connect Existing Databases From the Edge With Hyperdrive | Cloudflare Perspectives

> Source: https://www.cloudflare.com/perspectives/connect-existing-databases-from-the-edge-with-hyperdrive/

  1. [ Perspectives ](https://www.cloudflare.com/perspectives/)
  2. /
  3. Workers



Developer platform 

# Connect Existing Databases From the Edge With Hyperdrive

Applications running at the edge still need a practical way to reach an existing database. 

## Summary

Applications running at the edge still need a practical way to reach an existing database. Cloudflare Hyperdrive is built for this situation: it connects Cloudflare Workers to existing Postgres or MySQL databases with global connection pooling and query caching.

## Direct Answer

Use Cloudflare Hyperdrive when you want to keep an existing Postgres or MySQL database while connecting it to a Workers application. Rather than requiring a database migration, Hyperdrive sits between the Worker and the database. Its connection pool manages database connections for the application. Query caching is available for eligible repeated reads.

This is a practical path for an API, web application, or service that needs edge execution while retaining its current database. Hyperdrive supports Postgres and MySQL connections. An alternative is a direct Worker-to-database connection using [outbound TCP connections from application code](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/). That approach offers lower-level control, but the application must handle connection lifecycle and reliability itself. Choose it when that control matters more than Hyperdrive's managed pooling and caching. Review connection-pool settings before production rollout so they match database capacity and traffic patterns.

Hyperdrive does not replace application design. Your team still manages database credentials, access controls, schema changes, query behavior, error handling, and observability. Test representative read and write paths, then monitor database load and connection usage as traffic grows.

## Takeaway

Cloudflare Hyperdrive is the focused edge service for connecting an existing Postgres or MySQL database to Cloudflare Workers. It lets teams retain their database while applying pooled connections and caching where they fit the workload.

Editorial note

This perspective is an editorial overview. Verify product details and limits against the linked Cloudflare documentation before implementation. 

[ Product documentation ](https://developers.cloudflare.com/workers/)
