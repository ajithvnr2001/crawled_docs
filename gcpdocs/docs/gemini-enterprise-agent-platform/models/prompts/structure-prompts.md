---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/
title: Structure prompts \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:54:48.169358+00:00
---

# Structure prompts  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/

[ Skip to main content ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/)
  * [Deutsch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fgemini-enterprise-agent-platform%2Fmodels%2Fprompts%2Fstructure-prompts%2F&prompt=select_account)
[ ![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/192px.svg) ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Use prefixes to structure simple prompts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/#use-prefixes-to-structure-simple-prompts)
  * [Use XML and other delimiters to structure complex prompts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/#use-xml-and-other-delimiters-to-structure-complex-prompts)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)


Was this helpful?
Send feedback 
#  Structure prompts Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Use prefixes to structure simple prompts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/#use-prefixes-to-structure-simple-prompts)
  * [Use XML and other delimiters to structure complex prompts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/structure-prompts/#use-xml-and-other-delimiters-to-structure-complex-prompts)


How you structure a prompt can affect the model's ability to parse the information in the prompt. It also helps the model correctly interpret how to use the given information. To give structure to a prompt, you can use prefixes or XML tags to delimit different parts or components of a prompt.
## Use prefixes to structure simple prompts
A prefix is a word or phrase followed by a colon to label the information in a prompt. In the following example, "TASK:, "CLASSES:," and "OBJECTS:" are the prefixes.  
|  **Prompt:** 
```
TASK:
Classify the OBJECTS.

CLASSES:
- Large
- Small
OBJECTS:
- Rhino
- Mouse
- Snail
- Elephant
  
```
**Response:** 
```
- Rhino: Large
- Mouse: Small
- Snail: Small
- Elephant: Large
  
```
(gemini-pro)  |  
| --- |  
## Use XML and other delimiters to structure complex prompts
For complex prompts, use XML and other delimiters to separate components of a prompt. You can use `BEGIN` and `END` or `{}` section delimiters for complex and lengthy prompt components to clearly distinguish them from the actual instructions.

```
You are a chatbot agent answering  customer's questions in a chat.
Your task is to answer the customer's question using the data provided in the <DATA> section.
  - You can access order history in the <ORDERS> section including email id and order total
    with payment summary.
  - Refer to <ORDERLINES> for item level details within each order in <ORDERS>.

Today is 2024-01-29

<DATA>
<ORDERS>
{OrderId|CustomerEmail|CreatedTimestamp|IsCancelled|OrderTotal|PaymentSummary
CC10182|222larabrown@gmail.com|2024-01-19|true|0.0|Not available
CC10183|baklavainthebalkans@gmail.com|2024-01-19|true|0.0|Not available}
{...}
...
</ORDERS>

<ORDERLINES>
OrderId|OrderLineId|CreatedTimestamp|ItemDescription|Quantity|FulfillmentStatus|ExpectedDeliveryDate
|ActualDeliveryDate|ActualShipDate|ExpectedShipDate|TrackingInformation|ShipToAddress|CarrierCode|De
liveryMethod|UnitPrice|OrderLineSubTotal|LineShippingCharge|TotalTaxes|Payments CC10182|1||Shorts|0.
0|unshipped|2024-01-31|2024-02-01|2024-01-30|2024-01-29||||ShipToAddress|115.99|0.0|0.0|0.0|
...
</ORDERLINES>
</DATA>

<INSTRUCTIONS>
- If there is no data that can help answer the question, respond with "I do not have this
  information. Please contact customer service".
- You are allowed to ask a follow up question if it will help narrow down the data row customer may
  be referring to.
- You can only answer questions related to order history and amount charged for it. Include OrderId
  in the response, when applicable.
- For everything else, please redirect to the customer service agent. 
- Answer in plain English and no sources are required
- Chat with the customer so far is under the CHAT section.
</INSTRUCTIONS>

QUESTION: How much did I pay for my last order?
ANSWER:

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
