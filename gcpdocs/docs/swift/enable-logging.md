---
url: https://docs.cloud.google.com/swift/enable-logging/
title: Enable logging \u00a0|\u00a0 Swift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:26:33.264525+00:00
---

# Enable logging  |  Swift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/swift/enable-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Swift ](https://docs.cloud.google.com/swift)
  * [ Guides ](https://docs.cloud.google.com/swift/overview)



Send feedback 

#  Enable logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to enable debug logging in the Google Cloud client libraries for Swift. Logging requests, responses, and errors to the console makes it easier to troubleshoot applications.

**Warning:** The logs described in this document are meant for debugging applications. The logs include full request and response messages, which might include sensitive information. Before enabling these logs in production, consider the security and privacy implications.

## Before you begin

This guide uses the Secret Manager API. To enable this API, follow the [Secret Manager quickstart](https://docs.cloud.google.com/secret-manager/docs/quickstart).

For complete setup instructions for the Swift client libraries, see [Quickstart: Get started with Swift](https://docs.cloud.google.com/swift/quickstart).

## Enable logging

The Swift client libraries use Apple's [`swift-log`](https://github.com/apple/swift-log) package on GitHub (`Logging` module) to emit structured, contextual diagnostic messages. The `swift-log` package separates the logging API (`Logger`) from the components that collect and format log messages (`LogHandler`). By default, `swift-log` uses `StreamLogHandler` to write log messages to standard error, and many other [logging backends](https://www.swift.org/ecosystem/server-libraries/#logging) are available on Swift.org.

  1. Add the `swift-log` package and its `Logging` product to your target dependencies:
         
         swift package add-dependency \
             https://github.com/apple/swift-log.git --from 1.12.0
         # Replace Quickstart with the name of your target
         swift package add-target-dependency \
             Logging Quickstart --package swift-log
         

  2. Add the imports required to use the client library and `Logging`: 
         
         import GoogleCloudSecretManagerV1
         import GoogleGax
         import Logging

  3. Write a function that receives the project ID as a parameter: 
         
         func sample(projectId: String) async throws {

  4. Create a `Logger` and set its `logLevel` to `.debug`. Because the client libraries emit request, response, and error logs at the `.debug` level, a logger with the default `.info` level doesn't output these messages: 
         
         var logger = Logger(label: "com.example.my-app")
         logger.logLevel = .debug

  5. Initialize a client with logging enabled by setting `logger` on `ClientOptions`. Because `Logger` has value semantics, configure `logLevel` (and any custom metadata) before passing `logger` to `ClientOptions`; modifying `logger` afterward doesn't affect the client: 
         
         let client = try SecretManagerServiceClient(
           ClientOptions().with {
             $0.logger = logger
           })

  6. Use the client to send a request: 
         
         let secrets = client.listSecretsByItems(
           request: ListSecretsRequest().with { $0.parent = "projects/\(projectId)" })
         for try await item in secrets {
           print("  \(item)")
         }




### Expected output

When the client executes an RPC, it logs an `enter` message before sending the request, followed by either a `success` message with the response or an `error` message if the call fails. These log entries wrap the logical RPC call across any retry attempts rather than logging each individual attempt. When iterating over a paginated sequence such as `listSecretsByItems`, each fetched page issues a separate `listSecrets` RPC with its own `enter` and `success` or `error` log entries.

The output (formatted for readability) includes lines such as the following:
    
    
    2026-09-30T18:00:00+0000 debug com.example.my-app:
      gcp.artifact.id=google-cloud-secretmanager-v1
      gcp.client.service=secretmanager
      gcp.experimental.swift.client=SecretManagerServiceClient
      gcp.experimental.swift.method=listSecrets
      gcp.experimental.swift.request.id=550E8400-E29B-41D4-A716-446655440000
      [GoogleCloudSecretManagerV1] enter  : ListSecretsRequest(parent: "projects/my-project", ...) RequestOptions(...)
    

On success, the client logs the response:
    
    
    2026-09-30T18:00:01+0000 debug com.example.my-app:
      gcp.artifact.id=google-cloud-secretmanager-v1
      gcp.client.service=secretmanager
      gcp.experimental.swift.client=SecretManagerServiceClient
      gcp.experimental.swift.method=listSecrets
      gcp.experimental.swift.request.id=550E8400-E29B-41D4-A716-446655440000
      [GoogleCloudSecretManagerV1] success: ListSecretsRequest(...) RequestOptions(...) ListSecretsResponse(...)
    

If the request fails, the client logs the error details:
    
    
    2026-09-30T18:00:01+0000 debug com.example.my-app:
      gcp.artifact.id=google-cloud-secretmanager-v1
      gcp.client.service=secretmanager
      gcp.experimental.swift.client=SecretManagerServiceClient
      gcp.experimental.swift.method=listSecrets
      gcp.experimental.swift.request.id=550E8400-E29B-41D4-A716-446655440000
      [GoogleCloudSecretManagerV1] error  : ListSecretsRequest(...) RequestOptions(...) http(StatusError(...))
    

In addition to any metadata already attached to the `Logger` by your application, the client automatically attaches structured metadata to each log entry:

  * `gcp.artifact.id`: The client library package identifier (for example, `google-cloud-secretmanager-v1`).
  * `gcp.client.service`: The target Google Cloud service name (for example, `secretmanager`).
  * `gcp.experimental.swift.client`: The name of the service client (for example, `SecretManagerServiceClient`).
  * `gcp.experimental.swift.method`: The RPC method name being invoked (for example, `listSecrets`).
  * `gcp.experimental.swift.request.id`: A unique UUID generated for each RPC invocation to correlate its `enter` and `success` or `error` log entries.



## Complete code

The following example shows the complete code for this guide:
    
    
    import GoogleCloudSecretManagerV1
    import GoogleGax
    import Logging
    
    func sample(projectId: String) async throws {
      var logger = Logger(label: "com.example.my-app")
      logger.logLevel = .debug
      let client = try SecretManagerServiceClient(
        ClientOptions().with {
          $0.logger = logger
        })
      let secrets = client.listSecretsByItems(
        request: ListSecretsRequest().with { $0.parent = "projects/\(projectId)" })
      for try await item in secrets {
        print("  \(item)")
      }
    }

## What's next

  * Learn how to configure [Package traits](https://docs.cloud.google.com/swift/package-traits) for large client libraries.
  * Browse the [Swift Cloud Client Libraries](https://docs.cloud.google.com/swift/reference) reference documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
