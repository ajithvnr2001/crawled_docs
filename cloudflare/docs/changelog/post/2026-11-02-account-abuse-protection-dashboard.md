---
url: https://developers.cloudflare.com/changelog/post/2026-11-02-account-abuse-protection-dashboard/
title: New Account Abuse Protection Dashboard \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-05T09:11:07.457481+00:00
---

# New Account Abuse Protection Dashboard · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-02-account-abuse-protection-dashboard/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 2, 2026

## New Account Abuse Protection Dashboard

[Bots](https://developers.cloudflare.com/bots/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Account Abuse Protection customers in Early Access can now investigate login and sign up activity in a dedicated dashboard under **Security** > **Account Abuse Protection**.

  * Population overview: See total login and sign up events, unique accounts, IPs and devices, top countries and ASNs, and leaked credential check results. Filter accounts by signals such as leaked credential events and unique IPs to find the accounts that need review.
  * Individual Account overview: Review a single Hashed User ID's activity, including its top networks, locations and devices, and an event log with the Ray ID for each event. Mitigate the account with a Security Rule on its Hashed User ID.
  * New roles: The Account Abuse Protection role grants access to the dashboard. Account Abuse Protection PII role grants access to the dashboard as well as account-level PII, such as email address, and is required to create or edit Logpush jobs that include PII. The dashboard includes all login and sign up events from the date the feature was enabled.



For more information, refer to [**Account Abuse Protection**](https://developers.cloudflare.com/bots/account-abuse-protection/).
