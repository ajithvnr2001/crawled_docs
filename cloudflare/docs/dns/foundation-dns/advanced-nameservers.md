---
url: https://developers.cloudflare.com/dns/foundation-dns/advanced-nameservers/
title: Advanced nameservers \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:59:22.583429+00:00
---

# Advanced nameservers · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/foundation-dns/advanced-nameservers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /[Foundation DNS](https://developers.cloudflare.com/dns/foundation-dns/)
  4. /Advanced nameservers



# Advanced nameservers

Last updated Oct 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAnycast network groupsDedicated release processNameservers hosting and assignment Consistent assignment across new zonesCustom Nameserver compatibility

Advanced nameservers included with [Foundation DNS](https://developers.cloudflare.com/dns/foundation-dns/) offer improved resiliency and more consistent nameserver assignment.

Consider the sections below for details about advanced nameservers, and refer to [Set up advanced nameservers](https://developers.cloudflare.com/dns/foundation-dns/setup/) to learn how to enable this feature.

Note

To use your own nameserver names with Advanced anycast network groups, create an [Advanced Custom Nameserver set](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/#advanced-custom-nameserver-set). Zone, account, and tenant custom nameservers do not support Advanced anycast network groups. A zone can only use one nameserver configuration at a time.

Also, [some behaviors are different](https://developers.cloudflare.com/dns/foundation-dns/setup/#differences-from-standard-nameservers) when compared to standard nameservers.

## Anycast network groups

To increase resiliency, the advertisement of advanced nameserver IPs is organized into three anycast network groups.

Two groups consist of IPs advertised from geographically distributed data centers, and a third group consists of IPs advertised from all data centers in the Cloudflare network.

United Kingdom example

IPs | Group | Data centers  
---|---|---  
`108.162.198.1` | A | London and Edinburgh  
`172.64.40.1` | B | Manchester  
`162.159.60.1` | C | Manchester, London, and Edinburgh  
  
In DNS resolution, a resolver eventually acquires a list of all IPs where authoritative nameservers for a domain can be reached, and will then usually prefer the IP with the best resolution performance.

When, instead of advertising all IPs in all data centers, this group logic is applied, resiliency is improved because, if one of the data centers experiences a localized issue, the resolver can fall back to an IP advertised by the next closest data center. The third group adds another layer of redundancy, further enhancing resiliency.

Refer to [our blog post ↗︎](https://blog.cloudflare.com/foundation-dns-launch) for an in-depth explanation of the distributed groups logic.

Note

The IPs assigned to each nameserver are static, meaning they will not change without notification.

## Dedicated release process

Zones using advanced nameservers are less exposed to incidents or software regression.

The dedicated release process means that only changes that have been in production for a while will reach advanced nameservers.

## Nameservers hosting and assignment

While standard Cloudflare nameservers are hosted under `ns.cloudflare.com` or `secondary.cloudflare.com`, advanced nameservers use different domains:

  * `foundationdns.com`
  * `foundationdns.net`
  * `foundationdns.org`



Using the different TLDs (`.com`, `.net`, and `.org`) and making these available only to enterprise accounts allows for better predictability and consistency in nameserver assignment.

There should also be less conflicts when guaranteeing that directly descending zones do not have the same nameserver set.

Descending zones example

Consider the domain `example.com`, and subdomains `abc.example.com` and `123.example.com`:

  * `abc.example.com` and `123.example.com` directly descend from `example.com` and cannot have the same nameservers as `example.com`.
  * `abc.example.com` and `123.example.com` are sibling domains and can have the same nameservers.
  * `new.abc.example.com` directly descends from both `abc.example.com` and `example.com`, and cannot have the same nameservers as them, but can have the same nameservers as `123.example.com`.



### Consistent assignment across new zones

Advanced nameservers try to keep the same nameserver set (`blue`, `gold`, or `orange`) for new zones added to the same account, but a new zone can still be assigned a different set when:

  * The same domain is (or was recently) active on another Cloudflare account.
  * A directly descending zone in the same or another account already uses the same set.
  * The zone was previously deleted from Cloudflare and re-added.



Cloudflare cannot change the Advanced nameservers [automatically assigned](https://developers.cloudflare.com/dns/nameservers/nameserver-options/#assignment-method) to a zone, such as `blue.foundationdns.com`. To use the same nameservers across zones, use [account custom nameservers](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/account-custom-nameservers/) or assign the same [nameserver set](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/) (beta) to each zone. To keep Advanced anycast network groups, use an [Advanced Custom Nameserver set](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/#advanced-custom-nameserver-set).

## Custom Nameserver compatibility

Advanced Custom Nameserver sets are available in beta to Enterprise customers. These sets use custom nameserver names (for example, `ns1.example.com`) and distribute addresses across Advanced anycast network groups. To create one, refer to [Advanced Custom Nameserver set](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/#advanced-custom-nameserver-set).

Legacy [tenant](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/tenant-custom-nameservers/), [account](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/account-custom-nameservers/), or [zone](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/zone-custom-nameservers/)-level Custom Nameservers are not compatible with Advanced Nameservers.

[PreviousOverview](https://developers.cloudflare.com/dns/foundation-dns/)[NextSetup](https://developers.cloudflare.com/dns/foundation-dns/setup/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/foundation-dns/advanced-nameservers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
