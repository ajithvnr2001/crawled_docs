---
url: https://developers.cloudflare.com/changelog/post/2026-11-20-dispatch-namespace-rename-removed/
title: Dispatch namespaces can no longer be renamed \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-21T09:24:30.519677+00:00
---

# Dispatch namespaces can no longer be renamed · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-20-dispatch-namespace-rename-removed/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 20, 2026

## Dispatch namespaces can no longer be renamed

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can no longer rename a [dispatch namespace](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dispatch-namespace) after creating it.

Renaming a namespace could cause API requests to read, deploy, or delete Workers to fail because dispatch Workers and [outbound Workers](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/) retained the namespace name they were deployed with. This change prevents those failures by rejecting rename requests.

**What changes:**

  * `PUT` and `PATCH` requests to the [dispatch namespace API](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/methods/update/) return a `400` error with code `100413` if they change `name`:
        
        Dispatch namespaces cannot be renamed. The name in the request must match the namespace's current name. To use a different name, create a new dispatch namespace.

  * `wrangler dispatch-namespace rename` returns the same `100413` error.

  * Terraform applies that attempt to change `name` on a `cloudflare_workers_for_platforms_dispatch_namespace` resource fail.




**To move your Workers to a namespace with a different name:**

  1. Create a new dispatch namespace with the name you want.
  2. Deploy your user Workers to the new namespace.
  3. Update the [dispatch namespace binding](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/) in your dispatch Worker to reference the new namespace, then redeploy the dispatch Worker.
  4. Verify that requests are routed to the new namespace and your Workers work as expected.
  5. Delete the user Workers in the old namespace, then delete the old namespace.



For more information, refer to [How Workers for Platforms works](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dispatch-namespace).
