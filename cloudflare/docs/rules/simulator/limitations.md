---
url: https://developers.cloudflare.com/rules/simulator/limitations/
title: Rules simulator limitations \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-11-20T09:50:42.376959+00:00
---

# Rules simulator limitations · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/simulator/limitations/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Rules simulator](https://developers.cloudflare.com/rules/simulator/)
  4. /Limitations



# Rules simulator limitations

Last updated Nov 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAutomatic rule bypassesRequests handled by Snippets or WorkersUnsupported features

## Automatic rule bypasses

Rules simulator does not display rules that are automatically bypassed for operational reasons.

For example, when SSL/TLS certificates are in `pending_validation` status, security rules are automatically disabled for domain control validation (DCV) paths like `/.well-known/pki-validation/` and `/.well-known/acme-challenge/`. These bypasses will not appear in simulation results.

For more information, refer to [Why are some rules bypassed?](https://developers.cloudflare.com/waf/troubleshooting/faq/#why-are-some-rules-bypassed-when-i-did-not-create-an-exception) in the WAF documentation.

* * *

## Requests handled by Snippets or Workers

When a simulated request matches a [Snippet](https://developers.cloudflare.com/rules/snippets/) rule or a [Worker](https://developers.cloudflare.com/workers/) route, the simulation results do not include the **Cache Parameters** > **Cache Key** section.

Cloudflare computes the cache key on the subrequest that the Snippet or Worker sends with `fetch()`, not on the incoming request. Rules simulator does not trace that subrequest, so it cannot show the cache key. The Snippet or Worker code can also change the URL or headers of the subrequest, which changes the cache key.

To check whether the response is served from cache, send a real request and inspect the `cf-cache-status` response header.

* * *

## Unsupported features

Rules simulator currently does not support:

  * Hostnames using [Data Localization Suite](https://developers.cloudflare.com/data-localization/)
  * [Spectrum](https://developers.cloudflare.com/spectrum/) applications



Additionally, the following products will not appear in simulation results:

  * [Firewall rules (deprecated)](https://developers.cloudflare.com/firewall/)
  * [Load Balancing](https://developers.cloudflare.com/load-balancing/) and [Load Balancer Custom Rules](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/)
  * [IP Access rules](https://developers.cloudflare.com/waf/tools/ip-access-rules/)
  * [Rate limiting rules (previous version)](https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/)
  * [WAF managed rules (previous version)](https://developers.cloudflare.com/waf/reference/legacy/old-waf-managed-rules/)
  * [Content security rules](https://developers.cloudflare.com/client-side-security/rules/)



[PreviousUse Rules simulator](https://developers.cloudflare.com/rules/simulator/how-to/)[NextChangelog](https://developers.cloudflare.com/rules/simulator/changelog/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/simulator/limitations.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
