---
url: https://developers.cloudflare.com/changelog/post/2026-11-24-ai-security-prompt-logging/
title: Updated prompt logging for AI Security for Apps \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-25T10:59:48.298768+00:00
---

# Updated prompt logging for AI Security for Apps · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-24-ai-security-prompt-logging/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 24, 2026

## Updated prompt logging for AI Security for Apps

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To log prompt content for AI Security for Apps, configure [payload logging](https://developers.cloudflare.com/waf/payload-logging/configure-api/) and use a WAF custom rule that references a field with the `cf.llm.prompt` prefix.

When a custom rule matches, payload logging stores the extracted prompt. If no prompt is extracted and analysis falls back to the full request body, payload logging stores the full request body.

This workflow replaces the previous AI Security Log Mode Ruleset procedure. For more information, refer to [Log prompts for matching rules](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/get-started/#7-optional-log-prompts-for-matching-rules).
