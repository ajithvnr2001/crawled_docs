---
url: https://developers.cloudflare.com/changelog/post/2026-11-27-multipart-inspection-fields/
title: Inspect multipart part headers, preambles, and empty parts \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:26.954011+00:00
---

# Inspect multipart part headers, preambles, and empty parts · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-27-multipart-inspection-fields/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 27, 2026

## Inspect multipart part headers, preambles, and empty parts

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Five new Rules fields provide more detail about multipart request bodies:

Field | Contents  
---|---  
`http.request.body.multipart.headers` | Standard and custom headers grouped by lowercase name for each part.  
`http.request.body.multipart.headers.names` | Header names in original case and occurrence order for each part.  
`http.request.body.multipart.headers.values` | Header values aligned with the names for each part.  
`http.request.body.multipart.preamble` | Original bytes before the first boundary delimiter.  
`http.request.body.multipart.empty_parts_count` | Headerless, empty-body parts skipped during parsing.  
  
For example, match a custom header on the first parsed part:
    
    
    http.request.body.multipart.headers[0]["x-upload-tag"][0] eq "review"

Header arrays preserve part association and duplicate headers. The preamble includes the line ending before the first delimiter. The empty-part count includes only parts encountered before parsing stops.

These fields require an Enterprise plan. Request body inspection and multipart parsing limits apply.

For details, refer to the [multipart headers](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart.headers/), [preamble](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart.preamble/), and [empty-part count](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart.empty_parts_count/) field references.
