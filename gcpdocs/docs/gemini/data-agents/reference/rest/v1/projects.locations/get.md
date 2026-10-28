---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/
title: Method: projects.locations.get \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:52:42.054159+00:00
---

# Method: projects.locations.get  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/

[ Skip to main content ](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/)
  * [Deutsch](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/gemini-color.svg) ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [HTTP request](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#http-request)
  * [Path parameters](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#path-parameters)
  * [Request body](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#request-body)
  * [Response body](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#response-body)
  * [Authorization scopes](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#authorization-scopes)
  * [IAM Permissions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#iam-permissions)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)


Send feedback 
#  Method: projects.locations.get Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#http-request)
  * [Path parameters](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#path-parameters)
  * [Request body](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#request-body)
  * [Response body](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#response-body)
  * [Authorization scopes](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#authorization-scopes)
  * [IAM Permissions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#iam-permissions)


  * [HTTP request](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#body.HTTP_TEMPLATE)
  * [Path parameters](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#body.PATH_PARAMETERS)
  * [Request body](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#body.request_body)
  * [Response body](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#body.response_body)
  * [Authorization scopes](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#body.aspect)
  * [IAM Permissions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get/#body.aspect_1)


Gets information about a location.
### HTTP request
`GET https://geminidataanalytics.googleapis.com/v1/{name=projects/*/locations/*}`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters  
| Parameters  |  
| --- |  
| `name`  |  `string` Resource name for the location.  |  
### Request body
The request body must be empty.
### Response body
If successful, the response body contains an instance of `Location[](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListLocationsResponse#Location)`.
### Authorization scopes
Requires the following OAuth scope:
  * `https://www.googleapis.com/auth/cloud-platform`


For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).
### IAM Permissions
Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:
  * `geminidataanalytics.locations.get`


For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
