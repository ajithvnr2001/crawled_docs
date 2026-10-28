---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/
title: Message \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:13:30.768657+00:00
---

# Message  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/

[ Skip to main content ](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/)
  * [Deutsch](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fgemini%2Fdata-agents%2Freference%2Frest%2FShared.Types%2FMessage%2F&prompt=select_account)
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
#  Message Stay organized with collections  Save and categorize content based on your preferences.
  * [JSON representation](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/#SCHEMA_REPRESENTATION)


Message is one unit of communication between client and server. It is associated with a context and optionally a task. Since the server is responsible for the context definition, it must always provide a contextId in its messages. The client can optionally provide the contextId if it knows the context to associate the message to. Similarly for taskId, except the server decides if a task is created and whether to include the taskId.  
| JSON representation  |  
| --- |  
| 
```
{
  "messageId": string,
  "contextId": string,
  "taskId": string,
  "role": enum (Role[](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Role)),
  "content": [
    {
      object (Part[](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Part))
    }
  ],
  "metadata": {
    object
  },
  "extensions": [
    string
  ]
}
```
 |  
| Fields  |  
| --- |  
| `messageId`  |  `string` The unique identifier (e.g. UUID)of the message. This is required and created by the message creator.  |  
| `contextId`  |  `string` The context id of the message. This is optional and if set, the message will be associated with the given context.  |  
| `taskId`  |  `string` The task id of the message. This is optional and if set, the message will be associated with the given task.  |  
| `role`  |  `enum (`Role[](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Role)`)` A role for the message.  |  
| `content[]`  |  `object (`Part[](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Part)`)` protolint:disable REPEATED_FIELD_NAMES_PLURALIZED Content is the container of the message content.  |  
| `metadata`  |  `object (`Struct[](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` protolint:enable REPEATED_FIELD_NAMES_PLURALIZED Any optional metadata to provide along with the message.  |  
| `extensions[]`  |  `string` The URIs of extensions that are present or contributed to this Message.  |  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
