---
url: https://developers.cloudflare.com/changelog/post/2026-11-11-durable-objects-request-routing/
title: Improved Request Routing to Durable Objects \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-12T09:30:22.284344+00:00
---

# Improved Request Routing to Durable Objects · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-11-durable-objects-request-routing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 11, 2026

## Improved Request Routing to Durable Objects

[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has reduced the number of round trips needed to connect to a Durable Object when a location lookup follows a forwarding record to another data center.

When an object's destination isn't cached in Cloudflare's network, the first data center contacted may have a forwarding record pointing to another data center.

Previously, the first data center acquired a connection to the object at the destination and proxied it back to the caller. The caller then established its own direct connection to the object.

Now, the first data center returns the destination directly, without first acquiring a connection to the object. The caller then establishes a direct connection, avoiding the intermediate connection and duplicate acquisition.

Skipping this intermediate connection can reduce p99 connection latency for these relocation-related requests. Actual results depend on your workload and traffic patterns.

No code or configuration changes are required to benefit from this improvement.

To learn more about how Workers connect to Durable Objects, refer to [Durable Object namespaces](https://developers.cloudflare.com/durable-objects/api/namespace/#get).
