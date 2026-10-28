---
url: https://docs.cloud.google.com/fault-injection-testing/monitor-experiment/
title: Monitor experiment progress \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:14:51.873318+00:00
---

# Monitor experiment progress  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/monitor-experiment/

TODO(carmelaq): Optionally refine the following meta description to summarize your product. [ Skip to main content ](https://docs.cloud.google.com/fault-injection-testing/monitor-experiment/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/fault-injection-testing/monitor-experiment/)
  * [Deutsch](https://docs.cloud.google.com/fault-injection-testing/monitor-experiment/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/fault-injection-testing/monitor-experiment/?hl=es-419)
  * [Français](https://docs.cloud.google.com/fault-injection-testing/monitor-experiment/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/fault-injection-testing/monitor-experiment/?hl=id)
  * [Italiano](https://docs.cloud.google.com/fault-injection-testing/monitor-experiment/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/fault-injection-testing/monitor-experiment/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/fault-injection-testing/monitor-experiment/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/fault-injection-testing/monitor-experiment/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/fault-injection-testing/monitor-experiment/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/fault-injection-testing/monitor-experiment/?hl=ja)
  * [한국어](https://docs.cloud.google.com/fault-injection-testing/monitor-experiment/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Ffault-injection-testing%2Fmonitor-experiment%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/observability-color.svg) ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)


[Start free](https://console.cloud.google.com/freetrial)
To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Guides ](https://docs.cloud.google.com/fault-injection-testing/overview)


Was this helpful?
Send feedback 
#  Monitor experiment progress Stay organized with collections  Save and categorize content based on your preferences.
This page explains how to see the current status of an experiment.
Before proceeding, you must have the following:
  * Viewer permissions for the resources affected by the experiment.
  * The `roles/faulttesting.operator` role.


To monitor progress for an experiment:
  1. Go to the Fault Injection Testing **Overview** page.
  2. Select **Experiments** at the left-hand navigation.


The experiment can be in one of the following states:
  * **Preparing**. The dry run is in progress and the experiment is being prepared.
  * **Prepared**. The dry run is complete, and you can start the injection on request.
  * **Injecting**. Fault injection is in progress.
  * **Injected**. Fault injection has been completed on the target resources, and the experiment keeps running for the set duration.
  * **Reverting**. Reverting the faults from the target resources.
  * **Failed**. The fault injection was not successful.
  * **Completed**. The experiment is concluded, which can mean one of the following: 
    * The experiment completed all the expected steps.
    * The experiment was canceled prematurely.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
