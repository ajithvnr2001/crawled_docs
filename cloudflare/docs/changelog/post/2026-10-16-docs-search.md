---
url: https://developers.cloudflare.com/changelog/post/2026-10-16-docs-search/
title: Search Cloudflare documentation with the Cloudflare CLI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:32.236011+00:00
---

# Search Cloudflare documentation with the Cloudflare CLI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-16-docs-search/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 16, 2026

## Search Cloudflare documentation with the Cloudflare CLI

[Workers](https://developers.cloudflare.com/workers/)[Cloudflare CLI](https://developers.cloudflare.com/cf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare CLI `1.0.0-beta.16` includes `cf docs search`, so you and your coding agent can find Cloudflare documentation without leaving the terminal. Search for guides, tutorials, and examples across Cloudflare products.

To install or update to the latest release:

npmyarnpnpmbun
    
    
    npm install --global cf@latest
    
    
    yarn global add cf@latest
    
    
    pnpm add --global cf@latest
    
    
    bun add --global cf@latest

Describe what you want to do, or ask a question:
    
    
    cf docs search "proxy a DNS record"
    cf docs search "rate limit requests with WAF"
    cf docs search "schedule a worker"

The command searches live Cloudflare documentation and returns up to five ranked JSON results. Each result includes a title, description, and documentation URL. An Internet connection is required.

![Terminal demo of Cloudflare CLI beta-16 searching DNS and WAF documentation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1280,height=720,format=webp/_astro/docs-search-demo.cWBK3YBx.gif)

Agents can parse the results and fetch a complete page as Markdown. For example, use `jq` to select the first result, then request its URL with the `Accept: text/markdown` header:
    
    
    url=$(cf docs search "proxy a DNS record" | jq -r '.[0].url')
    curl -H "Accept: text/markdown" "$url"

This release also standardizes generated command names to kebab-case. For example, `cf accounts billing getCredits` becomes `cf accounts billing get-credits`. For the full list of breaking command and flag changes, refer to the [Cloudflare CLI release notes ↗︎](https://github.com/cloudflare/cf/blob/main/packages/cli/CHANGELOG.md).

For more information, refer to [Find Cloudflare documentation with a coding agent](https://developers.cloudflare.com/cf/agents/#find-cloudflare-documentation).
