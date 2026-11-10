---
url: https://docs.cloud.google.com/rust/docs/configure-polling-policies/
title: Configuring polling policies \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:34:12.242244+00:00
---

# Configuring polling policies  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/configure-polling-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Configuring polling policies Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Client Libraries for Rust provide helper functions to monitor the progress of long-running operations (LROs). These helpers use policies to configure polling frequency and determine which polling errors are transient and safe to retry, and which are unrecoverable.

Two policies control the behavior of LRO polling loops:

  * The **polling backoff policy** controls how long the loop waits before polling the status of an in-progress LRO.
  * The **polling error policy** controls how to handle a polling error. Some polling errors are unrecoverable, indicating that the operation stopped or that the caller lacks permission to check its status. Other polling errors are transient and indicate a temporary network or service issue.



You can set each policy independently, either for all LROs started on a client or for an individual request.

## Before you begin

This document uses Cloud Storage to illustrate polling policy configuration, though the same concepts apply to any Google Cloud service that uses LROs.

Before running the code in this document, complete the following prerequisites:

  * Follow [Get started with Rust](https://docs.cloud.google.com/rust/docs/quickstart) to set up your development environment.
  * Follow [Using Cloud Storage with Rust](https://docs.cloud.google.com/rust/docs/quickstart-storage) to set up a Google Cloud project with billing enabled, enable the Cloud Storage API, and configure credentials.
  * Create a Cloud Storage bucket with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/rename-hns-folders) enabled, create a source folder to rename, and grant your principal an Identity and Access Management (IAM) role with permission to manage folders, such as Storage Admin (`roles/storage.admin`).



### Dependencies

Add the required crates to your `Cargo.toml` file:
    
    
    cargo add google-cloud-storage google-cloud-lro google-cloud-gax anyhow
    

## Configure polling frequency for all requests on a client

If you use the same polling backoff policy across most requests on a client, configure the policy on the client builder. The following example configures exponential polling backoff for all LROs started by a `StorageControl` client:
    
    
    pub async fn client_backoff(bucket: &str, folder: &str, dest: &str) -> Result<()> {
        use google_cloud_gax::exponential_backoff::ExponentialBackoffBuilder;
        use google_cloud_lro::Poller;
        use std::time::Duration;
    
        let client = StorageControl::builder()
            .with_polling_backoff_policy(
                ExponentialBackoffBuilder::new()
                    .with_initial_delay(Duration::from_millis(250))
                    .with_maximum_delay(Duration::from_secs(10))
                    .build()?,
            )
            .build()
            .await?;
    
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

Unless you override the policy on an individual request, this configuration applies to every LRO started by the client. In this example, the client library waits 250 ms after the first poll and 500 ms after the second. The delay then doubles to 1 s, 2 s, 4 s, and 8 s before capping at 10 s for all subsequent polls.

## Configure polling frequency for a specific request

You can also configure the polling frequency on an individual request builder, which overrides any client-level polling backoff policy. Bring `RequestOptionsBuilder` into scope and call `with_polling_backoff_policy` on the request builder:
    
    
    pub async fn rpc_backoff(bucket: &str, folder: &str, dest: &str) -> Result<()> {
        use google_cloud_gax::exponential_backoff::ExponentialBackoffBuilder;
        use std::time::Duration;
        use google_cloud_gax::options::RequestOptionsBuilder;
        use google_cloud_lro::Poller;
    
        let client = StorageControl::builder().build().await?;
    
        let response = client
            .rename_folder()
            .with_polling_backoff_policy(
                ExponentialBackoffBuilder::new()
                    .with_initial_delay(Duration::from_millis(250))
                    .with_maximum_delay(Duration::from_secs(10))
                    .build()?,
            )
            .set_name(format!("projects/_/buckets/{bucket}/folders/{folder}"))
            .set_destination_folder_id(dest)
            .poller()
            .until_done()
            .await?;
    
        println!("LRO completed, response={response:?}");
    
        Ok(())
    }

## Configure polling error policies for all requests on a client

To control which polling errors the loop retries and when polling stops, pass a type that implements the `PollingErrorPolicy` trait, such as `Aip194Strict`.

The polling error policy governs errors only during the LRO wait loop. To handle transient errors when sending the initial request that starts the LRO, also configure a standard retry policy on the client:
    
    
    pub async fn client_errors(bucket: &str, folder: &str, dest: &str) -> Result<()> {
        use google_cloud_gax::polling_error_policy::Aip194Strict;
        use google_cloud_gax::polling_error_policy::PollingErrorPolicyExt;
        use google_cloud_gax::retry_policy;
        use google_cloud_gax::retry_policy::RetryPolicyExt;
        use std::time::Duration;
        use google_cloud_lro::Poller;
    
        let builder = StorageControl::builder().with_polling_error_policy(
            Aip194Strict
                .with_attempt_limit(100)
                .with_time_limit(Duration::from_secs(300)),
        );
    
        let client = builder
            .with_retry_policy(
                retry_policy::Aip194Strict
                    .with_attempt_limit(100)
                    .with_time_limit(Duration::from_secs(300)),
            )
            .build()
            .await?;
    
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

**Note:** With `Aip194Strict`, which implements [AIP-194](https://google.aip.dev/194), the client library retries transient I/O and `UNAVAILABLE` polling errors. Adding the `PollingErrorPolicyExt` decorators `with_attempt_limit(100)` and `with_time_limit(Duration::from_secs(300))` stops polling after 100 attempts or 300 s, whichever comes first.

## Configure polling error policies for a specific request

To override the polling error policy for a single request, bring `RequestOptionsBuilder` into scope and call `with_polling_error_policy` on the request builder:
    
    
    pub async fn rpc_errors(bucket: &str, folder: &str, dest: &str) -> Result<()> {
        use google_cloud_gax::polling_error_policy::Aip194Strict;
        use google_cloud_gax::polling_error_policy::PollingErrorPolicyExt;
        use google_cloud_gax::retry_policy;
        use google_cloud_gax::retry_policy::RetryPolicyExt;
        use std::time::Duration;
        use google_cloud_gax::options::RequestOptionsBuilder;
        use google_cloud_lro::Poller;
    
        let client = StorageControl::builder()
            .with_retry_policy(
                retry_policy::Aip194Strict
                    .with_attempt_limit(100)
                    .with_time_limit(Duration::from_secs(300)),
            )
            .build()
            .await?;
    
        let response = client
            .rename_folder()
            .with_polling_error_policy(
                Aip194Strict
                    .with_attempt_limit(100)
                    .with_time_limit(Duration::from_secs(300)),
            )
            .set_name(format!("projects/_/buckets/{bucket}/folders/{folder}"))
            .set_destination_folder_id(dest)
            .poller()
            .until_done()
            .await?;
    
        println!("LRO completed, response={response:?}");
    
        Ok(())
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
