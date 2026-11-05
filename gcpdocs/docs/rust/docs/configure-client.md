---
url: https://docs.cloud.google.com/rust/docs/configure-client/
title: Configure a client \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T22:24:28.318508+00:00
---

# Configure a client  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/configure-client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Configure a client Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud Client Libraries for Rust let you configure client behavior, such as endpoint overrides, authentication methods, and retry policies. You configure a client using a [`ClientBuilder`](https://docs.rs/google-cloud-gax/latest/google_cloud_gax/client_builder/struct.ClientBuilder.html) obtained by calling the service client's `builder()` method (for example, `SecretManagerService::builder()`).

## Customize the API endpoint

By default, client libraries connect to the global API endpoint for the service. If you need to connect to a regional endpoint or a private access endpoint, you can override the default endpoint configuration. For instructions and examples, see [Override the default endpoint](https://docs.cloud.google.com/rust/docs/override-default-endpoint).

## Configure authentication

While the client attempts to find [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) automatically, you can explicitly provide credentials using the `with_credentials` method on the client builder. For instructions and examples, see [Override the default authentication method](https://docs.cloud.google.com/rust/docs/override-default-authentication).

## Enable logging

You can enable debug logging to inspect requests and responses for troubleshooting. The Rust client libraries use the Tokio `tracing` crate to collect structured, async-aware diagnostics. For setup instructions, see [Enable logging](https://docs.cloud.google.com/rust/docs/enable-logging).

## Configure a proxy

To configure a proxy, use the [standard environment variables](https://docs.rs/reqwest/latest/reqwest/index.html#proxies) supported by `reqwest`. You don't need to configure proxy settings in your Rust code. Instead, set the following environment variables in your shell or container environment:
    
    
    export http_proxy="http://proxy.example.com:3128"
    export https_proxy="http://proxy.example.com:3128"
    

## Configure retries

The client libraries can automatically retry operations that fail due to transient errors. You can configure default retry policies or override retry limits for specific requests. For instructions and examples, see [Configuring retry policies](https://docs.cloud.google.com/rust/docs/configure-retry-policies).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
