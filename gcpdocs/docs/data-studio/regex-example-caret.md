---
url: https://docs.cloud.google.com/data-studio/regex-example-caret/
title: Caret (^) \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:59:49.684295+00:00
---

# Caret (^)  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/regex-example-caret/

[ Skip to main content ](https://docs.cloud.google.com/data-studio/regex-example-caret/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/data-studio/regex-example-caret/)
  * [Deutsch](https://docs.cloud.google.com/data-studio/regex-example-caret/?hl=de)
  * [Español](https://docs.cloud.google.com/data-studio/regex-example-caret/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/data-studio/regex-example-caret/?hl=es-419)
  * [Français](https://docs.cloud.google.com/data-studio/regex-example-caret/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/data-studio/regex-example-caret/?hl=id)
  * [Italiano](https://docs.cloud.google.com/data-studio/regex-example-caret/?hl=it)
  * [Português](https://docs.cloud.google.com/data-studio/regex-example-caret/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/data-studio/regex-example-caret/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/data-studio/regex-example-caret/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/data-studio/regex-example-caret/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/data-studio/regex-example-caret/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/data-studio/regex-example-caret/?hl=ja)
  * [한국어](https://docs.cloud.google.com/data-studio/regex-example-caret/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fdata-studio%2Fregex-example-caret%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/data-analytics-color.svg) ](https://docs.cloud.google.com/data-studio)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)


[Start free](https://console.cloud.google.com/freetrial)
Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)


Was this helpful?
Send feedback 
#  Caret (^) Stay organized with collections  Save and categorize content based on your preferences.
Use the caret to match the following adjacent characters at the beginning of a string.
For example, `^St` matches the following:
  * **St** art here
  * **St** and here
  * **St** op here


However, `^St` doesn't match the following:
  * 1 Start here
  * 2 Stand here
  * 3 Stop here


The preceding three lines start with a digit and a space, not with the letters "St".
Use this type of regular expression to create segments, filters, or goal steps that match a URI. For example, if you need to isolate data for a particular directory of pages, you can use expressions such as the following:
  * `^/mens/` (matches www.example.com**/mens/**)
  * `^/womens/` (matches www.example.com**/womens/**)


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
