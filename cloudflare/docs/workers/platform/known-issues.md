---
url: https://developers.cloudflare.com/workers/platform/known-issues/
title: Known issues \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-11-27T10:39:58.069712+00:00
---

# Known issues · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/platform/known-issues/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Platform](https://developers.cloudflare.com/workers/platform/)
  4. /Known issues



# Known issues

Last updated Nov 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRoute specificitywrangler devFetch API in CNAME setupFetch to IP addresses

Below are some known bugs and issues to be aware of when using Cloudflare Workers.

## Route specificity

  * When defining route specificity, a trailing `/*` in your pattern may not act as expected.



Consider two different Workers, each deployed to the same zone. Worker A is assigned the `example.com/images/*` route and Worker B is given the `example.com/images*` route pattern. With these in place, here are how the following URLs will be resolved:
    
    
    // (A) example.com/images/*
    // (B) example.com/images*
    
    "example.com/images"
    // -> B
    "example.com/images123"
    // -> B
    "example.com/images/hello"
    // -> B

You will notice that all examples trigger Worker B. This includes the final example, which exemplifies the unexpected behavior.

When adding a wildcard on a subdomain, here are how the following URLs will be resolved:
    
    
    // (A) *.example.com/a
    // (B) a.example.com/*
    
    "a.example.com/a"
    // -> B

## wrangler dev

  * When running `wrangler dev --remote`, all outgoing requests are given the `cf-workers-preview-token` header, which Cloudflare recognizes as a preview request. This applies to the entire Cloudflare network, so making HTTP requests to other Cloudflare zones is currently discarded for security reasons. To enable a workaround, insert the following code into your Worker script:


    
    
    const request = new Request(url, incomingRequest);
    request.headers.delete('cf-workers-preview-token');
    return await fetch(request);

## Fetch API in CNAME setup

If a Worker subrequest to a hostname in its own Partial (CNAME) zone returns HTTP `530` with Cloudflare error `1016`, refer to [Fetch a hostname in a Partial (CNAME) zone](https://developers.cloudflare.com/workers/runtime-apis/fetch/#fetch-a-hostname-in-a-partial-cname-zone).

## Fetch to IP addresses

For Workers subrequests, requests can only be made to URLs, not to IP addresses directly. To overcome this limitation [add an A or AAAA record to your zone](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) and then fetch that resource.

For example, in the zone `example.com` create a record of type `A` with the name `server` and value `192.0.2.1`, and then use:
    
    
    await fetch('http://server.example.com')

Do not use:
    
    
    await fetch('http://192.0.2.1')

[PreviousBuilt with Cloudflare button](https://developers.cloudflare.com/workers/platform/built-with-cloudflare/)[NextWorkers for Platforms ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/platform/known-issues.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
