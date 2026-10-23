---
url: https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/
title: IP Access rules parameters \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:47.774936+00:00
---

# IP Access rules parameters · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

Additional tools

  4. /[IP Access rules](https://developers.cloudflare.com/waf/tools/ip-access-rules/)
  5. /Parameters



# IP Access rules parameters

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIP addressIP rangeAutonomous System Number (ASN)Country

An IP Access rule will apply a certain action to incoming traffic based on the visitor's IP address, IP range, Autonomous System Number (ASN), or country.

## IP address

Type | Example value  
---|---  
IPv4 address | `192.0.2.3`  
IPv6 address | `2001:db8::`  
  
## IP range

Type | Example value | Start of range | End of range | Number of addresses  
---|---|---|---|---  
IPv4 `/24` range | `192.0.2.0/24` | `192.0.2.0` | `192.0.2.255` | 256  
IPv4 `/16` range | `192.168.0.0/16` | `192.168.0.0` | `192.168.255.255` | 65,536  
IPv6 `/128` range | `2001:db8::/128` | `2001:db8::` | `2001:db8::` | 1  
IPv6 `/64` range | `2001:db8::/64` | `2001:db8::` | `2001:db8:0000:0000:ffff:ffff:ffff:ffff` | 18,446,744,073,709,551,616  
IPv6 `/48` range | `2001:db8::/48` | `2001:db8::` | `2001:db8:0000:ffff:ffff:ffff:ffff:ffff` | 1,208,925,819,614,629,174,706,176  
IPv6 `/32` range | `2001:db8::/32` | `2001:db8::` | `2001:db8:ffff:ffff:ffff:ffff:ffff:ffff` | 79,228,162,514,264,337,593,543,950,336  
  
## Autonomous System Number (ASN)

Type | Example value  
---|---  
ASN | `AS13335`  
  
## Country

Specify a country using two-letter [ISO-3166-1 alpha-2 codes ↗︎](https://www.iso.org/iso-3166-country-codes.html). Additionally, the Cloudflare dashboard accepts country names. For example:

  * `US`
  * `CN`
  * `germany` (dashboard only)



Cloudflare uses the following special country alpha-2 codes that are not part of the ISO:

  * `T1`: [Tor exit nodes](https://developers.cloudflare.com/network/onion-routing/) (country name: `Tor`)
  * `XX`: Unknown/reserved



Notes

Country block is only available on Enterprise plans.

IP addresses globally allowed by Cloudflare will override a country block via IP Access rules, but they will not override a country block via [custom rules](https://developers.cloudflare.com/waf/custom-rules/).

[PreviousCreate a rule](https://developers.cloudflare.com/waf/tools/ip-access-rules/create/)[NextActions](https://developers.cloudflare.com/waf/tools/ip-access-rules/actions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/tools/ip-access-rules/parameters.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
