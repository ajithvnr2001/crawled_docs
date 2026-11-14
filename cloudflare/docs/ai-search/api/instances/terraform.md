---
url: https://developers.cloudflare.com/ai-search/api/instances/terraform/
title: Terraform \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-11-14T08:45:51.913153+00:00
---

# Terraform · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/api/instances/terraform/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /…

API

  4. /Instances
  5. /Terraform



# Terraform

Last updated Nov 13, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate an instance Default namespace Custom namespace Instance with a data sourceComputed valuesChanges that replace the instanceImport an instanceData sources Read one instance List instancesRelated resources

Use the [Cloudflare Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) to create, update, import, and read AI Search instances as code. Namespace support for instances is available from provider v5.29.0.

To manage the namespaces themselves, refer to [Namespaces with Terraform](https://developers.cloudflare.com/ai-search/api/namespaces/terraform/).

## Create an instance

Use the `cloudflare_ai_search_instance` resource. The `id` argument is the instance name.

### Default namespace

If you omit `namespace`, Terraform creates the instance in the `default` [namespace](https://developers.cloudflare.com/ai-search/concepts/namespaces/).
    
    
    resource "cloudflare_ai_search_instance" "docs" {
      account_id = var.account_id
      id         = "docs"
    }

An instance without a data source uses [built-in storage](https://developers.cloudflare.com/ai-search/configuration/data-source/built-in-storage/). You can upload documents to it with the [Items API](https://developers.cloudflare.com/ai-search/api/items/rest-api/).

### Custom namespace

To create an instance in a custom namespace, set `namespace`. Reference the `name` of a `cloudflare_ai_search_namespace` resource so that Terraform creates the namespace before the instance.
    
    
    resource "cloudflare_ai_search_namespace" "support" {
      account_id = var.account_id
      name       = "support"
    }
    
    resource "cloudflare_ai_search_instance" "docs" {
      account_id = var.account_id
      id         = "docs"
      namespace  = cloudflare_ai_search_namespace.support.name
    }

### Instance with a data source

Set `type` and `source` to connect a data source. `type` accepts `r2` or `web-crawler`.
    
    
    resource "cloudflare_ai_search_instance" "internal_docs" {
      account_id      = var.account_id
      id              = "internal-docs"
      namespace       = "default"
      type            = "r2"
      source          = "my-docs-bucket"
      max_num_results = 20
    }

For more information, refer to [R2 data source](https://developers.cloudflare.com/ai-search/configuration/data-source/r2/) and [Website data source](https://developers.cloudflare.com/ai-search/configuration/data-source/website/).

## Computed values

AI Search fills in some fields when you create an instance, for example the models (such as `aisearch_model` and `embedding_model`), `chunk_size`, and `token_id`. Terraform treats these fields as computed. If you omit them from your configuration, Terraform keeps the current value instead of planning a change.

## Changes that replace the instance

Caution

Some changes destroy the instance and create a new one. Replacing an instance permanently removes all its indexed data, including embeddings, chunks, and files uploaded to built-in storage.

The following changes replace the instance:

  * Changing `id` or `account_id`.
  * Changing `namespace`.
  * Changing `type`.



Review `terraform plan` output for `must be replaced` before you apply these changes.

## Import an instance

Import an existing instance with an ID in the format `<account_id>/<namespace>/<id>`:
    
    
    terraform import cloudflare_ai_search_instance.docs <account_id>/support/docs

For an instance in the default namespace, use `default` as the namespace:
    
    
    terraform import cloudflare_ai_search_instance.docs <account_id>/default/docs

You can also use an `import` block:
    
    
    import {
      to = cloudflare_ai_search_instance.docs
      id = "${var.account_id}/default/docs"
    }

## Data sources

Set `namespace` on both data sources. Use `default` for the default namespace.

### Read one instance

The `cloudflare_ai_search_instance` data source reads one instance by `id`.
    
    
    data "cloudflare_ai_search_instance" "docs" {
      account_id = var.account_id
      namespace  = "support"
      id         = "docs"
    }

### List instances

The `cloudflare_ai_search_instances` data source returns the instances in one namespace.
    
    
    data "cloudflare_ai_search_instances" "support" {
      account_id = var.account_id
      namespace  = "support"
    }

## Related resources

  * [Namespaces with Terraform](https://developers.cloudflare.com/ai-search/api/namespaces/terraform/)
  * [Instances REST API](https://developers.cloudflare.com/ai-search/api/instances/rest-api/)
  * [Namespaces](https://developers.cloudflare.com/ai-search/concepts/namespaces/)



[PreviousREST API](https://developers.cloudflare.com/ai-search/api/instances/rest-api/)[NextWorkers binding](https://developers.cloudflare.com/ai-search/api/search/workers-binding/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/api/instances/terraform.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
