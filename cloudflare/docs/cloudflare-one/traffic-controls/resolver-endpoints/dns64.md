---
url: https://developers.cloudflare.com/cloudflare-one/traffic-controls/resolver-endpoints/dns64/
title: DNS64 \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:57:11.413043+00:00
---

# DNS64 · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/traffic-controls/resolver-endpoints/dns64/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Traffic controls](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)

  4. /[Resolver endpoints](https://developers.cloudflare.com/cloudflare-one/traffic-controls/resolver-endpoints/)
  5. /DNS64



# DNS64

Last updated Oct 13, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRequest DNS64 DNS location setting EDNS option DoH headerVerify DNS64

Cloudflare Gateway supports DNS64 for IPv6-only networks. DNS64 synthesizes `AAAA` records from `A` records when no `AAAA` records are available.

Gateway uses the well-known prefix `64:ff9b::/96` for DNS64. Your network must provide network address translation from IPv6 to IPv4 (NAT64) for this prefix.

DNS64 synthesizes DNS answers. NAT64 translates network traffic.

## Request DNS64

DNS64 is off by default. You can request synthesis for a DNS location or an individual query.

Extension Mechanisms for DNS (EDNS) adds options to DNS queries. The location setting and EDNS option support UDP, TCP, DNS over TLS (DoT), and DNS over HTTPS (DoH).

Gateway supports these opt-in mechanisms:

Mechanism | Configuration | Scope  
---|---|---  
DNS location | **Enable DNS64** , or `dns64_enabled: true` through the API | Queries that match the location  
EDNS option | Option code `65051` with an empty payload | Individual DNS query  
DoH header | `cf-dns-options: dns64` | Individual DoH request  
  
Each mechanism independently requests DNS64. Turning off the location setting does not prevent per-query opt-in.

### DNS location setting

To request DNS64 for a location, turn on **Enable DNS64**. You can change this setting when you add or edit a [DNS location](https://developers.cloudflare.com/cloudflare-one/traffic-controls/resolver-endpoints/).

The setting applies to queries that match the location. For matching criteria, refer to [DNS query location matching](https://developers.cloudflare.com/cloudflare-one/traffic-controls/resolver-endpoints/dns-resolver-ips/#dns-query-location-matching).

To configure DNS64 through the API, set `dns64_enabled` to `true`. Include this field when you [create a location](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/locations/methods/create/) or [update a location](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/locations/methods/update/). The field has type `boolean` and defaults to `false`.

Preserve DNS64 in location updates

Location updates use `PUT`. Include `dns64_enabled` explicitly in every update. Omitting the field resets it to `false`, even if it was previously `true`. Preserve the other location settings in the update request.

### EDNS option

To request DNS64 for an individual query, include a Cloudflare-specific EDNS option. Set the following fields in the `OPT` record:

Field | Value  
---|---  
Option code | `65051`  
Option length | `0`  
Option data | Empty  
  
An option with a nonempty payload does not request DNS64. It does not turn off DNS64 requested by the location setting or DoH header.

If a query contains multiple instances of option `65051`, any instance with an empty payload requests DNS64.

To send an empty option with `dig`, replace `<DNS_RESOLVER_IP>` with the resolver IP address for your location:
    
    
    dig @"<DNS_RESOLVER_IP>" ipv4only.arpa AAAA +ednsopt=65051 +short

To send the same query over TCP, add `+tcp`:
    
    
    dig @"<DNS_RESOLVER_IP>" ipv4only.arpa AAAA +ednsopt=65051 +tcp +short

To send an EDNS option over DoH, use a request in DNS wire format. The JSON DoH query format cannot carry this option.

### DoH header

To request DNS64 over DoH, include the `cf-dns-options` header with the value `dns64`. The header works independently of the location setting. For a request example, refer to [Request DNS64](https://developers.cloudflare.com/cloudflare-one/traffic-controls/resolver-endpoints/dns-over-https/#request-dns64).

## Verify DNS64

When you request DNS64, an eligible `AAAA` query for `ipv4only.arpa` returns these synthesized addresses:
    
    
    64:ff9b::c000:aa
    64:ff9b::c000:ab

These addresses correspond to the `A` records for `ipv4only.arpa`: `192.0.0.170` and `192.0.0.171`.

To verify the location setting independently, omit the EDNS option and DoH header. With the location setting off and no per-query opt-in, this domain returns no `AAAA` answers.

DNS64 does not change existing `AAAA` answers, `A` queries, or DNS error responses. It does not apply to DNS policy block responses or DNS override answers.

Clients that independently validate DNS Security Extensions (DNSSEC) may reject synthesized answers. DNS64 cannot create valid DNSSEC signatures for the synthesized `AAAA` records.

[PreviousDNS over HTTPS (DoH)](https://developers.cloudflare.com/cloudflare-one/traffic-controls/resolver-endpoints/dns-over-https/)[NextGlobal policies](https://developers.cloudflare.com/cloudflare-one/traffic-controls/global-policies/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/traffic-controls/resolver-endpoints/dns64.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
