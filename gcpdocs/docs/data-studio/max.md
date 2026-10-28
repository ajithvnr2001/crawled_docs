---
url: https://docs.cloud.google.com/data-studio/max/
title: MAX \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:49:13.535823+00:00
---

# MAX  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/max/

[ Skip to main content ](https://docs.cloud.google.com/data-studio/max/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/data-studio/max/)
  * [Deutsch](https://docs.cloud.google.com/data-studio/max/?hl=de)
  * [Español](https://docs.cloud.google.com/data-studio/max/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/data-studio/max/?hl=es-419)
  * [Français](https://docs.cloud.google.com/data-studio/max/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/data-studio/max/?hl=id)
  * [Italiano](https://docs.cloud.google.com/data-studio/max/?hl=it)
  * [Português](https://docs.cloud.google.com/data-studio/max/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/data-studio/max/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/data-studio/max/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/data-studio/max/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/data-studio/max/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/data-studio/max/?hl=ja)
  * [한국어](https://docs.cloud.google.com/data-studio/max/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/data-analytics-color.svg) ](https://docs.cloud.google.com/data-studio)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Sample usage](https://docs.cloud.google.com/data-studio/max/#sample_usage)
  * [Syntax](https://docs.cloud.google.com/data-studio/max/#syntax)
    * [Parameters](https://docs.cloud.google.com/data-studio/max/#parameters)
    * [Notes](https://docs.cloud.google.com/data-studio/max/#notes)
  * [Examples](https://docs.cloud.google.com/data-studio/max/#examples)
  * [Related resources](https://docs.cloud.google.com/data-studio/max/#related_resources)


Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)


Send feedback 
#  MAX Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Sample usage](https://docs.cloud.google.com/data-studio/max/#sample_usage)
  * [Syntax](https://docs.cloud.google.com/data-studio/max/#syntax)
    * [Parameters](https://docs.cloud.google.com/data-studio/max/#parameters)
    * [Notes](https://docs.cloud.google.com/data-studio/max/#notes)
  * [Examples](https://docs.cloud.google.com/data-studio/max/#examples)
  * [Related resources](https://docs.cloud.google.com/data-studio/max/#related_resources)


Returns the maximum value from an expression.
## Sample usage
`MAX(Users per day)`
## Syntax
`MAX( X )`
### Parameters
  * `X` - a numeric, date, or text field or expression.


### Notes
  * `X` cannot be an aggregated field or the result of an aggregation function.


## Examples  
| Example formula  | Input  | Output  |  
| --- | --- | --- |  
|  ` MAX(Users per day) `  | 
  * 95 
  * 100 
  * 92 

 |  100   |  
|  ` MAX(End date) `  | 
  * 2022-02-10 
  * 2021-12-31 
  * 2022-02-09 

 |  2022-02-10   |  
|  ` MAX(Name) `  | 
  * Alex 
  * Kalani 
  * Yuri 

 |  Yuri   |  
## Related resources
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
