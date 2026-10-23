---
url: https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/guides/policy-reference/
title: Manage policy reference resources \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:09:48.401266+00:00
---

# Manage policy reference resources · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/guides/policy-reference/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Cloud Workload Security](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/)

  4. /[Guides](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/guides/)
  5. /Policy reference resources



# Manage policy reference resources

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a Rego moduleCreate Rego metadataCreate a tenant structure Node import format Edit nodes

Use **Policy reference** resources to share code and data between policies. You need access to manage Cloud Workload Security in your account.

## Create a Rego module

Rego modules hold reusable library code under `lib.`. Write each policy's `policy.` package and `valid` rule in the policy editor.

  1. In the Cloudflare dashboard, select your account and go to **Cloud Workload Security** > **Policy reference** > **Rego modules**.

[ Go to **Rego modules** ↗ ](https://dash.cloudflare.com/?to=/:account/one/cloud-workload-security/rego-modules)
  2. Select **Add Rego module** and enter a **Module name**.

  3. In **Rego source** , enter library code. This example checks whether a request turns off public access:

Library moduletxt
         
         package lib.bucket_rules
         
         private if {
           input.http.request.body.enabled == false
         }

**Package path** is derived from the source and is read-only.

  4. Select **Add Rego module** to save the module.




To call the library from a policy, import it and reference its rule:

Policy sourcetxt
    
    
    package policy.private_bucket
    
    import data.lib.bucket_rules
    
    default valid := false
    
    valid if {
      bucket_rules.private
    }

The policy also requires a filter to select the intended operation. Refer to [Configure policies](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/guides/configure-policies/).

## Create Rego metadata

Metadata stores reusable JSON values. An import path such as `metadata.bucket_rules` exposes the value as `data.metadata.bucket_rules` in Rego.

  1. In the Cloudflare dashboard, go to **Cloud Workload Security** > **Policy reference** > **Rego metadata**.

[ Go to **Rego metadata** ↗ ](https://dash.cloudflare.com/?to=/:account/one/cloud-workload-security/rego-metadata)
  2. Select **Add Rego metadata**. Enter a **Name** and an **Import path** in the format `metadata.<NAME>`.

  3. In **Data** , enter valid JSON. For example:
         
         {
           "require_private_buckets": true
         }

  4. Select **Add Rego metadata** to save the value.




For this example, a policy can read `data.metadata.bucket_rules.require_private_buckets`. Update the metadata to change the shared value without editing each policy.

## Create a tenant structure

Tenant structures describe an AWS or Cloudflare resource hierarchy. An optional **Package path** exposes the hierarchy to Rego, such as `data.tenant.aws.production`.

  1. In the Cloudflare dashboard, go to **Cloud Workload Security** > **Policy reference** > **Tenant structures**.

[ Go to **Tenant structures** ↗ ](https://dash.cloudflare.com/?to=/:account/one/cloud-workload-security/tenant-structures)
  2. Select **Add tenant structure**. Enter a **Name** and select **AWS** or **Cloudflare** for **Application**.

  3. (Optional) Enter a **Package path** using `tenant.aws.<NAME>` or `tenant.cloudflare.<NAME>`, matching your selected application.

  4. In **Nodes** , select **Import nodes** and choose a `.json` file. Review the imported nodes in **Table view** or **JSON view**.

  5. Select **Add tenant structure** to save the structure and nodes.




### Node import format

Use a JSON object keyed by each node's native resource ID. Each value contains `node_kind`, an optional `name`, and `parent` for a child node. Do not add a `native_id` field inside the value.

This AWS example places an account under a root. Replace the example IDs with your resource IDs:

nodes.jsonjson
    
    
    {
    	"r-example": {
    		"node_kind": "root",
    		"name": "Example organization"
    	},
    	"123456789012": {
    		"node_kind": "account",
    		"name": "Production account",
    		"parent": "r-example"
    	}
    }

AWS supports `root`, `ou`, and `account` nodes. Cloudflare supports `org`, `account`, and `zone` nodes. Native IDs must be unique, and each parent must exist in the structure.

### Edit nodes

Open an existing tenant structure to add, edit, or delete nodes in **Table view**. Select **Save** to apply the changes. **JSON view** is read-only.

Policies read mounted nodes by native ID. For example, `data.tenant.aws.production.nodes["123456789012"]` returns the example account node.

[PreviousManage traffic scope](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/guides/manage-traffic-scope/)[NextConfiguration](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/configuration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/cloud-workload-security/guides/policy-reference.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
