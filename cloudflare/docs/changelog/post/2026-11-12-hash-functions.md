---
url: https://developers.cloudflare.com/changelog/post/2026-11-12-hash-functions/
title: New hash functions \u2014 sha1(), md5(), and sha512() \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:05.003628+00:00
---

# New hash functions — sha1(), md5(), and sha512() · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-12-hash-functions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 12, 2026

## New hash functions — sha1(), md5(), and sha512()

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Rules supports three new hash functions: `sha1()`, `md5()`, and `sha512()`. Use them to compute hashes for systems that require these algorithms.

Like the existing `sha256()` function, each accepts a string or byte array and returns raw bytes:

Function | Algorithm | Output length  
---|---|---  
`md5()` | MD5 | 16 bytes  
`sha1()` | SHA-1 | 20 bytes  
`sha512()` | SHA-512 | 64 bytes  
  
For example, combine `sha512()` with `encode_base64()` to produce a Base64-encoded hash:
    
    
    encode_base64(sha512("hello world"))

For details, refer to the [`sha1()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#sha1), [`md5()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#md5), and [`sha512()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#sha512) function references.
