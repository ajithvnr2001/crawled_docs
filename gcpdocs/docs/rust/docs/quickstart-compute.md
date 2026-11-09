---
url: https://docs.cloud.google.com/rust/docs/quickstart-compute/
title: Quickstart: Use Compute Engine with Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-09T06:57:01.186079+00:00
---

# Quickstart: Use Compute Engine with Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/quickstart-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Quickstart: Use Compute Engine with Rust Stay organized with collections  Save and categorize content based on your preferences. 

The [Compute Engine](https://docs.cloud.google.com/compute/docs) API lets you create and run virtual machines (VMs) on Google Cloud.

This guide shows you how to initialize the Compute Engine client library for Rust and perform basic operations using the library.

## Prerequisites

Before you start this guide, make sure that you have an existing [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) with [billing enabled](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).

## Add the client library as a dependency

Use `cargo` to add the `google-cloud-compute-v1` crate to your `Cargo.toml` file:
    
    
    cargo add google-cloud-compute-v1
    

## List virtual machines

The client to create and manage virtual machines is called `Instances`. You can list the VMs in a project and zone using the `list()` method of this type:
    
    
    pub async fn sample(project_id: &str) -> anyhow::Result<()> {
        use google_cloud_compute_v1::client::Instances;
        use google_cloud_gax::paginator::ItemPaginator;
    
        const ZONE: &str = "us-central1-a";
    
        let client = Instances::builder().build().await?;
        println!("Listing instances for project {project_id}");
        let mut instances = client
            .list()
            .set_project(project_id)
            .set_zone(ZONE)
            .by_item();
        while let Some(item) = instances.next().await.transpose()? {
            println!("  {:?}", item.name);
        }
        println!("DONE");
        Ok(())
    }

## What's next

  * Learn more about the [Compute Engine client libraries](https://docs.cloud.google.com/compute/docs/api/libraries).
  * Learn about [Working with long-running operations](https://docs.cloud.google.com/rust/docs/long-running-operations).
  * Learn about [Configuring polling policies](https://docs.cloud.google.com/rust/docs/configure-polling-policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
