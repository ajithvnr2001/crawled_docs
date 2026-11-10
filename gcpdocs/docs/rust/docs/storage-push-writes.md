---
url: https://docs.cloud.google.com/rust/docs/storage-push-writes/
title: Push data on Cloud Storage object writes \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:31:46.798884+00:00
---

# Push data on Cloud Storage object writes  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/storage-push-writes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Push data on Cloud Storage object writes Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Storage client in the Cloud Client Libraries for Rust writes objects by pulling payload chunks from a type that implements the `StreamingSource` trait. Some applications generate data in a separate task or thread and need to push payload chunks to the upload instead.

This document shows you how to wrap an asynchronous channel receiver in a `StreamingSource` implementation so that you can push data to a Cloud Storage object write. If you are new to the client library, see [Using Cloud Storage with Rust](https://docs.cloud.google.com/rust/docs/quickstart-storage) first.

## Before you begin

Before running the code in this document, complete the following prerequisites:

  * Create or select a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) with [billing enabled](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).
  * Create a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) in your project.
  * Configure [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) and grant your principal an Identity and Access Management (IAM) role with permission to create objects in the bucket, such as Storage Object User (`roles/storage.objectUser`).



### Dependencies

Add the Cloud Storage client library and the supporting crates used in this document to your `Cargo.toml` file:
    
    
    cargo add google-cloud-storage anyhow bytes
    cargo add tokio --features rt,sync
    

## Convert a queue receiver into a streaming source

To decouple the task that produces data from the task that uploads the payload, connect them with an asynchronous queue. This document uses a Tokio [`mpsc` channel](https://docs.rs/tokio/latest/tokio/sync/mpsc/index.html), though you can use any channel or queue that integrates with your asynchronous runtime.

To adapt the channel receiver into a `StreamingSource` implementation, complete the following steps:

  1. Define a struct that wraps the channel `Receiver`: 
         
         use tokio::sync::mpsc::{self, Receiver};
         #[derive(Debug)]
         struct QueueSource(Receiver<bytes::Bytes>);

  2. Implement the `StreamingSource` trait for the wrapper struct so that each call to `next` awaits the next chunk from the receiver: 
         
         use google_cloud_storage::streaming_source::StreamingSource;
         impl StreamingSource for QueueSource {
             type Error = std::convert::Infallible;
             async fn next(&mut self) -> Option<Result<bytes::Bytes, Self::Error>> {
                 self.0.recv().await.map(Ok)
             }
         }




## Stream data from the queue to Cloud Storage

After implementing the `StreamingSource` trait, you can spawn the object upload in a background task and send chunks through the channel from your producer task. Because a channel receiver is a single-pass data source that doesn't implement `Seek`, start the upload using `send_buffered` rather than `send_unbuffered`.

Inside an `async` function that accepts `bucket_name` in the format `projects/_/buckets/BUCKET_ID` and `object_name`, complete the following steps:

  1. Initialize a `Storage` client: 
         
         use google_cloud_storage::client::Storage;
         let client = Storage::builder().build().await?;

  2. Create a bounded `mpsc` channel to obtain the `sender` and `receiver` handles: 
         
         let (sender, receiver) = mpsc::channel::<bytes::Bytes>(32);

  3. Configure the object upload with `QueueSource(receiver)` as the payload source. Don't await the `send_buffered` future yet: 
         
         let upload = client
             .write_object(bucket_name, object_name, QueueSource(receiver))
             .send_buffered();

  4. Spawn a background task to drive the upload while your producer generates data: 
         
         let task = tokio::spawn(upload);

  5. In the producer task, push data chunks into the `sender` handle: 
         
         for _ in 0..1000 {
             let line = "I will not write funny examples in class\n";
             sender
                 .send(bytes::Bytes::from_static(line.as_bytes()))
                 .await?;
         }

  6. After sending all data, drop the `sender` handle to close the channel and signal the end of the object stream: 
         
         drop(sender);

  7. Await the background task handle to verify that both the task and the upload request succeeded, and retrieve the uploaded `Object` metadata: 
         
         let object = task.await??;
         println!("object successfully uploaded {object:?}");


**Note:** If the upload fails before all chunks are sent, the background task exits and drops the receiver, causing `sender.send` to return a closed-channel error. In production code, if `sender.send` fails, await the background task handle to inspect the underlying Cloud Storage error.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this document, [delete the test objects](https://docs.cloud.google.com/storage/docs/deleting-objects) that you uploaded when you are finished.

## Complete code

The following example combines all of the preceding steps into a complete function:
    
    
    use google_cloud_storage::streaming_source::StreamingSource;
    use tokio::sync::mpsc::{self, Receiver};
    #[derive(Debug)]
    struct QueueSource(Receiver<bytes::Bytes>);
    impl StreamingSource for QueueSource {
        type Error = std::convert::Infallible;
        async fn next(&mut self) -> Option<Result<bytes::Bytes, Self::Error>> {
            self.0.recv().await.map(Ok)
        }
    }
    
    pub async fn queue(bucket_name: &str, object_name: &str) -> anyhow::Result<()> {
        use google_cloud_storage::client::Storage;
        let client = Storage::builder().build().await?;
    
        let (sender, receiver) = mpsc::channel::<bytes::Bytes>(32);
        let upload = client
            .write_object(bucket_name, object_name, QueueSource(receiver))
            .send_buffered();
        let task = tokio::spawn(upload);
    
        for _ in 0..1000 {
            let line = "I will not write funny examples in class\n";
            sender
                .send(bytes::Bytes::from_static(line.as_bytes()))
                .await?;
        }
        drop(sender);
        let object = task.await??;
        println!("object successfully uploaded {object:?}");
    
        Ok(())
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
