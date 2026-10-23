---
url: https://developers.cloudflare.com/notifications/get-started/
title: Configure alerts \u00b7 Cloudflare Notifications docs
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:51:30.868060+00:00
---

# Configure alerts · Cloudflare Notifications docs

> Source: https://developers.cloudflare.com/notifications/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Notifications](https://developers.cloudflare.com/notifications/)
  3. /Get started



# Configure alerts

Last updated Oct 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPermissionsManage alertsManage destinationsManage silences

This guide covers permissions, management, and delivery configuration for alerts. To create alerts, refer to [Monitors](https://developers.cloudflare.com/notifications/monitors/) or [Platform Notifications](https://developers.cloudflare.com/notifications/notification-available/).

[ Go to **Alerts** ↗ ](https://dash.cloudflare.com/?to=/:account/notifications)

## Permissions

To create an alert, you need one of the following:

  * **Super Administrator** or **Administrator** role in the dashboard
  * **Account edit** role (allows creating any alert type)
  * An API token with the [Notifications Read/Write permission](https://developers.cloudflare.com/fundamentals/api/reference/permissions/)



Some alert types are only available on Professional, Business, or Enterprise plans, or require a specific Cloudflare product.

## Manage alerts

Once created, each alert has an action menu (⋯) with the following options:

  * **Edit** : modify the alert name, delivery destinations, or configuration.
  * **Disable / Enable** : toggle the alert on or off.
  * **Test** : send a test alert with sample data to verify delivery.
  * **Mute** : temporarily suppress the alert for a preset duration (**1h** , **12h** , **24h**) or a custom time range. Muted alerts still appear in [Alert history](https://developers.cloudflare.com/notifications/notification-history/) and are marked as silenced.
  * **Delete** : permanently remove the alert.



## Manage destinations

Destinations define where your alerts are delivered. You can manage all destinations from **Alerts** > **Destinations**.

## Manage silences

You can view, edit, or delete existing silences from **Alerts** > **Silences**.

[ Go to **Alerts** ↗ ](https://dash.cloudflare.com/?to=/:account/notifications)

[PreviousOverview](https://developers.cloudflare.com/notifications/)[NextConfigure PagerDuty](https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/notifications/get-started/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
