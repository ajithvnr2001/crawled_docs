---
url: https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/
title: Use pre-release features in Gemini Code Assist for VS Code \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T15:17:58.624044+00:00
---

# Use pre-release features in Gemini Code Assist for VS Code  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/

[ Skip to main content ](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/)
  * [Deutsch](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/?hl=de)
  * [Español](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/?hl=it)
  * [Português](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/gemini-color.svg) ](https://docs.cloud.google.com/gemini/docs)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/#before-you-begin)
  * [Use the insiders build](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/#use-the-insiders-build)
  * [Use the standard release channel](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/#use-standard-release-channel)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)


Send feedback 
#  Use pre-release features in Gemini Code Assist for VS Code Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/#before-you-begin)
  * [Use the insiders build](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/#use-the-insiders-build)
  * [Use the standard release channel](https://docs.cloud.google.com/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist/#use-standard-release-channel)


This page describes how to use pre-release features of Gemini Code Assist for VS Code on the insiders release channel.
Pre-release builds can include bug fixes and features still in development that might be removed in a future release.
## Before you begin
[Set up Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/set-up-gemini).
## Use the insiders build
To configure the update channel, follow these steps:
  1. In your IDE, open the **Command palette** (`Cmd` + `Shift` + `P`) and then select **Open User Settings JSON**.
  2. Add the following line to your user settings JSON: `"geminicodeassist.updateChannel": "Insiders",`
  3. Save your user settings.


You are prompted to reload your window to use the latest insiders build.
## Use the standard release channel
To use the standard release channel instead of the insiders build, follow these steps:
  1. In your IDE, open the **Command palette** (`Cmd` + `Shift` + `P`) and then select **Open User Settings JSON**.
  2. Comment out or remove the following line of your user settings JSON: `"geminicodeassist.updateChannel": "Insiders",`
  3. Save your user settings.


You are prompted to reload your window to use the standard release channel.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
