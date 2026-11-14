---
url: https://developers.cloudflare.com/changelog/post/2026-11-13-terraform-namespaces/
title: Manage AI Search instances in any namespace with Terraform \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-14T08:45:52.382873+00:00
---

# Manage AI Search instances in any namespace with Terraform · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-13-terraform-namespaces/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 13, 2026

## Manage AI Search instances in any namespace with Terraform

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Starting with [Cloudflare Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) v5.29.0, you can manage [AI Search](https://developers.cloudflare.com/ai-search/) instances in any [namespace](https://developers.cloudflare.com/ai-search/concepts/namespaces/), not only `default`.

The `cloudflare_ai_search_instance` resource has a new `namespace` argument. It defaults to `default`, so existing configurations keep managing the same instances.
    
    
    resource "cloudflare_ai_search_namespace" "support" {
      account_id = var.account_id
      name       = "support"
    }
    
    resource "cloudflare_ai_search_instance" "docs" {
      account_id = var.account_id
      id         = "docs"
      namespace  = cloudflare_ai_search_namespace.support.name
    }

You can import existing instances and namespaces:
    
    
    terraform import cloudflare_ai_search_instance.docs <account_id>/support/docs
    terraform import cloudflare_ai_search_namespace.support <account_id>/support

The data sources read instances from the namespace you set:
    
    
    data "cloudflare_ai_search_instance" "docs" {
      account_id = var.account_id
      namespace  = "support"
      id         = "docs"
    }
    
    data "cloudflare_ai_search_instances" "support" {
      account_id = var.account_id
      namespace  = "support"
    }

When you upgrade to v5.29.0, review these changes:

  * The `cloudflare_ai_search_instance` import ID now includes the namespace: `<account_id>/<namespace>/<id>`. For instances in the default namespace, use `<account_id>/default/<id>`.
  * The `cloudflare_ai_search_instance` and `cloudflare_ai_search_instances` data sources require `namespace`. Set `namespace = "default"` for instances in the default namespace.
  * `cloudflare_ai_search_instances` returns the instances in one namespace. The `filter.namespace` argument of `cloudflare_ai_search_instance` is removed.
  * Changing `namespace` replaces the instance.


