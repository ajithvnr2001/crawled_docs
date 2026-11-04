---
url: https://developers.cloudflare.com/changelog/post/2026-11-02-service-token-tags/
title: Organize and authorize Access service tokens with tags \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-04T08:48:16.604502+00:00
---

# Organize and authorize Access service tokens with tags · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-02-service-token-tags/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 2, 2026

## Organize and authorize Access service tokens with tags

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now assign key-value tags to [Access service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#tag-service-tokens) and use those tags to organize credentials or control application access. Each token supports up to five tags, such as `environment: production` or `team: payments`.

Add or edit tags when you create or update a token in the dashboard or service token API. You can search and filter by tag on the **Service Tokens** page. Tags also appear in [Resource Tagging](https://developers.cloudflare.com/resource-tagging/), where you can query them alongside other tagged resources.

The **Service Token Tag** policy selector matches valid tokens with an exact key-value pair. Use it in a **Service Auth** policy to authorize tokens by environment or team without listing each token individually. For example, this API policy configuration accepts valid tokens tagged `environment: production`:
    
    
    {
    	"name": "Production service tokens",
    	"decision": "non_identity",
    	"include": [
    		{
    			"service_token_tag": {
    				"key": "environment",
    				"value": "production"
    			}
    		}
    	]
    }

For setup instructions, refer to [Tag service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#tag-service-tokens) and [Authorize service tokens by tag](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#authorize-service-tokens-by-tag).
