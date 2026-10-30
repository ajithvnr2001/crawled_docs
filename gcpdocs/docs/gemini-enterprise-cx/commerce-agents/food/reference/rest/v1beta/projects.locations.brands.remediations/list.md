---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.remediations/list/
title: Method: projects.locations.brands.remediations.list \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:40:07.595097+00:00
---

# Method: projects.locations.brands.remediations.list  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.remediations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  Method: projects.locations.brands.remediations.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Lists remediations.

### HTTP request

`GET https://foodorderingaiagent.googleapis.com/v1beta/{parent=projects/*/locations/*/brands/*}/remediations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent brand containing the remediations. Format: projects/{project}/locations/{location}/brands/{brand}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of remediations to return. The service may return fewer than this value. If unspecified, at most 50 remediations will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token received from a previous `remediations.list` call.  
`filter` |  `string` Optional. Useful for the UI to filter by State (e.g., state="ACTIVE").  
  
### Request body

The request body must be empty.

### Response body

Response message for `[MenuService.ListRemediations](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.remediations/list#google.cloud.foodorderingaiagent.v1beta.MenuService.ListRemediations)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "remediations": [
        {
          object ([Remediation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.remediations#Remediation))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`remediations[]` |  `object (`[Remediation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.remediations#Remediation)`)` The list of retrieved remediations.  
`nextPageToken` |  `string` A token that can be sent as `pageToken` to retrieve the next page.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
