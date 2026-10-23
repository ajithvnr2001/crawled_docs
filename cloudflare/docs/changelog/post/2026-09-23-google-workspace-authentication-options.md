---
url: https://developers.cloudflare.com/changelog/post/2026-09-23-google-workspace-authentication-options/
title: Authentication options for Google Workspace identity providers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:47.765965+00:00
---

# Authentication options for Google Workspace identity providers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-23-google-workspace-authentication-options/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 23, 2026

## Authentication options for Google Workspace identity providers

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-23-google-workspace-authentication-options/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Google Workspace identity provider integrations now include prompt controls and device-scoped login hints in the Cloudflare dashboard and API.

Choose Google's default behavior, silent authentication, consent, or account selection. If silent authentication cannot use an active Google session, Access retries once with Google's default interactive flow.

Access can also send a domain-matched login hint. It sends the hint when one email from a previous Access login on the same device matches the Google Workspace domain.

For configuration details, refer to [Google Workspace authentication options](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/google-workspace/#authentication-options).
