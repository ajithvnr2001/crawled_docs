---
url: https://developers.cloudflare.com/changelog/post/2026-11-03-aap-ai-assistant-scope/
title: See which AI assistants act for your users in Account Abuse Protection \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-05T09:11:07.517553+00:00
---

# See which AI assistants act for your users in Account Abuse Protection · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-03-aap-ai-assistant-scope/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 3, 2026

## See which AI assistants act for your users in Account Abuse Protection

[Bots](https://developers.cloudflare.com/bots/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Account Abuse Protection](https://developers.cloudflare.com/bots/account-abuse-protection/) now shows when a recognized AI assistant makes a login or sign up request, and which account it was acting for.

  * **Population overview** : See which AI assistants are active across your users and how many accounts use them.
  * **Account activity** : Every login and sign up event shows whether an AI assistant made the request, and which one.
  * **AI assistant filters** : filter accounts by number of AI assistant events or number of AI assistants.



Use this to investigate and mitigate a single account without blocking an assistant for everyone else who relies on it, and to tune your agent settings in [AI Crawler and Agent access policies](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/).

AI assistant visibility covers login and sign up events only. Requests from assistants that Cloudflare does not recognize appear as ordinary traffic.

For more information, refer to [AI assistants](https://developers.cloudflare.com/bots/account-abuse-protection/#ai-assistants).
