---
url: https://docs.cloud.google.com/swift/override-credentials/
title: Override the default authentication credentials \u00a0|\u00a0 Swift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T05:53:00.039947+00:00
---

# Override the default authentication credentials  |  Swift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/swift/override-credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Swift ](https://docs.cloud.google.com/swift)
  * [ Guides ](https://docs.cloud.google.com/swift/overview)



Send feedback 

#  Override the default authentication credentials Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud client libraries for Swift automatically configure the authentication credentials used to authenticate requests to Google Cloud. Some applications might need to override the default credentials. This document shows you how to override the default authentication credentials.

## Before you begin

This guide uses the Cloud Natural Language API. To enable this API, follow the [Natural Language API setup guide](https://docs.cloud.google.com/natural-language/docs/setup).

For complete setup instructions for the Swift client libraries, see [Quickstart: Get started with Swift](https://docs.cloud.google.com/swift/quickstart).

## Override the default credentials with an API key

[API keys](https://docs.cloud.google.com/docs/authentication/api-keys) are text strings that grant access to some Google Cloud services. Using API keys can simplify development because they require less configuration than other [authentication methods](https://docs.cloud.google.com/docs/authentication). Before you use API keys, read [Best practices for managing API keys](https://docs.cloud.google.com/docs/authentication/api-keys-best-practices) to understand the associated security risks.

In this example, you configure the Natural Language API client to authenticate using an API key:

  1. Add the imports required to use the client library and authentication types: 
         
         import Foundation
         import GoogleAuth
         import GoogleGax
         import GoogleCloudLanguageV2

  2. Write a function that receives the API key as a parameter: 
         
         func sample(apiKey: String) async throws {

  3. Create a `Credentials` instance with the API key, and pass it to `ClientOptions` when initializing the client: 
         
         let credentials = try Credentials(configuration: .apiKey(apiKey))
         let client = try LanguageServiceClient(
           ClientOptions().with { $0.credentials = credentials }
         )

  4. Use the client to analyze the sentiment of a text document: 
         
         let document = Document().with {
           $0.type = .plainText
           $0.source = .content("Hello World!")
         }
         let response = try await client.analyzeSentiment(
           request: .init().with { $0.document = document })
         print("response=\(response)")




## Complete code

The following example shows the complete code for this guide:
    
    
    import Foundation
    import GoogleAuth
    import GoogleGax
    import GoogleCloudLanguageV2
    
    func sample(apiKey: String) async throws {
      let credentials = try Credentials(configuration: .apiKey(apiKey))
      let client = try LanguageServiceClient(
        ClientOptions().with { $0.credentials = credentials }
      )
      let document = Document().with {
        $0.type = .plainText
        $0.source = .content("Hello World!")
      }
      let response = try await client.analyzeSentiment(
        request: .init().with { $0.document = document })
      print("response=\(response)")
    }

## What's next

  * [Override the default endpoint](https://docs.cloud.google.com/swift/override-endpoint) describes how to change the default endpoint used by the Swift client libraries.
  * [Enable logging](https://docs.cloud.google.com/swift/enable-logging) describes how to enable debug logging to troubleshoot requests and responses.
  * Learn how to configure [Package traits](https://docs.cloud.google.com/swift/package-traits) for large client libraries.
  * Browse the [Swift Cloud Client Libraries](https://docs.cloud.google.com/swift/reference) reference documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
