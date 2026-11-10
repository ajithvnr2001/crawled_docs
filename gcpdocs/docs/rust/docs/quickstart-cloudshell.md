---
url: https://docs.cloud.google.com/rust/docs/quickstart-cloudshell/
title: Set up Rust on Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:34:10.917984+00:00
---

# Set up Rust on Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/quickstart-cloudshell/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Set up Rust on Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Shell provides a browser-based command-line environment for running examples and testing Google Cloud APIs. This document shows you how to configure the Rust toolchain and run a Secret Manager sample using the Cloud Client Libraries for Rust in Cloud Shell.

## Before you begin

Before running the commands in this document, select or create a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) with [billing enabled](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).

## Start Cloud Shell

Complete the following steps to select a project and open a Cloud Shell session:

  1. In the Google Cloud console, select or create a Google Cloud project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Click **Activate Cloud Shell** at the top of the Google Cloud console to start a shell session. If prompted, [authorize Cloud Shell](https://docs.cloud.google.com/shell/docs/auth) to use your credentials for Google Cloud API calls.




## Configure Rust

Cloud Shell includes [`rustup`](https://rust-lang.github.io/rustup/) preinstalled. Complete the following steps to configure and verify the Rust toolchain:

  1. Configure the stable Rust toolchain as the default:
         
         rustup default stable
         

  2. Verify your Cargo and Rust installation:
         
         cargo --version
         




## Install a client library in Cloud Shell

To enable the API, add dependencies, and run the sample program, complete the following steps:

  1. Enable the Secret Manager API in your project:
         
         gcloud services enable secretmanager.googleapis.com
         

  2. Create a binary crate and change to its directory:
         
         cargo new my-project
         cd my-project
         

  3. Add the [Secret Manager client library](https://docs.cloud.google.com/secret-manager/docs/overview), [`google-cloud-gax`](https://crates.io/crates/google-cloud-gax), and [`tokio`](https://crates.io/crates/tokio) to your project:
         
         cargo add google-cloud-secretmanager-v1 google-cloud-gax
         cargo add tokio --features macros,rt-multi-thread
         

  4. Replace the contents of `src/main.rs` with the following code: 
         
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

  5. Run the program, passing your Google Cloud project ID as an argument:
         
         PROJECT_ID=$(gcloud config get project)
         cargo run -- "${PROJECT_ID}"
         

The program prints the names of the secrets in your project. If your project doesn't have any secrets yet, [create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) and run the command again to see it in the output.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this document, [delete any test secrets](https://docs.cloud.google.com/secret-manager/docs/delete-secrets) that you created and remove the `my-project` directory from your Cloud Shell home directory when you're finished.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
