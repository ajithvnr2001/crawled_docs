---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/
title: SendMessageConfiguration \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:12:46.698223+00:00
---

# SendMessageConfiguration  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/

[ Skip to main content ](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/)
  * [Deutsch](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fgemini%2Fdata-agents%2Freference%2Frest%2FShared.Types%2FSendMessageConfiguration%2F&prompt=select_account)
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


Was this helpful?
Send feedback 
#  SendMessageConfiguration Stay organized with collections  Save and categorize content based on your preferences.
  * [JSON representation](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/#SCHEMA_REPRESENTATION)


Configuration of a send message request.  
| JSON representation  |  
| --- |  
| 
```
{
  "acceptedOutputModes": [
    string
  ],
  "pushNotification": {
    object (PushNotificationConfig[](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/PushNotificationConfig))
  },
  "historyLength": integer,
  "blocking": boolean
}
```
 |  
| Fields  |  
| --- |  
| `acceptedOutputModes[]`  |  `string` The output modes that the agent is expected to respond with.  |  
| `pushNotification`  |  `object (`PushNotificationConfig[](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/PushNotificationConfig)`)` A configuration of a webhook that can be used to receive updates  |  
| `historyLength`  |  `integer` The maximum number of messages to include in the history. if 0, the history will be unlimited.  |  
| `blocking`  |  `boolean` If true, the message will be blocking until the task is completed. If false, the message will be non-blocking and the task will be returned immediately. It is the caller's responsibility to check for any task updates.  |  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
