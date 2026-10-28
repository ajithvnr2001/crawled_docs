---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/
title: Best practices: Knowledge documents \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:18:39.783343+00:00
---

# Best practices: Knowledge documents  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/

[ Skip to main content ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/)
  * [Deutsch](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fgemini-enterprise-cx%2Fagent-assist%2Fknowledge-documents%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/ai-and-machine-learning-color.svg) ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Irrelevant content](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/#irrelevant_content)
  * [Format](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/#format)
  * [Document usefulness](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/#document_usefulness)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)


Was this helpful?
Send feedback 
#  Best practices: Knowledge documents Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Irrelevant content](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/#irrelevant_content)
  * [Format](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/#format)
  * [Document usefulness](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents/#document_usefulness)


Knowledge documents are articles (for use with [Article Suggestion](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/article-suggestion)) or FAQ documents (for use with [FAQ Assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/faq)) that make up a [knowledge base](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-base). Agent Assist analyzes an ongoing conversation between a human agent and an end-user and suggests relevant knowledge documents or FAQ answers to the agent. For more information on creating a knowledge base, see the [knowledge base tutorial](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-base). This document highlights best practices that help to optimize the quality of suggestions.
## Irrelevant content
We recommend that you remove irrelevant content from your knowledge documents, particularly at the beginning of documents. Article Suggestion shows the first few sentences of a document to human agents as snippets to help the agents understand what the document is about. If the beginning of a document has irrelevant information, it could mislead the human agents. Common irrelevant content includes the following:
  * A navigation bar
  * Last-modified dates
  * Feedback forms


## Format
Exclude documents with mostly audio, video, or images. Article Suggestion and FAQ Assist process text content only.
If some of your documents are very long (more than 1,000 words), break them down into multiple short documents. This helps document suggestion quality and also makes it easier for agents to find answers in the suggested documents.
## Document usefulness
We also recommend that you include only your most useful and frequently visited documents in the knowledge base. Which documents are most useful depends on who will be seeing suggestions based on that knowledge base. For example, if you intend to have tier-2 technical support agents seeing suggestions, you should make sure to include documents that contain technical information and are often viewed by the agents receiving the suggestions.
We also recommend that you exclude documents that are inactive, out of date, or very rarely visited. Such documents are unlikely to be useful to agents.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
