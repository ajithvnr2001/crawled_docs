---
url: https://developers.cloudflare.com/changelog/post/2026-11-19-redesigned-dashboard/
title: Redesigned Spectrum dashboard \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-19T10:02:04.633135+00:00
---

# Redesigned Spectrum dashboard · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-19-redesigned-dashboard/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 19, 2026

## Redesigned Spectrum dashboard

[Spectrum](https://developers.cloudflare.com/spectrum/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Spectrum pages in the Cloudflare dashboard have been redesigned. Your existing applications and their settings do not change.

The **Spectrum Applications** page lists each application's type, edge port, origin, and edge IP type, with the last minute of connections, ingress, and egress. You can search the list and sort it by column.

Creating or editing an application now opens a full page instead of a modal, with settings grouped into **Application Configuration** , **Origin Configuration** , and **Advanced Options**. To edit an application, select its hostname, or select the three dots next to it > **Edit**.

You can now create and edit applications that use [static IPs](https://developers.cloudflare.com/spectrum/about/static-ip/) or [BYOIP](https://developers.cloudflare.com/spectrum/about/byoip/) addresses in the dashboard. Under **Edge IP Type** , select **Dedicated IPs**. Leave **Subdomain** blank to create an application on the zone apex.

New TCP and UDP applications created in the dashboard now have **IP Access Rules** turned off by default, which matches the API default. To enforce IP Access rules for an application, turn on **IP Access Rules** under **Advanced Options**. Existing applications keep their current setting.

To create your first application, refer to [Get started with Spectrum](https://developers.cloudflare.com/spectrum/get-started/).

To share feedback on the redesigned dashboard, complete [this form ↗︎](https://forms.gle/BW9RoXZpgx7B5HZC6).
