---
url: https://docs.cloud.google.com/rust/docs/initialize-client/
title: Initialize a client \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:34:11.306773+00:00
---

# Initialize a client  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/initialize-client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Initialize a client Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Client Libraries for Rust use client structs as the main interface to Google Cloud services, with methods corresponding to each RPC offered by the service. Before calling a service, you initialize its client.

This document shows you how to initialize a Secret Manager client with its default configuration and call an RPC. The same pattern applies to all other Google Cloud services.

## Before you begin

Before running the code in this document, complete the following prerequisites:

  * Follow [Create and access a secret using Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart) to set up a Google Cloud project and enable the Secret Manager API.
  * Configure [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) for your local environment. For more information, see [Authenticate with client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).



### Dependencies

Add the required crates to your `Cargo.toml` file:
    
    
    cargo add google-cloud-secretmanager-v1 google-cloud-gax anyhow
    cargo add tokio --features macros,rt-multi-thread
    

## Initialize a client and make an RPC

To initialize a client, call `builder` on the client struct to obtain a [`ClientBuilder`](https://docs.rs/google-cloud-gax/latest/google_cloud_gax/client_builder/struct.ClientBuilder.html) and then call `build`. Complete the following steps to initialize a client with default settings and call an RPC:

  1. Import the `SecretManagerService` client type: 
         
         use google_cloud_secretmanager_v1::client::SecretManagerService;

  2. Build the client with its default configuration: 
         
         let client = SecretManagerService::builder().build().await?;

  3. Use the initialized client to call `list_locations`, which lists the locations supported by Secret Manager for your project: 
         
         use google_cloud_gax::paginator::Paginator as _;
         let mut items = client
             .list_locations()
             .set_name(format!("projects/{project_id}"))
             .by_page();
         while let Some(page) = items.next().await {
             let page = page?;
             for location in page.locations {
                 println!("{}", location.name);
             }
         }




The output resembles the following:
    
    
    projects/PROJECT_NUMBER/locations/europe-west8
    projects/PROJECT_NUMBER/locations/europe-west9
    projects/PROJECT_NUMBER/locations/us-east5
    

In this output, `PROJECT_NUMBER` is the numeric project number for your Google Cloud project.

## Complete code

The following example combines client initialization and the `list_locations` call into a runnable program:
    
    
    pub async fn initialize_client(project_id: &str) -> anyhow::Result<()> {
        use google_cloud_secretmanager_v1::client::SecretManagerService;
    
        // Initialize a client with the default configuration. This is an
        // asynchronous operation that may fail, as it requires acquiring an an
        // access token.
        let client = SecretManagerService::builder().build().await?;
    
        // Once initialized, use the client to make requests.
        use google_cloud_gax::paginator::Paginator as _;
        let mut items = client
            .list_locations()
            .set_name(format!("projects/{project_id}"))
            .by_page();
        while let Some(page) = items.next().await {
            let page = page?;
            for location in page.locations {
                println!("{}", location.name);
            }
        }
    
        Ok(())
    }
    
    #[tokio::main]
    async fn main() -> anyhow::Result<()> {
        let project_id = std::env::args().nth(1).unwrap();
    
        initialize_client(&project_id).await
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
