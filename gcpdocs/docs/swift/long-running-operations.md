---
url: https://docs.cloud.google.com/swift/long-running-operations/
title: Long-running operations \u00a0|\u00a0 Swift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T05:43:31.901247+00:00
---

# Long-running operations  |  Swift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/swift/long-running-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Swift ](https://docs.cloud.google.com/swift)
  * [ Guides ](https://docs.cloud.google.com/swift/overview)



Send feedback 

#  Long-running operations Stay organized with collections  Save and categorize content based on your preferences. 

Some Google Cloud APIs perform operations that take longer to complete than the duration of a typical HTTP request-response cycle. These operations are known as long-running operations (LROs). Instead of blocking until the work finishes, these API methods return an operation resource, and the client polls the service periodically until the operation completes.

The Google Cloud client libraries for Swift simplify working with LROs by providing helper methods that handle polling and exponential backoff automatically. This document shows you how to use these polling helper methods.

## Before you begin

This document uses the Workflows API. To enable this API, follow the [Workflows quickstart](https://docs.cloud.google.com/workflows/docs/create-workflow-gcloud).

For complete setup instructions for the Swift client libraries, see [Quickstart: Get started with Swift](https://docs.cloud.google.com/swift/quickstart).

## Make an API request with a long-running operation

In this example, you use the `WorkflowsClient` client to create a workflow. The `createWorkflowPollingUntilDone` method starts the operation and automatically polls until the operation completes, returning the created `Workflow` resource. To make an API request with a long-running operation, follow these steps:

  1. Add the imports required to use the client library: 
         
         import Foundation
         import GoogleGax
         import GoogleCloudWorkflowsV1

  2. Write a function that accepts the project ID, location, and workflow ID as parameters: 
         
         func sample(projectId: String, location: String, workflowId: String) async throws {

  3. Initialize the client with the default options: 
         
         let client = try WorkflowsClient()

  4. Create the workflow and poll the operation until it completes: 
         
         let workflow = Workflow().with {
           $0.description = "A sample workflow"
           $0.sourceCode = .sourceContents(
             """
             main:
               steps:
                 - returnStep:
                     return "Hello World!"
             """
           )
         }
         let response = try await client.createWorkflowPollingUntilDone(
           parent: "projects/\(projectId)/locations/\(location)",
           workflow: workflow,
           workflowId: workflowId
         )
         print("Workflow created: \(response.name)")




## Operation return types

Depending on the underlying API design, the return type of a `*PollingUntilDone` helper method varies:

  * **gRPC and[AIP-151](https://google.aip.dev/151) APIs**: for APIs that follow the AIP-151 specification on google.aip.dev, such as Workflows and Cloud Run, the operation service metadata includes the response type of the target resource. In these libraries, polling helpers unwrap the operation and return the target resource directly, such as a `Workflow` or `Service` resource.
  * **Discovery-based APIs** : for APIs such as Compute Engine, the Discovery document schema defines operation methods as returning a service `Operation` status resource, such as `GoogleCloudComputeV1.Operation`. When the task finishes, the polling helper returns this completed `Operation` resource rather than fetching the created or modified resource.



To retrieve the created or modified resource after a Discovery-based operation completes, await the polling helper method and then call the corresponding `get` method for the target resource using the identifiers from the request or properties on the returned `Operation` resource, such as `operation.targetLink`. If the operation fails, the polling helper throws an error.

## Complete code

The following example shows the complete code for this document:
    
    
    import Foundation
    import GoogleGax
    import GoogleCloudWorkflowsV1
    
    func sample(projectId: String, location: String, workflowId: String) async throws {
      let client = try WorkflowsClient()
      let workflow = Workflow().with {
        $0.description = "A sample workflow"
        $0.sourceCode = .sourceContents(
          """
          main:
            steps:
              - returnStep:
                  return "Hello World!"
          """
        )
      }
      let response = try await client.createWorkflowPollingUntilDone(
        parent: "projects/\(projectId)/locations/\(location)",
        workflow: workflow,
        workflowId: workflowId
      )
      print("Workflow created: \(response.name)")
    }

## What's next

  * Learn how to [override the default polling policies](https://docs.cloud.google.com/swift/override-polling-policy) for long-running operations.
  * Learn how to [override the default retry policies](https://docs.cloud.google.com/swift/override-retry-policy).
  * Learn how to [override the default endpoint](https://docs.cloud.google.com/swift/override-endpoint).
  * Learn how to [override the default authentication credentials](https://docs.cloud.google.com/swift/override-credentials).
  * Learn how to [enable logging](https://docs.cloud.google.com/swift/enable-logging) to troubleshoot requests and responses.
  * Learn how to configure [package traits](https://docs.cloud.google.com/swift/package-traits) for large client libraries.
  * Browse the [Swift Cloud client libraries](https://docs.cloud.google.com/swift/reference) reference documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
