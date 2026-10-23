---
url: https://developers.cloudflare.com/changelog/post/2026-10-23-undelete-seven-day-window/
title: D1 database undelete requests limited to the last 7 days \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:48.857883+00:00
---

# D1 database undelete requests limited to the last 7 days · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-23-undelete-seven-day-window/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 23, 2026

## D1 database undelete requests limited to the last 7 days

[D1](https://developers.cloudflare.com/d1/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-23-undelete-seven-day-window/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [D1 undelete API](https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/undelete/) now only accepts requests for databases that were deleted within the last 7 days. Requests to undelete a database that was deleted more than 7 days ago will fail and return an error.

If you delete a D1 database by mistake, send the undelete request as soon as possible, and no later than 7 days after deletion.

For more information, refer to the [undelete D1 database API reference](https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/undelete/).
