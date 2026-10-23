---
url: https://developers.cloudflare.com/changelog/post/2026-10-13-audit-logs-v2-view-actions/
title: Audit Logs v2 now captures view actions \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:32.682702+00:00
---

# Audit Logs v2 now captures view actions · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-13-audit-logs-v2-view-actions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 13, 2026

## Audit Logs v2 now captures view actions

[Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Audit Logs v2 now records `view` actions for supported endpoints, providing visibility into read activity across Cloudflare products. These actions correspond to `GET` requests and provide additional context for security investigations and forensic analysis.

The Audit Logs v2 dashboard excludes `view` actions by default to reduce noise. Remove the default **Action type** is not `view` filter to include them, or set **Action type** to `view` to show only view actions.

View actions are always available through the Audit Logs v2 API and Logpush, regardless of the dashboard filter.

Caution

`GET` requests can generate a high volume of audit logs. When using the API or Logpush, apply appropriate filters to limit the volume of delivered logs.

For more information, refer to the [Audit Logs v2 documentation](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/#view-actions).
