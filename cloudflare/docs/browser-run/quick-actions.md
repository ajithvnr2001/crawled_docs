---
url: https://developers.cloudflare.com/browser-run/quick-actions/
title: Quick Actions \u00b7 Cloudflare Browser Run docs
method: scrapling+scrapegraph
fetched_at: 2026-11-14T08:45:55.827508+00:00
---

# Quick Actions · Cloudflare Browser Run docs

> Source: https://developers.cloudflare.com/browser-run/quick-actions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Browser Run](https://developers.cloudflare.com/browser-run/)
  3. /Quick Actions



# Quick Actions

Last updated Nov 13, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you begin REST API Workers binding Test Quick Actions locally

Quick Actions provide simple interfaces for common browser tasks like capturing screenshots, extracting HTML content, generating PDFs, and more. You can use Quick Actions in two ways:

  * **REST API** : HTTP endpoints for one-off requests or external integration.
  * **Workers Bindings** : Call Quick Actions directly from a [Cloudflare Worker](https://developers.cloudflare.com/workers/) using `env.BROWSER.quickAction()`.



The following are the available options:

  * [/content - Fetch HTML](https://developers.cloudflare.com/browser-run/quick-actions/content-endpoint/)
  * [/screenshot - Capture screenshot](https://developers.cloudflare.com/browser-run/quick-actions/screenshot-endpoint/)
  * [/pdf - Render PDF](https://developers.cloudflare.com/browser-run/quick-actions/pdf-endpoint/)
  * [/markdown - Extract Markdown from a webpage](https://developers.cloudflare.com/browser-run/quick-actions/markdown-endpoint/)
  * [/snapshot - Capture multiple page formats](https://developers.cloudflare.com/browser-run/quick-actions/snapshot/)
  * [/accessibilityTree - Capture accessibility tree](https://developers.cloudflare.com/browser-run/quick-actions/accessibility-tree-endpoint/)
  * [/scrape - Scrape HTML elements](https://developers.cloudflare.com/browser-run/quick-actions/scrape-endpoint/)
  * [/json - Capture structured data using AI](https://developers.cloudflare.com/browser-run/quick-actions/json-endpoint/)
  * [/links - Retrieve links from a webpage](https://developers.cloudflare.com/browser-run/quick-actions/links-endpoint/)
  * [/crawl - Crawl web content](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/)
  * [Reference](https://developers.cloudflare.com/api/resources/browser_rendering/)



[`/crawl`](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/) is available via the REST API only.

Use Quick Actions when you need a fast, simple way to perform common browser tasks such as capturing screenshots, extracting HTML, or generating PDFs without writing complex scripts. For more advanced automation, custom workflows, or persistent browser sessions, use [Puppeteer](https://developers.cloudflare.com/browser-run/puppeteer/), [Playwright](https://developers.cloudflare.com/browser-run/playwright/), or [CDP](https://developers.cloudflare.com/browser-run/cdp/).

## Before you begin

### REST API

To use Quick Actions via the REST API, [create a custom API Token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with the following permissions:

  * `Browser Run - Edit`



### Workers binding

To use Quick Actions from a [Worker](https://developers.cloudflare.com/workers/), configure a [browser binding](https://developers.cloudflare.com/browser-run/reference/wrangler/#bindings) in your `wrangler.json`. No API token is needed when using the Workers binding.
    
    
    {
      "browser": {
        "binding": "BROWSER"
      }
    }

Caution

The `.quickAction()` method requires a compatibility date of `2026-03-24` or later.
    
    
    {
      "compatibility_date": "2026-03-24",
      "browser": {
        "binding": "BROWSER"
      }
    }

### Test Quick Actions locally

Under `npx wrangler dev`, `.quickAction()` uses a Chrome instance on your machine. It returns the same responses and errors as Browser Run, with two exceptions:

  * The `json` action returns placeholder data, because [Workers AI](https://developers.cloudflare.com/workers-ai/) is not available locally. If a field in `response_format.json_schema` sets `const`, `enum`, or `default`, it gets that value, or the first `enum` entry. Other fields get an empty value, such as `""`, `0`, `false`, or `[]`. Wrangler also logs a warning.
  * The [Kitesurf](https://developers.cloudflare.com/browser-run/kitesurf/) browser is not available. If you pass `browser: "kitesurf"`, `.quickAction()` throws an error.



To get real `json` results or use Kitesurf during local development, set `"remote": true` in your browser binding configuration:
    
    
    {
      "browser": {
        "binding": "BROWSER",
        "remote": true
      }
    }

Note

You can monitor Browser Run (formerly Browser Rendering) usage in two ways:

  * In the Cloudflare dashboard, go to the **Browser Run** page to view aggregate metrics, including total Quick Actions requests and total browser hours used. [ Go to **Browser Run** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/browser-run)
  * `X-Browser-Ms-Used` header: Returned in every Quick Actions response, reporting browser time used for that request (in milliseconds).



[PreviousGet started](https://developers.cloudflare.com/browser-run/get-started/)[Next/content - Fetch HTML](https://developers.cloudflare.com/browser-run/quick-actions/content-endpoint/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/browser-run/quick-actions/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
