---
url: https://developers.cloudflare.com/changelog/post/2026-11-20-radar-zero-wire-cves/
title: CVE pages in Zero Wire \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-21T09:24:30.539848+00:00
---

# CVE pages in Zero Wire · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-20-radar-zero-wire-cves/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 20, 2026

## CVE pages in Zero Wire

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Cloudflare Radar**](https://developers.cloudflare.com/radar/) [Zero Wire ↗︎](https://radar.cloudflare.com/zero-wire) now has a page for every published CVE. Each page brings together what you need to decide how urgently to act on a vulnerability: how severe it is, whether it is being exploited, what it affects, and how to fix it.

![Animation searching the CVE list for log4j, filtering to Critical severity, sorting by highest score, and opening the Log4Shell CVE page, then scrolling through all of its sections, from exploitation to references](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=900,format=webp/_astro/radar-zero-wire-cves.EBDpI3NT.webp)

#### Browse CVEs

The [CVE list ↗︎](https://radar.cloudflare.com/zero-wire/cves) includes every published CVE. Sort them by date or CVSS score, search by CVE ID or keyword, such as a product or vendor name, and filter by severity and year. Each row shows the CVE's score and highlights CVEs in the CISA Known Exploited Vulnerabilities (KEV) catalog and those with a fix available.

#### CVE pages

Each CVE page, such as [CVE-2021-44228 (Log4Shell) ↗︎](https://radar.cloudflare.com/zero-wire/cves/CVE-2021-44228), starts with its CVSS score, description, and key dates, followed by:

  * **Exploitation** : whether the CVE is in the CISA KEV catalog, including known ransomware use, the CISA SSVC assessment, and the FIRST EPSS probability of exploitation.
  * **Affected products** : the affected vendors, products, and versions, as listed by the organization that published the CVE and by NVD.
  * **Recommended actions** : how to fix the vulnerability, or reduce the risk until you can, including CISA's guidance for known exploited CVEs.
  * **Severity** : every CVSS score for the CVE, with each metric explained.
  * **Weaknesses and attack patterns** : the related CWE weaknesses and CAPEC attack patterns.
  * **References** : advisories, patches, and other sources.



CVEs cited in [Zero Wire briefings ↗︎](https://radar.cloudflare.com/zero-wire) link to their CVE pages, and each CVE page links back to the briefings that cite it.

#### Search and follow

Search for a CVE ID or keyword from anywhere on Radar, using the search bar or Cmd+K (Ctrl+K on Windows and Linux), to jump straight to a CVE page.

![Radar search showing CVE results for log4j](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2880,height=1620,format=webp/_astro/radar-zero-wire-cves-search.B09HTzyf.webp)

To follow new CVEs, subscribe to the [RSS ↗︎](https://radar.cloudflare.com/zero-wire/cves/feed), [Atom ↗︎](https://radar.cloudflare.com/zero-wire/cves/feed?format=atom), or [JSON ↗︎](https://radar.cloudflare.com/zero-wire/cves/feed?format=json) feed. Each feed can be filtered by severity, such as the feed of [Critical CVEs ↗︎](https://radar.cloudflare.com/zero-wire/cves/feed?severity=critical).

Explore the [CVE list ↗︎](https://radar.cloudflare.com/zero-wire/cves) on Cloudflare Radar.
