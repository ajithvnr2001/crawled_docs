---
url: https://developers.cloudflare.com/changelog/post/2026-11-23-remove-foundation-dns-boolean/
title: DNS settings endpoints remove deprecated Foundation DNS boolean \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-24T12:11:00.565475+00:00
---

# DNS settings endpoints remove deprecated Foundation DNS boolean · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-23-remove-foundation-dns-boolean/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 23, 2026

## DNS settings endpoints remove deprecated Foundation DNS boolean

[DNS](https://developers.cloudflare.com/dns/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Starting today, the [DNS settings endpoints](https://developers.cloudflare.com/api/resources/dns/subresources/settings/) no longer return or accept the deprecated `foundation_dns` boolean for zone settings or account defaults. The rollout is expected to take seven days. Use `nameservers.type: "cloudflare.advanced"` to configure Advanced Nameservers.

Update clients that still read or write `foundation_dns`. Remove handling for the boolean and use the nameserver type instead. The zone settings JSON for [`/zones/{zone_id}/dns_settings`](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/zone/) is:
    
    
    {
      "nameservers": {
        "type": "cloudflare.advanced"
      }
    }

Cloudflare will make an equivalent change to [`/accounts/{account_id}/dns_settings`](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/) at the same time.

`PATCH` requests that include `foundation_dns` will be rejected.

This API update does not change your Foundation DNS subscription or whether Advanced Nameservers are enabled on your zones. It does not require a zone migration.
