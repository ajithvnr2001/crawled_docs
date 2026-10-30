---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.stores/batchGet/
title: Method: projects.locations.brands.stores.batchGet \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:40:36.822849+00:00
---

# Method: projects.locations.brands.stores.batchGet  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.stores/batchGet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  Method: projects.locations.brands.stores.batchGet Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Batch gets stores.

### HTTP request

`GET https://foodorderingaiagent.googleapis.com/v1/{parent=projects/*/locations/*/brands/*}/stores:batchGet`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource shared by all stores being retrieved. Format: projects/{project}/locations/{location}/brands/{brand}  
  
### Query parameters

Parameters  
---  
`names[]` |  `string` Required. The names of the stores to retrieve. A maximum of 1000 stores can be retrieved in a batch. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
  
### Request body

The request body must be empty.

### Response body

Response message for `[MenuService.BatchGetStores](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.stores/batchGet#google.cloud.foodorderingaiagent.v1.MenuService.BatchGetStores)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "stores": [
        {
          object ([Store](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.stores#Store))
        }
      ]
    }  
  
Fields  
---  
`stores[]` |  `object (`[Store](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.stores#Store)`)` The requested stores.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
