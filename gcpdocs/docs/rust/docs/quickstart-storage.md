---
url: https://docs.cloud.google.com/rust/docs/quickstart-storage/
title: Using Cloud Storage with Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:34:12.752565+00:00
---

# Using Cloud Storage with Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/quickstart-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Using Cloud Storage with Rust Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage is a managed service for storing unstructured data. The `google-cloud-storage` crate in the Cloud Client Libraries for Rust provides an idiomatic Rust API that resumes interrupted uploads and downloads, verifies data integrity, retries transient metadata errors, and polls long-running operations.

This document shows you how to create a Cloud Storage bucket, write an object to that bucket, read the object contents back, and delete both resources.

## Before you begin

Before running the code in this document, complete the following prerequisites:

  * Create or select a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) with [billing enabled](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).
  * Follow [Get started with Rust](https://docs.cloud.google.com/rust/docs/quickstart) to install Rust and set up your development environment.
  * Configure [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) and grant your principal an Identity and Access Management (IAM) role with permission to create and delete buckets and objects, such as Storage Admin (`roles/storage.admin`).



### Dependencies

Add the Cloud Storage client library and supporting crates to your `Cargo.toml` file:
    
    
    cargo add google-cloud-storage anyhow bytes
    cargo add tokio --features macros,rt-multi-thread
    

## Create a bucket

Operations on buckets and object metadata use the `StorageControl` client:

  1. Initialize a `StorageControl` client: 
         
         use google_cloud_storage as gcs;
         use google_cloud_storage::client::StorageControl;
         let control = StorageControl::builder().build().await?;

  2. Configure a `create_bucket` request with your project ID and globally unique bucket ID: 
         
         let bucket = control
             .create_bucket()
             .set_parent("projects/_")
             .set_bucket_id(bucket_id)
             .set_bucket(
                 gcs::model::Bucket::new()
                     .set_project(format!("projects/{project_id}"))
             )

  3. Optional: Configure bucket attributes such as [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access): 
         
         gcs::model::Bucket::new()
             .set_project(format!("projects/{project_id}"))
             .set_iam_config(
                 gcs::model::bucket::IamConfig::new().set_uniform_bucket_level_access(
                     gcs::model::bucket::iam_config::UniformBucketLevelAccess::new()
                         .set_enabled(true),
                 ),
             ),

  4. Send the request and await the created `Bucket` metadata: 
         
         .send()
             .await?;
         println!("bucket successfully created {bucket:?}");




## Write an object

Operations that read or write object data use the `Storage` client:

  1. Initialize a `Storage` client: 
         
         use google_cloud_storage::client::Storage;
         let client = Storage::builder().build().await?;

  2. Write an object named `hello.txt` to the bucket using `write_object`: 
         
         let object = client
             .write_object(&bucket.name, "hello.txt", "Hello World!")
             .send_buffered()
             .await?;
         println!("object successfully uploaded {object:?}");




## Read an object

To read the contents of an object, call `read_object` and collect the streamed chunks:
    
    
    let mut reader = client.read_object(&bucket.name, "hello.txt").send().await?;
    let mut contents = Vec::new();
    while let Some(chunk) = reader.next().await.transpose()? {
        contents.extend_from_slice(&chunk);
    }
    println!(
        "object contents successfully downloaded {:?}",
        bytes::Bytes::from_owner(contents)
    );

When executed, this step prints the downloaded bytes:
    
    
    object contents successfully downloaded b"Hello World!"
    

## Delete the object and bucket

Delete the object and bucket in your program when they are no longer needed:
    
    
    control
        .delete_object()
        .set_bucket(&bucket.name)
        .set_object(&object.name)
        .set_generation(object.generation)
        .send()
        .await?;
    control
        .delete_bucket()
        .set_name(&bucket.name)
        .send()
        .await?;

## Complete code

The following function combines all of the preceding steps:
    
    
    pub async fn sample(project_id: &str, bucket_id: &str) -> anyhow::Result<()> {
        use google_cloud_storage as gcs;
        use google_cloud_storage::client::StorageControl;
        let control = StorageControl::builder().build().await?;
        let bucket = control
            .create_bucket()
            .set_parent("projects/_")
            .set_bucket_id(bucket_id)
            .set_bucket(
                gcs::model::Bucket::new()
                    .set_project(format!("projects/{project_id}"))
                    .set_iam_config(
                        gcs::model::bucket::IamConfig::new().set_uniform_bucket_level_access(
                            gcs::model::bucket::iam_config::UniformBucketLevelAccess::new()
                                .set_enabled(true),
                        ),
                    ),
            )
            .send()
            .await?;
        println!("bucket successfully created {bucket:?}");
    
        use google_cloud_storage::client::Storage;
        let client = Storage::builder().build().await?;
    
        let object = client
            .write_object(&bucket.name, "hello.txt", "Hello World!")
            .send_buffered()
            .await?;
        println!("object successfully uploaded {object:?}");
    
        let mut reader = client.read_object(&bucket.name, "hello.txt").send().await?;
        let mut contents = Vec::new();
        while let Some(chunk) = reader.next().await.transpose()? {
            contents.extend_from_slice(&chunk);
        }
        println!(
            "object contents successfully downloaded {:?}",
            bytes::Bytes::from_owner(contents)
        );
    
        control
            .delete_object()
            .set_bucket(&bucket.name)
            .set_object(&object.name)
            .set_generation(object.generation)
            .send()
            .await?;
        control
            .delete_bucket()
            .set_name(&bucket.name)
            .send()
            .await?;
    
        Ok(())
    }

## Clean up

If the sample exits early before running the deletion steps, [delete the bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets) manually so that you don't incur ongoing charges for the resources created in this document.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
