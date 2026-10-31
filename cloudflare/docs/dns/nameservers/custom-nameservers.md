---
url: https://developers.cloudflare.com/dns/nameservers/custom-nameservers/
title: Custom nameservers \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:22.858580+00:00
---

# Custom nameservers · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/nameservers/custom-nameservers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /[Nameservers](https://developers.cloudflare.com/dns/nameservers/)
  4. /Custom nameservers



# Custom nameservers

Last updated Oct 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfiguration optionsAvailabilityRestrictions

With custom (or vanity) nameservers, a domain can use Cloudflare DNS without using Cloudflare-branded nameservers. For instance, you can configure `ns1.example.com` and `ns2.example.com` as nameservers for `example.com`.

To use custom nameservers, a zone must be using Cloudflare as Primary ([Full setup](https://developers.cloudflare.com/dns/zone-setups/full-setup/)) or [Secondary](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/) DNS provider.

There are two custom nameserver configurations, and a zone can only use one of them:

  * [Nameserver sets](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/) (beta) are created at the account level and assigned to individual zones. This is a modern feature that supports Advanced Nameservers and more.
  * Legacy zone, account, and tenant custom nameservers are configured with an `ns_set` number between 1 and 5.



## Configuration options

  * [Nameserver sets](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/)
  * [Set up zone custom nameservers](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/zone-custom-nameservers/)
  * [Set up account custom nameservers](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/account-custom-nameservers/)
  * [Set up tenant custom nameservers](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/tenant-custom-nameservers/)



## Availability

  * Nameserver sets are in beta and available for Enterprise customers, via API or on the dashboard. Once created, a nameserver set can be used by zones in the same account.
  * Zone custom nameservers are available for zones on Business or Enterprise plans. Via API or on the dashboard.
  * Account custom nameservers are available for customers on Business (after [contacting Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/)) or Enterprise plans. Once configured, account custom nameservers can be used by all zones in the account, regardless of the zone plan. Via API or on the dashboard.
  * Tenant custom nameservers, if created by the tenant owner, will be available to all zones belonging to any account that is part of the tenant. Via API only.



## Restrictions

Legacy zone, account, and tenant custom nameservers are organized in different sets (`ns_set`). Each nameserver set must have at least two and no more than five custom nameserver names.

For modern nameserver sets, refer to [Limits](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/#limits).

To use your own nameserver names with Advanced anycast network groups, create an [Advanced Custom Nameserver set](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/#advanced-custom-nameserver-set). Zone, account, and tenant custom nameservers do not support Advanced anycast network groups. A zone can only use one nameserver configuration at a time.

[PreviousNameserver options](https://developers.cloudflare.com/dns/nameservers/nameserver-options/)[NextNameserver sets](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/nameservers/custom-nameservers/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
