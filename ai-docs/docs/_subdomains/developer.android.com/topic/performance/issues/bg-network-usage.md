---
url: https://developer.android.com/topic/performance/issues/bg-network-usage/
title: Excessive Mobile Network Usage in Background \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:21.852245+00:00
---

# Excessive Mobile Network Usage in Background  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/issues/bg-network-usage/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Excessive Mobile Network Usage in Background Stay organized with collections  Save and categorize content based on your preferences. 

When an app connects to the mobile network in the background, the app wakes up the CPU and turns on the radio. Doing so repeatedly can run down a device's battery. An app is considered to be running in the background if it is in the `PROCESS_STATE_BACKGROUND` or `PROCESS_STATE_CACHED` state.

This page explains how to determine why your app is excessively using the mobile network while running in the background, and what to do about it.

**Note:** For information on how Android Play Vitals tracks and reports this issue, see [Excessive Mobile Network Usage in Background in Android vitals](https://developer.android.com/google/play/vitals/bg-network-usage).

## Investigate mobile-network-usage behavior

**Warning:** Battery Historian is no longer actively maintained; if possible, consider using [system tracing](https://developer.android.com/topic/performance/tracing), the [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview) power metric, or the [Power Profiler](https://developer.android.com/studio/profile/power-profiler) to get insights into battery performance.

Tools such as Battery Historian can help you gain more insight into your app's mobile-network usage. Battery Historian provides a visualization of mobile-radio use on a per-app basis, which can help you gain a clearer picture of what's happening with your app. For more information about Battery Historian, see [Analyzing Power Use with Battery Historian](https://developer.android.com/topic/performance/power/battery-historian#asd). In investigating your app's mobile-network-usage behavior, you should take particular note of the _Mobile network use_ line.

For information about the mechanics of using Battery Historian, see [Batterystats and Battery Historian Walkthrough](https://developer.android.com/topic/performance/power/setup-battery-historian).

## Reduce mobile network usage

You can move your app’s mobile-network usage to the foreground, alerting the user to the fact that a download is in progress, and providing them with controls to pause or stop the download. To do so, call [`DownloadManager`](https://developer.android.com/reference/android/app/DownloadManager), and set [`setNotificationVisibility(int)`](https://developer.android.com/reference/android/app/DownloadManager.Request#setNotificationVisibility\(int\)) as appropriate.

## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [Excessive Wi-Fi Scanning in the Background](https://developer.android.com/topic/performance/issues/bg-wifi)



[ Previous arrow_back  Excessive Background Wi-Fi Scans  ](https://developer.android.com/topic/performance/issues/bg-wifi)

[ Next Excessive Battery Usage  arrow_forward  ](https://developer.android.com/topic/performance/issues/excessive-battery-usage)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
