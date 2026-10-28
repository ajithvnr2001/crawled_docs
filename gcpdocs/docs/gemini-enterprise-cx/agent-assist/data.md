---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/
title: Upload data \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:18:10.094567+00:00
---

# Upload data  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/

[ Skip to main content ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/)
  * [Deutsch](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fgemini-enterprise-cx%2Fagent-assist%2Fdata%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/ai-and-machine-learning-color.svg) ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Overview](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/#overview)
  * [Data types](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/#data_types)
  * [What's next](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)


Was this helpful?
Send feedback 
#  Upload data Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Overview](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/#overview)
  * [Data types](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/#data_types)
  * [What's next](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data/#whats_next)


## Overview
In order to make suggestions, Agent Assist relies on data in the form of either documents or conversation transcripts. You must upload your data before you can use Agent Assist. The linked tutorials at the bottom of this page walk you through the steps required to upload your data using the [Agent Assist console](https://agentassist.cloud.google.com). You can use the console to configure Agent Assist features and test out how they function.
## Data types
Agent Assist uses two types of data to make suggestions to human agents: **Conversation datasets** , which are collections of conversation transcripts, and **knowledge bases** , which are collections of _knowledge documents_ (articles or FAQ documents). Agent Assist features analyze a conversation in real time and make suggestions to human agents based on either conversation datasets or knowledge bases.
[Smart Reply](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-reply) and [Summarization](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-console) surface suggestions trained on conversation datasets. Smart Reply suggests text responses to agents as they converse with an end-user, and Summarization suggests conversation summaries after an exchange with an end-user has completed. Each model is custom by definition because each conversation dataset is made up of your own conversation transcript data.
The [FAQ Assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/faq) and [Article Suggestion](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/article-suggestion) features draw on knowledge bases to make recommendations instead of conversation datsets. Article Suggestion suggests _knowledge documents_ (such as articles) to agents during a conversation. FAQ Assist makes suggestions based on FAQ pairs (an FAQ question and its associated answer) rather than entire articles. You do not need to train a custom model in order to use these features: Agent Assist uses default baseline suggestion models to make suggestions from your knowledge base. If you want to upload your own conversation data to train a custom suggestion model for Article Suggestion, please contact your Google representative. Custom suggestion models are not available for FAQ Assist.
## What's next
Create a [conversation dataset](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-dataset) or a [knowledge base](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-base).
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
