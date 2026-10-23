---
url: https://developer.android.com/topic/performance/benchmarking/benchmarking-overview/
title: Benchmark your app \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:48.944655+00:00
---

# Benchmark your app  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/benchmarking/benchmarking-overview/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Benchmark your app Stay organized with collections  Save and categorize content based on your preferences. 

Benchmarking is a way to inspect and monitor the performance of your app. You can regularly run benchmarks to analyze and debug performance problems and help ensure that you don't introduce regressions in recent changes.

Android offers the Macrobenchmark library for analyzing and testing different kinds of situations in your app.

## Macrobenchmark

The [Macrobenchmark](https://developer.android.com/studio/profile/macrobenchmark) library measures larger end-user interactions, such as startup, interacting with the UI, and animations. The library provides direct control over the performance environment you're testing. It lets you control compiling and lets you start and stop your app to directly measure actual app startup or scrolling.

The Macrobenchmark library injects events and monitors results externally from a test app that is built with your tests. Therefore, when writing the benchmarks, you don't call your app code directly and instead navigate within your app as a user.

## Additional resources

### Views content

  * [Benchmark your app (Views)](https://developer.android.com/topic/performance/views/benchmarking/benchmarking-overview-views)



## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [Create Baseline Profiles {:#creating-profile-rules}](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)
  * [JankStats Library](https://developer.android.com/topic/performance/jankstats)
  * [Overview of measuring app performance](https://developer.android.com/topic/performance/measuring-performance)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
