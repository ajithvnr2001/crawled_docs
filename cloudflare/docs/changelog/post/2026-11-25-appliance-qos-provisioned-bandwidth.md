---
url: https://developers.cloudflare.com/changelog/post/2026-11-25-appliance-qos-provisioned-bandwidth/
title: Prioritized traffic now takes effect on congested WAN circuits for Cloudflare One Appliance \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-26T10:37:13.660852+00:00
---

# Prioritized traffic now takes effect on congested WAN circuits for Cloudflare One Appliance · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-25-appliance-qos-provisioned-bandwidth/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 25, 2026

## Prioritized traffic now takes effect on congested WAN circuits for Cloudflare One Appliance

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Prioritized traffic](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/) on [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) now takes effect when your WAN circuit is slower than the appliance port, which is common for branch Internet connections. Enter the circuit's upload speed on each WAN, and the appliance shapes upload traffic to 95% of that value. Traffic then queues on the appliance instead of in your modem or ISP network, so the appliance can send prioritized applications, such as voice and video calls, ahead of everything else.

  * **Two traffic classes** : Applications in the **Prioritized traffic** list go first. All other traffic is default (best effort). Prioritized traffic cannot completely starve default traffic, and flows within each class share bandwidth fairly.
  * **Dashboard** : When you create or edit a WAN, enter **Provisioned upload bandwidth (Mbps)** and, optionally, **Provisioned download bandwidth (Mbps)**. Saved values appear in the WAN details.
  * **API** : Set `provisioned_upload_kbps` and `provisioned_download_kbps`, in kilobits per second, when you [create](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/wans/methods/create/) or [update](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/wans/methods/edit/) a WAN. To remove a value with a `PATCH` request, set it to `null`.



Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Magic WAN Write`
  * `Magic Transit Write`

Patch Site WANbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/sites/$SITE_ID/wans/$WAN_ID" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"provisioned_upload_kbps": 100000,
    		"provisioned_download_kbps": 500000
    	}'

Both fields are optional. If you do not set the upload value, the appliance does not shape the WAN, which matches how it worked before. The appliance does not currently shape download traffic. Upload shaping requires Appliance version 2026.10.3 or later, which appliances install automatically during their interrupt window.

For details, refer to [How traffic prioritization works](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/#how-traffic-prioritization-works).
