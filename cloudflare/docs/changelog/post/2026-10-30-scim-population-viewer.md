---
url: https://developers.cloudflare.com/changelog/post/2026-10-30-scim-population-viewer/
title: Inspect provisioned users and groups with the SCIM population viewer \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:17.564831+00:00
---

# Inspect provisioned users and groups with the SCIM population viewer · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-30-scim-population-viewer/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 30, 2026

## Inspect provisioned users and groups with the SCIM population viewer

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The SCIM population viewer lets you inspect the users and groups provisioned to Cloudflare One by each identity provider. You can check which resources Cloudflare has received without making API requests or opening a support ticket.

In **Zero Trust** > **Integrations** > **Identity providers** , select a user or group count in **SCIM resources** to open the viewer. You can:

  * Search users by username, email, name, or resource ID, and groups by name or resource ID.
  * Inspect resource attributes in formatted or JSON views.
  * View group members and compare Cloudflare and IdP resource IDs with provisioning logs.
  * Delete individual resources from the Cloudflare SCIM population when you have edit permission.

![SCIM users table with search controls and blurred personal information](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1132,height=960,format=webp/_astro/scim-population-viewer.CFxa6Ccp.png)

The viewer shows provisioned resources rather than provisioning event history. Use [SCIM provisioning logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/scim-logs/) to investigate failed requests. Existing SCIM deprovisioning and policy behavior remain unchanged.

For dashboard instructions and API examples, refer to [View SCIM users and groups](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim-population-viewer/).
