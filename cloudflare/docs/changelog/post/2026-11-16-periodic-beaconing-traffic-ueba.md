---
url: https://developers.cloudflare.com/changelog/post/2026-11-16-periodic-beaconing-traffic-ueba/
title: Cloudflare One adds Periodic Beaconing Traffic detection \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-17T10:23:32.347182+00:00
---

# Cloudflare One adds Periodic Beaconing Traffic detection · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-16-periodic-beaconing-traffic-ueba/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 16, 2026

## Cloudflare One adds Periodic Beaconing Traffic detection

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare One now includes Periodic Beaconing Traffic as a risk behavior. It analyzes Gateway HTTP traffic for regular check-ins to the same destination.

Cloudflare flags a user after more than 30 contacts to the same destination in six hours. Contacts must be evenly spaced, from 10 seconds to about 12 minutes apart. Few other users in your organization contact that destination.

Detection uses traffic behavior only. It does not use threat intelligence, categories, or reputation. Malware can check in with a command-and-control (C2) server this way, but legitimate software also checks in regularly. Treat each event as a lead to investigate, not proof that a destination is C2.

By default, the behavior is off and its risk level is Info. To turn it on, go to **Risk score** > **Risk behaviors**. Cloudflare reports a continuing beacon once. Events usually arrive 3 to 6 hours after the six-hour window closes.

Periodic Beaconing Traffic is available on Enterprise plans.
