---
url: https://developers.cloudflare.com/changelog/product-group/application-performance/
title: Application performance Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:30.693938+00:00
---

# Application performance Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product-group/application-performance/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloud Workload Security

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Oct 14, 2026

## [Configure Advanced Custom Nameservers with nameserver sets (beta)](https://developers.cloudflare.com/changelog/post/2026-10-14-nameserver-sets/)

[DNS](https://developers.cloudflare.com/dns/)

[Nameserver sets](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/) are now available in beta to Enterprise accounts. A nameserver set groups two to five custom nameserver names with Cloudflare-assigned IP addresses. You can assign the set to zones in the same account.

Enterprise customers using Cloudflare DNS can create Advanced Custom Nameserver sets. These sets distribute addresses across Advanced anycast network groups to improve resiliency.

Compared to legacy `custom_ns` sets, modern nameserver sets offer several advantages:

  * **Sets are reusable objects.** Accounts are no longer limited to 5 numbered sets. Create a set once and assign it to one or more zones in the same account.
  * **Custom address counts.** Assign each nameserver up to 3 IPv4 and 3 IPv6 addresses. This allows for more flexible setups.
  * **Diverse addresses.** IPv4 and IPv6 addresses are now both selected from a diverse set of prefixes for increased redundancy.
  * **Support for Advanced Custom Nameservers.** Set `advanced` to `true` to allocate addresses from Advanced anycast network groups, providing the same benefits as Cloudflare branded [Advanced nameservers](https://developers.cloudflare.com/dns/foundation-dns/advanced-nameservers/) to your custom nameservers.
  * **Explicit changes.** Sets are immutable, so adding or removing a nameserver name never changes the configuration of zones that already use a set.



Create a set by sending a `POST` request to `/accounts/{account_id}/dns_settings/nameserver_sets` with the following body:
    
    
    {
    	"advanced": true,
    	"ip_set": 1,
    	"nameservers": [
    		{ "name": "ns1.example.com" },
    		{ "name": "ns2.example.com" },
    		{ "name": "ns3.example.com" }
    	]
    }

Then, send a `PATCH` request to `/zones/{zone_id}/dns_settings` with the returned nameserver set ID:
    
    
    {
    	"nameservers": {
    		"type": "custom",
    		"nameserver_set_id": "0123456789abcdef0123456789abcdef"
    	}
    }

This configures the zone to use the nameserver set.

For more information, including other setup steps, refer to [Nameserver sets](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/).

Legacy `custom_ns` sets remain supported. A single account can use both.

Oct 14, 2026

## [Remove surrounding bytes with trim functions](https://developers.cloudflare.com/changelog/post/2026-10-14-trim-functions/)

[Rules](https://developers.cloudflare.com/rules/)

Cloudflare Rules supports three new functions for removing surrounding bytes. Use them to remove whitespace before comparing request values. All HTTP products support these functions on all plans:

  * `trim()` removes bytes from both ends.
  * `trim_start()` removes bytes from the start.
  * `trim_end()` removes bytes from the end.



By default, these functions remove ASCII whitespace. An optional constant string specifies a custom set of bytes.

If the input value is nil, these functions return nil.

For example, this expression removes surrounding whitespace before comparing a header value:
    
    
    trim(http.request.headers["x-label"][0]) eq "approved"

For details, refer to the [`trim()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#trim), [`trim_start()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#trim_start), and [`trim_end()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#trim_end) function references.

Oct 13, 2026

## [Deeper Core Web Vitals Diagnostics: LCP & INP Sub-Part Metrics in Real User Monitoring](https://developers.cloudflare.com/changelog/post/2026-10-13-core-web-vital-subparts/)

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

The Core Web Vitals tell you whether a page is slow but beyond perceived load time, layout instability, or responsiveness they do not guide you to the problematic area directly. To help you with this, Real User Monitoring (RUM) in Web Analytics now breaks Largest Contentful Paint (LCP) and Interaction to Next Paint (INP) into their respective sub-parts. It also splits connection time into TCP and TLS. You can see this visualised in the dashboard or query it through the GraphQL Analytics API.

#### LCP sub-parts

LCP is broken into four phases, so you can see which one is impacting your perceived load time:

  1. **Time to First Byte:** how long the browser waits for the HTML document (`timeToFirstByte` in GraphQL).
  2. **Resource load delay:** how long the browser takes to discover the LCP resource after the document starts arriving (`lcpResourceLoadDelay`).
  3. **Resource load duration:** how long it takes to download that resource (`lcpResourceLoadTime`).
  4. **Element render delay:** the gap between the resource arriving and the element appearing on screen (`lcpElementRenderDelay`).



You do not have to remember all this detail, there are tooltips available to guide you next to each sub-part metric in the dashboard.

![LCP sub-parts visual in the dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1704,height=384,format=webp/_astro/dash-web_analytics-lcp-sub-parts.CSpKXT00.png)

#### INP sub-parts

INP is broken into three phases, guiding you to the area slowing down responsiveness:

  1. **Input delay:** how long an interaction (click, tap or key press) is blocked before it can be processed (`inpInputDelay`).
  2. **Processing duration:** how long your event handlers take to run (`inpProcessingDuration`).
  3. **Presentation delay:** how long the browser takes to render the next frame after the handlers finish (`inpPresentationDelay`).

![INP sub-parts visual in the dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1704,height=382,format=webp/_astro/dash-web_analytics-inp-sub-parts.DWKDfc7K.png)

#### TCP and TLS timing

The page load timing breakdown now separates connection setup from the TLS handshake, so you can tell a slow network path from a slow TLS negotiation:

  * **Connection time (excluding TLS)** (`connectionTimeWithoutTLS`)
  * **TLS handshake time:** (`tlsTime`).



Note: we've retained `connectionTime` in the GraphQL API so you can still analyze the combined time.

#### How to query the GraphQL data

The sub-parts are available on `rumWebVitalsEventsAdaptiveGroups` as percentiles, for example: `lcpResourceLoadDelayP50` or `inpInputDelayP50`. The connection split is available on `rumPerformanceEventsAdaptiveGroups` as `connectionTimeWithoutTLSP50` and `tlsTimeP50`, and so on for the other percentiles.

The percentiles available are: P25, P50, P75, P90, P95, P99, P999. All values are in microseconds. A negative value means the data is not available.

#### How to get started

[ Go to **Real user monitoring** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/speed/rum)

Head to the 'Core Web Vitals' section, here you can scroll down the report to see the sub-parts. The 'Page Load' section contains the Connection and TLS negotiation durations.

For more on the data, refer to [the Web Analytics docs](https://developers.cloudflare.com/web-analytics/) and [the GraphQL Analytics API docs](https://developers.cloudflare.com/analytics/graphql-api/).

Oct 9, 2026

## [Failed detections field available in Rules](https://developers.cloudflare.com/changelog/post/2026-10-09-failed-detections/)

[WAF](https://developers.cloudflare.com/waf/)[Rules](https://developers.cloudflare.com/rules/)

You can now use `cf.appsec.request.failed_detections` to control how your rules handle requests when a security detection reports a failure.

The field is an `Array<String>` of detection IDs that reports failures from content scanning, WAF attack score, attack signature detection, leaked credentials detection, and AI prompt detections for personally identifiable information (PII), prompt injection, custom topics, and unsafe topics.

The field does not alter the existing behavior of detections. Use it in rules to choose how to handle requests with reported failures.

When no failures are reported, the field returns `[]`. You can use it on all plans, but your plan must still include the detections and rule features you want to use.

Supported rules:

  * Custom rules at the zone and account levels
  * Rate limiting rules at the zone and account levels
  * Request Header Transform Rules at the zone level



Match any reported failure:
    
    
    len(cf.appsec.request.failed_detections) gt 0

Match a reported leaked credentials detection failure:
    
    
    any(cf.appsec.request.failed_detections[*] eq "waf_credential_check")

For more information, refer to the [Failed detections field reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.appsec.request.failed_detections/).

Oct 6, 2026

## [Warnings when approaching your DNS records quota](https://developers.cloudflare.com/changelog/post/2026-10-06-dns-records-quota-warning/)

[DNS](https://developers.cloudflare.com/dns/)

The DNS records page in the Cloudflare dashboard now shows a warning once you have used 85% of your [DNS records quota](https://developers.cloudflare.com/dns/manage-dns-records/#dns-records-quota).

The warning reflects the quota that applies to you. If your zone has its own quota, the warning shows that zone's usage. If your account uses an [account-level DNS records quota](https://developers.cloudflare.com/dns/manage-dns-records/#per-account-quota), the warning shows your usage across all zones in the account.

![Warning on the DNS records page showing that a domain has used 86% of its DNS record limit](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1520,height=226,format=webp/_astro/dns-records-quota-warning.iH_msM4_.png)

Oct 2, 2026

## [hash_in_range() is globally available for HTTP products](https://developers.cloudflare.com/changelog/post/2026-10-02-hash-in-range-ga/)

[Rules](https://developers.cloudflare.com/rules/)

`hash_in_range()` is globally available for HTTP products on all plans. It hashes fields into an integer within a specified range. Use this result to select a portion of requests.

Use `cf.random_seed` to select approximately 10% of requests at random:
    
    
    hash_in_range(0, 100, cf.random_seed) < 10

With Cloudflare for SaaS, use [custom metadata](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/) to control rollout progression. Define `rollout_pct` as a custom key for each hostname. Set its value to an integer from 0 to 100. The expression selects approximately that percentage of requests:
    
    
    hash_in_range(0, 100, cf.random_seed) < coalesce(lookup_json_integer(cf.hostname.metadata, "rollout_pct"), 0)

If `rollout_pct` is missing, `coalesce()` supplies `0`. The rule then matches no requests.

For details, refer to the [`hash_in_range()` function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#hash_in_range).

Oct 1, 2026

## [Handle missing values with coalesce()](https://developers.cloudflare.com/changelog/post/2026-10-01-coalesce-function/)

[Rules](https://developers.cloudflare.com/rules/)

The `coalesce()` function returns the first argument that is not nil. Use it to provide a fallback in rule expressions:
    
    
    http.request.uri.path eq coalesce(http.request.uri.args["expected_path"][0], "/")

For details, refer to the [`coalesce()` function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#coalesce).

Oct 1, 2026

## [Compare dynamic values in Rules expressions](https://developers.cloudflare.com/changelog/post/2026-10-01-dynamic-comparison-values/)

[Rules](https://developers.cloudflare.com/rules/)

Cloudflare Rules expressions now support dynamic values on both sides of equality and ordering comparisons. You can compare request fields or function results with one another.

For example, compare the current request path with its original value:
    
    
    http.request.uri.path ne raw.http.request.uri.path

For supported operators and examples, refer to [Compare dynamic values](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#compare-dynamic-values).

Sep 30, 2026

## [Longer rule descriptions in logs](https://developers.cloudflare.com/changelog/post/2026-09-30-longer-rule-descriptions-in-logs/)

[Rules](https://developers.cloudflare.com/rules/)

Cloudflare logs now include up to 128 bytes of a rule description, increased from 80 bytes. Longer descriptions provide more context when investigating matched rules and make it easier to identify the relevant rule without referring back to its configuration.

Descriptions longer than 128 bytes are truncated without splitting a UTF-8 character. This change does not affect the Rulesets API, which continues to accept rule descriptions of up to 4,096 bytes.

For more information, refer to [Rule object structure and properties](https://developers.cloudflare.com/ruleset-engine/rulesets-api/json-object/#rule-object-structure-and-properties).

Sep 28, 2026

## [Invalidate cached content instead of purging it](https://developers.cloudflare.com/changelog/post/2026-09-28-cache-invalidation/)

[Cache / CDN](https://developers.cloudflare.com/cache/)

You can now invalidate cached content instead of purging it. Invalidation marks matching content as stale. On the next request, Cloudflare revalidates the content with your origin. If your origin responds with `304 Not Modified`, Cloudflare reuses the cached content instead of downloading it again.

Use invalidation to refresh a group of assets when only some of them have changed. For example, invalidate all content that shares a cache tag. Cloudflare reuses unchanged assets instead of downloading them again. This requires your origin to return an `ETag` or `Last-Modified` header and support conditional requests.

Invalidation supports the same selectors as purge: URLs, cache tags, hostnames, URL prefixes, and everything. To invalidate content, send a `POST` request to the new `invalidate_cache` endpoint:
    
    
    curl --request POST \
      "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/invalidate_cache" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{"tags":["product-images"]}'

In the dashboard, use **Invalidate Cache** on the **Caching** > **Configuration** page.

Your cache settings determine whether Cloudflare serves stale content while it revalidates. Cloudflare can also serve invalidated content stale if your origin returns a `5xx` error or cannot be reached. To stop serving cached content, purge it instead.

Invalidation requests count toward the same [rate limits](https://developers.cloudflare.com/cache/guides/invalidate-cache/#limits) as purge requests.

Purge behavior for Cache Reserve also changes with this release. For details, refer to [Cache Reserve purge behavior](https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/#purge-behavior).

For more information, refer to [Invalidate cached content](https://developers.cloudflare.com/cache/guides/invalidate-cache/).

Sep 28, 2026

## [Purge now forces a cache miss for Cache Reserve content](https://developers.cloudflare.com/changelog/post/2026-09-28-cache-reserve-purge-behavior/)

[Cache / CDN](https://developers.cloudflare.com/cache/)

Purge requests now force a cache miss for [Cache Reserve](https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/) content, regardless of purge type. Previously, purging by cache tag, hostname, prefix, or everything marked matching Cache Reserve content for revalidation. Purging by URL already removed content from Cache Reserve and is unchanged.

This change applies to purge requests from the API and the dashboard. Cache Reserve now handles purges the same way as the edge cache.

#### Cost impact

After a purge, the next request for affected content is a Cache Reserve miss. Your origin must deliver the content in full, even if it has not changed. Cloudflare then writes the content to Cache Reserve again, which is billed as a [Class A operation](https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/#pricing).

Purging by tag, hostname, prefix, or everything does not delete content from Cache Reserve right away. Matching content continues to incur storage costs until a later request replaces it or its retention period ends.

If you frequently purge Cache Reserve content by tag, hostname, prefix, or everything, review the effect on your origin egress and Cache Reserve usage.

#### Keep revalidating Cache Reserve content

To keep content in Cache Reserve and revalidate it instead, send the same request to the new `invalidate_cache` endpoint:
    
    
    curl --request POST \
      "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/invalidate_cache" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{"tags":["product-images"]}'

In the dashboard, use **Invalidate Cache** on the **Caching** > **Configuration** page.

If your origin responds with `304 Not Modified`, Cloudflare reuses the stored content instead of fetching it from your origin again. Compared with purging, invalidation reduces origin egress but not Cache Reserve operations. Updating the stored content after a `304` response is still a Class A operation. Invalidating by URL also updates the stored content when you send the request, which is a Class A operation.

Unlike the previous purge behavior, invalidation can serve stale content while it revalidates if your cache settings allow it. This applies only to copies in the edge cache, not to content served from Cache Reserve. Cloudflare can also serve invalidated content stale if your origin returns a `5xx` error or cannot be reached. For details, refer to [Invalidate cached content](https://developers.cloudflare.com/cache/guides/invalidate-cache/#stale-content-during-revalidation).

Sep 22, 2026

## [concat() now supports up to 32 arguments](https://developers.cloudflare.com/changelog/post/2026-09-22-concat-argument-limit/)

[Rules](https://developers.cloudflare.com/rules/)

The `concat()` function in Cloudflare Rules now accepts up to 32 arguments, increased from 16. This allows you to build richer dynamic values directly in Rules expressions and simplify configurations that combine request data.

A common use case is adding a request header that sends context to your origin. The following Rulesets API request adds a Request Header Transform Rule to an existing `http_request_late_transform` phase ruleset. Its 18-argument expression combines request and network information into one header value:
    
    
    curl --request POST \
      "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/$RULESET_ID/rules" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "ref": "add_request_context_header",
        "description": "Add request context for the origin",
        "expression": "true",
        "action": "rewrite",
        "action_parameters": {
          "headers": {
            "X-Request-Context": {
              "operation": "set",
              "expression": "concat(\"ip=\", to_string(ip.src), \";country=\", ip.src.country, \";host=\", http.host, \";method=\", http.request.method, \";path=\", http.request.uri.path, \";query=\", http.request.uri.query, \";ray-id=\", cf.ray_id, \";asn=\", to_string(ip.src.asnum), \";user-agent=\", http.user_agent)"
            }
          }
        }
      }'

For more information, refer to the [`concat()` function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#concat) and [HTTP request header modification](https://developers.cloudflare.com/rules/transform/request-header-modification/).

Sep 17, 2026

## [Validate Rulesets changes before deployment](https://developers.cloudflare.com/changelog/post/2026-09-17-rulesets-dry-run-validation/)

[Rules](https://developers.cloudflare.com/rules/)

Cloudflare Rules now validates ruleset changes before deployment, helping you catch invalid expressions, action parameters, permission issues, unavailable features, and quota limits without publishing the configuration.

The Cloudflare dashboard performs this validation automatically when you create or update rules from **Security** > **Security rules** or **Rules** > **Overview**.

Supported Rulesets API mutation endpoints now also accept the `dry_run=true` query parameter. A dry run performs the same authorization and server-side validation checks as the requested change, but does not persist or publish it. Successful operations that normally return a `200` response return `result: null`. Operations that normally return `204` continue to do so.

#### API example

Add `dry_run=true` to a Rulesets API request to validate it without creating the ruleset:
    
    
    curl --request POST \
      "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets?dry_run=true" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "name": "Custom firewall rules",
        "kind": "zone",
        "phase": "http_request_firewall_custom",
        "rules": [
          {
            "action": "block",
            "expression": "ip.src.country eq \"GB\"",
            "description": "Block requests from the United Kingdom",
            "enabled": true
          }
        ]
      }'

For more information, refer to [Validate rule changes before deployment](https://developers.cloudflare.com/ruleset-engine/rulesets-api/dry-run/).

Sep 14, 2026

## [Shadowed record warnings are now available for all zones](https://developers.cloudflare.com/changelog/post/2026-09-14-shadowed-record-warnings/)

[DNS](https://developers.cloudflare.com/dns/)

Cloudflare now displays warnings for shadowed records in all zones. A record is shadowed when a subdomain delegation gives authority for its name, or a name below it, to another set of nameservers. The record remains present, but your zone is not authoritative for it thus Cloudflare will not respond with it to matching DNS queries. These warnings help you find records that may no longer resolve from the expected zone.

Shadow metadata is also available in DNS records API responses when you set `include_shadow_metadata=true`. The metadata identifies the delegating `NS` records and, when applicable, whether an `A` or `AAAA` record is glue. For more information, refer to [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records/).

Sep 2, 2026

## [Configure Origin Range Requests with the Rulesets API](https://developers.cloudflare.com/changelog/post/2026-09-02-origin-range-requests-rulesets-api/)

[Cache / CDN](https://developers.cloudflare.com/cache/)

The Rulesets API now supports Origin Range Requests in Cache Rules. This setting lets Cloudflare fetch large files from your origin in cache-aligned byte ranges. Cloudflare may expand a client range and issue several single-range origin requests.

Set `origin_range_requests.mode` to `on`, `off`, or `default` for any traffic matched by a Cache Rule.

To override Cloudflare's default Origin Range Requests behavior, set the mode to `off`. The following rule turns off generated origin range requests for all traffic without changing cache eligibility:
    
    
    {
      "expression": "true",
      "action": "set_cache_settings",
      "action_parameters": {
        "origin_range_requests": {
          "mode": "off"
        }
      }
    }

Origin Range Requests do not make otherwise ineligible content cacheable. If your origin ignores `Range` and returns a complete `200 OK`, Cloudflare can use the response but must download the complete file. Origins should honor `Accept-Encoding: identity` and return consistent, unencoded partial responses.

For configuration details and mode behavior, refer to [Origin Range Requests in Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/settings/#origin-range-requests). For client responses and the complete origin contract, refer to [Range request behavior](https://developers.cloudflare.com/cache/reference/range-requests/).

Aug 31, 2026

## [Load Balancing now supports pool sets](https://developers.cloudflare.com/changelog/post/2026-08-31-pool-sets/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Cloudflare Load Balancing now supports pool sets through the API. Pool sets combine geographic matching with location-specific traffic steering. One load balancer can now use different routing behavior for different locations.

Each pool set can match a Cloudflare data center, country, or region. It then supplies the candidate pools and can apply its own steering policy, pool weights, and fallback pool. Cloudflare evaluates pool sets in array order and applies the first matching pool set.

For example, this pool set uses Dynamic Latency steering for traffic from Germany:
    
    
    {
    	"pool_sets": [
    		{
    			"name": "germany-lowest-latency",
    			"match": { "topology": { "countries": ["DE"] } },
    			"overrides": {
    				"pools": [
    					"0930eec54a4c7ae6616985b79f678210",
    					"c8b4f5a6d7e84910a2b3c4d5e6f70819"
    				],
    				"steering_policy": "dynamic_latency"
    			}
    		}
    	]
    }

Use pool sets for active-active traffic distribution, location-specific failover, and regional routing policies. For proxied traffic, a pool set can also return a fixed HTTP response instead of selecting a pool.

For configuration details and more examples, refer to [Pool sets](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/pool-sets/).

Aug 27, 2026

## [APO caches more crawler and bot traffic again](https://developers.cloudflare.com/changelog/post/2026-08-27-accept-header-caching/)

[Automatic Platform Optimization](https://developers.cloudflare.com/automatic-platform-optimization/)

We fixed a regression where Automatic Platform Optimization (APO) stopped caching some HTML requests that did not send an explicit `Accept: text/html` header — commonly crawlers, bots, and uptime monitors. These requests were being served from your origin (`cf-cache-status: DYNAMIC`) instead of the cache.

APO now caches these requests again. No action is needed. If you added a Transform Rule to set `Accept: text/html` as a workaround, you can remove it.

For details on how APO decides what to cache, refer to [About APO](https://developers.cloudflare.com/automatic-platform-optimization/about/).

Aug 21, 2026

## [Web Analytics improves soft navigation measurement for Single Page Applications (SPAs)](https://developers.cloudflare.com/changelog/post/2026-08-21-improved-soft-navigation-measurement-for-single-page-applications/)

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

Cloudflare Web Analytics (Real User Monitoring) is rolling out accuracy improvements to client-side soft navigations. **Update: this update is complete as of 2026-09-04.**

**This change may alter the volume of reported pageviews and visits in the dashboard and GraphQL API. The reported Largest Contentful Paint (LCP) metric may also fluctuate.** The extent of these variances depend on your front-end architecture and visitor traffic patterns.

Single Page Applications (SPAs)—such as websites built with React, Angular, Vue, or Svelte—predominantly use soft navigations. Soft navigations avoid fully unloading the current page and rendering the next one from scratch as visitors navigate.

Any client-side navigation counts as a soft navigation, including navigations intercepted by [the Navigation API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API) or triggered by [the History API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/History_API). This means a non-SPA website can have soft navigation activity if its implementation uses these APIs.

The main improvement comes from [Google Chrome's new Soft Navigation API ↗︎](https://developer.chrome.com/docs/web-platform/soft-navigations). It natively measures [Largest Contentful Paint (LCP)](https://developers.cloudflare.com/web-analytics/data-metrics/core-web-vitals/#core-web-vitals-metrics) on soft navigations, removing a blind spot in perceived loading speed across pageviews.

We've extended our `navigationType` values to segment these different types of navigations:

`navigationType` | New? | Description  
---|---|---  
`navigate` | ❌ | Hard navigations that traditional websites (or "Multi Page Applications") perform when clicking links or submitting forms  
`soft-navigation` | ✅ | Where [the new Soft Navigation API ↗︎](https://developer.chrome.com/docs/web-platform/soft-navigations) is available and a visitor makes a client-side navigation, we record these events  
`routing-apis` | ✅ | Where the native Soft Navigation API is unavailable (e.g. Safari, Firefox, older Chromium-based browsers), we fallback to measuring soft navigations using [the Navigation API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API) or [History API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/History_API). We cannot collect LCP for these, but the other Core Web Vitals are present.  
  
Prior to this change, we only used History API and all navigations were bucketed into `navigate`.

For more information, refer to the [Navigation Types](https://developers.cloudflare.com/web-analytics/data-metrics/dimensions/#navigation-types) and [Web Analytics SPA](https://developers.cloudflare.com/web-analytics/get-started/web-analytics-spa/) documentation pages.

Aug 17, 2026

## [Load balancing analytics now filters by pool name](https://developers.cloudflare.com/changelog/post/2026-08-17-pool-name-analytics-filter/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Load balancing analytics now filters traffic data by pool name instead of pool ID, aligning the query behavior with the pool names displayed in the filter dropdown.

Previously, the analytics pool filter queried by internal pool ID while displaying pool names in the UI dropdown. This mismatch caused filtering issues when pools shared similar names or when you expected results based on the visible pool name. Because the underlying query used a different identifier than what appeared on screen, the displayed data could be confusing or incorrect.

The pool filter now queries by the same pool name shown in the dropdown. When you select a pool from the filter, the analytics graphs and tables display data for that specific pool as you would expect. This change affects:

  * **Requests over time** , filtering the chart series to the selected pool.
  * **Pool distribution** , showing only the selected pool segment.
  * **Top endpoints** , displaying cards for origins in the selected pool.
  * **Latency** , showing latency data for the selected pool.



The **Logs** view and health event filtering are unchanged.

To use this, go to **Traffic** > **Load Balancing Analytics** for a zone. The same pool filter appears in the analytics view for an individual load balancer under **Load Balancing** at the account level.

For more information about analytics filters and metrics, refer to [Load Balancing Analytics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/).

Aug 13, 2026

## [Oracle Cloud Infrastructure Object Storage support in Cloud Connector](https://developers.cloudflare.com/changelog/post/2026-08-13-oci-object-storage-cloud-connector/)

[Rules](https://developers.cloudflare.com/rules/)

Cloud Connector now supports public Oracle Cloud Infrastructure (OCI) Object Storage buckets. You can route matching requests to OCI without managing a separate origin-routing configuration.

OCI support uses the Amazon S3 Compatibility API. Both path-style and virtual-hosted endpoint formats are supported, including traditional `oraclecloud.com` and dedicated `customer-oci.com` path-style endpoints.

Public buckets only

Cloud Connector does not sign requests or provide OCI credentials. Your bucket must allow anonymous object reads. Private buckets and pre-authenticated request URLs are not supported.

#### API example

Set `provider` to `oci_storage` and provide a supported OCI hostname. The following rule uses a virtual-hosted endpoint:
    
    
    {
    	"expression": "http.request.uri.path wildcard \"/assets/*\"",
    	"provider": "oci_storage",
    	"description": "Route assets to OCI Object Storage",
    	"enabled": true,
    	"parameters": {
    		"host": "<BUCKET_NAME>.vhcompat.objectstorage.<REGION>.oci.customer-oci.com"
    	}
    }

For endpoint formats and bucket requirements, refer to [Supported cloud providers in Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/providers/#oracle-cloud-infrastructure-object-storage).

Aug 13, 2026

## [Certificate Transparency Monitoring is now Generally Available](https://developers.cloudflare.com/changelog/post/2026-08-13-ct-monitoring-ga/)

[SSL/TLS](https://developers.cloudflare.com/ssl/)

Certificate Transparency Monitoring is now [generally available ↗︎](https://blog.cloudflare.com/certificate-transparency-monitoring-ga) across all Cloudflare plans.

Alerts for certificates Cloudflare issues on your behalf (Universal SSL renewals, backup certificates, Advanced Certificate Manager, Total TLS) are now automatically filtered out. Alert emails are also clearer and more actionable, with structured certificate details and a direct link to manage CT Monitoring in the Cloudflare dashboard.

Learn more in the [launch blog post ↗︎](https://blog.cloudflare.com/certificate-transparency-monitoring-ga) or the [CT Monitoring docs](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/).

Aug 7, 2026

## [Load Balancing health notifications now resolve automatically](https://developers.cloudflare.com/changelog/post/2026-08-07-stateful-health-notifications/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/) health notifications are now stateful. When a pool or endpoint becomes unhealthy, the notification opens an incident in your alerting tool as before. When that same pool or endpoint recovers, the follow-up notification is matched to the original alert and resolves that incident automatically, so you no longer have to close it by hand.

As part of this change, Load Balancing also sends a notification when a pool or endpoint returns to a healthy state, not only when it becomes unhealthy. Expect to see recovery notifications alongside the failure notifications you already receive.

This applies to your existing Load Balancing health alerts with no configuration change, and it matches the behavior already used by [Health Checks](https://developers.cloudflare.com/health-checks/) notifications.

Two things to keep in mind:

  * A recovery notification is matched to the earlier unhealthy notification for the **same pool or endpoint**. Renaming an endpoint while an incident is open prevents the match, so that incident stays open until you close it.
  * If a health change cannot be classified as either healthy or unhealthy, the notification is still delivered, but without the state needed to open or resolve an incident.



Refer to [Integrate with PagerDuty](https://developers.cloudflare.com/load-balancing/additional-options/pagerduty-integration/) to learn more about routing Load Balancing health notifications to an incident management tool.

Aug 3, 2026

## [See fallback pool traffic separately in load balancing analytics](https://developers.cloudflare.com/changelog/post/2026-08-03-fallback-pool-analytics/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Load balancing analytics now shows traffic served by your [fallback pool](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/#fallback-pools) separately from traffic routed to the same pool by normal steering.

Previously, requests were grouped by pool name alone. If the pool acting as your fallback also received traffic through your steering policy, both appeared as a single series, so it was not obvious from the graph whether Cloudflare was still making health-based routing decisions or had fallen back to the pool of last resort. Because the fallback pool ignores health, that distinction matters when you are diagnosing an outage or reviewing how much traffic was shed.

Fallback traffic is now labeled with the pool name followed by `(Fallback)`. A pool named `eu-west`, for example, is shown as `eu-west (Fallback)`. This label appears as its own entry in:

  * **Requests over time** , as a separate series in the chart.
  * **Pool distribution** , as a separate segment.
  * **Top endpoints** , as a separate card for the pool.



The **Latency** view and the health event **Logs** are unchanged.

To see this, go to **Traffic** > **Load Balancing Analytics** for a zone. The same breakdown appears in the analytics view for an individual load balancer under **Load Balancing** at the account level.

Refer to [load balancing analytics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/) to learn more.

Jul 21, 2026

## [Faster and more secure TLS handshakes to your origins, automatically](https://developers.cloudflare.com/changelog/post/2026-07-21-automatic-origin-key-exchange/)

[SSL/TLS](https://developers.cloudflare.com/ssl/)

Cloudflare now takes the guesswork out of TLS 1.3 key agreement with your origins. Automatic key exchange predicts the preferred algorithm and sends its key share in the first `ClientHello`, helping avoid a `HelloRetryRequest` and one extra network round trip.

Automatic key exchange is on for all existing zones and on by default for new zones. When an origin supports both classical and post-quantum key agreements, Cloudflare prefers the post-quantum `X25519MLKEM768` hybrid key agreement.

To change this behavior, go to **SSL/TLS** > **Overview** > **Origin connection & post-quantum encryption**. Turn off **Automatic key exchange** to stop automatic scans and preference updates. Turning it off does not change your compliance requirements.

**Compliance requirements** apply only to TLS 1.3 connections. The **Post-quantum hybrid** option requires hybrid post-quantum key agreements support on your origin server. The **Federal Information Processing Standards (FIPS)** option requires FIPS-compliant key agreements. Select both to require key agreements that satisfy both, or leave both unselected to allow all supported key agreements.

For requirements, configuration options, and rollout details, refer to [Automatic key exchange to origins](https://developers.cloudflare.com/ssl/origin-configuration/automatic-key-exchange/).

Jul 16, 2026

## [Bot management fields and ASN support in Cache Rules](https://developers.cloudflare.com/changelog/post/2026-07-16-cache-rules-bot-fields-asn/)

[Rules](https://developers.cloudflare.com/rules/)

#### Bot management fields and ASN support in Cache Rules

Cache Rules now supports bot management fields and the `ip.src.asnum` field in expression filters. You can now build cache policies that differentiate between automated and human traffic, or segment caching behavior by autonomous system number (ASN).

This allows you to apply different caching strategies for verified bots, high-risk traffic, or specific network operators without affecting legitimate user requests. For example, you can set shorter cache TTLs for suspected bot traffic or bypass cache entirely for requests from specific ASNs.

#### New fields

The following fields are now available in Cache Rules expressions:

Field | Type | Description  
---|---|---  
`cf.bot_management.score` | Number | Bot score from `1` to `99`, where a lower value indicates a higher likelihood that the request originates from a bot.  
`cf.bot_management.ja3_hash` | String | JA3 fingerprint of the request, which helps identify the client making the connection.  
`cf.bot_management.ja4` | String | JA4 fingerprint of the request, which provides a more detailed client identification than JA3.  
`cf.bot_management.verified_bot` | Boolean | Whether the request originates from a verified bot, such as a search engine crawler.  
`cf.bot_management.static_resource` | Boolean | Whether the request is for a static resource and therefore exempt from bot detection.  
`cf.bot_management.js_detection.passed` | Boolean | Whether the browser passed JavaScript detection when the feature is enabled.  
`cf.bot_management.detection_ids` | Array<Number> | List of IDs that correspond to Bot Management heuristic detections made on the request.  
`cf.bot_management.tags` | Array<String> | List of tags associated with the bot traffic, such as `API`, `GOOGLE`, or `BING`. Match a tag with an expression such as `any(cf.bot_management.tags[*] eq "API")`.  
`cf.bot_management.signed_agent` | Boolean | Whether the request originates from a known agent that identifies itself with Web Bot Auth.  
`cf.bot_management.corporate_proxy` | Boolean | Whether the request originates from a known corporate proxy.  
`ip.src.asnum` | Number | The autonomous system number (ASN) of the incoming request's IP address.  
  
Note

Bot management fields require a Bot Management subscription. `ip.src.asnum` is available on all plans.

#### Example

Cache Rules expressions support combining these fields with other criteria. The following example sets a shorter cache TTL for API requests that originate from a high-risk bot or an unexpected ASN:
    
    
    (http.request.uri.path contains "/api/" and cf.bot_management.score lt 30)
    or
    (http.request.uri.path contains "/api/" and not ip.src.asnum in {12345 67890})

To learn more, refer to the [Cache Rules documentation](https://developers.cloudflare.com/cache/how-to/cache-rules/) and the [Fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/).

← Prev

1[2](https://developers.cloudflare.com/changelog/product-group/application-performance/2/)…[4](https://developers.cloudflare.com/changelog/product-group/application-performance/4/)

[Next →](https://developers.cloudflare.com/changelog/product-group/application-performance/2/)
