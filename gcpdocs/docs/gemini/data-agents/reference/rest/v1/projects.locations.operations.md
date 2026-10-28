---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.operations
title: REST Resource: projects.locations.operations \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: httpx+scrapegraph (scrapling: scrapling status 429 | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 1299 in create_browser_context (../../../../usr/local/lib/python3.10/dist-packages/crawl4ai/browser_manager.py):
Error: Browser is not available. It may have been closed, crashed, or not yet started. Ensure the browser is running before creating new contexts.

Code context:
1294                   raise RuntimeError(
1295                       "Cannot create new browser contexts when using "
1296                       "use_persistent_context=True. Persistent context uses a "
1297                       "single shared context."
1298                   )
1299 →             raise RuntimeError(
1300                   "Browser is not available. It may have been closed, crashed, "
1301                   "or not yet started. Ensure the browser is running before "
1302                   "creating new contexts."
1303               )
1304           # Base settings)
fetched_at: 2026-10-27T16:24:36.263164+00:00
---

# REST Resource: projects.locations.operations  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.operations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  REST Resource: projects.locations.operations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Operation
    * JSON representation
  * Methods



## Resource: Operation

This resource represents a long-running operation that is the result of a network API call.

JSON representation  
---  
      
    
    {
      "name": string,
      "metadata": {
        "@type": string,
        field1: ...,
        ...
      },
      "done": boolean,
    
      // Union field result can be only one of the following:
      "error": {
        object ([Status](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "response": {
        "@type": string,
        field1: ...,
        ...
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`name` |  `string` The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.  
`metadata` |  `object` Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`done` |  `boolean` If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  
Union field `result`. The operation result, which can be either an `error` or a valid `response`. If `done` == `false`, neither `error` nor `response` is set. If `done` == `true`, exactly one of `error` or `response` can be set. Some services might not provide the result. `result` can be only one of the following:  
`error` |  `object (`[Status](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` The error result of the operation in case of failure or cancellation.  
`response` |  `object` The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
## Methods  
  
---  
  
### `[cancel](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.operations/cancel)`

|  Starts asynchronous cancellation on a long-running operation.  
  
### `[delete](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.operations/delete)`

|  Deletes a long-running operation.  
  
### `[get](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.operations/get)`

|  Gets the latest state of a long-running operation.  
  
### `[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.operations/list)`

|  Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
