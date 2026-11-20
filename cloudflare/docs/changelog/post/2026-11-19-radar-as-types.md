---
url: https://developers.cloudflare.com/changelog/post/2026-11-19-radar-as-types/
title: Autonomous system types on Cloudflare Radar \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-20T09:50:37.493568+00:00
---

# Autonomous system types on Cloudflare Radar · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-19-radar-as-types/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 19, 2026

## Autonomous system types on Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Cloudflare Radar**](https://developers.cloudflare.com/radar/) now shows the [type](https://developers.cloudflare.com/radar/glossary/#autonomous-system-types) of each [autonomous system (AS)](https://developers.cloudflare.com/radar/glossary/#autonomous-systems): Access ISP, Hosting/Cloud/Content, or Organization. AS types are inferred automatically, so an individual AS can be misclassified. They make it easier to tell, for example, whether traffic or attacks come from residential and mobile networks or from data centers.

  * **Access ISP** (`ACCESS_ISP`): networks that connect end users, such as home broadband and mobile operators, plus transit providers.
  * **Hosting/Cloud/Content** (`HOSTING_CLOUD_CONTENT`): hosting providers, cloud platforms, and content delivery networks.
  * **Organization** (`ORGANIZATION`): enterprises, universities, governments, banks, and IXP route servers.



ASes without a type are shown as **Unclassified**. To report a wrong AS type, email [radar@cloudflare.com](mailto:radar@cloudflare.com?subject=%5BASN%5D%20Report%20wrong%20type).

![Chart of HTTP traffic from the top five ASes beside a table of the top ten, with house, cloud, and building icons before the AS numbers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=4293,height=1170,format=webp/_astro/radar-traffic-by-as-type.BngPlZ7u.png)

_Top ASes by HTTP traffic in[Portugal ↗︎](https://radar.cloudflare.com/traffic/pt#traffic-volume-by-autonomous-system), with the type of each AS shown before its number._

#### Radar pages

  * AS pages, such as [AS7922 ↗︎](https://radar.cloudflare.com/as7922), show the AS type in the AS information card.
  * An icon before the AS number shows its type across Radar. Hover over the icon to see the AS type.
  * The [Data Explorer ↗︎](https://radar.cloudflare.com/explorer) can break down and filter HTTP, NetFlows, DNS, and layer 7 attack data by AS type.

![AS information card listing the AS type as Access ISP, above a table of related ASes with house, cloud, and building icons](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=800,height=1560,format=webp/_astro/radar-as-type.Bc1MutZP.png)

_The AS type in the[AS7922 ↗︎](https://radar.cloudflare.com/traffic/as7922#asn-information) information card._

![Line chart of HTTP requests by AS type, scaled from zero to the maximum, where Access ISP stays well above Hosting/Cloud/Content and Organization stays near zero. A bar below shows Access ISP at 66% and Hosting/Cloud/Content at 33% of requests](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1250,format=webp/_astro/radar-explorer-as-type.CYlq3tWB.png)

_Worldwide HTTP requests by AS type over the last four weeks, from the[Data Explorer ↗︎](https://radar.cloudflare.com/explorer?dataSet=http&groupBy=as_category&dateRange=28d&filters=normalization%253DMIN0_MAX)._

#### API

  * The [Get AS details](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/asns/methods/get/), [List ASes](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/asns/methods/list/), and [Get AS details by IP address](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/asns/methods/ip/) endpoints return a new `category` field with the AS type, or `null` when the AS is not classified.
  * The [HTTP](https://developers.cloudflare.com/api/resources/radar/subresources/http/), [NetFlows](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/), [DNS](https://developers.cloudflare.com/api/resources/radar/subresources/dns/), and [layer 7 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/) endpoints accept a new `asCategory` filter, and their summary and timeseries groups endpoints support a new `AS_CATEGORY` dimension. Both accept `ACCESS_ISP`, `HOSTING_CLOUD_CONTENT`, `ORGANIZATION`, and `UNCLASSIFIED`, where `UNCLASSIFIED` also covers traffic that could not be mapped to an AS. For HTTP, they are supported for date ranges starting on or after 2023-05-01.
  * The [global search](https://developers.cloudflare.com/api/resources/radar/subresources/search/methods/global/) endpoint returns an `entity` with details of the matched AS, including its `category`, for AS results, and of the matched region for region (`adm1` and `adm2`) results.



For example, to get the share of HTTP requests by AS type in the last week:

Get HTTP requests summary by dimensionbash
    
    
    curl "https://api.cloudflare.com/client/v4/radar/http/summary/AS_CATEGORY?dateRange=7d" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Visit an [AS page ↗︎](https://radar.cloudflare.com/as7922) on Cloudflare Radar to see its type, or read the [AS type definitions](https://developers.cloudflare.com/radar/glossary/#autonomous-system-types).
