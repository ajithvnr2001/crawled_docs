---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/
title: Simulator \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:58:40.642886+00:00
---

# Simulator  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/

[ Skip to main content ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/)
  * [Deutsch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fgemini-enterprise-cx%2Fcx-agent-studio%2Fsimulator%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/ai-and-machine-learning-color.svg) ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Options](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/#options)
  * [Injecting data](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/#injecting_data)
  * [Tracing information](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/#tracing_information)
  * [CX Insights integration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/#insights)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)


Was this helpful?
Send feedback 
#  Simulator Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Options](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/#options)
  * [Injecting data](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/#injecting_data)
  * [Tracing information](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/#tracing_information)
  * [CX Insights integration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator/#insights)


While developing your agent application, you can test interactions with your agent using the _Preview agent_ simulator.
The simulator is found in the bottom left of the page. You can type a message to the agent, followed by pressing Enter, and the agent will respond. Alternatively, you can use the microphone button to send audio messages.
## Options
The simulator has multiple options accessible from the panel title bar:
  * **Start new conversation** : Clears any conversation data displayed in the preview window.
  * **Conversation history** : Displays prior conversation data. You must have data logging enabled to see conversation history (available in **Settings - > Logging**).
  * **Hide/Show trace** : Shows or hides debug trace information. This option is set to **Show** by default.
  * **Save as golden** : Use the conversation as an [evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation).


## Injecting data
You can click the plus button in the message input area to inject certain types of data:
  * Upload files
  * Variables


## Tracing information
For each conversational turn with your agent, you can view tracing information which includes:
  * steps performed
  * latency for steps
  * tool execution with input and output
  * error information
  * raw JSON responses


You can click the expansion buttons and links for tracing items to get more details about each tracing item. You can use this information to help understand the steps the agent application performs for each conversational turn and to help debug issues.
![tracing screenshot](https://docs.cloud.google.com/static/gemini-enterprise-cx/cx-agent-studio/images/tracing.png)
## CX Insights integration
When looking at the conversation history, you can click **Go to Insights** above the history to open your conversation history filtered for this agent application in [CX Insights](https://docs.cloud.google.com/contact-center/insights/docs).
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
