---
url: https://developers.cloudflare.com/changelog/post/2026-11-09-radar-bots-directory-botbase/
title: Redesigned Bots Directory on Cloudflare Radar, now powered by BotBase \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-10T09:28:45.789203+00:00
---

# Redesigned Bots Directory on Cloudflare Radar, now powered by BotBase · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-09-radar-bots-directory-botbase/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 9, 2026

## Redesigned Bots Directory on Cloudflare Radar, now powered by BotBase

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [**Cloudflare Radar**](https://developers.cloudflare.com/radar/) [Bots Directory ↗︎](https://radar.cloudflare.com/bots/directory) now uses [BotBase](https://developers.cloudflare.com/bots/botbase/), Cloudflare's catalog of the bots and agents it tracks, and has a new design matching the Radar homepage.

![Animation filtering the Bots Directory and opening the Cloudflare Crawler bot page, with its Identity and Traffic sections](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1000,height=563,format=webp/_astro/radar-bots-directory-botbase.b-N2AJvi.gif)

Each bot page has a new **Identity** section showing the bot's access level, content use, [Web Bot Auth](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/) verification, and user agents. Bot operators are also searchable from the Radar site search.

#### API

The [List bots](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/list/) and [Get bot details](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/get/) endpoints now describe each bot with:

  * `categories`: a bot can now have more than one category. Categories follow BotBase's groups, which add `COMMERCE`, and some older categories are now part of broader groups.
  * `accessLevel`: `DIRECT` if the bot reaches websites under its own identity, or `INTERMEDIARY` if it acts on behalf of another agent or a person.
  * `contentUse`: `full` if the content it fetches is kept and reused (for example, for model training or a search index), `reference` if it is cited or linked back to the source, or `immediate` if it is used once to answer a user's request.
  * `documentationUrl` and `operatorWebsiteUrl` (bot details only).



`category` and `operatorUrl` are deprecated in favor of `categories` and `documentationUrl`.

Visit the [Bots Directory ↗︎](https://radar.cloudflare.com/bots/directory) on Cloudflare Radar.
