---
url: https://docs.cloud.google.com/rust/docs/update-field-mask/
title: Update a resource using a field mask \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:34:09.623454+00:00
---

# Update a resource using a field mask  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/update-field-mask/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Update a resource using a field mask Stay organized with collections  Save and categorize content based on your preferences. 

When updating a resource in Google Cloud, you often want to modify specific fields without replacing the entire resource. The Cloud Client Libraries for Rust support field masks so that you can specify which fields an update operation modifies and leave all other fields unchanged.

## Before you begin

This document uses the Secret Manager API, though the same concepts apply to other Google Cloud services.

Before running the code in this document, complete the following prerequisites:

  * Follow [Get started with Rust](https://docs.cloud.google.com/rust/docs/quickstart) to set up your development environment.
  * Follow [Create and access a secret using Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart) to enable the Secret Manager API and configure authentication.



### Dependencies

The `google-cloud-wkt` crate provides well-known types for Google Cloud APIs, including `FieldMask`. Add `google-cloud-secretmanager-v1`, `google-cloud-wkt`, `anyhow`, and `tokio` to your `Cargo.toml` file:
    
    
    cargo add google-cloud-secretmanager-v1 google-cloud-wkt anyhow
    cargo add tokio --features macros,rt-multi-thread
    

## How field masks work

A `FieldMask` contains a set of symbolic field paths that identify which fields an update operation modifies or a read operation returns.

In an update operation, the service changes only the fields listed in the mask and ignores values on any unlisted fields in the request message. If you omit the field mask on an update request, the operation applies to all mutable fields.

To reset a specific field to its default value, include the field path in the mask and leave that field at its default value on the resource struct.

## Update fields on a resource

To create a secret and selectively update its `labels` and `annotations` fields using a `FieldMask`, complete the following steps:

  1. Initialize a `SecretManagerService` client and create a secret with empty `labels` and `annotations`: 
         
         let client = SecretManagerService::builder().build().await?;
         
         let secret = client
             .create_secret()
             .set_parent(format!("projects/{project_id}"))
             .set_secret_id("your-secret")
             .set_secret(
                 Secret::new().set_replication(Replication::new().set_automatic(Automatic::new())),
             )
             .send()
             .await?;
         println!("CREATE = {secret:?}");

  2. Send an `update_secret` request that sets `labels`, `annotations`, the current `etag` to prevent overwriting concurrent updates, and an update mask covering `"annotations"` and `"labels"`: 
         
         let tag = |mut labels: HashMap<_, _>, msg: &str| {
             labels.insert("updated".to_string(), msg.to_string());
             labels
         };
         
         let update = client
             .update_secret()
             .set_secret(
                 Secret::new()
                     .set_name(&secret.name)
                     .set_etag(secret.etag)
                     .set_labels(tag(secret.labels, "your-label"))
                     .set_annotations(tag(secret.annotations, "your-annotations")),
             )
             .set_update_mask(FieldMask::default().set_paths(["annotations", "labels"]))
             .send()
             .await?;
         println!("UPDATE = {update:?}");

The `set_update_mask` call specifies the exact field paths to modify: 
         
         .set_update_mask(FieldMask::default().set_paths(["annotations", "labels"]))




The output confirms that the operation updated both fields:
    
    
    labels: {"updated": "your-label"},
    ...
    annotations: {"updated": "your-annotations"},
    

## Complete code

The following function combines secret creation and the field-mask update:
    
    
    use google_cloud_secretmanager_v1::client::SecretManagerService;
    use google_cloud_secretmanager_v1::model::replication::Automatic;
    use google_cloud_secretmanager_v1::model::{Replication, Secret};
    use google_cloud_wkt::FieldMask;
    use std::collections::HashMap;
    
    pub async fn sample(project_id: &str) -> anyhow::Result<()> {
        let client = SecretManagerService::builder().build().await?;
    
        let secret = client
            .create_secret()
            .set_parent(format!("projects/{project_id}"))
            .set_secret_id("your-secret")
            .set_secret(
                Secret::new().set_replication(Replication::new().set_automatic(Automatic::new())),
            )
            .send()
            .await?;
        println!("CREATE = {secret:?}");
    
        let tag = |mut labels: HashMap<_, _>, msg: &str| {
            labels.insert("updated".to_string(), msg.to_string());
            labels
        };
    
        let update = client
            .update_secret()
            .set_secret(
                Secret::new()
                    .set_name(&secret.name)
                    .set_etag(secret.etag)
                    .set_labels(tag(secret.labels, "your-label"))
                    .set_annotations(tag(secret.annotations, "your-annotations")),
            )
            .set_update_mask(FieldMask::default().set_paths(["annotations", "labels"]))
            .send()
            .await?;
        println!("UPDATE = {update:?}");
    
        Ok(())
    }

## Clean up

To avoid incurring charges to your Google Cloud account and to prevent `ALREADY_EXISTS` errors on subsequent runs, [delete the `your-secret` secret](https://docs.cloud.google.com/secret-manager/docs/delete-secrets) when you're finished.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
