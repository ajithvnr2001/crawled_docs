---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/
title: Google Search tool \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:58:48.175519+00:00
---

# Google Search tool  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/

[ Skip to main content ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/)
  * [Deutsch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/ai-and-machine-learning-color.svg) ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Configuration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/#configuration)
  * [Settings precedence](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/#google_search_domain_precedence)
  * [Runtime context URLs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/#runtime_context_urls)
  * [Citations and inline citations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/#citations_and_inline_citations)
    * [Attribution requirements](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/#attribution_requirements)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)


Was this helpful?
Send feedback 
#  Google Search tool Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Configuration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/#configuration)
  * [Settings precedence](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/#google_search_domain_precedence)
  * [Runtime context URLs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/#runtime_context_urls)
  * [Citations and inline citations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/#citations_and_inline_citations)
    * [Attribution requirements](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search/#attribution_requirements)


The Google Search tool enables your agent to base its responses on up-to-date information from the web, effectively grounding the conversation in real-world data. This tool is ideal for scenarios requiring world knowledge, current events, or a broad range of topics.
## Configuration
Configure the following settings when creating the tool:
  * **Name** : The display name for the tool instance (for example: `search_web`).
  * **Description** : A brief description of the tool's purpose. Reasoning agents use this description to decide when to invoke the tool.
  * **Excluded domains** : A list of domains to exclude from search results (max 2000). For example: "www.example.com" or "example.com"
  * **Preferred domains** : A list of domains to restrict search results to (max 20). For example: "www.example.com" or "example.com"
  * **URLs for context** : Specific URLs to fetch for grounding context (max 20). The model uses content from these pages directly. For example: "example.com/page/path"
  * **Modalities** : Customize how the agent processes and summarizes search results for different modalities: 
    * **Text prompt** : Instructions for processing search results in text conversations.
    * **Voice prompt** : Instructions for processing search results in voice conversations (for example, keeping answers concise and natural for speech, and avoiding reciting raw URLs).


## Settings precedence
Domain and URL settings apply in the following order:
  1. **Excluded domains** : Highest precedence. Domains are excluded even if listed in **URLs for context** or **Preferred domains**.
  2. **URLs for context** : Content is fetched unless the domain is excluded.
  3. **Preferred domains** : Lowest precedence.


## Runtime context URLs
In addition to the URLs for context provided in tool configuration, you can instruct your agent to dynamically inject URLs at runtime.
For example, you can add the following in your agent instructions: `none If the user query is about x, look into these urls url1, url2, url3 using the 'Product Information Search' tool.`
## Citations and inline citations
When an agent grounds its response using the Google Search tool, the runtime response includes citation metadata in `SessionOutput.citations` to trace generated statements back to web sources.
Citation metadata contains two primary components:
  * **Cited chunks (`cited_chunks`)**: The list of source documents used for grounding, including the source `uri`, page `title`, snippet `text`, and the `requires_attribution` indicator.
  * **Inline citations (`inline_citations`)**: Precise byte-range offsets (`start_index` and `end_index`) in the response text that map directly to `cited_chunk_indices`. You can use inline citations in your client application to render interactive superscript badges, footnotes, or inline links anchored to specific claims in the agent's response.


### Attribution requirements
Citations returned from web grounding may require attribution to the original source:
  * Check the `requires_attribution` field on each `CitedChunk`.
  * If `requires_attribution` is `true`, your client application must display source attribution and link to the source URI for end users.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
