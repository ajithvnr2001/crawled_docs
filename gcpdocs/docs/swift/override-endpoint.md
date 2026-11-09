---
url: https://docs.cloud.google.com/swift/override-endpoint/
title: Override the default endpoint \u00a0|\u00a0 Swift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-09T05:44:40.020960+00:00
---

# Override the default endpoint  |  Swift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/swift/override-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Swift ](https://docs.cloud.google.com/swift)
  * [ Guides ](https://docs.cloud.google.com/swift/overview)



Send feedback 

#  Override the default endpoint Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud client libraries for Swift automatically configure the endpoint for each service. Some applications might need to override the default endpoint, either because their network has specific requirements or because they need to use regional versions of a service. This document shows you how to override the default endpoint.

## Before you begin

This guide uses the Secret Manager API. To enable this API, follow the [Secret Manager quickstart](https://docs.cloud.google.com/secret-manager/docs/quickstart).

For complete setup instructions for the Swift client libraries, see [Quickstart: Get started with Swift](https://docs.cloud.google.com/swift/quickstart).

## Override the default endpoint

In this example, you configure the client library to use Secret Manager [regional endpoints](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/regional-endpoints). You can use the same override to configure the endpoint with one of the [private access options](https://docs.cloud.google.com/vpc/docs/private-access-options), or for [locational endpoints](https://docs.cloud.google.com/storage/docs/locational-endpoints) in the services that support them.

  1. Add the imports required to use the client library: 
         
         import Foundation
         import GoogleGax
         import GoogleCloudSecretManagerV1

  2. Write a function that receives the project ID and region as parameters: 
         
         func sample(projectId: String, region: String) async throws {

  3. Initialize a client and override the endpoint to use a regional endpoint: 
         
         let client = try SecretManagerServiceClient(
           ClientOptions().with {
             $0.endpoint = "https://secretmanager.\(region).rep.googleapis.com"
           })

  4. Use the client to retrieve the list of secrets in a region and iterate over the results: 
         
         let secrets = client.listSecretsByItems(
           request: ListSecretsRequest().with { $0.parent = "projects/\(projectId)/locations/\(region)" })
         for try await item in secrets {
           print("  \(item)")
         }




## Complete code

The following example shows the complete code for this guide:
    
    
    import Foundation
    import GoogleGax
    import GoogleCloudSecretManagerV1
    
    func sample(projectId: String, region: String) async throws {
      let client = try SecretManagerServiceClient(
        ClientOptions().with {
          $0.endpoint = "https://secretmanager.\(region).rep.googleapis.com"
        })
      let secrets = client.listSecretsByItems(
        request: ListSecretsRequest().with { $0.parent = "projects/\(projectId)/locations/\(region)" })
      for try await item in secrets {
        print("  \(item)")
      }
    }

## What's next

  * [Enable logging](https://docs.cloud.google.com/swift/enable-logging) describes how to enable debug logging to troubleshoot requests and responses.
  * Learn how to configure [Package traits](https://docs.cloud.google.com/swift/package-traits) for large client libraries.
  * Browse the [Swift Cloud Client Libraries](https://docs.cloud.google.com/swift/reference) reference documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
