---
url: https://developers.cloudflare.com/notifications/
title: Cloudflare Alerts \u00b7 Cloudflare Notifications docs
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:51:30.857977+00:00
---

# Cloudflare Alerts · Cloudflare Notifications docs

> Source: https://developers.cloudflare.com/notifications/

  1. [Home](https://developers.cloudflare.com/)
  2. /Notifications



# Alerts

Last updated Oct 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMonitorsPlatform NotificationsDelivery methodsGet startedMonitorsPlatform NotificationsAlert historyAPI referenceReference

Alerts is part of [Cloudflare Observability](https://developers.cloudflare.com/observability/). In the dashboard, you can find it under **Observability** > **Alerts**.

Alerts are organized into two categories: **Monitors** that you define yourself, and **Platform Notifications** that Cloudflare evaluates automatically.

## Monitors

Monitors evaluate a SQL API query on a schedule and send a notification when the result meets your detection criteria. You choose the dataset, define the query, and select a detection method: threshold, anomaly detection, or service-level objective (SLO). Refer to [Monitors](https://developers.cloudflare.com/notifications/monitors/) for configuration details.

## Platform Notifications

Platform Notifications are pre-configured alert types tied to specific Cloudflare products. You enable the ones you care about, choose where they are delivered, and Cloudflare evaluates the trigger conditions. They cover products such as DDoS Protection, SSL/TLS, Health Checks, Load Balancing, and Billing. Refer to [Platform Notifications](https://developers.cloudflare.com/notifications/notification-available/) for the full list.

## Delivery methods

All alerts can be delivered to:

  * **Email** (all plans)
  * **[Webhooks](https://developers.cloudflare.com/notifications/get-started/configure-webhooks/)** (all plans; accounts without a paid zone can configure up to 100 webhook destinations)
  * **[PagerDuty](https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/)** (Business and higher)
  * **Connected services** , including coding agents



## [Get started](https://developers.cloudflare.com/notifications/get-started/)

Create and manage alerts from the Cloudflare dashboard. Configure where alerts are delivered.

## [Monitors](https://developers.cloudflare.com/notifications/monitors/)

Define custom threshold, anomaly detection, and SLO monitors on SQL API datasets.

## [Platform Notifications](https://developers.cloudflare.com/notifications/notification-available/)

Browse built-in notification types organized by Cloudflare product.

## [Alert history](https://developers.cloudflare.com/notifications/notification-history/)

View a log of alerts that have been sent on your account.

## [API reference](https://developers.cloudflare.com/notifications/api-reference/)

Manage alerts programmatically using the Cloudflare API.

## [Reference](https://developers.cloudflare.com/notifications/reference/)

Troubleshooting, common errors, and details on specific alert types.

[NextConfigure alerts](https://developers.cloudflare.com/notifications/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/notifications/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
