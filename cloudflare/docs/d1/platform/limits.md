---
url: https://developers.cloudflare.com/d1/platform/limits/
title: Limits \u00b7 Cloudflare D1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:20.625050+00:00
---

# Limits · Cloudflare D1 docs

> Source: https://developers.cloudflare.com/d1/platform/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[D1](https://developers.cloudflare.com/d1/)
  3. /Platform
  4. /Limits



# Limits

Last updated Oct 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFrequently Asked Questions How much work can a D1 database do? How many simultaneous connections can a Worker open to D1?

Feature | Limit  
---|---  
Databases per account | Workers Paid: 1,000,000. The first 100,000 databases are included. Each database above 100,000 costs [$0.10 per month](https://developers.cloudflare.com/d1/platform/pricing/#billing-metrics). Free: 10.  
Maximum database size | 10 GB (Workers Paid) / 500 MB (Free)  
Maximum storage per account | 1 TB (Workers Paid) 1 / 5 GB (Free)  
[Time Travel](https://developers.cloudflare.com/d1/reference/time-travel/) duration (point-in-time recovery) | 30 days (Workers Paid) / 7 days (Free)  
Maximum Time Travel restore operations | 10 restores per 10 minutes (per database)  
Queries per Worker invocation (read [subrequest limits](https://developers.cloudflare.com/workers/platform/limits/#subrequests)) | 1000 (Workers Paid) / 50 (Free)  
Maximum number of columns per table | 100  
Maximum number of rows per table | Unlimited (excluding per-database storage limits)  
Maximum string, `BLOB` or table row size | 2,000,000 bytes (2 MB)  
Maximum SQL statement length | 100,000 bytes (100 KB)  
Maximum bound parameters per query | 100  
Maximum arguments per SQL function | 32  
Maximum characters (bytes) in a `LIKE` or `GLOB` pattern | 50 bytes  
Maximum bindings per Workers script | Approximately 5,000 2  
Maximum SQL query duration | 30 seconds 3  
Maximum file import (`d1 execute`) size | 5 GB 4  
Maximum query result size | 50 MB 5  
  
Batch limits

Limits for individual queries (listed above) apply to each individual statement contained within a batch statement. For example, the maximum SQL statement length of 100 KB applies to each statement inside a `db.batch()`.

The Queries per Worker invocation limit is an exception: a `db.batch()` call counts as a single query against it, not one query per statement. For example, a batch containing 2,000 statements executes in a single Worker invocation, while issuing 2,000 individual queries in one invocation fails with `Too many API requests by single Worker invocation`.

Cloudflare also offers other storage solutions such as [Workers KV](https://developers.cloudflare.com/kv/api/), [Durable Objects](https://developers.cloudflare.com/durable-objects/), and [R2](https://developers.cloudflare.com/r2/get-started/). Each product has different advantages and limits. Refer to [Choose a data or storage product](https://developers.cloudflare.com/workers/platform/storage-options/) to review which storage option is right for your use case.

Need a higher limit?

To request an adjustment to a limit, complete the [Limit Increase Request Form ↗︎](https://forms.gle/eX6pXvit1wBv77Yw5). If the limit can be increased, Cloudflare will contact you with next steps.

## Frequently Asked Questions

Frequently asked questions related to D1 limits:

### How much work can a D1 database do?

D1 is designed for horizontal scale out across multiple, smaller (10 GB) databases, such as per-user, per-tenant or per-entity databases. The Workers Paid plan includes 100,000 databases per account. You pay [$0.10 per D1 database per month](https://developers.cloudflare.com/d1/platform/pricing/#billing-metrics) above the included amount. Query and storage charges apply separately.

#### Storage

Each D1 database can store up to 10 GB of data.

Caution

Note that the 10 GB limit of a D1 database cannot be further increased.

#### Concurrency and throughput

Each individual D1 database is inherently single-threaded, and processes queries one at a time.

Your maximum throughput is directly related to the duration of your queries.

  * If your average query takes 1 ms, you can run at most 1,000 queries per second.
  * If your average query takes 100 ms, you can run at most 10 queries per second.



Note that there is a small overhead per request that is not included in the timings that D1 reports. As a result, a database receiving many small requests would reach its limit before `1 / query duration` requests per second.

To get more throughput from a single database, reduce the number of requests rather than only the duration of each query. For example, use [`batch()`](https://developers.cloudflare.com/d1/worker-api/d1-database/#batch) to send multiple statements in a single request, so that the per-request overhead is paid once for the whole batch.

A database that receives too many concurrent requests will first attempt to queue them. If the queue becomes full, the database will return an ["overloaded" error](https://developers.cloudflare.com/d1/observability/debug-d1/#error-list).

Each individual D1 database is backed by a single [Durable Object](https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/). When using [D1 read replication ↗︎](https://developers.cloudflare.com/d1/best-practices/read-replication/#primary-database-instance-vs-read-replicas) each replica instance is a different Durable Object and the guidelines apply to each replica instance independently.

#### Query performance

Query performance is the most important factor for throughput. As a rough guideline:

  * Read queries like `SELECT name FROM users WHERE id = ?` with an appropriate index on `id` will take less than a millisecond for SQL duration.
  * Write queries like `INSERT` or `UPDATE` can take several milliseconds for SQL duration, and depend on the number of rows written. Writes need to be durably persisted across several locations - learn more on [how D1 persists data under the hood ↗︎](https://blog.cloudflare.com/d1-read-replication-beta/#under-the-hood-how-d1-read-replication-is-implemented).
  * Data migrations like a large `UPDATE` or `DELETE` affecting millions of rows must be run in batches. A single query that attempts to modify hundreds of thousands of rows or hundreds of MBs of data at once will exceed execution limits. Break the work into smaller chunks (e.g., processing 1,000 rows at a time) to stay within platform limits.



To ensure your queries are fast and efficient, [use appropriate indexes in your SQL schema](https://developers.cloudflare.com/d1/best-practices/use-indexes/).

#### CPU and memory

Operations on a D1 database, including query execution and result serialization, run within the [Workers platform CPU and memory limits](https://developers.cloudflare.com/workers/platform/limits/#memory).

Exceeding these limits, or hitting other platform limits, will generate errors. Refer to the [D1 error list for more details](https://developers.cloudflare.com/d1/observability/debug-d1/#error-list).

### How many simultaneous connections can a Worker open to D1?

You can open up to six connections (to D1) simultaneously for each invocation of your Worker.

For more information on a Worker's simultaneous connections, refer to [Simultaneous open connections](https://developers.cloudflare.com/workers/platform/limits/#simultaneous-open-connections).

## Footnotes

  1. The maximum storage per account can be increased by request on Workers Paid and Enterprise plans. Refer to the guidance on limit increases on this page to request an increase. ↩

  2. A single Worker script can have up to 1 MB of script metadata. A binding is defined as a binding to a resource, such as a D1 database, KV namespace, [environmental variable](https://developers.cloudflare.com/workers/configuration/environment-variables/), or secret. Each resource binding is approximately 150-bytes, however environmental variables and secrets are controlled by the size of the value you provide. Excluding environmental variables, you can bind up to ~5,000 D1 databases to a single Worker script. ↩

  3. Requests to Cloudflare API must resolve in 30 seconds. Therefore, this duration limit also applies to the entire batch call. ↩

  4. The imported file is uploaded to R2. Refer to [R2 upload limit](https://developers.cloudflare.com/r2/platform/limits). ↩

  5. This limit takes effect on 2026-11-04. Queries that return a result larger than 50 MB will fail and return an error. Import and export operations via the [REST API](https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/export/) are not subject to this limit. For more information, refer to the [query result size limit changelog entry](https://developers.cloudflare.com/changelog/post/2026-10-30-query-result-size-limit/). ↩




[PreviousPricing](https://developers.cloudflare.com/d1/platform/pricing/)[NextAlpha database migration guide](https://developers.cloudflare.com/d1/platform/alpha-migration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/d1/platform/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
