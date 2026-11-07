---
url: https://developers.cloudflare.com/changelog/post/2026-11-06-fast-flux-detection-ueba/
title: Cloudflare One adds fast flux detection to UEBA \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-07T08:31:56.829711+00:00
---

# Cloudflare One adds fast flux detection to UEBA · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-06-fast-flux-detection-ueba/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 6, 2026

## Cloudflare One adds fast flux detection to UEBA

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare One now includes fast flux detection as a predefined risk behavior for user and entity behavior analytics (UEBA). When enabled, detections contribute to a user's risk score.

Fast flux is a DNS technique that rapidly changes the IP addresses returned for a domain. Threat actors can use it to make malicious infrastructure harder to track and take down. Detecting it can help security teams identify potentially risky activity and investigate it sooner.

To turn on fast flux detection, go to **Risk score** > **Risk behaviors** in the Cloudflare Zero Trust dashboard.

Fast flux detection is available on Enterprise plans.

For more information, refer to [User risk score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/).
