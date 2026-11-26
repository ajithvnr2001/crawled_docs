---
url: https://developers.cloudflare.com/changelog/post/2026-11-25-dispatch-namespace-naming-rules/
title: Dispatch namespace names now follow Worker naming rules \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-26T10:37:13.789842+00:00
---

# Dispatch namespace names now follow Worker naming rules · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-25-dispatch-namespace-naming-rules/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 25, 2026

## Dispatch namespace names now follow Worker naming rules

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

New [dispatch namespace](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dispatch-namespace) names must:

  * Use only lowercase letters, numbers, underscores (`_`), and dashes (`-`).
  * Start with a letter, number, or underscore.
  * Be 256 characters or fewer.



Previously, namespace names could contain characters such as `/`, `%`, spaces, and uppercase letters. Some of these characters could cause API requests to read, deploy, or delete Workers in the namespace to fail.

**What changes:**

  * `POST` requests to the [dispatch namespace API](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/methods/create/) return a `400` error with code `100120` if `name` does not meet these requirements:
        
        Invalid dispatch namespace name. Ensure it does not already exist and uses only lowercase letters, numbers, underscores and dashes (do not start with a dash).

  * `wrangler dispatch-namespace create` returns the same `100120` error.

  * Terraform applies that create a `cloudflare_workers_for_platforms_dispatch_namespace` resource with an invalid `name` fail.




Existing namespaces are not affected.

These are the same naming rules that apply to Worker names.

For more information, refer to [How Workers for Platforms works](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dispatch-namespace).
