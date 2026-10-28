---
url: https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/
title: Fully qualified domain name objects overview \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:53:10.036540+00:00
---

# Fully qualified domain name objects overview  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/

[ Skip to main content ](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/)
  * [Deutsch](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/?hl=es-419)
  * [Français](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/?hl=id)
  * [Italiano](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/?hl=ja)
  * [한국어](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/security-and-identity-color.svg) ](https://docs.cloud.google.com/firewall/docs)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Map FQDN objects to IP addresses](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/#how-fqdns-work)
  * [Considerations for FQDN objects](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/#fqdn-limitations)
  * [Format domain names](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/#domain-name-format)
  * [What's next](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)


Was this helpful?
Send feedback 
#  Fully qualified domain name objects overview Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Map FQDN objects to IP addresses](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/#how-fqdns-work)
  * [Considerations for FQDN objects](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/#fqdn-limitations)
  * [Format domain names](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/#domain-name-format)
  * [What's next](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview/#whats_next)


Fully qualified domain name (FQDN) objects let you define firewall rules by using domain names instead of specific IP addresses. This document describes how FQDN objects map to IP addresses and support various Cloud DNS services:
  * [Cloud DNS response policies](https://docs.cloud.google.com/dns/docs/zones/manage-response-policies)
  * [VPC network-scoped managed private zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview)
  * [Compute Engine internal DNS names](https://docs.cloud.google.com/compute/docs/internal-dns)
  * Public DNS zones


This document is intended for network administrators and security engineers who configure and manage firewall policies.
To use FQDN objects, the Virtual Private Cloud (VPC) network can't use an [outbound server policy](https://docs.cloud.google.com/dns/docs/server-policies-overview#dns-server-policy-out) with an [alternative name server](https://docs.cloud.google.com/dns/docs/server-policies-overview#altns-targets). For more information, see [VPC network resolution order](https://docs.cloud.google.com/dns/docs/vpc-name-res-order#vpc_steps).
## Map FQDN objects to IP addresses
Cloud Next Generation Firewall (Cloud NGFW) periodically resolves FQDN objects to IP addresses. Cloud NGFW follows the Cloud DNS [VPC name resolution order](https://docs.cloud.google.com/dns/docs/vpc-name-res-order) in the VPC network that contains the firewall rule's targets.
Cloud NGFW uses the following behavior for IP address resolution:
  * **Support CNAME chasing**. Cloud NGFW uses Cloud DNS [CNAME chasing](https://docs.cloud.google.com/dns/docs/cnamechasing) if the answer to a FQDN object query is a CNAME record.
  * **Program IP addresses**. Cloud NGFW uses the resolved IP addresses when it programs the firewall rules that use FQDN objects. Each FQDN object can be mapped to a maximum of 32 IPv4 addresses and 32 IPv6 addresses.
If the DNS answer for an FQDN object query resolves to more than 32 IPv4 addresses or more than 32 IPv6 addresses, Cloud NGFW limits the programmed IP addresses in the firewall rules to the first 32 IPv4 addresses and the first 32 IPv6 addresses.
  * **Ignore FQDN objects**. If Cloud NGFW cannot resolve an FQDN object to an IP address, it ignores the FQDN object. In the following situations, Cloud NGFW ignores an FQDN object:
    * When `NXDOMAIN` answers are received. `NXDOMAIN` answers are explicit answers from a name server indicating that no DNS record for the FQDN object query exists.
    * When no IP address exists in an answer. In this situation, an FQDN object query doesn't result in an answer with an IP address that Cloud NGFW can use to program a firewall rule.
    * When Cloud DNS server is unreachable. Cloud NGFW ignores FQDN objects if a DNS server that provides the answer is unreachable.
When an FQDN object is ignored, Cloud NGFW programs the remaining portions of a firewall rule, if possible.


## Considerations for FQDN objects
Consider the following for FQDN objects:
  * You can combine FQDNs with other parameters. For details about source parameter combinations in ingress rules, see [Sources for ingress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-src). For details about destination parameter combinations in egress rules, see [Destinations for egress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-egress-dest).
  * Because FQDN objects map to and are programmed as IP addresses, Cloud NGFW uses the following behavior when two or more FQDN objects map to the same IP address. Assume you have the following two firewall rules that apply to the same target:
    * Rule 1: priority `100`, ingress allow from source FQDN `example1.com`
    * Rule 2: priority `200`, ingress allow from source FQDN `example2.com`
If both `example1.com` and `example2.com` resolve to the same IP address, ingress packets from both `example1.com` and `example2.com` match the first firewall rule because this rule has a higher priority.
  * Considerations for using FQDN objects include the following:
    * A DNS query can have unique answers based on the location of the requesting client.
    * DNS answers can be highly variable when a DNS-based load balancing system is involved.
    * A DNS answer might contain more than 32 IPv4 addresses.
    * A DNS answer might contain more than 32 IPv6 addresses.
In the preceding situations, because Cloud NGFW performs DNS queries in each region that contains the VM network interface to which the firewall rule applies, the programmed IP addresses in firewall rules don't contain all possible IP addresses associated with the FQDN.
Most Google domain names, such as `googleapis.com`, are subject to one or more of these situations. Use IP addresses or [address groups](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies) instead.
  * Avoid using FQDN objects with DNS `A` records that have a time to live (TTL) of less than 90 seconds.


## Format domain names
FQDN objects must follow the [standard FQDN format](https://wikipedia.org/wiki/Fully_qualified_domain_name#Syntax). This format is defined in [RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035#section-2.3.1), [RFC 1123](https://datatracker.ietf.org/doc/html/rfc1123#section-2), and [RFC 4343](https://datatracker.ietf.org/doc/html/rfc4343). Cloud NGFW rejects FQDN objects that include a domain name that doesn't meet all of the following formatting rules:
  * Each FQDN object must be a domain name with at least two labels:
    * Each label must match a regular expression that includes only these characters: `[a-z]([-a-z0-9][a-z0-9])?.`.
    * Each label must have a length of 1-63 characters.
    * Labels must be concatenated with a dot (.).
Consequently, FQDN objects don't support wildcard characters (`*`) or top-level (or root) domain names, such as `*.example.com.` and `.org`, because these include only a single label.
  * FQDN objects support [Internationalized Domain Names (IDNs)](https://wikipedia.org/wiki/Internationalized_domain_name). You can supply an IDN in either Unicode or [Punycode](https://wikipedia.org/wiki/Punycode) format. Consider the following:
    * If you specify an IDN in Unicode format, Cloud NGFW converts it to Punycode format before processing.
    * You can use the [IDN converter](https://www.verisign.com/en_US/channel-resources/domain-registry-products/idn/idn-conversion-tool/index.xhtml) to create the Punycode representation of an IDN.
    * The character limit of 1-63 per label applies to IDNs after conversion to Punycode format.
  * The encoded length of a fully qualified domain name (FQDN) cannot exceed 255 bytes (octets).


Cloud NGFW doesn't support equivalent domain names in the same firewall rule. For example, if the two domain names (or Punycode representations of IDNs) differ at most by a terminal dot (`.`), Cloud NGFW considers them equivalent.
## What's next
  * [Firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details)
  * [Google Threat Intelligence for firewall policy rules](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview)
  * [Address groups for firewall policies](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies)


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
