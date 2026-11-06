---
url: https://developers.cloudflare.com/dns/private-origins/troubleshooting/
title: Troubleshooting \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-11-06T09:03:47.250985+00:00
---

# Troubleshooting · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/private-origins/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /[Private origins](https://developers.cloudflare.com/dns/private-origins/)
  4. /Troubleshooting



# Troubleshooting

Last updated Nov 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOrder of checksError 1002: DNS points to prohibited IPSetting seems off but traffic routes through tunnelTraffic not reaching originTimeouts with no response from the originLarge responses hang or stallCacheable assets return 403525 or 526 errorsOrigin sees public Cloudflare IPs as the sourcePackets reach the origin but no response returnsTunnel shows IKE established but health checks failTraffic tries to route over the public Internet

## Order of checks

Work through these in order:

  1. Public side: DNS, TLS, WAF, and other proxied features.
  2. Cloudflare to your private network: private network routing is on, and the route to the origin is in your default virtual network.
  3. Your connectivity: tunnel or connector health, and routes.
  4. Your network: routing, firewall rules, return path, and MSS clamp.



## Error 1002: DNS points to prohibited IP

This error occurs when you proxy a private IP address and your account does not have the Private Origins entitlement. Contact your account team to enable it.

## Setting seems off but traffic routes through tunnel

Check for other records on the same name.

Private network routing applies per name, not per record. If you have multiple `A` or `AAAA` records on the same name and at least one of them has private network routing enabled, all records on that name will use private network routing.

## Traffic not reaching origin

If traffic is not reaching your private origin:

  1. Verify your connection is healthy: IPsec, GRE, or CNI tunnel health for Cloudflare WAN, tunnel status for Cloudflare Tunnel, or node status for Cloudflare Mesh.
  2. Confirm the route to the origin is in your default virtual network.
  3. Confirm the origin IP is routable within your private network.
  4. Check that `private_routing` is set to `true` on the DNS record.
  5. Verify the record has proxy status enabled.



## Timeouts with no response from the origin

Applies to Cloudflare WAN and Cloudflare Mesh. Check both:

  * The Cloudflare source IP range is set to a private `/12`, not a public range.
  * Your network has return routes that send the Cloudflare source ranges (`100.64.0.0/12` or your configured `/12`, and `2606:4700:cf1:5000::/64`) back through your Cloudflare connection.



Refer to [Cloudflare source IP ranges](https://developers.cloudflare.com/dns/private-origins/private-network-routing/#cloudflare-source-ip-ranges).

## Large responses hang or stall

On IPsec tunnels, the MSS clamp is missing or above `1360`. Set the TCP MSS clamp on your tunnels to `1360` or lower.

## Cacheable assets return 403

Known issue with Tiered Cache when the origin is reached over Cloudflare WAN. As a workaround, create a [Cache Rule](https://developers.cloudflare.com/cache/how-to/cache-rules/) that bypasses cache for the affected hostnames. Refer to [Limitations](https://developers.cloudflare.com/dns/private-origins/#limitations).

## 525 or 526 errors

The origin certificate does not match the hostname, or the private CA is not in the Custom Origin Trust Store. Verify the certificate served by the origin and the trust store configuration.

## Origin sees public Cloudflare IPs as the source

The account is on legacy routing. Request Unified Routing through your account team.

## Packets reach the origin but no response returns

An asymmetric return path or a stateful firewall drop. Make sure return traffic goes back through the same connection Cloudflare used to reach the origin.

## Tunnel shows IKE established but health checks fail

ICMP is blocked on the path or the health check is misconfigured. Allow ICMP between the tunnel endpoints and confirm the health check direction is `bidirectional` and type is `reply`.

## Traffic tries to route over the public Internet

The **Use private network routing** toggle is not turned on for the DNS record. Edit the record and turn the toggle on. Refer to [Private network routing](https://developers.cloudflare.com/dns/private-origins/private-network-routing/) for dashboard and API steps.

[PreviousPrivate network routing](https://developers.cloudflare.com/dns/private-origins/private-network-routing/)[NextOverview](https://developers.cloudflare.com/dns/internal-dns/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/private-origins/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
