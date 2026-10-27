---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores.documents/list/
title: Method: projects.locations.dataStores.documents.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T05:38:02.573001+00:00
---

# Method: projects.locations.dataStores.documents.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores.documents/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.dataStores.documents.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists Documents in a DataStore.

### HTTP request

`GET https://vectorsearch.googleapis.com/v1beta/{parent}/documents`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the DataStore to list Documents from. Format: `projects/{project}/locations/{location}/dataStores/{dataStore}`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, at most 10 Documents are returned. The maximum value is 1,000; larger values are coerced to 1,000.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. Not currently supported. A request that sets this field fails with `INVALID_ARGUMENT`.  
`orderBy` |  `string` Optional. Not currently supported. A request that sets this field fails with `INVALID_ARGUMENT`.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[DocumentService.ListDocuments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores.documents/list#google.cloud.vectorsearch.v1beta.DocumentService.ListDocuments)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "documents": [
        {
          object ([Document](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores.documents#Document))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`documents[]` |  `object (`[Document](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores.documents#Document)`)` The list of Documents.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/vectorsearch`
  * `https://www.googleapis.com/auth/vectorsearch.readonly`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
