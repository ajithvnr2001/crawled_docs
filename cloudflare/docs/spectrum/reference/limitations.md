---
url: https://developers.cloudflare.com/spectrum/reference/limitations/
title: Limitations \u00b7 Cloudflare Spectrum docs
method: scrapling+scrapegraph
fetched_at: 2026-10-29T08:14:03.983588+00:00
---

# Limitations · Cloudflare Spectrum docs

> Source: https://developers.cloudflare.com/spectrum/reference/limitations/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Spectrum](https://developers.cloudflare.com/spectrum/)
  3. /Reference
  4. /Limitations



# Limitations

Last updated Oct 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIPv4 hostname quotaHTTPSUDPMinecraftUniversal SSLPrivate Network Load BalancingCloudflare TunnelListen on ports configurationIP access control

The following limitations apply to Spectrum applications.

## IPv4 hostname quota

By default, an account is limited to **10 unique Spectrum hostnames** using Cloudflare-managed IPv4 addresses, across all zones on the account. Each hostname is backed by a dedicated IPv4 address, and this quota is applied at the account level — not per zone.

IPv6-only Spectrum applications do not count against this quota.

If you need more than 10 IPv4-backed Spectrum hostnames, you can:

  * **Use[BYOIP](https://developers.cloudflare.com/spectrum/about/byoip/)** — bring your own IP space so Spectrum applications are not constrained by the default shared-IPv4 allocation.
  * **Use IPv6-only Spectrum applications** — IPv6 addresses are not subject to the same scarcity as IPv4.
  * **CNAME multiple subdomains to a single Spectrum application** — point several DNS-only (gray-clouded) `CNAME` records at one Spectrum application hostname. This works only when those hostnames share the same origin (one origin per application).
  * **Use[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)** — configure the Spectrum application as the target (fallback origin) for Custom Hostnames.



Contact your account team if you expect to exceed the quota.

## HTTPS

At the moment, HTTPS applications do not support HTTP/3.

## UDP

Cloudflare does not support packet fragmentation for UDP packets. If packets are fragmented, they will be dropped at Cloudflare’s edge.

Spectrum UDP applications are supported with [BYOIP](https://developers.cloudflare.com/spectrum/about/byoip/), including [CDN and Spectrum service bindings](https://developers.cloudflare.com/byoip/service-bindings/cdn-and-spectrum/). They are not currently supported with [Magic Transit service bindings](https://developers.cloudflare.com/byoip/service-bindings/).

## Minecraft

Minecraft Java Edition is supported but Minecraft Bedrock Edition is not supported.

## Universal SSL

[Universal SSL](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/) is not compatible with Cloudflare Spectrum. Use either an [advanced certificate](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/) or a [custom certificate](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/) instead.

## Private Network Load Balancing

When using [Spectrum](https://developers.cloudflare.com/load-balancing/private-network/#on-ramps) as an on-ramp into Private Network Load Balancing, the [proxy protocol](https://developers.cloudflare.com/spectrum/how-to/enable-proxy-protocol/) setting in Spectrum is not supported. This applies regardless of the [off-ramp](https://developers.cloudflare.com/load-balancing/private-network/) used to reach your private origin, including Cloudflare WAN and Cloudflare Tunnel.

## Cloudflare Tunnel

You can use [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) as a private origin for Spectrum TCP and UDP applications through a [virtual network](https://developers.cloudflare.com/cloudflare-one/networks/virtual-networks/). Spectrum routes traffic through the Cloudflare Tunnel connector associated with the virtual network.

The origin must be a single private IP address that is routable within the specified virtual network. Port ranges, hostname origins (`origin_dns`), and multiple addresses in `origin_direct` are not supported. [Proxy Protocol](https://developers.cloudflare.com/spectrum/how-to/enable-proxy-protocol/) is not supported, so `proxy_protocol` must be set to `off`.

For setup instructions, refer to [Create a Spectrum application using a virtual network origin](https://developers.cloudflare.com/spectrum/get-started/#create-a-spectrum-application-using-a-virtual-network-origin).

Alternative L4 routing

To route non-HTTP (TCP or UDP) traffic from a public Spectrum application to a private endpoint via Cloudflare Tunnel, you can also configure a [Cloudflare Load Balancer with Private Network Load Balancing (LTM)](https://developers.cloudflare.com/load-balancing/private-network/) in between.

By defining private IP addresses as origins inside your Load Balancer pool and associating them with your tunnel's Virtual Network ID (`virtual_network_id`), the Load Balancer receives the L4 traffic from Spectrum and routes it to your private origin over the Cloudflare Tunnel.

## Listen on ports configuration

By default, Spectrum is configured to listen on all ports, which can raise concerns for security auditors. However, it is important to note that Spectrum will only proxy connections from edge ports that are specifically configured within Cloudflare.

When a TCP handshake is initiated to any port for a Spectrum IP, the handshake will always be completed. If there is a Spectrum application configured for the port, the connection will be proxied to origin. If no application is configured, the connection is immediately terminated and no origin connection will be opened.

Spectrum will only ever proxy traffic to an origin if there is a Spectrum application configured for that port.

## IP access control

Currently, [custom rules](https://developers.cloudflare.com/waf/custom-rules/) do not work with Spectrum applications. Use [IP Access rules](https://developers.cloudflare.com/waf/tools/ip-access-rules/) to allowlist, block, and challenge traffic for Spectrum applications based on the request's IP address, Autonomous System Number (ASN), or country.

Refer to [Configuration options](https://developers.cloudflare.com/spectrum/reference/configuration-options/#ip-access-rules) for more information.

[PreviousEvent logs](https://developers.cloudflare.com/spectrum/reference/logs/)[NextSettings by plan](https://developers.cloudflare.com/spectrum/reference/settings-by-plan/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/spectrum/reference/limitations.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
