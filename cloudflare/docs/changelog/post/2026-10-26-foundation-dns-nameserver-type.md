---
url: https://developers.cloudflare.com/changelog/post/2026-10-26-foundation-dns-nameserver-type/
title: Advanced Nameservers use a nameserver type \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-27T07:31:30.476740+00:00
---

# Advanced Nameservers use a nameserver type · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-26-foundation-dns-nameserver-type/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 26, 2026

## Advanced Nameservers use a nameserver type

[DNS](https://developers.cloudflare.com/dns/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Starting today, the [DNS settings endpoints](https://developers.cloudflare.com/api/resources/dns/subresources/settings/) gradually begin to represent Advanced Nameservers with `nameservers.type: "cloudflare.advanced"`. The rollout is expected to take seven days. Previously, the API used the `"foundation_dns": true` setting for this configuration.

Before the rollout reaches an account, the endpoints continue to return `nameservers.type: "cloudflare.standard"` for Advanced Nameservers. The endpoints accept `nameservers.type: "cloudflare.advanced"` in `PATCH` requests for entitled accounts throughout the rollout. The zone settings JSON for [`/zones/{zone_id}/dns_settings`](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/zone/) is:
    
    
    {
      "nameservers": {
        "type": "cloudflare.advanced"
      },
      "foundation_dns": true
    }

Cloudflare will make an equivalent change to [`/accounts/{account_id}/dns_settings`](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/) at the same time.

The `foundation_dns` boolean remains available as a deprecated compatibility alias in zone and account-default settings. Use `nameservers.type: "cloudflare.advanced"` for new writes.

You can continue to read and write `foundation_dns` during this transition. If a `PATCH` request includes both values, they must match. The API rejects conflicting values.

Update clients that treat `nameservers.type` as a closed enum to recognize the `"cloudflare.advanced"` value.

This API update does not change your Foundation DNS subscription or whether Advanced Nameservers are enabled on your zones. It does not require a zone migration.

In a future API change, Cloudflare will remove the `foundation_dns` parameter from the API endpoint. After migrating to `nameservers.type`, remove handling for the boolean from your client.
