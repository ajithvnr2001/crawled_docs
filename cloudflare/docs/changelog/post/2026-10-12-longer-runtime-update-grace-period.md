---
url: https://developers.cloudflare.com/changelog/post/2026-10-12-longer-runtime-update-grace-period/
title: More time for requests to finish during Workers runtime updates \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:33.255679+00:00
---

# More time for requests to finish during Workers runtime updates · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-12-longer-runtime-update-grace-period/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 12, 2026

## More time for requests to finish during Workers runtime updates

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Pending requests and connections to Workers now have a grace period of up to 20 minutes during Workers runtime updates. Previously, the grace period was up to 30 seconds.

This gives long-running HTTP requests, streamed AI responses, and live WebSocket sessions more time to continue before an update interrupts them.

![Workers runtime versions: existing work drains on the previous version; new HTTP requests use the updated version](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=920,height=414,format=svg/_astro/runtime-update-grace-period.B6z5mX9l.svg)

New incoming HTTP requests go to the updated version of the Workers runtime once it is ready. Processes running the previous version stop accepting these requests and drain existing work. The grace period applies to each process running the previous version. When it ends, unfinished requests and open connections on that process are terminated.

You should design your application to reconnect WebSockets, safely retry interrupted requests, and recover saved state after a restart. WebSockets can disconnect before the grace period ends, including connections using the [WebSocket Hibernation API](https://developers.cloudflare.com/durable-objects/best-practices/websockets/).

For more information, refer to [Workers runtime updates](https://developers.cloudflare.com/workers/platform/limits/#runtime-updates).
