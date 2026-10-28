---
url: https://developers.cloudflare.com/changelog/post/2026-10-27-introspection-include-attributes/
title: SQL API introspection: `include_attributes` parameter \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-28T08:03:52.988346+00:00
---

# SQL API introspection: `include_attributes` parameter · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-27-introspection-include-attributes/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 27, 2026

## SQL API introspection: `include_attributes` parameter

[Analytics](https://developers.cloudflare.com/analytics/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The SQL API introspection endpoint has a new `include_attributes` query parameter. Setting it to `true` discovers the keys of a dataset's `attributes` JSON column, and their types, from the preceding seven days of your account's data. Discovered keys are returned in the dataset's `attributes` response field.

Some datasets store additional key-value data in an `attributes` JSON column, which you query with exact-key lookups such as `attributes['http.method']`. The previous way to discover these keys, `include_custom_attributes`, returned names in a `custom_attributes` field. The new names make it clearer that each returned name is a key you access through the `attributes` column.

`include_custom_attributes` and `custom_attributes` are deprecated but still work. Update integrations to use `include_attributes` and `attributes`.
    
    
    curl --get "https://api.cloudflare.com/client/v4/analytics/sql/introspection" \
      --header "Authorization: Bearer <API_TOKEN>" \
      --data-urlencode "account_tag=<ACCOUNT_TAG>" \
      --data-urlencode "dataset_name=events.httpRequests" \
      --data-urlencode "include_attributes=true"

For more information, refer to [Attributes](https://developers.cloudflare.com/analytics/sql-api/datasets/#attributes).
