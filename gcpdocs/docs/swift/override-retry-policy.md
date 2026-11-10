---
url: https://docs.cloud.google.com/swift/override-retry-policy/
title: Override the default retry policies \u00a0|\u00a0 Swift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T05:53:21.068327+00:00
---

# Override the default retry policies  |  Swift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/swift/override-retry-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Swift ](https://docs.cloud.google.com/swift)
  * [ Guides ](https://docs.cloud.google.com/swift/overview)



Send feedback 

#  Override the default retry policies Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud client libraries for Swift automatically retry requests that fail with transient errors. Some applications need different behavior: they might need to fail faster, keep trying for longer, or retry requests that the libraries consider unsafe to retry. This document shows you how to override the default retry policies.

## Before you begin

This guide uses the Secret Manager API. To enable this API, follow the [Secret Manager quickstart](https://docs.cloud.google.com/secret-manager/docs/quickstart).

For complete setup instructions for the Swift client libraries, see [Quickstart: Get started with Swift](https://docs.cloud.google.com/swift/quickstart).

## Default retry behavior

Each client is configured with three policies that together control retries:

  * The _retry policy_ determines whether to retry an error and when to stop retrying. By default, it retries [AIP-194](https://google.aip.dev/194) (at `google.aip.dev`) transient errors and I/O errors for idempotent requests only, stopping after 60 seconds or 10 attempts, whichever comes first.
  * The _backoff policy_ determines how long to wait between attempts. By default, it uses exponential backoff, starting at one second and doubling up to a maximum of one minute.
  * The _retry throttler_ prevents the client from adding load to a service that is already failing. By default, it uses an adaptive throttler.



A request is only retried when it's safe to do so: either the request failed before any data was sent, or the error is transient and the request is idempotent. The client libraries use a conservative heuristic for idempotency: only `GET` and `PUT` requests qualify.

## Override the policies for a client

The policies set on a client apply to every request made through that client:

  1. Add the imports required to use the client library: 
         
         import Foundation
         import GoogleGax
         import GoogleCloudSecretManagerV1

  2. Write a function that receives the project ID as a parameter: 
         
         func sample(projectId: String) async throws {

  3. Initialize a client that stops retrying sooner than the default. Use `BaseRetryPolicy.unbounded()` to keep the default definition of which errors are transient, and chain `withTimeLimit(_:)` and `withAttemptLimit(_:)` to set the limits. You can use either limit on its own: 
         
         let client = try SecretManagerServiceClient(
           ClientOptions().with {
             $0.retryPolicy = BaseRetryPolicy.unbounded().withTimeLimit(.seconds(10)).withAttemptLimit(3)
           })

  4. Initialize a client that also configures a custom backoff policy between attempts: 
         
         let slowerClient = try SecretManagerServiceClient(
           ClientOptions().with {
             $0.retryPolicy = BaseRetryPolicy.unbounded().withTimeLimit(.seconds(10)).withAttemptLimit(3)
             $0.backoffPolicy = ExponentialBackoff(
               clamping: .milliseconds(250),
               maximumDelay: .seconds(5),
               scaling: 1.5
             )
           })




The library provides additional retry policies: `AlwaysRetry.unbounded()` retries every error, which is only safe when the operation is idempotent, and `NeverRetry` disables retries. Applications with requirements not covered by the built-in types can implement the `RetryPolicy` protocol.

## Override the policy for a single request

Every client method accepts a `RequestOptions` value. The policies that it sets apply to that request only and take precedence over the client configuration:
    
    
    let options = RequestOptions().with {
      $0.retryPolicy = NeverRetry()
    }
    let secret = try await client.getSecret(
      request: GetSecretRequest().with { $0.name = "projects/\(projectId)/secrets/my-secret" },
      options: options)
    print("secret: \(secret)")

## Retry a request that the library considers unsafe

Because the idempotency heuristic is conservative, some requests aren't retried by default even though the service documents them as safe to repeat. A delete request guarded by an `etag` is one example: repeating it can't delete a different version of the resource. Set `idempotent` to `true` on `RequestOptions` to indicate that the request is safe to retry:
    
    
    let retried = RequestOptions().with {
      $0.retryPolicy = BaseRetryPolicy.unbounded().withTimeLimit(.seconds(30))
      $0.idempotent = true
    }
    try await slowerClient.deleteSecret(
      request: DeleteSecretRequest().with {
        $0.name = "projects/\(projectId)/secrets/my-secret"
        $0.etag = "\"an-etag-from-a-previous-read\""
      },
      options: retried)

**Warning:** Overriding the idempotency of a request that isn't idempotent might apply the request more than once.

## Complete code

The following example shows the complete code for this guide:
    
    
    import Foundation
    import GoogleGax
    import GoogleCloudSecretManagerV1
    
    func sample(projectId: String) async throws {
      let client = try SecretManagerServiceClient(
        ClientOptions().with {
          $0.retryPolicy = BaseRetryPolicy.unbounded().withTimeLimit(.seconds(10)).withAttemptLimit(3)
        })
      let slowerClient = try SecretManagerServiceClient(
        ClientOptions().with {
          $0.retryPolicy = BaseRetryPolicy.unbounded().withTimeLimit(.seconds(10)).withAttemptLimit(3)
          $0.backoffPolicy = ExponentialBackoff(
            clamping: .milliseconds(250),
            maximumDelay: .seconds(5),
            scaling: 1.5
          )
        })
      let options = RequestOptions().with {
        $0.retryPolicy = NeverRetry()
      }
      let secret = try await client.getSecret(
        request: GetSecretRequest().with { $0.name = "projects/\(projectId)/secrets/my-secret" },
        options: options)
      print("secret: \(secret)")
      let retried = RequestOptions().with {
        $0.retryPolicy = BaseRetryPolicy.unbounded().withTimeLimit(.seconds(30))
        $0.idempotent = true
      }
      try await slowerClient.deleteSecret(
        request: DeleteSecretRequest().with {
          $0.name = "projects/\(projectId)/secrets/my-secret"
          $0.etag = "\"an-etag-from-a-previous-read\""
        },
        options: retried)
    }

## What's next

  * [Override the default endpoint](https://docs.cloud.google.com/swift/override-endpoint) describes how to change the default endpoint used by the Swift client libraries.
  * [Override the default authentication credentials](https://docs.cloud.google.com/swift/override-credentials) describes how to change the default credentials used by the Swift client libraries.
  * [Enable logging](https://docs.cloud.google.com/swift/enable-logging) describes how to enable debug logging to troubleshoot requests and responses.
  * Learn how to configure [Package traits](https://docs.cloud.google.com/swift/package-traits) for large client libraries.
  * Browse the [Swift Cloud Client Libraries](https://docs.cloud.google.com/swift/reference) reference documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
