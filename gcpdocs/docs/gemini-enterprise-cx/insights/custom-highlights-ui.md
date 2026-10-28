---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/
title: Analyze conversations using Custom Highlights \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:59:29.068098+00:00
---

# Analyze conversations using Custom Highlights  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/

[ Skip to main content ](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/)
  * [Deutsch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/ai-and-machine-learning-color.svg) ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Overview](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/#overview)
    * [Rules to determine a match](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/#rules_to_determine_a_match)
  * [Create a custom highlight using the console](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/#custom_highlight)
  * [Analyze a CX Insights conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/#analyze)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)


Was this helpful?
Send feedback 
#  Analyze conversations using Custom Highlights Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Overview](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/#overview)
    * [Rules to determine a match](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/#rules_to_determine_a_match)
  * [Create a custom highlight using the console](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/#custom_highlight)
  * [Analyze a CX Insights conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/#analyze)


## Overview
Custom Highlights functions in a similar way as the [Smart Highlights](https://docs.cloud.google.com/gemini-enterprise-cx/insights/smart-highlights) feature. A **highlight** contains key words or phrases that CX Insights recognizes as being important to determining the user's intent. If highlights are present, they are labeled in the returned transcript. Smart Highlights automatically detects highlights based on a range of pre-set scenarios, while Custom Highlights lets you specify custom criteria that should be recognized as highlights.
A custom highlight can be made up of one or more **phrase match rule groups**. A phrase match rule group contains one or more **rules**. You can use the following parameters to customize the behavior of your rules.
### Rules to determine a match
You can specify whether a highlight should be detected if only one of the rule groups resolves to `true`, or if all of the rule groups resolve to `true`. Similarly, you can specify that a rule group should resolve to `true` if only one of its rules is met, or if conditions for all rules in the rule group must be met.
## Create a custom highlight using the console
Permissions required for this task
To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 
  * `contactcenterinsights.phraseMatchers.create`


  1. Navigate to the [CX Insights console](https://ccai.cloud.google.com/insights).
  2. If prompted, sign in using your Google Account.
  3. Enter your project ID.
  4. Select **_Conversation Highlights_** from the navigation menu on the left and go to the **_Custom Highlights_** tab.
  5. Click **_Add New_** , then type in the highlight name and the key words to be detected.


The configuration in the console assumes the following:
  * There are at most two phrase match rule groups in the highlight and `ALL_OF` logic is applied at highlight level.
  * One of the phrase match rule groups must contain positive conditions and default to `ANY_OF` logic (represented by **_Keywords to match_**). You can add a second phrase match rule group that only contains negative conditions and defaults to `ALL_OF` logic (represented by **_Keywords to exclude_**).
  * Keywords are case insensitive.


## Analyze a CX Insights conversation
After a custom highlight is created, you can use it to analyze your conversations. See the how-to section to learn [how to analyze a conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-analyze-conversation-ui).
When an analysis has completed, you can view your custom highlights annotations in the **_Annotations_** panel along with other types of annotations in each conversation.
In the **_Custom Highlights_** tab, you can also find a chart and a table that display the number of each highlight present in the analyzed conversations for different time windows.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
