---
url: https://developers.cloudflare.com/changelog/product-group/cloudflare-one/
title: Cloudflare One Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:30.071049+00:00
---

# Cloudflare One Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product-group/cloudflare-one/

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

Oct 19, 2026

## [Cloud Workload Security is now available in Beta](https://developers.cloudflare.com/changelog/post/2026-10-19-cloud-workload-security-beta/)

[Cloud Workload Security](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/)

[Cloud Workload Security (CWS)](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/) is now available in Beta. Apply policy controls to cloud API requests before they reach your cloud provider.

Define policies with request filters and Rego checks. For example, block requests that would make an R2 bucket public. Use workloads and policy sets to target your cloud environments.

Manage your policies in the Cloudflare dashboard. Run the CWS proxy in your environment and route client requests through it to enforce your policies.

CWS requires a Zero Trust subscription. The Zero Trust Free plan is sufficient.

To configure your first guardrail, follow [Get started with Cloud Workload Security](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/get-started/).

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

Oct 15, 2026

## [Application Library now supports custom applications](https://developers.cloudflare.com/changelog/post/2026-10-15-app-library-custom-applications/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)

Starting today, you can create [custom applications](https://developers.cloudflare.com/cloudflare-one/team-and-resources/app-library/custom-applications/) in the [Application Library](https://developers.cloudflare.com/cloudflare-one/team-and-resources/app-library/) and reference them in Gateway DNS, Network, and HTTP policies. You can define an application with hostnames, IP subnets, or both. Then, optionally add TCP or UDP ports or port ranges to restrict HTTP and Network matching.

![Custom application form with a name, application ID, category, two hostnames, and a TCP port 443 constraint](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1928,height=1108,format=webp/_astro/custom-application-create.hLzR_NQZ.png)

This release also improves search and filtering in the Application Library, updates the interfaces, data, and metrics used to review applications, and makes it easier to select and manage applications in the Gateway policy builder.

![Gateway HTTP policy builder with a custom application selected in the Application selector under the Artificial Intelligence category](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1472,height=1324,format=webp/_astro/custom-application-gateway-policy-builder.DFnrNoHS.png)

For more information, refer to [Custom applications](https://developers.cloudflare.com/cloudflare-one/team-and-resources/app-library/custom-applications/) and [Applications and app types](https://developers.cloudflare.com/cloudflare-one/traffic-controls/application-app-types/).

Oct 15, 2026

## [Validate data loss prevention matches with Cloudflare Workers](https://developers.cloudflare.com/changelog/post/2026-10-15-dlp-custom-validation-workers/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Data loss prevention (DLP) custom pattern entries can use Cloudflare Workers in your account to validate matches with organization-specific logic. Your Worker can adjust a match's confidence or reject the match.

For setup steps and the Worker contract, refer to [Validate data loss prevention matches with Cloudflare Workers](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/custom-validation-workers/).

Oct 15, 2026

## [BGP route filtering for IPsec and GRE tunnels](https://developers.cloudflare.com/changelog/post/2026-10-15-bgp-filter-profiles/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Cloudflare WAN and Magic Transit IPsec and GRE tunnels now support BGP import and export filtering.

Create reusable filter profiles that specify an `allow` or `deny` action and a list of Classless Inter-Domain Routing (CIDR) targets with exact, more-specific, or prefix-length matching. Each tunnel supports one import filter and one export filter.

You can create and assign profiles through the dashboard, API, or Terraform. Profile changes apply without resetting the BGP session.

For configuration details, refer to:

  * [Filter BGP routes for Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#filter-bgp-routes)
  * [Filter BGP routes for Magic Transit](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#filter-bgp-routes)



Oct 15, 2026

## [Gateway and Workers integration is now in public beta](https://developers.cloudflare.com/changelog/post/2026-10-15-gateway-workers-public-beta/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Workers](https://developers.cloudflare.com/workers/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)

Cloudflare Gateway now integrates with Cloudflare Workers in public beta on all Zero Trust plans. You can use the **Forward** action in [Gateway HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-controls/http-policies/) to run your own code on matching, permitted traffic without managing a separate proxy.

The **Forward** action lets you transform HTTP requests and responses, return a coaching page, or run background tasks such as Slack notifications and R2 captures. Your Worker receives the request and [Gateway context](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/available-context/), including connection metadata, user identity, and device posture when available.

![A matching Gateway Forward policy sends HTTP traffic to a Worker, which processes requests and responses for Internet or private-network upstream services.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2048,height=1053,format=webp/_astro/gateway-workers-forward.CFUFJAE0.png)

Gateway handles the proxy connection, TLS decryption, and upstream routing. It evaluates HTTP request policies before Forward policies and inspects the final response before returning it to the user.

Gateway inspects the original request body before delivering it to your Worker. A body-inspection Block decision can interrupt the Worker.

To get started, [deploy a Worker and configure a Forward policy](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/forward-traffic/), or adapt one of the [Worker templates](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/).

Oct 14, 2026

## [Account context in Access deny redirects](https://developers.cloudflare.com/changelog/post/2026-10-14-deny-redirect-account-id/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

App-aware Cloudflare Access deny redirects include an `account_id` query parameter when account context is available. Custom block pages can use it to identify the account that owns the application represented by `kid`.

For example, a custom redirect can include:
    
    
    https://denied.example.com/?kid=<APP_AUD>&account_id=<ACCOUNT_ID>&original_url=app.example.com%2Fadmin

The account ID helps block-page integrations look up applications through account-scoped APIs. It is context, not proof of authentication or authorization.

For parameter descriptions and an example, refer to [Custom redirect URL parameters](https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/access-block-page/#custom-redirect-url-parameters).

Oct 14, 2026

## [Infrastructure applications support a configurable session duration](https://developers.cloudflare.com/changelog/post/2026-10-14-infrastructure-ssh-session-duration/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Infrastructure applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) now have a configurable session duration with a default value of 24 hours. You can set the session duration when creating or editing an infrastructure application in the dashboard or via the API.

![Session duration setting in infrastructure application configuration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2824,height=522,format=webp/_astro/infrastructure-ssh-session-duration.DI7ApX89.png)

When the session duration elapses, any active SSH connections through that application will be closed, and users will need to reconnect. Previously, infrastructure applications did not enforce a session duration limit. Sessions could persist beyond 24 hours in some cases, but were never guaranteed beyond 10 hours due to [Gateway connection limits](https://developers.cloudflare.com/cloudflare-one/access-controls/troubleshooting/#long-lived-ssh-sessions-disconnect).

When a target matches multiple infrastructure applications, the shortest session duration applies.

For more information, refer to [Session duration](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#session-duration).

Oct 13, 2026

## [Request Gateway DNS64 through DNS locations and EDNS](https://developers.cloudflare.com/changelog/post/2026-10-13-gateway-dns64-opt-in/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

You can now request DNS64 through Cloudflare Gateway DNS location settings or Extension Mechanisms for DNS (EDNS) options.

DNS64 synthesizes `AAAA` records from `A` records for IPv6-only networks. These networks require network address translation from IPv6 to IPv4 (NAT64).

Turn on **Enable DNS64** for a location, or include an empty EDNS option `65051` in individual queries. Both mechanisms support UDP, TCP, DNS over TLS (DoT), and DNS over HTTPS (DoH).

For example, request DNS64 through EDNS with `dig`:
    
    
    dig @"<DNS_RESOLVER_IP>" ipv4only.arpa AAAA +ednsopt=65051 +short

The existing `cf-dns-options: dns64` DoH header remains supported independently. DNS64 is off by default. Each mechanism independently requests synthesis.

For configuration, API update behavior, and request examples, refer to [DNS64](https://developers.cloudflare.com/cloudflare-one/traffic-controls/resolver-endpoints/dns64/).

Oct 12, 2026

## [Cloudflare One Client for Windows (version 2026.8.2110.0)](https://developers.cloudflare.com/changelog/post/2026-10-12-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves an issue where the client could repeatedly disconnect and reconnect when a split tunnel configuration with hostname-based entries failed to apply.

Oct 12, 2026

## [Cloudflare One Client for macOS (version 2026.8.2110.0)](https://developers.cloudflare.com/changelog/post/2026-10-12-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves an issue where the client could repeatedly disconnect and reconnect when a split tunnel configuration with hostname-based entries failed to apply.

Oct 12, 2026

## [Cloudflare One Client for Linux (version 2026.8.2110.0)](https://developers.cloudflare.com/changelog/post/2026-10-12-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves an issue where the client could repeatedly disconnect and reconnect when a split tunnel configuration with hostname-based entries failed to apply.

Oct 12, 2026

## [Unified dashboard navigation for Zero Trust](https://developers.cloudflare.com/changelog/post/2026-10-12-unified-dashboard-navigation/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

The Cloudflare dashboard now combines Zero Trust and main dashboard navigation. You can move between Cloudflare products from the same navigation.

All customers can browse Zero Trust products from the primary navigation.

Zero Trust customers can also access other services from this navigation. These include the developer platform, account memberships, and resource tagging.

As part of this change, the Zero Trust Network items were removed in favor of the new experiences available under _Networking_ navigation, and Resolvers & Proxies was moved under Traffic Controls (previously Traffic Policies).

This update is available to all customers starting today.

For more information, refer to the [Cloudflare One documentation](https://developers.cloudflare.com/cloudflare-one/).

Oct 7, 2026

## [Cloudflare One Client for macOS (version 2026.8.2100.0)](https://developers.cloudflare.com/changelog/post/2026-10-07-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release includes the following highlights:

  * Traffic to split tunnel excluded resources is no longer briefly blocked while the client is connecting or reconnecting. The client now keeps its learned split tunnel configuration across reconnects.
  * Support for routing non-RFC 1918 local IPv4 networks through the tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Faster connects and lower memory use. The hosts file is now read once and shared across the client’s DNS resolvers instead of being reloaded by each one.



**Additional changes and improvements**

  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Individual DNS-over-HTTPS queries now time out instead of hanging when the upstream server stops responding.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Added an MDM setting to prefer IPv4 when resolving hostnames in proxy mode. The setting is off by default.
  * Fixed the client reconnecting while Emergency Disconnect was active after switching organizations or re-registering.
  * Fixed the client being unable to connect after an upgrade when its stored registration credentials no longer matched its configuration.
  * Fixed the client service restarting unexpectedly when it was slow to respond, such as after waking from sleep.
  * Fixed Extra Logging failing to capture packets across all interfaces.
  * Fixed an issue that could prevent remote diagnostics from completing.
  * Fixed DNS connectivity checks failing on IPv6-only networks.
  * Fixed the client service exiting when its route-monitoring socket was closed after sleep or wake.
  * Fixed DNS enforcement checks making the client service unresponsive on systems with large routing tables.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report “No network” after a successful manual disconnect.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



Oct 7, 2026

## [Cloudflare One Client for Windows (version 2026.8.2100.0)](https://developers.cloudflare.com/changelog/post/2026-10-07-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release includes the following highlights:

  * Traffic to split tunnel excluded resources is no longer briefly blocked while the client is connecting or reconnecting. The client now keeps its learned split tunnel configuration across tunnel reconnections.
  * Support for routing non-RFC 1918 local IPv4 networks through the tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved connection reliability on devices with very large hosts files. The client now detects a large hosts file, allows more time for its initial DNS check, and shows a banner letting the user know that connecting may take longer.
  * Faster tunnel reconnections and lower memory use. The hosts file is now read once and shared across the client’s DNS resolvers instead of being reloaded by each one.
  * A service recovery mechanism, backed by a Windows scheduled task, now starts the client service on system unlock if it is not already running. This is enabled by default.



**Additional changes and improvements**

  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Individual DNS-over-HTTPS queries now time out instead of hanging when the upstream server stops responding.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Added an MDM setting to prefer IPv4 when resolving hostnames in proxy mode. The setting is off by default.
  * The client no longer requires the Windows WLAN AutoConfig service to be running.
  * Fixed the client reconnecting while Emergency Disconnect was active after switching organizations or re-registering.
  * Fixed the client being unable to connect after an upgrade when its stored registration credentials no longer matched its configuration.
  * Fixed the client service restarting unexpectedly when it was slow to respond, such as after waking from sleep.
  * Fixed the client service failing to restart after an unexpected termination.
  * Fixed the client UI getting stuck in a connecting state after sleep and wake even though the tunnel was connected.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report “No network” after a successful manual disconnect.
  * Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation.
  * Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
  * Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
  * Fixed the client UI crashing at startup when it could not write to the Windows registry.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * A Windows DNS client regression may cause connectivity check failures on systems containing large hosts files. While this release includes a fix to mitigate this issue, users may still experience reduced DNS performance and connectivity check failures.



Oct 7, 2026

## [Cloudflare One Client for Linux (version 2026.8.2100.0)](https://developers.cloudflare.com/changelog/post/2026-10-07-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release includes the following highlights:

  * Traffic to split tunnel excluded resources is no longer briefly blocked while the client is connecting or reconnecting. The client now keeps its learned split tunnel configuration across reconnects.
  * Support for routing non-RFC 1918 local IPv4 networks through the tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Faster tunnel reconnections and lower memory use. The hosts file is now read once and shared across the client’s DNS resolvers instead of being reloaded by each one.
  * Added an MDM setting to prefer IPv4 when resolving hostnames in proxy mode. The setting is off by default.



**Additional changes and improvements**

  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Individual DNS-over-HTTPS queries now time out instead of hanging when the upstream server stops responding.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Fixed the client reconnecting while Emergency Disconnect was active after switching organizations or re-registering.
  * Fixed the client being unable to connect after an upgrade when its stored registration credentials no longer matched its configuration.
  * Fixed the client service restarting unexpectedly when it was slow to respond, such as after waking from sleep.
  * Fixed the client window not appearing on first launch after a fresh install on RHEL 10.
  * Fixed duplicate WARP routing policy rules accumulating on reconnect.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report “No network” after a successful manual disconnect.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * When in DNS Only mode, the client may send DNS queries for names that are configured for Local Domain Fallback to the encrypted DNS server instead of falling back to the system configuration. Local Domain Fallback works as expected in other client modes.



Oct 7, 2026

## [Cloudflare Organizations is generally available](https://developers.cloudflare.com/changelog/post/2026-10-07-organizations-generally-available/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

Cloudflare Organizations is now generally available for Enterprise customers and MSSP/Distributor partners.

Organizations provides a top-level container for centrally managing accounts, members, analytics, and shared policies. Organization Super Administrators receive implicit access to every account in their Organization without requiring separate account memberships.

Enterprise customers can manage accounts in a single-tier Organization. MSSP/Distributor partners can use nested sub-organizations to manage customer accounts.

Organization Roles remains in beta, and current product limitations still apply.

For more information, refer to [Cloudflare Organizations](https://developers.cloudflare.com/fundamentals/organizations/) and [current limitations](https://developers.cloudflare.com/fundamentals/organizations/limitations/).

Oct 5, 2026

## [Detect organization-specific risks with CASB custom finding types](https://developers.cloudflare.com/changelog/post/2026-10-05-casb-custom-findings/)

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

[Cloudflare CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) now supports [**custom finding types**](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/custom-finding-types/), giving security teams full control over the security conditions CASB detects across their SaaS and cloud integrations.

In addition to CASB's library of standard finding types, you can now write your own detection logic using [Rego ↗︎](https://www.openpolicyagent.org/docs/policy-language), the open-source policy language from Open Policy Agent (OPA). Use custom finding types to match your organization's own thresholds and exceptions, such as flagging admin accounts without two-factor authentication, and get higher-confidence findings to act on.

![Create a custom finding type with a name, severity, scope, and Rego detection logic](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1194,height=1194,format=webp/_astro/create-custom-finding-type.CF3GXoPZ.png)

#### Key capabilities

  * **Write your own detection logic** — Define exactly what CASB flags using Rego expressions evaluated against asset data from your connected integrations.
  * **Target any supported provider and asset class** — Scope a custom finding type to a provider (such as Google Workspace or Microsoft 365) and asset class (such as users, files, or groups), and apply it to all integrations for that provider or a selected subset.
  * **Built-in validation** — Select **Validate** to check your expression for syntax errors and schema issues before you create the finding type.
  * **Inspect and duplicate standard finding types** — Open any standard finding type to view its detection logic, then duplicate it as the starting point for a custom finding type.
  * **Works with CASB policies** — Use custom finding types in [CASB remediation policies](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/) to send matching findings to Slack, ServiceNow, or any other webhook destination.



#### Get started

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com), go to **Cloud & SaaS findings** > **Findings library**.
  2. Select **Create finding**.
  3. Enter a name, description, and severity.
  4. Select a provider and asset class, then set the integration scope.
  5. Write your Rego expression and select **Validate**.
  6. Select **Create finding**.



CASB evaluates the custom finding type against assets as they are created or updated within the selected scope. Matching assets appear as posture finding instances under **Posture Findings**.

#### Learn more

  * Learn how to [create and manage custom finding types](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/custom-finding-types/) in Cloudflare One.
  * Learn how to [manage findings](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/) in Cloudflare One.
  * Learn how to [create and manage CASB remediation policies](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/) in Cloudflare One.



CASB custom finding types are now available in Cloudflare One.

Oct 5, 2026

## [BGP over IPsec and GRE tunnels generally available](https://developers.cloudflare.com/changelog/post/2026-10-05-bgp-over-tunnels-ga/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

BGP peering over IPsec and GRE tunnels is generally available for Cloudflare WAN and Magic Transit. You can use it for production workloads.

BGP peering exchanges routes dynamically between your devices and your Cloudflare virtual network routing table. You no longer need to update static routes manually as your network changes.

BGP over IPsec and GRE tunnels is available to all accounts that use [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing). No enablement is required. BGP over CNI remains in closed beta.

For configuration details, refer to:

  * [Configure BGP routes for Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes)
  * [Configure BGP routes for Magic Transit](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#configure-bgp-routes)



Oct 2, 2026

## [New strict service token authentication setting for Access](https://developers.cloudflare.com/changelog/post/2026-10-02-strict-service-token-authentication/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

The strict service token authentication setting applies consistent behavior to requests made with service tokens. When the setting is on for a Zero Trust organization, Access handles requests with service token headers as follows:

  * If authentication or authorization fails, Access always returns `401` or `403` instead of redirecting the client to the login page with `302`.
  * Only Service Auth policies can authorize the request. Access ignores Allow policies and any `CF_Authorization` cookie sent with the request.
  * Access does not return a `CF_Authorization` cookie to the client after successful authentication. Subsequent requests should continue to use service token headers.
  * Failed requests for recognized service tokens appear in [Access authentication logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/#non-identity-authentication).



Zero Trust organizations created on or after October 5, 2026 have strict service token authentication turned on by default and cannot turn it off. Cloudflare recommends that existing organizations turn it on as well.

Organizations created before October 5, 2026 can configure the setting in the dashboard or through the API.

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Access settings**.

[ Go to **Access settings** ↗ ](https://one.dash.cloudflare.com/?to=/:account/access-controls/settings)
  2. Under **Manage service tokens** , turn on **Strict service token authentication**.

  3. In the confirmation dialog, select **Enable**.




To turn off strict service token authentication, turn off the setting and select **Disable**.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/access/organizations" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"strict_service_token_auth": true
    	}'

To turn off strict service token authentication, set `strict_service_token_auth` to `false`.

For behavior and configuration details, refer to [Strict service token authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#strict-service-token-authentication).

Oct 1, 2026

## [Simplified permissions for tagging targets with Access for Infrastructure](https://developers.cloudflare.com/changelog/post/2026-10-01-infrastructure-target-tag-permissions/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

You can now tag [targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#tag-targets) using only the `Zero Trust Write` API token permission. Previously, tagging targets through the API required both `Zero Trust Write` and `Tag Write` permissions on the API token.

This change applies to inline target tagging through the [Infrastructure Access Targets API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/). Tagging resources through the general [Resource Tagging API](https://developers.cloudflare.com/resource-tagging/) still requires the `Tag Admin`, `Tag Write`, or equivalent role.

For more information, refer to [Tag targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#tag-targets).

Sep 30, 2026

## [Cloudflare One Client for Windows (version 2026.8.2033.1)](https://developers.cloudflare.com/changelog/post/2026-09-30-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * The client no longer requires the Windows WLAN AutoConfig service to be running.
  * Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report 'No network' after a successful manual disconnect.
  * Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.
  * Fixed the client UI crashing at startup when it could not write to the Windows registry.
  * Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
  * Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



For Zero Trust documentation, see: <https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/> For Consumer documentation, see: <https://developers.cloudflare.com/warp-client/>

Sep 30, 2026

## [Role-based access control for Browser Isolation policies](https://developers.cloudflare.com/changelog/post/2026-09-30-browser-isolation-rbac/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Isolation policies](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/) support role-based access control (RBAC). Because isolation policies are Gateway HTTP policies with the _Isolate_ action, Gateway's account-level and resource-scoped roles apply to them directly.

Use the `Zero Trust HTTP Policies Admin` account-level role to grant access to all HTTP policies in the account. You can also assign a [resource-scoped role](https://developers.cloudflare.com/cloudflare-one/traffic-controls/granular-permissions/) to let a team member manage a specific isolation policy without exposing other Gateway resources.

[Policy settings](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/#policy-settings) such as copy/paste, file download/upload, keyboard, and printing are part of the policy object and follow the same permissions.

For setup instructions, refer to [Granular permissions for Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-controls/granular-permissions/).

Sep 29, 2026

## [Cloudflare One Client for Windows (version 2026.8.2028.1)](https://developers.cloudflare.com/changelog/post/2026-09-29-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * The client no longer requires the Windows WLAN AutoConfig service to be running.
  * Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report 'No network' after a successful manual disconnect.
  * Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.
  * Fixed the client UI crashing at startup when it could not write to the Windows registry.
  * Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
  * Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



Sep 29, 2026

## [Cloudflare One Client for macOS (version 2026.8.2028.1)](https://developers.cloudflare.com/changelog/post/2026-09-29-warp-macos-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the macOS Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Fixed Extra Logging failing to capture packets across all interfaces.
  * Fixed an issue that could prevent remote diagnostics from completing.
  * Fixed DNS connectivity checks failing on IPv6-only networks.
  * Fixed the client service exiting when its route-monitoring socket was closed after sleep or wake.
  * Fixed DNS enforcement checks making the client service unresponsive on systems with large routing tables.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report 'No network' after a successful manual disconnect.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



← Prev

1[2](https://developers.cloudflare.com/changelog/product-group/cloudflare-one/2/)…[14](https://developers.cloudflare.com/changelog/product-group/cloudflare-one/14/)

[Next →](https://developers.cloudflare.com/changelog/product-group/cloudflare-one/2/)
