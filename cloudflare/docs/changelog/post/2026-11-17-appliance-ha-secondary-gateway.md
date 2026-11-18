---
url: https://developers.cloudflare.com/changelog/post/2026-11-17-appliance-ha-secondary-gateway/
title: Configure a separate WAN gateway for each appliance in a high availability site \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:16.942593+00:00
---

# Configure a separate WAN gateway for each appliance in a high availability site · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-17-appliance-ha-secondary-gateway/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 17, 2026

## Configure a separate WAN gateway for each appliance in a high availability site

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now give each [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) in a [high availability (HA)](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#about-high-availability-configurations) site its own default gateway on a static WAN. Before this change, both appliances in an HA pair shared the same WAN gateway. Now each appliance can connect to its own Internet circuit, such as a different ISP for each appliance, with its own static IP and gateway.

  * In the dashboard, when you configure a static WAN on an HA site, enter the secondary appliance's gateway in the new **Secondary gateway address** field, next to **Primary gateway address**.
  * In the API, set `static_addressing.secondary_gateway_address` when you [create](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/wans/methods/create/) or [update](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/wans/methods/edit/) a WAN. To remove the value with a `PATCH` request, set it to `null`.



The field is optional. If you leave it blank, the secondary appliance uses the primary gateway address, which matches how HA sites worked before. You can only use this field on sites in HA mode.
    
    
    curl --request PATCH \
    https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id} \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{
    	"static_addressing": {
    		"address": "203.0.113.2/30",
    		"gateway_address": "203.0.113.1",
    		"secondary_address": "198.51.100.2/30",
    		"secondary_gateway_address": "198.51.100.1"
    	}
    }'

For details, refer to [About high availability configurations](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#about-high-availability-configurations).
