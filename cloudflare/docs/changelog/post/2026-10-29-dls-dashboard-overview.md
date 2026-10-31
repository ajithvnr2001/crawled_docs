---
url: https://developers.cloudflare.com/changelog/post/2026-10-29-dls-dashboard-overview/
title: View your data localization settings in one dashboard page \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:17.099118+00:00
---

# View your data localization settings in one dashboard page · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-29-dls-dashboard-overview/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 29, 2026

## View your data localization settings in one dashboard page

[Data Localization Suite](https://developers.cloudflare.com/data-localization/)[SSL/TLS](https://developers.cloudflare.com/ssl/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Cloudflare dashboard now includes a **Data Localization Suite** Overview, a read-only view of the data localization settings on your account. It shows your Regional Services, Customer Metadata Boundary, and Geo Key Manager settings in one place, so you no longer need to check several dashboard pages and APIs to see where your traffic is processed and where your logs and private keys are stored.

To find it, go to **Application Security** > **Data Localization Suite** , or search for "DLS" in the dashboard.

The Overview has a tab for each product:

  * **Regional Services** : regionalized hostnames (filter by region or zone), regionalized IP bindings, and regionalized Spectrum applications, each with its region.
  * **Customer Metadata Boundary** : whether the boundary is on, the region (US or EU), and whether out-of-region access is allowed.
  * **Geo Key Manager** : every custom certificate with a geo policy, with its hostname, zone, region, and status.



Each item links to the dashboard page where you change its setting, and each tab links to the product's documentation.

To learn more, refer to the [Data Localization Suite documentation](https://developers.cloudflare.com/data-localization/).
