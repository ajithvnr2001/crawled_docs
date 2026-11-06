---
url: https://developers.cloudflare.com/dns/private-origins/private-network-routing/
title: Private network routing \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-11-06T09:03:45.511746+00:00
---

# Private network routing · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/private-origins/private-network-routing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /[Private origins](https://developers.cloudflare.com/dns/private-origins/)
  4. /Private network routing



# Private network routing

Last updated Nov 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAspects to considerAutomatically detected rangesCloudflare source IP rangesEnable private network routing API field behavior

Private network routing allows you to proxy HTTP/HTTPS traffic from public hostnames to origins in your private network. When you enable this setting on a DNS record, Cloudflare reaches the origin over your private network connectivity instead of the public Internet.

For end-to-end setup, refer to the guide for your connectivity type: [Cloudflare WAN](https://developers.cloudflare.com/dns/private-origins/set-up-via-cloudflare-wan/), [Cloudflare Tunnel](https://developers.cloudflare.com/dns/private-origins/set-up-via-cloudflare-tunnel/), or [Cloudflare Mesh](https://developers.cloudflare.com/dns/private-origins/set-up-via-cloudflare-mesh/).

## Aspects to consider

Before you enable private network routing, consider the following:

  * Private Origins needs to be available on your account and you need a working connection to your private network through Cloudflare WAN (IPsec, GRE, or CNI), Cloudflare Tunnel, or Cloudflare Mesh. The route to the origin must be in your default virtual network.
  * If you connect over Cloudflare WAN or Cloudflare Mesh, your account must be on [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing). Contact your account team to enable it. This applies to new and existing accounts. Cloudflare Tunnel does not need Unified Routing.
  * Private network routing is available for `A` (IPv4) and `AAAA` (IPv6) records only. Records must be [proxied](https://developers.cloudflare.com/dns/proxy-status/).
  * If you have multiple `A` or `AAAA` records on the same name, and at least one of them has private network routing enabled, all records on that name will use private network routing. This is consistent with the [proxy status behavior](https://developers.cloudflare.com/dns/proxy-status/#mix-proxied-and-unproxied) in these cases.



## Automatically detected ranges

The following private address ranges are automatically detected:

Range | Description  
---|---  
`10.0.0.0/8` | Private ([RFC 1918 ↗︎](https://www.rfc-editor.org/rfc/rfc1918.html))  
`172.16.0.0/12` | Private ([RFC 1918 ↗︎](https://www.rfc-editor.org/rfc/rfc1918.html))  
`192.168.0.0/16` | Private ([RFC 1918 ↗︎](https://www.rfc-editor.org/rfc/rfc1918.html))  
`fc00::/7` | Private ([RFC 4193 ↗︎](https://www.rfc-editor.org/rfc/rfc4193.html))  
`100.64.0.0/10` | CGNAT ([RFC 6598 ↗︎](https://www.rfc-editor.org/rfc/rfc6598.html))  
  
Caution

`100.64.0.0/10` is detected as private, but the default Cloudflare source range `100.64.0.0/12` sits inside it. If your origins use addresses in `100.64.0.0/12`, [change the Cloudflare source IP range](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/) to a different private `/12` before you enable private network routing.

When you use an IP address from one of these ranges, the **Use private network routing** toggle turns on automatically. You can also turn it on manually for public IP addresses that are only reachable through your tunnel.

## Cloudflare source IP ranges

When Cloudflare reaches an origin over Cloudflare WAN or Cloudflare Mesh, traffic comes from the Cloudflare source IP ranges:

IP version | Range | Configurable  
---|---|---  
IPv4 | `100.64.0.0/12` (default) | Yes, to another private `/12`  
IPv6 | `2606:4700:cf1:5000::/64` | No  
  
Add return routes in your private network that send these ranges back to Cloudflare, and allow them in your origin's firewall. Refer to [Configure Cloudflare source IPs](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/).

Behind Cloudflare Tunnel, your origin sees the host running `cloudflared` as the source instead.

## Enable private network routing

Virtual networks

Traffic routes through your default virtual network. Selecting a specific virtual network is not supported.

  1. In the Cloudflare dashboard, go to the **DNS Records** page.

[ Go to **Records** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/dns/records)
  2. Select **Add record** or select **Edit** on an existing `A` or `AAAA` record.

  3. Enter the origin IP address.

  4. Verify that **Proxy status** is enabled (orange cloud).

  5. Turn on **Use private network routing**.

For private IP addresses (for example, `10.0.0.50`), the toggle turns on automatically. For public IP addresses used with private infrastructure, turn on the toggle manually.

  6. Select **Save**.




To create a record with private routing enabled, use a [POST request](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/create/) and set `private_routing` to `true`:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `DNS Write`

Create DNS Recordbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"type": "A",
    		"name": "app.example.com",
    		"content": "10.0.0.50",
    		"proxied": true,
    		"private_routing": true
    	}'

To enable private routing on an existing record, use a [PATCH request](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/edit/):

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `DNS Write`

Update DNS Recordbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records/$DNS_RECORD_ID" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"private_routing": true
    	}'

### API field behavior

If you use the API to create or edit DNS records with private network routing, consider the following:

Scenario | `private_routing` value  
---|---  
Proxied `A`/`AAAA` record with private IP | Auto-set to `true`  
Proxied `A`/`AAAA` record with public IP | Defaults to `false`  
Non-`A`/`AAAA` record types | Field not supported  
  
Also, if you manually set `private_routing: false` on a proxied `A`/`AAAA` record with private IP, the API will return an error.

[PreviousSet up a private origin via Cloudflare Mesh](https://developers.cloudflare.com/dns/private-origins/set-up-via-cloudflare-mesh/)[NextTroubleshooting](https://developers.cloudflare.com/dns/private-origins/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/private-origins/private-network-routing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
