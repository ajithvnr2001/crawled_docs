---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/performance/early-hints-for-saas/
title: Early Hints for SaaS \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-16T06:38:29.730639+00:00
---

# Early Hints for SaaS · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/performance/early-hints-for-saas/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)

  4. /[Performance](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/performance/)
  5. /Early Hints for SaaS



# Early Hints for SaaS

Last updated Oct 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesEnable Early Hints per custom hostname via the API

[Early Hints](https://developers.cloudflare.com/cache/advanced-configuration/early-hints/) allows the browser to begin loading resources while the origin server is compiling the full response. This improves webpage’s loading speed for the end user. As a SaaS provider, you may prioritize speed for some of your custom hostnames. Using custom metadata, you can [enable Early Hints](https://developers.cloudflare.com/cache/advanced-configuration/early-hints/#enable-early-hints) per custom hostname.

* * *

## Prerequisites

Before you can employ Early Hints for SaaS, you need to create a custom hostname. Review [Get Started with Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/) if you have not already done so.

* * *

## Enable Early Hints per custom hostname via the API

  1. [Locate your zone ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/), available in the Cloudflare dashboard.

  2. Locate your Authentication Key on the [**API Tokens** ↗︎](https://dash.cloudflare.com/?to=/:account/profile/api-tokens) page, under **Global API Key**.

  3. If you are [creating a new custom hostname](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/create/), make an API call such as the example below, specifying `"early_hints": "on"`:




Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `SSL and Certificates Write`

Create Custom Hostnamebash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_hostnames" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"hostname": "<CUSTOM_HOSTNAME>",
    		"ssl": {
    				"method": "http",
    				"type": "dv",
    				"settings": {
    						"http2": "on",
    						"min_tls_version": "1.2",
    						"tls_1_3": "on",
    						"early_hints": "on"
    				},
    				"bundle_method": "ubiquitous",
    				"wildcard": false
    		}
    	}'

  4. For an existing custom hostname, use a `GET` call to retrieve its `id` and current `ssl.settings` values:



Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `SSL and Certificates Write`
  * `SSL and Certificates Read`

List Custom Hostnamesbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_hostnames?hostname=%7Bhostname%7D" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

For example, the response may contain the following settings:
    
    
    {
      "ssl": {
        "settings": {
          "ciphers": [
            "ECDHE-ECDSA-AES128-GCM-SHA256",
            "ECDHE-RSA-AES128-GCM-SHA256"
          ],
          "early_hints": "off",
          "http2": "on",
          "min_tls_version": "1.2",
          "tls_1_3": "on"
        }
      }
    }

  5. Copy the complete `ssl.settings` object from the response. Change only `early_hints` to `on`, then make a `PATCH` call:



Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `SSL and Certificates Write`

Edit Custom Hostnamebash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_hostnames/$CUSTOM_HOSTNAME_ID" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"ssl": {
    				"settings": {
    						"ciphers": [
    								"ECDHE-ECDSA-AES128-GCM-SHA256",
    								"ECDHE-RSA-AES128-GCM-SHA256"
    						],
    						"early_hints": "on",
    						"http2": "on",
    						"min_tls_version": "1.2",
    						"tls_1_3": "on"
    				}
    		}
    	}'

A `PATCH` request replaces the existing `ssl.settings` object. The example copies every setting from the sample response. Copy the values from your response, and omit settings that were not present.

[PreviousCache for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/performance/cache-for-saas/)[NextAnalytics](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/hostname-analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/performance/early-hints-for-saas.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
