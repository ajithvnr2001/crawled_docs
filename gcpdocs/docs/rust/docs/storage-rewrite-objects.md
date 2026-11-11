---
url: https://docs.cloud.google.com/rust/docs/storage-rewrite-objects/
title: Rewrite Cloud Storage objects \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T05:43:22.657186+00:00
---

# Rewrite Cloud Storage objects  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/storage-rewrite-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Rewrite Cloud Storage objects Stay organized with collections  Save and categorize content based on your preferences. 

Rewriting an object in Cloud Storage copies or transforms an existing object, such as moving it across locations, rotating its encryption key, or changing its [storage class](https://docs.cloud.google.com/storage/docs/storage-classes). Depending on the object size and the [rewrite parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite), Cloud Storage might complete the operation in a single call or return intermediate progress with a `rewrite_token`. When a call returns a `rewrite_token`, pass that token to subsequent requests until the rewrite finishes.

This document shows you how to configure a rewrite request and drive the rewrite loop using the `rewrite_until_done` helper or a manual loop in the Cloud Client Libraries for Rust. If you're new to the client library, see [Using Cloud Storage with Rust](https://docs.cloud.google.com/rust/docs/quickstart-storage) first.

## Before you begin

Before running the code in this document, complete the following prerequisites:

  * Create or select a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) with [billing enabled](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).
  * Create a dedicated test [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) in your project.
  * Configure [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) for your environment.
  * Grant your principal an Identity and Access Management (IAM) role with permission to read, write, and delete objects in the bucket, such as Storage Admin (`roles/storage.admin`).



### Dependencies

Add the Cloud Storage client library and supporting crates to your `Cargo.toml` file:
    
    
    cargo add google-cloud-storage google-cloud-gax anyhow bytes
    cargo add tokio --features macros,rt-multi-thread
    

## Prepare the client and rewrite request

Both the automatic helper and manual loop start from a configured `StorageControl` client and `RewriteObject` request builder. Inside a scope that accepts `bucket_name` in the format `projects/_/buckets/BUCKET_ID`, complete the following steps:

  1. Initialize a `StorageControl` client with a retry policy. We recommend allowing at least 30 seconds per request. This example uses `RetryableErrors` with a 5-attempt limit and no per-operation [overall time limit](https://docs.rs/google-cloud-gax/latest/google_cloud_gax/retry_policy/trait.RetryPolicyExt.html#method.with_time_limit): 
         
         let control = StorageControl::builder()
             .with_retry_policy(RetryableErrors.with_attempt_limit(5))
             .build()
             .await?;

  2. Create the `rewrite_object` request builder, mark the request idempotent so that the client can retry transient errors, and set the source and destination bucket and object names: 
         
         let mut builder = control
             .rewrite_object()
             .with_idempotency(true) // retry transient errors
             .set_source_bucket(bucket_name)
             .set_source_object(&source_object.name)
             .set_destination_bucket(bucket_name)
             .set_destination_name("rewrite-object-clone");

  3. Optional: Limit the maximum number of bytes rewritten per call so that individual requests return progress faster instead of requiring a longer request timeout. This example sets a small 1 MiB limit to force multiple iterations; use a larger value in production: 
         
         builder = builder.set_max_bytes_rewritten_per_call(1024 * 1024);

  4. Optional: Specify destination object metadata, such as changing the [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) to Nearline (`NEARLINE`): 
         
         builder = builder.set_destination(Object::new().set_storage_class("NEARLINE"));

**Note:** The Nearline, Coldline, and Archive storage classes enforce a [minimum storage duration](https://docs.cloud.google.com/storage/pricing#early-delete). You might incur early deletion charges if you delete or overwrite objects before that period ends.



## Run the rewrite loop automatically

For most use cases, bring the `RewriteObjectExt` trait into scope and call `rewrite_until_done` on the request builder. This helper manages the `rewrite_token` across iterations and resolves to the destination `Object` metadata after the rewrite completes:
    
    
    use google_cloud_storage::builder_ext::RewriteObjectExt;
    let dest_object = builder.rewrite_until_done().await?;
    println!("dest_object={dest_object:?}");

## Run the rewrite loop manually

If you need to log intermediate byte counts, checkpoint progress, or resume a rewrite from another process, drive the rewrite loop manually:

  1. Define a helper function that sends a single `RewriteObject` request, logs progress, and returns either the completed `Object` metadata when `resp.done` is `true` or the next `rewrite_token`: 
         
         enum RewriteProgress {
             // This holds the rewrite token
             Incomplete(String),
             Done(Box<Object>),
         }
         
         async fn make_one_request(builder: RewriteObject) -> Result<RewriteProgress> {
             let resp = builder.send().await?;
             if resp.done {
                 println!(
                     "DONE:     total_bytes_rewritten={}; object_size={}",
                     resp.total_bytes_rewritten, resp.object_size
                 );
                 return Ok(RewriteProgress::Done(Box::new(
                     resp.resource
                         .expect("A `done` response must have an object."),
                 )));
             }
             println!(
                 "PROGRESS: total_bytes_rewritten={}; object_size={}",
                 resp.total_bytes_rewritten, resp.object_size
             );
             Ok(RewriteProgress::Incomplete(resp.rewrite_token))
         }

  2. Call the helper in a loop, cloning the request builder on each iteration and passing the returned token to `set_rewrite_token` whenever `make_one_request` returns `RewriteProgress::Incomplete`: 
         
         let dest_object = loop {
             let progress = make_one_request(builder.clone()).await?;
             match progress {
                 RewriteProgress::Incomplete(rewrite_token) => {
                     builder = builder.set_rewrite_token(rewrite_token);
                 }
                 RewriteProgress::Done(object) => break object,
             };
         };
         println!("dest_object={dest_object:?}");


**Note:** Rewrite tokens remain valid for up to one week, so you can store a `rewrite_token` and resume an interrupted rewrite from another process with matching request parameters.

## Complete code

The following example uploads a 3 MiB source object and rewrites it to the Nearline storage class in 1 MiB increments using the manual loop. After the rewrite finishes, the example deletes the test objects and empty test bucket:
    
    
    use gcs::Result;
    use gcs::builder::storage_control::RewriteObject;
    use gcs::client::StorageControl;
    use gcs::model::Object;
    use gcs::retry_policy::RetryableErrors;
    use google_cloud_gax::options::RequestOptionsBuilder;
    use google_cloud_gax::retry_policy::RetryPolicyExt as _;
    use google_cloud_storage as gcs;
    
    pub async fn rewrite_object(bucket_name: &str) -> anyhow::Result<()> {
        let source_object = upload(bucket_name).await?;
    
        let control = StorageControl::builder()
            .with_retry_policy(RetryableErrors.with_attempt_limit(5))
            .build()
            .await?;
    
        let mut builder = control
            .rewrite_object()
            .with_idempotency(true) // retry transient errors
            .set_source_bucket(bucket_name)
            .set_source_object(&source_object.name)
            .set_destination_bucket(bucket_name)
            .set_destination_name("rewrite-object-clone");
    
        // Optionally limit the max bytes written per request.
        builder = builder.set_max_bytes_rewritten_per_call(1024 * 1024);
    
        // Optionally change the storage class to force GCS to copy bytes
        builder = builder.set_destination(Object::new().set_storage_class("NEARLINE"));
    
        let dest_object = loop {
            let progress = make_one_request(builder.clone()).await?;
            match progress {
                RewriteProgress::Incomplete(rewrite_token) => {
                    builder = builder.set_rewrite_token(rewrite_token);
                }
                RewriteProgress::Done(object) => break object,
            };
        };
        println!("dest_object={dest_object:?}");
    
        cleanup(control, bucket_name, &source_object.name, &dest_object.name).await;
        Ok(())
    }
    
    enum RewriteProgress {
        // This holds the rewrite token
        Incomplete(String),
        Done(Box<Object>),
    }
    
    async fn make_one_request(builder: RewriteObject) -> Result<RewriteProgress> {
        let resp = builder.send().await?;
        if resp.done {
            println!(
                "DONE:     total_bytes_rewritten={}; object_size={}",
                resp.total_bytes_rewritten, resp.object_size
            );
            return Ok(RewriteProgress::Done(Box::new(
                resp.resource
                    .expect("A `done` response must have an object."),
            )));
        }
        println!(
            "PROGRESS: total_bytes_rewritten={}; object_size={}",
            resp.total_bytes_rewritten, resp.object_size
        );
        Ok(RewriteProgress::Incomplete(resp.rewrite_token))
    }
    
    // Upload an object to rewrite
    async fn upload(bucket_name: &str) -> anyhow::Result<Object> {
        let storage = gcs::client::Storage::builder().build().await?;
        // We need the size to exceed 1MiB to exercise the rewrite token logic.
        let payload = bytes::Bytes::from(vec![65_u8; 3 * 1024 * 1024]);
        let object = storage
            .write_object(bucket_name, "rewrite-object-source", payload)
            .send_unbuffered()
            .await?;
        Ok(object)
    }
    
    // Clean up the resources created in this sample
    async fn cleanup(control: StorageControl, bucket_name: &str, o1: &str, o2: &str) {
        let _ = control
            .delete_object()
            .set_bucket(bucket_name)
            .set_object(o1)
            .send()
            .await;
        let _ = control
            .delete_object()
            .set_bucket(bucket_name)
            .set_object(o2)
            .send()
            .await;
        let _ = control.delete_bucket().set_name(bucket_name).send().await;
    }

The output is similar to the following, showing progress across three iterations and the destination object metadata:
    
    
    PROGRESS: total_bytes_rewritten=1048576; object_size=3145728
    PROGRESS: total_bytes_rewritten=2097152; object_size=3145728
    DONE:     total_bytes_rewritten=3145728; object_size=3145728
    dest_object=Object { name: "rewrite-object-clone", ... }
    

## Clean up

If the sample exits early or you run individual snippets without the cleanup helper, [delete any remaining test objects](https://docs.cloud.google.com/storage/docs/deleting-objects) and [delete your test bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets) when you're finished so that you don't incur ongoing charges to your Google Cloud account.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
