---
url: https://docs.cloud.google.com/data-studio/substr/
title: SUBSTR \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:11:13.795695+00:00
---

# SUBSTR  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/substr/

[ Skip to main content ](https://docs.cloud.google.com/data-studio/substr/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/data-studio/substr/)
  * [Deutsch](https://docs.cloud.google.com/data-studio/substr/?hl=de)
  * [Español](https://docs.cloud.google.com/data-studio/substr/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/data-studio/substr/?hl=es-419)
  * [Français](https://docs.cloud.google.com/data-studio/substr/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/data-studio/substr/?hl=id)
  * [Italiano](https://docs.cloud.google.com/data-studio/substr/?hl=it)
  * [Português](https://docs.cloud.google.com/data-studio/substr/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/data-studio/substr/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/data-studio/substr/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/data-studio/substr/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/data-studio/substr/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/data-studio/substr/?hl=ja)
  * [한국어](https://docs.cloud.google.com/data-studio/substr/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/data-analytics-color.svg) ](https://docs.cloud.google.com/data-studio)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Sample usage](https://docs.cloud.google.com/data-studio/substr/#sample_usage)
  * [Syntax](https://docs.cloud.google.com/data-studio/substr/#syntax)
    * [Parameters](https://docs.cloud.google.com/data-studio/substr/#parameters)
    * [Notes](https://docs.cloud.google.com/data-studio/substr/#notes)
  * [Examples](https://docs.cloud.google.com/data-studio/substr/#examples)
  * [Related resources](https://docs.cloud.google.com/data-studio/substr/#related_resources)


Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)


Was this helpful?
Send feedback 
#  SUBSTR Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Sample usage](https://docs.cloud.google.com/data-studio/substr/#sample_usage)
  * [Syntax](https://docs.cloud.google.com/data-studio/substr/#syntax)
    * [Parameters](https://docs.cloud.google.com/data-studio/substr/#parameters)
    * [Notes](https://docs.cloud.google.com/data-studio/substr/#notes)
  * [Examples](https://docs.cloud.google.com/data-studio/substr/#examples)
  * [Related resources](https://docs.cloud.google.com/data-studio/substr/#related_resources)


Returns a specific sequence of characters from the text.
## Sample usage
`SUBSTR(Campaign, 1, 6)`
## Syntax
`SUBSTR(X, start_index, length)`
### Parameters
  * `X` - A field or expression of any type.
  * `start_index` - The position from the start of the string from which to begin extracting.
  * `length` - The number of characters to extract.


### Notes
  * The first character of a field is at index 1.
  * To begin extracting from the end of the string, use a negative index. The last character of a string is at index -1, the second to the last is at -2, etc.


## Examples  
| Example formula  | Input  | Output  |  
| --- | --- | --- |  
| `SUBSTR(Campaign, 1, 6)`  | Summer Sale  | Summer  |  
| `SUBSTR(Campaign, -4, 4)`  | Summer Sale  | Sale  |  
## Related resources
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
