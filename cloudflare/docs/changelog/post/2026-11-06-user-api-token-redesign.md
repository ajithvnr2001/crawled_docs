---
url: https://developers.cloudflare.com/changelog/post/2026-11-06-user-api-token-redesign/
title: User API tokens have a redesigned creation experience \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-06T09:03:45.302323+00:00
---

# User API tokens have a redesigned creation experience · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-06-user-api-token-redesign/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 6, 2026

## User API tokens have a redesigned creation experience

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

User API tokens now use a redesigned dashboard experience that more closely matches Account API tokens, making it easier to create and review user-owned credentials while preserving their user-scoped behavior.

![Redesigned User API token creation flow](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1982,height=1438,format=webp/_astro/2026-11-06-user-api-token-redesign.DtWlHJJL.png)

#### What's new

  * **A more consistent creation flow** : User API tokens now follow the same modern dashboard pattern as Account API tokens, including a clearer create and review experience.
  * **Improved policy editing** : Policies are now easier to read and manage, with inline controls to add, edit, and remove policy blocks before creating the token.
  * **Clearer restrictions during setup** : Expiration presets and client IP address filtering are built directly into the creation flow so you can review token restrictions in one place.



These tokens still act on behalf of the creating user, even though the dashboard experience is now more consistent with Account API tokens. For more information, refer to [Create API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/), [Create tokens via API](https://developers.cloudflare.com/fundamentals/api/how-to/create-via-api/), and [Account API tokens](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/).
