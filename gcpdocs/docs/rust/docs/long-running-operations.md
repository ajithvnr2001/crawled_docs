---
url: https://docs.cloud.google.com/rust/docs/long-running-operations/
title: Working with long-running operations \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:34:11.237847+00:00
---

# Working with long-running operations  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/long-running-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Working with long-running operations Stay organized with collections  Save and categorize content based on your preferences. 

Some Google Cloud API methods take a significant amount of time to complete. Instead of blocking until the work finishes, these methods return an [`Operation`](https://docs.rs/google-cloud-longrunning/latest/google_cloud_longrunning/model/struct.Operation.html) resource that represents an in-progress operation so that your application can poll for its status and final result.

The Cloud Client Libraries for Rust provide helpers for working with these long-running operations (LROs). This document shows you how to start an LRO, poll automatically until completion, inspect intermediate progress updates, and poll manually.

## Before you begin

This document uses Cloud Storage to keep the code examples concrete, though the same concepts apply to any Google Cloud service that uses LROs.

Before running the code in this document, complete the following prerequisites:

  * Create or select a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) with [billing enabled](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).
  * Follow [Get started with Rust](https://docs.cloud.google.com/rust/docs/quickstart) to set up your development environment and credentials.
  * Create a Cloud Storage bucket with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/rename-hns-folders) enabled, create a source folder to rename, and grant your principal an Identity and Access Management (IAM) role with permission to manage folders, such as Storage Admin (`roles/storage.admin`).



### Dependencies

Add the client library and LRO crates to your `Cargo.toml` file:
    
    
    cargo add google-cloud-storage google-cloud-lro google-cloud-longrunning anyhow
    

Add `tokio` for asynchronous execution and timers:
    
    
    cargo add tokio --features full
    

## Start a long-running operation

The examples in this document call the Cloud Storage [rename folder](https://docs.cloud.google.com/storage/docs/rename-hns-folders) operation, which returns an LRO. To start an LRO directly and obtain the initial `Operation` resource, complete the following steps:

  1. Add `use` declarations to shorten type paths: 
         
         use anyhow::anyhow;
         use google_cloud_longrunning as longrunning;
         use google_cloud_storage::client::StorageControl;

  2. Define an `async` function that accepts the bucket ID, source folder ID, and destination folder ID: 
         
         pub async fn manual(bucket: &str, folder: &str, dest: &str) -> anyhow::Result<()> {

  3. Initialize the `StorageControl` client: 
         
         let client = StorageControl::builder().build().await?;

  4. Create the `rename_folder` request builder: 
         
         let operation = client
             .rename_folder()
             .set_name(format!("projects/_/buckets/{bucket}/folders/{folder}"))
             .set_destination_folder_id(dest)

  5. Send the request and await the initial [`Operation`](https://docs.rs/google-cloud-longrunning/latest/google_cloud_longrunning/model/struct.Operation.html) resource, which represents the background operation: 
         
         .send()
         .await?;




After starting the operation, wait for it to finish to retrieve its final outcome.

## Automatically poll a long-running operation

For most use cases, use the `Poller` trait's `until_done` method instead of calling `send` directly. The poller starts the LRO, polls according to the client's backoff and error policies, and resolves to the final response:

  1. Bring the `Poller` trait into scope: 
         
         use google_cloud_lro::Poller;

  2. Initialize a `StorageControl` client and configure the `rename_folder` request builder: 
         
         let response = client
             .rename_folder()
             .set_name(format!("projects/_/buckets/{bucket}/folders/{folder}"))
             .set_destination_folder_id(dest)

  3. Call `poller` and `until_done` on the request builder to await completion and print the result: 
         
         .poller()
             .until_done()
             .await?;
         
         println!("LRO completed, response={response:?}");




### Complete automatic polling code

The following function shows the complete automatic polling example:
    
    
    pub async fn automatic(bucket: &str, folder: &str, dest: &str) -> anyhow::Result<()> {
        use google_cloud_lro::Poller;
    
        let client = StorageControl::builder().build().await?;
    
        let response = client
            .rename_folder()
            .set_name(format!("projects/_/buckets/{bucket}/folders/{folder}"))
            .set_destination_folder_id(dest)
            .poller()
            .until_done()
            .await?;
    
        println!("LRO completed, response={response:?}");
    
        Ok(())
    }

## Poll a long-running operation with intermediate results

The `until_done` method returns only the final outcome and omits intermediate metadata updates. If your application needs progress updates while the LRO runs, obtain a poller with `poller` and call `poll` in a loop:

  1. Import `Poller` and `PollingResult`: 
         
         use google_cloud_lro::{Poller, PollingResult};

  2. Convert the request builder into a poller using `poller`: 
         
         .poller();

  3. Call `poller.poll().await` in a loop to process `InProgress`, `PollingError`, and `Completed` states: 
         
         while let Some(p) = poller.poll().await {
             match p {
                 PollingResult::Completed(r) => {
                     println!("LRO completed, response={r:?}");
                 }
                 PollingResult::InProgress(m) => {
                     println!("LRO in progress, metadata={m:?}");
                 }
                 PollingResult::PollingError(e) => {
                     println!("Transient error polling the LRO: {e}");
                 }
             }
             tokio::time::sleep(std::time::Duration::from_millis(500)).await;
         }




When calling `poll` directly, your loop controls the delay between polling attempts. Choose a delay suited to the expected duration of the operation.

### Complete code for polling with intermediate results

The following function shows the complete `poll` loop:
    
    
    pub async fn polling(bucket: &str, folder: &str, dest: &str) -> anyhow::Result<()> {
        use google_cloud_lro::{Poller, PollingResult};
    
        let client = StorageControl::builder().build().await?;
    
        let mut poller = client
            .rename_folder()
            .set_name(format!("projects/_/buckets/{bucket}/folders/{folder}"))
            .set_destination_folder_id(dest)
            .poller();
    
        while let Some(p) = poller.poll().await {
            match p {
                PollingResult::Completed(r) => {
                    println!("LRO completed, response={r:?}");
                }
                PollingResult::InProgress(m) => {
                    println!("LRO in progress, metadata={m:?}");
                }
                PollingResult::PollingError(e) => {
                    println!("Transient error polling the LRO: {e}");
                }
            }
            tokio::time::sleep(std::time::Duration::from_millis(500)).await;
        }
    
        Ok(())
    }

## Manually poll a long-running operation

Although the `Poller` trait handles almost all use cases, you can also poll an [`Operation`](https://docs.rs/google-cloud-longrunning/latest/google_cloud_longrunning/model/struct.Operation.html) manually using `get_operation`:

  1. After starting the LRO with `send`, enter a loop and check the `done` field: 
         
         let response: anyhow::Result<Folder> = loop {
             if operation.done {

  2. Inspect `operation.result`. The `result` field is an `Option` because some operations, such as deletions, finish without returning a payload. For `rename_folder`, the service returns a `Folder` resource: 
         
         match &operation.result {
             None => {
                 break Err(anyhow!("missing result for finished operation"));
             }

  3. Check whether the operation finished with an error. The error variant contains a [`Status`](https://docs.rs/google-cloud-rpc/latest/google_cloud_rpc/model/struct.Status.html) message that the following example formats into an error, or that you can convert to a client error using [`Error::service`](https://docs.rs/google-cloud-gax/latest/google_cloud_gax/error/struct.Error.html#method.service): 
         
         Some(r) => {
             break match r {
                 longrunning::model::operation::Result::Error(s) => {
                     Err(anyhow!("operation completed with error {s:?}"))
                 }

  4. If the operation succeeded, unpack the `Any` payload into the expected `Folder` response type: 
         
         longrunning::model::operation::Result::Response(any) => {
             let response = any.to_msg::<Folder>()?;
             Ok(response)
         }

  5. Add a wildcard arm because enums in the Cloud Client Libraries for Rust are marked `#[non_exhaustive]`: 
         
         _ => Err(anyhow!("unexpected result branch {r:?}")),

  6. Optional: While `operation.done` is `false`, unpack `operation.metadata` to inspect progress updates: 
         
         if let Some(any) = &operation.metadata {
             let metadata = any.to_msg::<RenameFolderMetadata>()?;
             println!("LRO in progress, metadata={metadata:?}");
         }

  7. Wait before polling again. This example sleeps for a fixed 500 ms for brevity; in production code, use truncated [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff): 
         
         tokio::time::sleep(std::time::Duration::from_millis(500)).await;

  8. Call `get_operation` with `operation.name` to refresh the operation status: 
         
         if let Ok(attempt) = client
             .get_operation()
             .set_name(&operation.name)
             .send()
             .await
         {
             operation = attempt;
         }


**Note:** For brevity, this manual loop ignores `get_operation` errors. In production code that polls manually, distinguish unrecoverable errors from transient errors and enforce a maximum attempt or time limit.

### Complete manual polling code

The following function combines all of the manual polling steps:
    
    
    pub async fn manual(bucket: &str, folder: &str, dest: &str) -> anyhow::Result<()> {
        use google_cloud_storage::model::Folder;
        use google_cloud_storage::model::RenameFolderMetadata;
    
        let client = StorageControl::builder().build().await?;
    
        let operation = client
            .rename_folder()
            .set_name(format!("projects/_/buckets/{bucket}/folders/{folder}"))
            .set_destination_folder_id(dest)
            .send()
            .await?;
        println!("LRO started, response={operation:?}");
    
        let mut operation = operation;
        let response: anyhow::Result<Folder> = loop {
            if operation.done {
                match &operation.result {
                    None => {
                        break Err(anyhow!("missing result for finished operation"));
                    }
                    Some(r) => {
                        break match r {
                            longrunning::model::operation::Result::Error(s) => {
                                Err(anyhow!("operation completed with error {s:?}"))
                            }
                            longrunning::model::operation::Result::Response(any) => {
                                let response = any.to_msg::<Folder>()?;
                                Ok(response)
                            }
                            _ => Err(anyhow!("unexpected result branch {r:?}")),
                        };
                    }
                }
            }
            if let Some(any) = &operation.metadata {
                let metadata = any.to_msg::<RenameFolderMetadata>()?;
                println!("LRO in progress, metadata={metadata:?}");
            }
            tokio::time::sleep(std::time::Duration::from_millis(500)).await;
            if let Ok(attempt) = client
                .get_operation()
                .set_name(&operation.name)
                .send()
                .await
            {
                operation = attempt;
            }
        };
        println!("LRO completed, response={response:?}");
    
        Ok(())
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
