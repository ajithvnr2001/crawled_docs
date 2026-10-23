---
url: https://developers.cloudflare.com/changelog/post/2026-10-14-nameserver-sets/
title: Configure Advanced Custom Nameservers with nameserver sets (beta) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:32.553886+00:00
---

# Configure Advanced Custom Nameservers with nameserver sets (beta) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-14-nameserver-sets/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 14, 2026

## Configure Advanced Custom Nameservers with nameserver sets (beta)

[DNS](https://developers.cloudflare.com/dns/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
