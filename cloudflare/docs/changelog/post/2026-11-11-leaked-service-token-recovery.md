---
url: https://developers.cloudflare.com/changelog/post/2026-11-11-leaked-service-token-recovery/
title: GitHub automatically detects leaked Access service tokens \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-12T09:30:22.704425+00:00
---

# GitHub automatically detects leaked Access service tokens · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-11-leaked-service-token-recovery/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 11, 2026

## GitHub automatically detects leaked Access service tokens

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

GitHub secret scanning automatically detects Cloudflare Access service token secrets exposed in public repositories and reports them to Cloudflare. Access then disables the affected token and emails account administrators.

Other secret scanning tools can identify Access service tokens using their consistent Client Secret format: `cfast_`, followed by 40 alphanumeric characters and an eight-character hexadecimal checksum. For tools that support custom detection rules, use this regular expression to find possible secrets:
    
    
    cfast_[A-Za-z0-9]{40}[a-f0-9]{8}

This pattern applies to Client Secrets created on or after August 26, 2026, not legacy 64-character hexadecimal secrets. Matching the pattern does not validate the checksum or confirm that the secret is active. For details, refer to [Client Secret format](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#client-secret-format).

#### Recover a leaked service token

Before you can re-enable a leaked token, you must rotate its secret.

Leaked secrets do not support a rotation grace period. When you rotate one, the previous secret is discarded immediately. Update your services with the new secret, then re-enable the token.

For API rotations, omit `previous_client_secret_expires_at`. A future expiration returns `400`. Attempting to re-enable the token before rotation returns `409`.

![Leaked service token rotation dialog warning that the current secret is revoked immediately and the token remains disabled.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=524,height=370,format=webp/_astro/leaked-service-token-rotation.DjbE6paK.png)

For recovery steps and leak metadata fields, refer to [Recover a leaked service token](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#recover-a-leaked-service-token).
