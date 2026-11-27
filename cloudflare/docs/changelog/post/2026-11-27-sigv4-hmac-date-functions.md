---
url: https://developers.cloudflare.com/changelog/post/2026-11-27-sigv4-hmac-date-functions/
title: Sign storage requests with HMAC and automatic UTC dates \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-27T10:39:57.737838+00:00
---

# Sign storage requests with HMAC and automatic UTC dates · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-27-sigv4-hmac-date-functions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 27, 2026

## Sign storage requests with HMAC and automatic UTC dates

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Rules language supports HMAC signing, Signature Version 4 (SigV4) key derivation, and UTC date formatting. Use these functions in Request Header Transform Rules to authenticate reads from private Amazon S3 and Google Cloud Storage buckets.

  * `hmac_md5()`, `hmac_sha1()`, `hmac_sha256()`, and `hmac_sha512()` compute raw keyed digests.
  * `sign_sigv4_hmac_sha256()` derives the signing key and returns the lowercase hexadecimal signature in one call.
  * `format_date()` formats the request timestamp for date headers and credential scopes.
  * `encode_hex()` converts raw digests to lowercase hexadecimal text.



For example, set `x-amz-date` or `x-goog-date` dynamically using:
    
    
    format_date(http.request.timestamp.sec, "%Y%m%dT%H%M%SZ")

The same rule can build an `Authorization` header from that request timestamp. Callers do not need to supply a date header. You remain responsible for constructing the canonical request and string to sign.

The HMAC and SigV4 signing functions are available on Pro, Business, and Enterprise plans. `format_date()` is available on all plans without an additional entitlement. Use it in URI, request header, and response header rewrite expressions, not rule filters.

For complete expressions and security considerations, refer to [Sign requests to private S3 and GCS buckets](https://developers.cloudflare.com/rules/transform/examples/sign-private-storage-requests/) and the [Rules language function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/).
