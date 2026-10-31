---
url: https://developers.cloudflare.com/changelog/post/2026-10-30-classic-dns-records-page-retired/
title: New DNS records experience is now the default for everyone \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:17.359326+00:00
---

# New DNS records experience is now the default for everyone · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-30-classic-dns-records-page-retired/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 30, 2026

## New DNS records experience is now the default for everyone

[DNS](https://developers.cloudflare.com/dns/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The new DNS records experience [announced in May](https://developers.cloudflare.com/changelog/post/2026-05-20-new-dns-records-ux/) is now the default for all users on all plans, including Enterprise. The classic DNS records page has been retired and is no longer available in the Cloudflare dashboard.

#### Changing a record's type

When the new experience first launched, it did not support changing the type of an existing DNS record. Based on your feedback, we have since added this, so you can now change a record's type (for example, from `A` to `CNAME`) directly from the DNS records page. Under the hood, the dashboard uses the [batch DNS records endpoint](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/batch/) for this.

#### Questions or feedback

If you run into an issue with the new experience, contact your account team or [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/).
