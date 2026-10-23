---
url: https://developers.cloudflare.com/changelog/post/2026-10-14-deny-redirect-account-id/
title: Account context in Access deny redirects \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:32.563183+00:00
---

# Account context in Access deny redirects · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-14-deny-redirect-account-id/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 14, 2026

## Account context in Access deny redirects

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

App-aware Cloudflare Access deny redirects include an `account_id` query parameter when account context is available. Custom block pages can use it to identify the account that owns the application represented by `kid`.

For example, a custom redirect can include:
    
    
    https://denied.example.com/?kid=<APP_AUD>&account_id=<ACCOUNT_ID>&original_url=app.example.com%2Fadmin

The account ID helps block-page integrations look up applications through account-scoped APIs. It is context, not proof of authentication or authorization.

For parameter descriptions and an example, refer to [Custom redirect URL parameters](https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/access-block-page/#custom-redirect-url-parameters).
