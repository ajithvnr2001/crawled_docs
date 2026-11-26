---
url: https://developers.cloudflare.com/changelog/post/2026-11-25-appliance-dnat-translations/
title: Reach overlapping remote networks with DNAT translations on Cloudflare One Appliance \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-26T10:37:13.623755+00:00
---

# Reach overlapping remote networks with DNAT translations on Cloudflare One Appliance · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-25-appliance-dnat-translations/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 25, 2026

## Reach overlapping remote networks with DNAT translations on Cloudflare One Appliance

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure DNAT (destination NAT) translations on a [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) LAN, in beta. A DNAT translation maps a local **pre-NAT prefix** to a **post-NAT prefix** of the same size, which is the real prefix of a remote subnet reachable through Cloudflare WAN, such as a data center connected over an IPsec tunnel. Hosts on the LAN send traffic to the pre-NAT prefix, and the Appliance translates it 1:1 to the remote subnet and back.

Use DNAT translations to reach a remote network that uses the same addresses as your site, without renumbering either side. You can also use them to avoid adding routes for remote subnets to your local network. Combine DNAT translations with [static NAT for a subnet](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/nat-subnet/) when both sides of the connection use the same addresses.

  * In the dashboard, edit a LAN in your Appliance profile's **Network configuration** , then select **Add DNAT translation** under **DNAT translations**.

[ Go to **Appliances** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/connections/appliances)
  * In the API, set the `remote_subnets` array when you [create](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/lans/methods/create/) or [update](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/lans/methods/edit/) a LAN. Each item has a `local_alias_prefix` (pre-NAT) and a `remote_prefix` (post-NAT).




Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Magic WAN Write`
  * `Magic Transit Write`

Patch Site LANbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/sites/$SITE_ID/lans/$LAN_ID" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"remote_subnets": [
    				{
    						"local_alias_prefix": "100.64.1.0/24",
    						"remote_prefix": "10.1.1.0/24"
    				}
    		]
    	}'

DNAT translations require Appliance OS version 2026.11.2 or later, which deploys automatically.

For details, refer to [DNAT translations](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dnat-translations/).
