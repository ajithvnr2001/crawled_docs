---
url: https://developers.cloudflare.com/changelog/post/2026-11-25-search-for-agents/
title: Introducing Search for Agents \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-26T10:37:13.806857+00:00
---

# Introducing Search for Agents · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-25-search-for-agents/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 25, 2026

## Introducing Search for Agents

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Search for Agents makes your website searchable by AI agents without manually configuring a search integration. Turn it on under **Quick Actions** on your domain's **Overview** page in the Cloudflare dashboard. Cloudflare creates an AI Search instance, starts indexing your content, and exposes a search endpoint on your domain.

![Search for Agents toggle turned on in the Cloudflare dashboard, with a Beta badge and a link to feature documentation.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=958,height=244,format=webp/_astro/search-for-agents.CkMydMyZ.png)

Cloudflare adds discovery metadata to your HTML pages and, when Markdown for Agents is on, to Markdown responses. Agents can discover the endpoint and search with keywords or natural-language queries:
    
    
    curl --get "https://example.com/.well-known/search" \
      --data-urlencode "q=How do I verify webhook signatures?"

The endpoint supports both `GET` and HTTP `QUERY` requests. It returns relevant content in Markdown, not an AI-generated answer, so agents can use the results with their own models.

Search for Agents is available on all plans. Usage is subject to [AI Search pricing and plan limits](https://developers.cloudflare.com/ai-search/platform/limits-pricing/). You can customize configurable settings in the AI Search instance created for your domain.

Read the [announcement blog post ↗︎](https://blog.cloudflare.com/search-for-agents) and refer to the [Search for Agents guide](https://developers.cloudflare.com/ai-search/how-to/search-for-agents/) for setup instructions and default settings.
