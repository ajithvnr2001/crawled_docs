---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/ListBoundariesResponse/
title: ListBoundariesResponse \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T05:45:21.457244+00:00
---

# ListBoundariesResponse  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/ListBoundariesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  ListBoundariesResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



A page of the response received from the boundaries.list method.

A paginated response where more pages are available has `nextPageToken` set. This token can be used in a subsequent request to retrieve the next page.

NOTE: A response may contain fewer elements than the request `pageSize` and still have a `nextPageToken`.

JSON representation  
---  
      
    
    {
      "boundaries": [
        {
          object ([Boundary](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.boundaries#Boundary))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`boundaries[]` |  `object (`[Boundary](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.boundaries#Boundary)`)` The list of Boundaries under the parent. This list can be paginated.  
`nextPageToken` |  `string` Pagination token.If the result set is too large to fit in a single response, this token is returned. It encodes the position of the current result cursor. Feeding this value into a new list request with the `pageToken` parameter gives the next page of the results.When `nextPageToken` is not filled in, there is no next page and the list returned is the last page in the result set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
