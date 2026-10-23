---
url: https://developer.android.com/topic/performance/tracing/profiling-manager/overview/
title: Overview \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:42.079105+00:00
---

# Overview  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/tracing/profiling-manager/overview/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The [`ProfilingManager`](https://developer.android.com/reference/android/os/ProfilingManager) Android API lets you collect real user performance profiles, such as [system traces](https://developer.android.com/topic/performance/tracing), programmatically. The `ProfilingManager` API supports two types of trace collections: traces that you explicitly start and event-based traces.

This section focuses on traces that you explicitly start and covers the following topics:

  * How to collect traces with `ProfilingManager`.
  * How to retrieve those traces.
  * How to visualize traces in Perfetto UI.
  * Important details about how `ProfilingManager` works.

**Key Point:** This guide is for developers who want to set up a way to collect end-user performance profiles.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-19 UTC."],[],[]] 
