---
url: https://docs.cloud.google.com/rust/docs/configure-retry-policies/
title: Configuring retry policies \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:34:12.443509+00:00
---

# Configuring retry policies  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/configure-retry-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Configuring retry policies Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Client Libraries for Rust can automatically retry operations that fail due to transient errors. This document shows you how to configure a default retry policy on a client, set attempt and time limits, and override the retry policy for individual requests.

## Before you begin

The examples in this document use Secret Manager, though the same concepts apply to other Google Cloud services.

Before running the code in this document, follow [Create and access a secret using Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart) to enable the Secret Manager API and configure authentication.

### Dependencies

Add the required crates to your `Cargo.toml` file:
    
    
    cargo add google-cloud-secretmanager-v1 google-cloud-gax anyhow
    

## Configure a default retry policy

This example uses the `Aip194Strict` policy, which implements the guidelines in [AIP-194](https://google.aip.dev/194) for retrying Google API requests.

**Note:** `Aip194Strict` retries transient errors only for requests that are idempotent or known not to have reached the service. Retried requests consume API quota and can incur billed charges.

To configure `Aip194Strict` as the default retry policy for a client, complete the following steps:

  1. Set the retry policy during [client initialization](https://docs.cloud.google.com/rust/docs/initialize-client): 
         
         let client = SecretManagerService::builder()
             .with_retry_policy(Aip194Strict)
             .build()
             .await?;

  2. Send requests using the configured client: 
         
         let mut list = client
             .list_secrets()
             .set_parent(format!("projects/{project_id}"))
             .by_item();
         while let Some(secret) = list.next().await {
             let secret = secret?;
             println!("  secret={}", secret.name);
         }




### Complete code for a default retry policy

The following example applies `Aip194Strict` to a Secret Manager client:
    
    
    use google_cloud_gax::paginator::ItemPaginator as _;
    use google_cloud_gax::retry_policy::Aip194Strict;
    use google_cloud_secretmanager_v1::client::SecretManagerService;
    
    pub async fn sample(project_id: &str) -> anyhow::Result<()> {
        let client = SecretManagerService::builder()
            .with_retry_policy(Aip194Strict)
            .build()
            .await?;
    
        let mut list = client
            .list_secrets()
            .set_parent(format!("projects/{project_id}"))
            .by_item();
        while let Some(secret) = list.next().await {
            let secret = secret?;
            println!("  secret={}", secret.name);
        }
    
        Ok(())
    }

## Configure a default retry policy with limits

By default, `Aip194Strict` doesn't bound the number of attempts or total time spent retrying. To configure attempt and time limits on a client, bring the `RetryPolicyExt` trait into scope and complete the following steps:

  1. Configure the retry policy with `with_attempt_limit` and `with_time_limit` on the client builder: 
         
         let client = SecretManagerService::builder()
             .with_retry_policy(
                 Aip194Strict
                     .with_attempt_limit(5)
                     .with_time_limit(Duration::from_secs(15)),
             )
             .build()
             .await?;

  2. Send requests using the configured client: 
         
         let mut list = client
             .list_secrets()
             .set_parent(format!("projects/{project_id}"))
             .by_item();
         while let Some(secret) = list.next().await {
             let secret = secret?;
             println!("  secret={}", secret.name);
         }




### Complete code for a retry policy with limits

The following example applies `Aip194Strict` with custom attempt and time limits:
    
    
    use google_cloud_gax::paginator::ItemPaginator as _;
    use google_cloud_gax::retry_policy::Aip194Strict;
    use google_cloud_gax::retry_policy::RetryPolicyExt;
    use google_cloud_secretmanager_v1::client::SecretManagerService;
    use std::time::Duration;
    
    pub async fn sample(project_id: &str) -> anyhow::Result<()> {
        let client = SecretManagerService::builder()
            .with_retry_policy(
                Aip194Strict
                    .with_attempt_limit(5)
                    .with_time_limit(Duration::from_secs(15)),
            )
            .build()
            .await?;
    
        let mut list = client
            .list_secrets()
            .set_parent(format!("projects/{project_id}"))
            .by_item();
        while let Some(secret) = list.next().await {
            let secret = secret?;
            println!("  secret={}", secret.name);
        }
    
        Ok(())
    }

## Override the retry policy for a single request

You can override the retry policy on an individual request when you know that retrying a specific operation is safe for your application. For example, deleting a secret can succeed at most once, even though the client library treats delete operations as non-idempotent by default.

Bring `RequestOptionsBuilder`, `RetryPolicyExt`, and `AlwaysRetry` into scope, and then call `with_retry_policy` on the request builder:
    
    
    client
        .delete_secret()
        .set_name(format!("projects/{project_id}/secrets/{secret_id}"))
        .with_retry_policy(
            AlwaysRetry
                .with_attempt_limit(5)
                .with_time_limit(Duration::from_secs(15)),
        )
        .send()
        .await?;

### Complete code for a per-request retry policy

The following example overrides the retry policy, attempt limit, and time limit for a single `delete_secret` request:
    
    
    use google_cloud_gax::options::RequestOptionsBuilder;
    use google_cloud_gax::retry_policy::AlwaysRetry;
    use google_cloud_gax::retry_policy::RetryPolicyExt;
    use google_cloud_secretmanager_v1::client::SecretManagerService;
    use std::time::Duration;
    
    pub async fn sample(
        client: &SecretManagerService,
        project_id: &str,
        secret_id: &str,
    ) -> anyhow::Result<()> {
        client
            .delete_secret()
            .set_name(format!("projects/{project_id}/secrets/{secret_id}"))
            .with_retry_policy(
                AlwaysRetry
                    .with_attempt_limit(5)
                    .with_time_limit(Duration::from_secs(15)),
            )
            .send()
            .await?;
    
        Ok(())
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
