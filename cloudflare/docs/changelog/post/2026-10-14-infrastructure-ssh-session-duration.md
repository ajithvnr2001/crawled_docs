---
url: https://developers.cloudflare.com/changelog/post/2026-10-14-infrastructure-ssh-session-duration/
title: Infrastructure applications support a configurable session duration \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:32.547356+00:00
---

# Infrastructure applications support a configurable session duration · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-14-infrastructure-ssh-session-duration/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 14, 2026

## Infrastructure applications support a configurable session duration

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Infrastructure applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) now have a configurable session duration with a default value of 24 hours. You can set the session duration when creating or editing an infrastructure application in the dashboard or via the API.

![Session duration setting in infrastructure application configuration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2824,height=522,format=webp/_astro/infrastructure-ssh-session-duration.DI7ApX89.png)

When the session duration elapses, any active SSH connections through that application will be closed, and users will need to reconnect. Previously, infrastructure applications did not enforce a session duration limit. Sessions could persist beyond 24 hours in some cases, but were never guaranteed beyond 10 hours due to [Gateway connection limits](https://developers.cloudflare.com/cloudflare-one/access-controls/troubleshooting/#long-lived-ssh-sessions-disconnect).

When a target matches multiple infrastructure applications, the shortest session duration applies.

For more information, refer to [Session duration](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#session-duration).
