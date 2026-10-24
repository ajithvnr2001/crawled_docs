---
url: https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/
title: Token formats \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-24T07:00:53.732053+00:00
---

# Token formats · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /…

Cloudflare's API

  4. /Get started
  5. /Token formats



# Token formats

Last updated Oct 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLeaked token detection GitHub Secret ScanningPre-2026 formatsWrangler OAuth access tokensVerify a token

Cloudflare API keys and API tokens use a prefixed, scannable format that makes them identifiable by credential scanning tools. Each credential type in the following table has a distinct prefix followed by 40 characters and a checksum.

Credential type | Description | Format  
---|---|---  
Global API Key | Global key tied to your user account (full access) | `cfk_[40 characters][checksum]`  
User API Token | Scoped token you create for specific permissions | `cfut_[40 characters][checksum]`  
Account API Token | Token owned by the account, not tied to a specific user | `cfat_[40 characters][checksum]`  
  
Existing tokens continue to work. Every new token you create or [roll](https://developers.cloudflare.com/fundamentals/api/how-to/roll-token/) uses the scannable format automatically.

## Leaked token detection

The prefixed format and checksum allow credential scanning tools to detect leaked Cloudflare tokens with high confidence. Cloudflare partners with credential scanning providers to proactively find your leaked tokens and revoke them before they can be used maliciously.

### GitHub Secret Scanning

Cloudflare participates in [GitHub's Secret Scanning program ↗︎](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning). GitHub scans every commit for Cloudflare API credentials in both public and private repositories.

  * **Public repositories** — When GitHub detects a leaked Cloudflare token, it verifies the token using the checksum and sends Cloudflare a webhook. Cloudflare automatically revokes the token and notifies you by email so you can generate a replacement.
  * **Private repositories** — GitHub notifies you about any leaked Cloudflare tokens so you can rotate them.



## Pre-2026 formats

Tokens created before the scannable format was introduced use unprefixed strings. These tokens continue to work. Cloudflare scans for and revokes leaked tokens in both the old and new formats.

Credential type | Old format  
---|---  
Global API Key | 37–45 character lowercase hex string  
User API Token | 40-character alphanumeric string  
Account API Token | 40-character alphanumeric string  
  
## Wrangler OAuth access tokens

When you authenticate with [`wrangler login`](https://developers.cloudflare.com/workers/wrangler/commands/general/#login), Wrangler receives a user OAuth access token that starts with `cfoat_`. Run [`wrangler auth token`](https://developers.cloudflare.com/workers/wrangler/commands/general/#auth-token) to retrieve the current token for use with another tool or script. The command automatically refreshes the token if it has expired.

Treat the returned value as a secret. Do not commit it to source control or share it.

## Verify a token

To check that a user API token is valid, send it to the [Verify Token](https://developers.cloudflare.com/api/resources/user/subresources/tokens/methods/verify/) endpoint:
    
    
    curl "https://api.cloudflare.com/client/v4/user/tokens/verify" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

If the token is valid, the response includes the token's `id` and a `status` of `active`.

[PreviousGet Origin CA keys](https://developers.cloudflare.com/fundamentals/api/get-started/ca-keys/)[NextAccount API tokens](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/api/get-started/token-formats.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
