---
url: https://docs.cloud.google.com/rust/docs/quickstart/
title: Get started with Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:34:10.979284+00:00
---

# Get started with Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Get started with Rust Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to set up a local Rust development environment, install one of the Cloud Client Libraries for Rust, and run your first Google Cloud API request.

## Before you begin

Before running the commands in this document, complete the following prerequisites:

  * Install Rust by following the official [Rust getting started guide](https://www.rust-lang.org/learn/get-started). Verify your installation:
        
        cargo --version
        

  * Install an editor or IDE.

  * Select or create a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) with [billing enabled](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).

  * Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk) and [initialize it](https://docs.cloud.google.com/sdk/docs/initialize) so that an active account and default project are configured.




## Create a Rust project

Complete the following steps to create a binary crate for your program:

  1. Create a binary crate:
         
         cargo new my-project
         

  2. Change to the new project directory:
         
         cd my-project
         




## Install a Google Cloud client library

The Cloud Client Libraries for Rust provide idiomatic Rust clients for Google Cloud services such as Secret Manager. To add and build the Secret Manager client library, complete the following steps:

  1. Enable the Secret Manager API in your project:
         
         gcloud services enable secretmanager.googleapis.com
         

  2. Add the [Secret Manager client library](https://docs.cloud.google.com/secret-manager/docs/overview) to your project:
         
         cargo add google-cloud-secretmanager-v1
         

  3. Add the [`google-cloud-gax` crate](https://crates.io/crates/google-cloud-gax) for pagination helpers:
         
         cargo add google-cloud-gax
         

  4. Add the [`tokio` crate](https://crates.io/crates/tokio) for the asynchronous runtime:
         
         cargo add tokio --features macros,rt-multi-thread
         

  5. Replace the contents of `src/main.rs` with the following code to list secrets in your project: 
         
         #[tokio::main]
         async fn main() -> Result<(), Box<dyn std::error::Error>> {
             use google_cloud_gax::paginator::ItemPaginator as _;
             use google_cloud_secretmanager_v1::client::SecretManagerService;
             let project_id = std::env::args().nth(1).unwrap();
             let client = SecretManagerService::builder().build().await?;
         
             let mut items = client
                 .list_secrets()
                 .set_parent(format!("projects/{project_id}"))
                 .by_item();
             while let Some(item) = items.next().await {
                 println!("{}", item?.name);
             }
             Ok(())
         }

  6. Build your program to verify that it compiles without errors:
         
         cargo build
         




## Run your Rust program

Authenticate your local environment and run the sample program:

  1. Configure Application Default Credentials for your local environment:
         
         gcloud auth application-default login
         

**Note:** For more information about authentication, see [Authenticate with client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).
  2. Run your program, passing your Google Cloud project ID as an argument:
         
         PROJECT_ID=$(gcloud config get project)
         cargo run -- "${PROJECT_ID}"
         

The program prints the names of the secrets in your project. If your project doesn't have any secrets yet, [create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) and run the command again to see it in the output.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this document, [delete any test secrets](https://docs.cloud.google.com/secret-manager/docs/delete-secrets) that you created and remove the local `my-project` directory when you're finished.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
