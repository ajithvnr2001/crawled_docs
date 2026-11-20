---
url: https://developers.cloudflare.com/changelog/post/2026-11-19-snapshot-all-formats/
title: Capture PDFs, links, scraped elements, and extracted JSON with /snapshot \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-20T09:50:37.755036+00:00
---

# Capture PDFs, links, scraped elements, and extracted JSON with /snapshot · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-19-snapshot-all-formats/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 19, 2026

## Capture PDFs, links, scraped elements, and extracted JSON with /snapshot

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run](https://developers.cloudflare.com/browser-run/)'s [`/snapshot` endpoint](https://developers.cloudflare.com/browser-run/quick-actions/snapshot/) can now return four more formats from a single page load: `pdf`, `links`, `scrape`, and `json`. Before, `/snapshot` returned HTML, screenshots, Markdown, and the accessibility tree, so a workflow that also needed a PDF or structured data had to prepare the same page again in a second request.

Use the new formats when you need to:

  * **PDF** : print the page, with the same `pdfOptions` as the [`/pdf`](https://developers.cloudflare.com/browser-run/quick-actions/pdf-endpoint/) endpoint.
  * **Links** : collect the links on the page, with the same `visibleLinksOnly` and `excludeExternalLinks` options as [`/links`](https://developers.cloudflare.com/browser-run/quick-actions/links-endpoint/).
  * **Scraped elements** : return the elements matched by `elements`, the same payload as [`/scrape`](https://developers.cloudflare.com/browser-run/quick-actions/scrape-endpoint/). `elements` is required when you request it.
  * **Extracted JSON** : extract structured data from the page HTML with [Workers AI](https://developers.cloudflare.com/workers-ai/), with the same `prompt`, `response_format`, and `custom_ai` fields as [`/json`](https://developers.cloudflare.com/browser-run/quick-actions/json-endpoint/). `prompt` or `response_format` is required, and the request incurs Workers AI usage.



Request them through `formats`, the same way as the existing formats. This example returns a PDF, the page links, and the text of each paragraph:
    
    
    const response = await env.BROWSER.quickAction("snapshot", {
    	url: "https://example.com/",
    	formats: ["pdf", "links", "scrape"],
    	elements: [{ selector: "p" }],
    });
    
    const { result } = await response.json();
    console.log(result.pdf);
    console.log(result.links);
    
    
    const response = await env.BROWSER.quickAction("snapshot", {
    	url: "https://example.com/",
    	formats: ["pdf", "links", "scrape"],
    	elements: [{ selector: "p" }],
    });
    
    const { result } = await response.json();
    console.log(result.pdf);
    console.log(result.links);

Formats are captured in a fixed order rather than the order of the `formats` array, and the PDF is printed last because print handlers can change the page. A live page can change between captures, and any format that fails fails the whole request. For JSON snapshots, one `actionTimeout` budget (default 60 seconds, maximum 120 seconds) covers navigation, captures, retries, and the AI request.

You still need to request at least two distinct formats. If you only need one, use the corresponding single-format endpoint.

Refer to the [`/snapshot` documentation](https://developers.cloudflare.com/browser-run/quick-actions/snapshot/) for the full list of accepted values and options.
