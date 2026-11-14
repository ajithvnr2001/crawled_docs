---
url: https://developers.cloudflare.com/ai-search/api/namespaces/terraform/
title: Terraform \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-11-14T08:45:51.796378+00:00
---

# Terraform · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/api/namespaces/terraform/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /…

API

  4. /Namespaces
  5. /Terraform



# Terraform

Last updated Nov 13, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a namespace Arguments Attributes Changes that replace the namespaceCreate a namespace with an instanceImport a namespaceData sources Read one namespace List namespacesRelated resources

Use the [Cloudflare Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) to create, update, import, and read AI Search [namespaces](https://developers.cloudflare.com/ai-search/concepts/namespaces/) as code. To create instances in a namespace you manage with Terraform, use provider v5.29.0 or later.

## Create a namespace

Use the `cloudflare_ai_search_namespace` resource.
    
    
    resource "cloudflare_ai_search_namespace" "support" {
      account_id  = var.account_id
      name        = "support"
      description = "Customer support content"
    }

### Arguments

Argument | Required | Description  
---|---|---  
`account_id` | Yes | Your Cloudflare account ID.  
`name` | Yes | The namespace name. Use 1 to 28 lowercase letters, digits, and hyphens. The name must start and end with a letter or digit.  
`description` | No | A description of up to 256 characters.  
`public_endpoint_params` | No | The namespace public endpoint configuration. Refer to [Namespace public endpoints](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/namespace/).  
  
### Attributes

Attribute | Description  
---|---  
`id` | The namespace name. Same value as `name`.  
`created_at` | When the namespace was created, as an RFC 3339 timestamp.  
`public_endpoint_id` | The identifier of the namespace public endpoint, if one exists.  
  
### Changes that replace the namespace

Changing `name` or `account_id` replaces the namespace. Terraform deletes the old namespace and creates a new one. Changing `description` or `public_endpoint_params` updates the namespace in place.

A namespace that still contains instances cannot be deleted. Move or delete its instances before you change its name.

## Create a namespace with an instance

Set `namespace` on a `cloudflare_ai_search_instance` to the `name` of the namespace resource. The reference makes Terraform create the namespace before the instance, and destroy the instance before the namespace.
    
    
    resource "cloudflare_ai_search_namespace" "support" {
      account_id = var.account_id
      name       = "support"
    }
    
    resource "cloudflare_ai_search_instance" "docs" {
      account_id = var.account_id
      id         = "docs"
      namespace  = cloudflare_ai_search_namespace.support.name
    }

AI Search rejects deleting a namespace that still contains instances. If an instance in the namespace is not managed in the same configuration, or does not reference the namespace resource, `terraform destroy` fails until you move or delete that instance.

For more instance options, refer to [Instances with Terraform](https://developers.cloudflare.com/ai-search/api/instances/terraform/).

## Import a namespace

Import an existing namespace with an ID in the format `<account_id>/<name>`:
    
    
    terraform import cloudflare_ai_search_namespace.support <account_id>/support

You can also use an `import` block:
    
    
    import {
      to = cloudflare_ai_search_namespace.support
      id = "${var.account_id}/support"
    }

## Data sources

### Read one namespace

The `cloudflare_ai_search_namespace` data source reads one namespace. Set either `name` or a `filter` object with `search`, for example `filter = { search = "support" }`.
    
    
    data "cloudflare_ai_search_namespace" "support" {
      account_id = var.account_id
      name       = "support"
    }

### List namespaces

The `cloudflare_ai_search_namespaces` data source lists the namespaces in an account. Use the optional `search` argument to return only namespaces whose name or description contains a string, and `max_items` to limit the number of results. The namespaces are returned in `result`.
    
    
    data "cloudflare_ai_search_namespaces" "all" {
      account_id = var.account_id
    }

## Related resources

  * [Instances with Terraform](https://developers.cloudflare.com/ai-search/api/instances/terraform/)
  * [Namespaces REST API](https://developers.cloudflare.com/ai-search/api/namespaces/rest-api/)
  * [Namespaces](https://developers.cloudflare.com/ai-search/concepts/namespaces/)



[PreviousREST API](https://developers.cloudflare.com/ai-search/api/namespaces/rest-api/)[NextWorkers binding](https://developers.cloudflare.com/ai-search/api/instances/workers-binding/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/api/namespaces/terraform.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
