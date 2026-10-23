---
url: https://developers.cloudflare.com/changelog/post/2026-10-16-cjk-keyword-search/
title: AI Search keyword search supports Japanese, Chinese, and Korean queries \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:32.294198+00:00
---

# AI Search keyword search supports Japanese, Chinese, and Korean queries · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-16-cjk-keyword-search/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 16, 2026

## AI Search keyword search supports Japanese, Chinese, and Korean queries

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) keyword search with the `trigram` tokenizer now matches Japanese, Chinese, and Korean queries, including full natural-language questions such as `経費精算の締め日はいつですか？`. Previously, a query without spaces was treated as a single exact phrase and usually returned no keyword results.

The `porter` tokenizer does not work well for these languages. If your content is in Japanese, Chinese, or Korean, set `keyword_tokenizer` to `trigram`. Changing the tokenizer triggers a full reindex.

Refer to [Keyword search](https://developers.cloudflare.com/ai-search/configuration/indexing/keyword-search/#keyword-tokenizer) for tokenizer details.
