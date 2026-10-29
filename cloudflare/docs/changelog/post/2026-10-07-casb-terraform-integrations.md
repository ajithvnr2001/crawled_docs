---
url: https://developers.cloudflare.com/changelog/post/2026-10-07-casb-terraform-integrations/
title: Create CASB integrations with Terraform \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-29T08:13:59.370657+00:00
---

# Create CASB integrations with Terraform · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-07-casb-terraform-integrations/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 7, 2026

## Create CASB integrations with Terraform

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create Cloudflare CASB integrations using the [Cloudflare Terraform provider](https://developers.cloudflare.com/terraform/). This lets you manage supported integrations alongside your other infrastructure-as-code.

The following example creates a Google Cloud Platform integration:
    
    
    resource "cloudflare_zero_trust_casb_integration" "google_cloud_platform" {
      account_id = var.cloudflare_account_id
      name       = "Google Cloud Platform"
      paused     = false
    
      google_cloud_platform = {
        google_cloud_platform_service_account = {
          service_account_key_json = file("service-account-key.json")
        }
      }
    }

The `cloudflare_zero_trust_casb_integration` resource requires provider version 5.27.0 or later. Version 4 of the provider and integrations that use OAuth are not supported.

For setup instructions and integration guides, refer to [Cloud and SaaS integrations](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/).
