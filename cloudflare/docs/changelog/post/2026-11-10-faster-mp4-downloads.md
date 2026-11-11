---
url: https://developers.cloudflare.com/changelog/post/2026-11-10-faster-mp4-downloads/
title: Faster MP4 downloads from Cloudflare Stream \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:00:58.506016+00:00
---

# Faster MP4 downloads from Cloudflare Stream · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-10-faster-mp4-downloads/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 10, 2026

## Faster MP4 downloads from Cloudflare Stream

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Generating [MP4 downloads from Cloudflare Stream](https://developers.cloudflare.com/stream/viewing-videos/download-videos/#generate-downloadable-mp4-files) is now up to 40% faster, with no changes to your implementation required. This improvement is most impactful for on-demand videos over 1 minute in duration.

You can generate an MP4 download in the Dashboard, with the [`cf`, the Cloudflare CLI](https://developers.cloudflare.com/cf/) CLI, or by sending a `POST` request.

cf clish
    
    
    cf stream videos downloads create default --identifier "$VIDEO_UID"

Create downloadbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/stream/$IDENTIFIER/downloads/default" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Both of these response include the download URL and processing progress:
    
    
    {
    	"result": {
    		"default": {
    			"status": "inprogress",
    			"percentComplete": 75.0,
    			"url": "https://customer-<CODE>.cloudflarestream.com/<VIDEO_UID>/downloads/default.mp4"
    		}
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

For more information, refer to [Generate downloadable MP4 files](https://developers.cloudflare.com/stream/viewing-videos/download-videos/#generate-downloadable-mp4-files).
