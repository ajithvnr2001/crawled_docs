---
url: https://developers.cloudflare.com/changelog/product-group/core-platform/
title: Core platform Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:28.318507+00:00
---

# Core platform Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product-group/core-platform/

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

Oct 17, 2026

## [Test Cron Triggers with Local Explorer](https://developers.cloudflare.com/changelog/post/2026-10-17-local-explorer-cron-triggers/)

[Workers](https://developers.cloudflare.com/workers/)[Cloudflare CLI](https://developers.cloudflare.com/cf/)

Local Explorer can now send one-off Cron Trigger invocations to a Worker's `scheduled()` handler during local development. This removes the need to construct request URLs when testing handler behavior.

Start your local development server with [`cf dev`](https://developers.cloudflare.com/cf/projects/#start-development), [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev), or the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/). Open `/cdn-cgi/local/explorer` on the server URL and select **Cron Triggers**.

The browser interface supports the following tasks:

  * Invoke configured cron expressions
  * Build ad hoc expressions
  * Set reusable scheduled times
  * Inspect outcomes and `noRetry()` status



Ad hoc triggers and scheduled time presets stay in your browser. They do not change `cloudflare.config.ts`, your Wrangler configuration, or deployed Cron Triggers. Local development does not run cron schedules automatically.

Full logs and traces are available in the development session that owns the Worker when that session has **Observability** turned on.

The following example uses port `8787`. Replace it with your development server port, such as `5173` for Vite.

The Local Explorer API exposes the same operation for tools and AI agents. The request targets an exact Worker name and accepts a cron expression and optional scheduled time:
    
    
    curl -X POST \
      "http://localhost:8787/cdn-cgi/local/explorer/api/local/scheduled?worker=my-worker" \
      -H "Content-Type: application/json" \
      --data '{"cron":"0 * * * *","scheduled_time":1745856238000}'

For more details, refer to [Test Cron Triggers with Local Explorer](https://developers.cloudflare.com/workers/local-development/local-explorer/#test-cron-triggers).

Oct 16, 2026

## [Search Cloudflare documentation with the Cloudflare CLI](https://developers.cloudflare.com/changelog/post/2026-10-16-docs-search/)

[Workers](https://developers.cloudflare.com/workers/)[Cloudflare CLI](https://developers.cloudflare.com/cf/)

Cloudflare CLI `1.0.0-beta.16` includes `cf docs search`, so you and your coding agent can find Cloudflare documentation without leaving the terminal. Search for guides, tutorials, and examples across Cloudflare products.

To install or update to the latest release:

npmyarnpnpmbun
    
    
    npm install --global cf@latest
    
    
    yarn global add cf@latest
    
    
    pnpm add --global cf@latest
    
    
    bun add --global cf@latest

Describe what you want to do, or ask a question:
    
    
    cf docs search "proxy a DNS record"
    cf docs search "rate limit requests with WAF"
    cf docs search "schedule a worker"

The command searches live Cloudflare documentation and returns up to five ranked JSON results. Each result includes a title, description, and documentation URL. An Internet connection is required.

![Terminal demo of Cloudflare CLI beta-16 searching DNS and WAF documentation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1280,height=720,format=webp/_astro/docs-search-demo.cWBK3YBx.gif)

Agents can parse the results and fetch a complete page as Markdown. For example, use `jq` to select the first result, then request its URL with the `Accept: text/markdown` header:
    
    
    url=$(cf docs search "proxy a DNS record" | jq -r '.[0].url')
    curl -H "Accept: text/markdown" "$url"

This release also standardizes generated command names to kebab-case. For example, `cf accounts billing getCredits` becomes `cf accounts billing get-credits`. For the full list of breaking command and flag changes, refer to the [Cloudflare CLI release notes ↗︎](https://github.com/cloudflare/cf/blob/main/packages/cli/CHANGELOG.md).

For more information, refer to [Find Cloudflare documentation with a coding agent](https://developers.cloudflare.com/cf/agents/#find-cloudflare-documentation).

Oct 16, 2026

## [50,000 routes per account and Tunnels for Platforms](https://developers.cloudflare.com/changelog/post/2026-10-16-tunnels-for-platforms-and-50k-routes/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Two changes make it easier to run Cloudflare Tunnel at scale.

#### 50,000 routes per account by default

The default limit for [routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/) is now 50,000 per account, up from 1,000. This limit covers [CIDR routes](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/) and [hostname routes](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) for [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/). The new limit applies to every account automatically, with no action required.

Published applications (public hostnames) are not routes and are not affected by this limit. Each tunnel supports roughly 5,000–10,000 published applications, depending on the size of its configuration. For details, refer to [Published application limits](https://developers.cloudflare.com/tunnel/concepts/routing/#published-application-limits).

#### Tunnels for Platforms

Every account includes 1,000 tunnels. With [Tunnels for Platforms](https://developers.cloudflare.com/tunnel/features/tunnels-for-platforms/), you can now run more than 1,000 tunnels in a single account — for example, one tunnel per device, per end customer, or per development environment.

![Buy additional tunnels from the Tunnels page in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1512,height=802,format=webp/_astro/tunnels-for-platforms.DuPYMNzo.gif)

To buy additional tunnels, go to **Networking** > **Tunnels** and select **Buy more tunnels** in the **Usage** card. Additional tunnels are billed at $4.50 per tunnel per month. Enterprise customers can contact their account team for committed or usage-based pricing.

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)

For pricing, limits, and best practices for managing large tunnel fleets, refer to [Tunnels for Platforms](https://developers.cloudflare.com/tunnel/features/tunnels-for-platforms/).

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

## [Audit Logs v2 now captures view actions](https://developers.cloudflare.com/changelog/post/2026-10-13-audit-logs-v2-view-actions/)

[Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/)

Audit Logs v2 now records `view` actions for supported endpoints, providing visibility into read activity across Cloudflare products. These actions correspond to `GET` requests and provide additional context for security investigations and forensic analysis.

The Audit Logs v2 dashboard excludes `view` actions by default to reduce noise. Remove the default **Action type** is not `view` filter to include them, or set **Action type** to `view` to show only view actions.

View actions are always available through the Audit Logs v2 API and Logpush, regardless of the dashboard filter.

Caution

`GET` requests can generate a high volume of audit logs. When using the API or Logpush, apply appropriate filters to limit the volume of delivered logs.

For more information, refer to the [Audit Logs v2 documentation](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/#view-actions).

Oct 9, 2026

## [Improved HTTP/3 client cancellation reporting](https://developers.cloudflare.com/changelog/post/2026-10-09-http3-499-reporting-improvement/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare has improved how it handles and reports client-cancelled HTTP/3 requests across Free, Pro, Business, and Enterprise plans. Customers now get a clearer view of client behavior in Cloudflare analytics and, where available, logs.

Previously, Cloudflare did not always stop an HTTP/3 request when the client cancelled its request stream. Some cancellations were already recorded as `499`, while others continued to the origin and showed the eventual upstream status.

Cloudflare now stops affected requests sooner, reducing unnecessary origin work, and records them as `499`. Customers may notice more `499` status codes for HTTP/3 traffic. This reflects more consistent reporting of existing cancellations, not an increase in failed requests.

Customers who use `499` status codes in availability calculations should consider excluding them from server-side error rates because they represent requests cancelled by clients.

For more information, refer to [Error 499](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-499/).

Oct 9, 2026

## [More efficient Markdown for Agents conversion](https://developers.cloudflare.com/changelog/post/2026-10-09-markdown-for-agents-in-process-conversion/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

[Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) now converts HTML with an in-process streaming engine at the edge. It processes content as it arrives instead of buffering the HTML response and sending it to a separate conversion service. This reduces conversion overhead and memory use.

This release also changes the conversion limit and response headers:

  * Conversion supports up to 6 MiB (6,291,456 bytes) of decompressed HTML, increased from 2 MiB (2,097,152 bytes). The limit applies after decompression, not to the compressed response size.
  * Converted responses no longer generate the `x-markdown-tokens` or `x-original-tokens` headers. Clients that use these values need to calculate token counts themselves.
  * `Content-Length` is removed from converted responses rather than recalculated, because the Markdown body is streamed.



For more information, refer to the [Markdown for Agents documentation](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/).

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

Oct 7, 2026

## [Query Log Explorer datasets from Observability Logs](https://developers.cloudflare.com/changelog/post/2026-10-07-log-search-in-observability-logs/)

[Log Explorer](https://developers.cloudflare.com/observability/logs/log-explorer/)

Log Explorer datasets are now queried from the [Logs](https://developers.cloudflare.com/observability/logs/) page under **Observability** in the Cloudflare dashboard. The Logs page brings Log Explorer and Workers Observability datasets together with a shared filter builder, SQL editor, and visualizations.

As part of this change, the **Log Explorer** menu is no longer shown in the dashboard navigation.

  * Your enabled datasets, saved queries, and SQL queries continue to work on the Logs page.
  * To manage datasets, open the dataset selector on the Logs page and select **Configure** next to the Log Explorer datasets.
  * The previous Log Search page remains available at its direct URL.



For more information, refer to [Log Search](https://developers.cloudflare.com/observability/logs/log-explorer/log-search/) and the [Logs overview](https://developers.cloudflare.com/observability/logs/).

Oct 7, 2026

## [Cloudflare Organizations is generally available](https://developers.cloudflare.com/changelog/post/2026-10-07-organizations-generally-available/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

Cloudflare Organizations is now generally available for Enterprise customers and MSSP/Distributor partners.

Organizations provides a top-level container for centrally managing accounts, members, analytics, and shared policies. Organization Super Administrators receive implicit access to every account in their Organization without requiring separate account memberships.

Enterprise customers can manage accounts in a single-tier Organization. MSSP/Distributor partners can use nested sub-organizations to manage customer accounts.

Organization Roles remains in beta, and current product limitations still apply.

For more information, refer to [Cloudflare Organizations](https://developers.cloudflare.com/fundamentals/organizations/) and [current limitations](https://developers.cloudflare.com/fundamentals/organizations/limitations/).

Oct 2, 2026

## [30 days of analytics data on every plan](https://developers.cloudflare.com/changelog/post/2026-10-02-30-days-analytics-on-every-plan/)

[Analytics](https://developers.cloudflare.com/analytics/)

Every plan now gets at least 30 days of analytics data. Adaptive analytics datasets, such as HTTP requests, security events, and DNS analytics, retain at least 31 days of data for Free and Pro domains, and you can query up to 30 days in a single request. Previously, Free and Pro domains could see between 24 hours and 8 days of history depending on the dataset.

A full month of history lets you investigate an issue after it happens, compare today with the same day in previous weeks, and tell a one-time spike from a longer trend. The change applies in the Cloudflare dashboard, in [Custom Dashboards](https://developers.cloudflare.com/analytics/custom-dashboards/), and through the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/).

Domain analytics also now live in one place. In the Cloudflare dashboard, select a domain and go to **Analytics** to see Traffic, Performance, Security, Cache, Origin, DNS, and Visitors as tabs that share one time range and one set of filters. Account-level analytics are under **Observability** > **Analytics**.

This change does not alter which datasets or fields your plan can access. Aggregated datasets, such as `httpRequests1hGroups`, keep their existing per-plan limits. To check the exact retention and query window for a zone or account, query the [settings](https://developers.cloudflare.com/analytics/graphql-api/features/discovery/settings/) for each dataset.

For plan-specific limits, refer to [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/#availability), [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/#availability), and [GraphQL Analytics API limits](https://developers.cloudflare.com/analytics/graphql-api/limits/#node-limits-and-availability).

Oct 2, 2026

## [Workers Observability logs and traces in Custom Dashboards](https://developers.cloudflare.com/changelog/post/2026-10-02-workers-observability-in-custom-dashboards/)

[Analytics](https://developers.cloudflare.com/analytics/)

You can now build Custom Dashboards charts from Workers Observability data. Two new datasets, **Workers Observability — Logs** and **Workers Observability — Traces (OTel)** , let you chart Worker invocations, log levels, errors, CPU and wall time, span counts, and durations next to HTTP traffic, security events, and other analytics datasets.

This gives you one dashboard for an application that spans Cloudflare's network and your Workers. For example, you can put request volume, WAF blocks, and Worker error rates on the same view, filter all three by time range, and spot whether a spike in errors lines up with a change in traffic.

The datasets are available for every Worker in your account that has [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) or [Workers Traces](https://developers.cloudflare.com/workers/observability/traces/) turned on. Custom Dashboards also now allow up to 100 dashboards for every account.

To get started, refer to [Workers Observability data in Custom Dashboards](https://developers.cloudflare.com/analytics/custom-dashboards/#workers-observability-data).

Oct 2, 2026

## [Organizations support increased account and zone limits](https://developers.cloudflare.com/changelog/post/2026-10-02-organization-account-zone-limits/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

Cloudflare Organizations now support up to **20,000 accounts** and **200,000 zones**. For MSSP/Distributors using sub-organizations, these limits are applied at the root Organization.

If you require a higher limit, reach out to your account team. The new limits apply to enterprise and MSSP/Distributor Organizations. Legacy reseller partner and brand partner tenants retain their existing quota behavior.

For more information, refer to [Account and zone limits](https://developers.cloudflare.com/fundamentals/organizations/limitations/#account-and-zone-limits).

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

Oct 2, 2026

## [Protect Quick Tunnels with email authentication](https://developers.cloudflare.com/changelog/post/2026-10-02-protected-quick-tunnels/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)

You can now restrict who can access a [Quick Tunnel](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/). Use the new `--allowed-mail` flag in `cloudflared` to require visitors to authenticate with a one-time PIN sent to their email before they reach your local service.
    
    
    cloudflared tunnel --url http://localhost:8080 --allowed-mail alice@example.com

![Protected Quick Tunnel demo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1512,height=854,format=webp/_astro/protected-quick-tunnels.DlA306r_.gif)

Previously, anyone with a `trycloudflare.com` URL could access the service behind it. Protected Quick Tunnels let you share a local development server, webhook receiver, or demo with specific people without creating a Cloudflare account or configuring a domain.

You can allow:

  * A single email address: `--allowed-mail alice@example.com`
  * Multiple email addresses, by repeating the flag or using a comma-separated list: `--allowed-mail 'alice@example.com,bob@example.com'`
  * Every address on a domain: `--allowed-mail '*@example.com'`



Visitors do not need a Cloudflare account. Access ends for everyone when you stop the `cloudflared` process.

To get started, [update `cloudflared`](https://developers.cloudflare.com/tunnel/downloads/) to the latest version and refer to [Restrict access by email](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/#restrict-access-by-email).

Oct 1, 2026

## [Account members can self-serve create Account API tokens](https://developers.cloudflare.com/changelog/post/2026-10-01-account-api-token-provisioning/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Account API token creation is no longer limited to Super Administrators. Members with the **API Token Provisioning** role can now create Account API tokens via the Dashboard, API, Terraform, or CF CLI, making it easier for developers and platform teams to provision credentials without depending on a Super Administrator for Account API Token Provisioning.

![Creating an Account API Token via CF CLI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1540,height=818,format=webp/_astro/2026-10-01-account-api-token-provisioning.Dn0G5DUa.png)

#### What's new

  * **Delegated creation** : Members with the **API Token Provisioning** role can create Account API tokens from the dashboard. Administrators can grant this role through the dashboard, API, or Terraform.
  * **OAuth support for token creation** : OAuth clients that request the `account_api_tokens:create` scope, starting with Cloudflare CLI, can create Account API tokens.
  * **Account API token permissions limited to the creator’s access at creation time** : Members can only create an Account API Token using the permissions they already have. For OAuth-created tokens, permissions are also limited to the scopes granted during authorization.
  * **Creator attribution and visibility** : Account API tokens now include creator metadata. Super Administrators and Administrators can view all Account API tokens in an account, while members with the **API Token Provisioning** role can only view tokens they created.



For more information, refer to [Account API tokens](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/), [Create tokens via API](https://developers.cloudflare.com/fundamentals/api/how-to/create-via-api/), and [Roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/).

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

## [Logpush is now available on all plans with usage-based pricing](https://developers.cloudflare.com/changelog/post/2026-09-30-logpush-usage-based-pricing/)

[Logpush](https://developers.cloudflare.com/logs/logpush/)[Logs](https://developers.cloudflare.com/logs/)

Cloudflare Logpush is now available on Free, Pro, Business, and Enterprise plans with usage-based pricing. Free, Pro, and Business customers can enable Logpush through self-service. Enterprise customers continue to work with their account team. Logpush Transformers are also now generally available.

Each account receives included monthly usage before charges apply:

  * **Internal exports** : 25 GB per month, then $0.03 per additional GB.
  * **External exports** : 25 GB per month, then $0.10 per additional GB.
  * **Transformations** : 1 GB per month, then $0.04 per additional GB.



R2 and Pipelines use the internal destination rate. All other destinations use the external destination rate.

Existing Enterprise contracts retain their current Logpush pricing through renewal. Workers Logpush for Workers Trace Events retains request-based pricing, and OpenTelemetry destinations retain event-based Workers Observability pricing.

For complete rates, measurement details, and billing examples, refer to [Logpush pricing](https://developers.cloudflare.com/logs/logpush/pricing/).

Sep 30, 2026

## [Transformers are now generally available](https://developers.cloudflare.com/changelog/post/2026-09-30-transformers-ga/)

[Logpush](https://developers.cloudflare.com/logs/logpush/)[Logs](https://developers.cloudflare.com/logs/)

Transformers are now generally available for supported Logpush datasets on Free, Pro, Business, and Enterprise plans. Use SQL to filter records, reshape fields, redact sensitive values, compute new fields, or add metadata before Logpush delivers each batch.

Create and preview Transformers in Transformer Studio or through the Cloudflare API, then attach them to eligible account-scoped or zone-scoped Logpush jobs that use NDJSON output. Cloudflare validates each query against the dataset schema before saving it.

Each account includes 1 GB of transformation input per month. Additional input costs $0.04 per GB. For setup instructions, supported SQL, limits, and examples, refer to [Transformers](https://developers.cloudflare.com/logs/logpush/transformers/). For billing details, refer to [Logpush pricing](https://developers.cloudflare.com/logs/logpush/pricing/).

Sep 30, 2026

## [Monetization Gateway closed beta](https://developers.cloudflare.com/changelog/post/2026-09-30-closed-beta/)

[Monetization Gateway](https://developers.cloudflare.com/monetization-gateway/)

Monetization Gateway is now available in closed beta. Sellers can use it to charge agents for access to APIs, Model Context Protocol (MCP) tools, sites, and datasets.

Sellers (domain owners) define which requests require payment, the cost, and where the payment should be sent. Buyers receive the payment instructions, sign an authorization, and receive the resource after the payment has been settled. The Monetization Gateway uses the x402 protocol to handle payment authorization within the HTTP request flow.

To learn more, request access in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/monetize/monetization-gateway), review the [Monetization Gateway documentation](https://developers.cloudflare.com/monetization-gateway/), or read the [blog ↗︎](https://blog.cloudflare.com/monetization-gateway-beta/).

Sep 30, 2026

## [Longer rule descriptions in logs](https://developers.cloudflare.com/changelog/post/2026-09-30-longer-rule-descriptions-in-logs/)

[Rules](https://developers.cloudflare.com/rules/)

Cloudflare logs now include up to 128 bytes of a rule description, increased from 80 bytes. Longer descriptions provide more context when investigating matched rules and make it easier to identify the relevant rule without referring back to its configuration.

Descriptions longer than 128 bytes are truncated without splitting a UTF-8 character. This change does not affect the Rulesets API, which continues to accept rule descriptions of up to 4,096 bytes.

For more information, refer to [Rule object structure and properties](https://developers.cloudflare.com/ruleset-engine/rulesets-api/json-object/#rule-object-structure-and-properties).

Sep 29, 2026

## [Identify Mesh, Workers VPC, and Cloudflare Tunnel replicas in network logs](https://developers.cloudflare.com/changelog/post/2026-09-29-mesh-workers-vpc-network-logs/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

You can now tell a person on a laptop apart from a Mesh node or an AI agent running on Workers, without matching on connector email addresses or Mesh IP ranges — and see exactly which Cloudflare Tunnel and `cloudflared` replica received each session.

[Gateway network logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#network-logs) and [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/) now identify two new kinds of traffic:

  * **Mesh** — Traffic sent from or delivered to a [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) node. Previously, Mesh nodes were logged the same way as devices running the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/), because Mesh nodes run the client in headless mode.
  * **Workers VPC** — Traffic sent by a Worker through a [Workers VPC](https://developers.cloudflare.com/workers-vpc/) binding. Previously, Workers VPC sessions were not recorded in Network Session Logs.

![Viewing Mesh and Workers VPC traffic in Gateway network logs](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1439,height=796,format=webp/_astro/2026-09-28-mesh-workers-vpc-network-logs.iGvLKYk7.gif)

#### Gateway network logs

To view these values in the dashboard, go to **Zero Trust** > **Insights & Logs** > **Logs** > **Network logs** , select **Columns** , and turn on **Traffic Source** and **Traffic Destination**. Both values also appear under **Network query details** when you open a log entry.

#### Network Session Logs

The `zero_trust_network_sessions` dataset, available through [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/), includes the following fields:

Field | Description  
---|---  
`OnrampType` | How the session entered Cloudflare One. Values: `CF1_CLIENT`, `MESH`, `WORKERS_VPC`, `MAGIC`, `OTHER`.  
`Offramp` | Where the session was routed. Sessions routed to a Mesh node report `MESH`.  
`SourceName` | Name of the Worker that started the session. Only populated for Workers VPC sessions.  
`SourceID` | Stable identifier of the Worker that started the session. Only populated for Workers VPC sessions.  
`DestinationReplicaID` | The replica that served the session, such as a specific replica of a Mesh node or a `cloudflared` replica of a Cloudflare Tunnel.  
  
For example, `OnrampType = 'WORKERS_VPC' AND Offramp = 'MESH'` returns every session where a Worker reached a service behind a Mesh node, and `SourceName` tells you which Worker it was.

Redeploy your Workers

`SourceName` and `SourceID` are only populated for Workers deployed after 29 September 2026. To include them for an existing Worker, redeploy it — for example, with `npx wrangler deploy`. No code changes are required.

#### See which tunnel and replica received a session

With `DestinationReplicaID`, you can now confirm which [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and which `cloudflared` replica received traffic for a specific session. Combine it with the existing `DestinationTunnelID` field to trace a session to an exact tunnel replica — or Mesh node replica — when you run multiple replicas for high availability. The replica ID matches the **Connector ID** shown in the dashboard, so you can [stream that replica's logs](https://developers.cloudflare.com/tunnel/observability/#remote-log-streaming) with `cloudflared tail --connector-id`.

Sessions logged before this change are not backfilled. For all available fields, refer to [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/).

Sep 28, 2026

## [Cloudflare CLI is now in beta](https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/)

[Workers](https://developers.cloudflare.com/workers/)[Cloudflare CLI](https://developers.cloudflare.com/cf/)

The [Cloudflare CLI](https://developers.cloudflare.com/cf/), `cf`, is now in beta. `cf` is one command-line interface for the public Cloudflare API and for Workers projects. Use it to manage zones, DNS, storage, and security settings, and to create, develop, and deploy Workers, without switching between tools.

Install `cf` globally, then sign in:

npmyarnpnpmbun
    
    
    npm install --global cf
    
    
    yarn global add cf
    
    
    pnpm add --global cf
    
    
    bun add --global cf
    
    
    cf auth login

With `cf`, you can:

  * **Manage resources across Cloudflare.** More than 2,900 commands cover the public Cloudflare API, and most print their results as JSON.
  * **Create and deploy Workers.** `cf init` creates a project that uses [`cloudflare.config.ts`](https://developers.cloudflare.com/cf/projects/cloudflare-config/), a typed configuration file. `cf dev`, `cf build`, and `cf deploy` develop, build, and deploy it.
  * **Move from Wrangler.** `cf migrate` converts a Wrangler configuration file to `cloudflare.config.ts`. You can also run `cf` resource commands in an existing Wrangler project without migrating it.
  * **Work with coding agents.** `cf cli search` finds the command for a task from a plain-language description, so an agent can find and run commands without prior knowledge of `cf`.



`cf` is in beta. Commands, configuration, and Build Output can change before the stable release.

To get started, refer to [Install and sign in](https://developers.cloudflare.com/cf/get-started/). To move an existing project, refer to [Migrate a Wrangler project](https://developers.cloudflare.com/cf/wrangler/migrate/).

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

← Prev

1[2](https://developers.cloudflare.com/changelog/product-group/core-platform/2/)…[9](https://developers.cloudflare.com/changelog/product-group/core-platform/9/)

[Next →](https://developers.cloudflare.com/changelog/product-group/core-platform/2/)
