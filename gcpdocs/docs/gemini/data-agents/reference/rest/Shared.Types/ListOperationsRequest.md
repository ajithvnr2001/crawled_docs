---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsRequest/
title: ListOperationsRequest \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:54:42.302997+00:00
---

# ListOperationsRequest  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsRequest/

[ Skip to main content ](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsRequest/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsRequest/)
  * [Deutsch](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsRequest/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsRequest/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsRequest/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsRequest/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsRequest/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsRequest/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsRequest/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsRequest/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsRequest/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsRequest/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsRequest/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/gemini-color.svg) ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)


[Start free](https://console.cloud.google.com/freetrial)
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)


Send feedback 
#  ListOperationsRequest Stay organized with collections  Save and categorize content based on your preferences.
  * [JSON representation](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsRequest/#SCHEMA_REPRESENTATION)


The request message for `Operations.ListOperations[](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.operations/list#google.longrunning.Operations.ListOperations)`.  
| JSON representation  |  
| --- |  
| 
```
{
  "name": string,
  "filter": string,
  "pageSize": integer,
  "pageToken": string,
  "returnPartialSuccess": boolean
}
```
 |  
| Fields  |  
| --- |  
| `name`  |  `string` The name of the operation's parent resource.  |  
| `filter`  |  `string` The standard list filter.  |  
| `pageSize`  |  `integer` The standard list page size.  |  
| `pageToken`  |  `string` The standard list page token.  |  
| `returnPartialSuccess`  |  `boolean` When set to `true`, operations that are reachable are returned as normal, and those that are unreachable are returned in the `ListOperationsResponse.unreachable[](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/ListOperationsResponse#FIELDS.unreachable)` field. This can only be `true` when reading across collections. For example, when `parent` is set to `"projects/example/locations/-"`. This field is not supported by default and will result in an `UNIMPLEMENTED` error if set unless explicitly documented otherwise in service or product specific documentation.  |  
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
