---
url: https://docs.cloud.google.com/swift/override-polling-policy/
title: Override the default polling policies \u00a0|\u00a0 Swift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:31:13.214007+00:00
---

# Override the default polling policies  |  Swift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/swift/override-polling-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Swift ](https://docs.cloud.google.com/swift)
  * [ Guides ](https://docs.cloud.google.com/swift/overview)



Send feedback 

#  Override the default polling policies Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud client libraries for Swift provide `*PollingUntilDone` methods to poll long-running operations until they complete. You might need to change the default polling limits, the backoff intervals, or the types of polling errors that stop the polling loop. This document shows you how to override the default polling policies in the client libraries.

## Before you begin

This document uses the Workflows API. To enable this API, follow the [Workflows quickstart](https://docs.cloud.google.com/workflows/docs/create-workflow-gcloud).

For complete setup instructions for the Swift client libraries, see [Quickstart: Get started with Swift](https://docs.cloud.google.com/swift/quickstart).

## Long-running operations

Some Google Cloud APIs perform operations that take too long to finish within a single request-response cycle. Instead of blocking until the work finishes, the API starts a background task on the server. It immediately returns an operation resource that represents the in-progress work.

To get the final result, the client must periodically poll the service for the operation's status. When you call a `*PollingUntilDone` helper method, the client library runs this polling loop for you:

  1. The client sends the initial request to start the background task on the server.
  2. While the operation is still in progress, the client waits for a delay determined by the _polling backoff policy_ and requests the latest status of the operation.
  3. If a status check fails—for example, due to a transient network or service error—the _polling error policy_ determines whether to continue polling or stop the loop. The policy also enforces overall time or attempt limits so polling doesn't run indefinitely.
  4. When the server reports that the operation has finished, the helper returns the completed resource—or throws the operation's error if the background task failed on the server.



## Default polling behavior

Each client uses the following default policies for this polling loop:

  * The _polling error policy_ continues polling on [AIP-194](https://google.aip.dev/194) (at google.aip.dev) transient errors, `TOO_MANY_REQUESTS` errors, and I/O errors, and stops polling after 30 minutes.
  * The _polling backoff policy_ uses truncated exponential backoff without jitter, starting at one second and doubling between attempts up to a maximum of five minutes.



In addition, each status request made during the polling loop is an idempotent RPC and uses the client's [retry policy](https://docs.cloud.google.com/swift/override-retry-policy) before reporting an error to the polling loop.

## Override the policies for a client

The policies that you set on a client apply to every long-running operation polled through that client. To override the default polling policies for a client, follow these steps:

  1. Add the imports required to use the client library: 
         
         import Foundation
         import GoogleGax
         import GoogleCloudWorkflowsV1

  2. Write a function that receives the project ID, location, and workflow ID as parameters: 
         
         func sample(projectId: String, location: String, workflowId: String) async throws {

  3. Initialize a client that stops polling sooner than the default. Call the `BasePollingErrorPolicy.unbounded()` method to keep the default definition of transient polling errors, and chain the `withTimeLimit(_:)` and `withAttemptLimit(_:)` methods to set the limits. You can use either limit on its own: 
         
         let client = try WorkflowsClient(
           ClientOptions().with {
             $0.pollingErrorPolicy = BasePollingErrorPolicy.unbounded()
               .withTimeLimit(.seconds(5 * 60))
               .withAttemptLimit(20)
           })

  4. Initialize a client that also configures a custom backoff policy between polling attempts: 
         
         let fasterClient = try WorkflowsClient(
           ClientOptions().with {
             $0.pollingErrorPolicy = BasePollingErrorPolicy.unbounded()
               .withTimeLimit(.seconds(5 * 60))
               .withAttemptLimit(20)
             $0.pollingBackoffPolicy = ExponentialBackoff(
               clamping: .milliseconds(500),
               maximumDelay: .seconds(10),
               scaling: 1.5
             )
           })
         try await fasterClient.deleteWorkflowPollingUntilDone(
           name: "projects/\(projectId)/locations/\(location)/workflows/\(workflowId)"
         )




The library also provides the following polling error policies:

  * `AIP194.unbounded()`: continues polling only on `UNAVAILABLE` errors. You can chain this policy with the `continueOnIO()` and `continueOnTooManyRequests()` methods.
  * `AlwaysPoll.unbounded()`: continues polling on all errors.



If your app has requirements that the built-in types don't cover, you can implement the `PollingErrorPolicy` and `PollingBackoffPolicy` protocols.

## Override the policy for a single request

Every `*PollingUntilDone` method accepts a `RequestOptions` value. The polling policies that it sets apply to that operation only and take precedence over the client configuration:
    
    
    let options = RequestOptions().with {
      $0.pollingErrorPolicy = BasePollingErrorPolicy.unbounded().withTimeLimit(.seconds(60))
      $0.pollingBackoffPolicy = ExponentialBackoff(
        clamping: .milliseconds(250),
        maximumDelay: .seconds(5)
      )
    }
    try await client.deleteWorkflowPollingUntilDone(
      request: DeleteWorkflowRequest().with {
        $0.name = "projects/\(projectId)/locations/\(location)/workflows/\(workflowId)"
      },
      options: options)

## Complete code

The following example shows the complete code for this document:
    
    
    import Foundation
    import GoogleGax
    import GoogleCloudWorkflowsV1
    
    func sample(projectId: String, location: String, workflowId: String) async throws {
      let client = try WorkflowsClient(
        ClientOptions().with {
          $0.pollingErrorPolicy = BasePollingErrorPolicy.unbounded()
            .withTimeLimit(.seconds(5 * 60))
            .withAttemptLimit(20)
        })
      let fasterClient = try WorkflowsClient(
        ClientOptions().with {
          $0.pollingErrorPolicy = BasePollingErrorPolicy.unbounded()
            .withTimeLimit(.seconds(5 * 60))
            .withAttemptLimit(20)
          $0.pollingBackoffPolicy = ExponentialBackoff(
            clamping: .milliseconds(500),
            maximumDelay: .seconds(10),
            scaling: 1.5
          )
        })
      try await fasterClient.deleteWorkflowPollingUntilDone(
        name: "projects/\(projectId)/locations/\(location)/workflows/\(workflowId)"
      )
      let options = RequestOptions().with {
        $0.pollingErrorPolicy = BasePollingErrorPolicy.unbounded().withTimeLimit(.seconds(60))
        $0.pollingBackoffPolicy = ExponentialBackoff(
          clamping: .milliseconds(250),
          maximumDelay: .seconds(5)
        )
      }
      try await client.deleteWorkflowPollingUntilDone(
        request: DeleteWorkflowRequest().with {
          $0.name = "projects/\(projectId)/locations/\(location)/workflows/\(workflowId)"
        },
        options: options)
    }

## What's next

  * Learn how to [override the default endpoint](https://docs.cloud.google.com/swift/override-endpoint).
  * Learn how to [override the default authentication credentials](https://docs.cloud.google.com/swift/override-credentials).
  * Learn how to [override the default retry policies](https://docs.cloud.google.com/swift/override-retry-policy).
  * Learn how to [enable logging](https://docs.cloud.google.com/swift/enable-logging) to troubleshoot requests and responses.
  * Learn how to configure [package traits](https://docs.cloud.google.com/swift/package-traits) for large client libraries.
  * Browse the [Swift Cloud Client Libraries](https://docs.cloud.google.com/swift/reference) reference documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
