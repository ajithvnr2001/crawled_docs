---
url: https://developers.cloudflare.com/changelog/post/2026-11-03-crawl-result-diagnostics/
title: Crawl results include URL outcomes and robots.txt diagnostics \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-04T08:48:16.543783+00:00
---

# Crawl results include URL outcomes and robots.txt diagnostics · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-03-crawl-result-diagnostics/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 3, 2026

## Crawl results include URL outcomes and robots.txt diagnostics

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Browser Run [`/crawl` results](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/#request-results-of-the-crawl-job) now include more detailed diagnostics. Each URL record can include an `outcome` that identifies the specific processing result, such as `success`, `robots_disallowed`, `timeout`, or `page_error`.

The job-level `robots` array reports the `robots.txt` state for up to 50 origins encountered by the crawl. Each entry includes the origin, whether usable rules were available, and the HTTP status when the crawler received a response.
    
    
    {
    	"robots": [
    		{
    			"origin": "https://example.com",
    			"state": "available",
    			"status": 200
    		}
    	],
    	"records": [
    		{
    			"url": "https://example.com/docs/",
    			"status": "completed",
    			"outcome": "success"
    		}
    	]
    }

For field definitions and all possible outcome values, refer to [URL outcomes](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/#url-outcomes) and [robots.txt diagnostics](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/#robotstxt-diagnostics).
