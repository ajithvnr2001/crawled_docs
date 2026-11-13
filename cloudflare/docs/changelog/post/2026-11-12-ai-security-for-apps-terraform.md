---
url: https://developers.cloudflare.com/changelog/post/2026-11-12-ai-security-for-apps-terraform/
title: Manage AI Security for Apps with Terraform \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:04.461047+00:00
---

# Manage AI Security for Apps with Terraform · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-12-ai-security-for-apps-terraform/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 12, 2026

## Manage AI Security for Apps with Terraform

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now manage [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/) with Terraform. Version 5.29.0 of the Terraform Cloudflare provider adds two resources:

  * [`cloudflare_ai_security` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/ai_security): Turns AI Security for Apps on or off for a zone.
  * [`cloudflare_ai_security_custom_topics` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/ai_security_custom_topics): Defines the [custom topics](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/unsafe-topics/#custom-topics) that AI Security for Apps scores each prompt against.



For example:
    
    
    resource "cloudflare_ai_security" "zone_ai_security" {
      zone_id = var.cloudflare_zone_id
      enabled = true
    }
    
    resource "cloudflare_ai_security_custom_topics" "zone_custom_topics" {
      zone_id = var.cloudflare_zone_id
    
      topics = [
        {
          label = "competitors"
          topic = "seeking info on competitors"
        }
      ]
    }

You can then use AI Security for Apps fields in custom rules managed with the `cloudflare_ruleset` resource, keeping your detection settings, topics, and mitigation rules in the same configuration.

For more examples, refer to [Terraform configuration examples](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/terraform-examples/).
