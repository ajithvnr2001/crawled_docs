---
url: https://developer.android.com/topic/performance/startupprofiles/overview/
title: Overview of Startup Profiles \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:04.287072+00:00
---

# Overview of Startup Profiles  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/startupprofiles/overview/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Overview of Startup Profiles Stay organized with collections  Save and categorize content based on your preferences. 

Startup Profiles are similar to Baseline Profiles, but they are used at compile time to optimize DEX layout for faster startup times, rather than for on-device optimization. To learn more about how startup profiles differ from Baseline Profiles, see [Compare Baseline Profiles and Startup Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview#compare-baseline-startup). For more on DEX layout optimization, see [DEX layout optimizations and startup profiles](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations).

Startup Profiles impact your app's APK size, and the performance impact they provide might be large or small depending on how your app is structured. We recommend running an A/B test to assess the effect of Startup Profiles on your app.

We recommend using both Baseline Profiles and Startup Profiles to fully optimize app startup.

![](https://developer.android.com/static/topic/performance/images/dex-layout-optimizations.png)**Figure 1.** Code locality improvement from DEX layout optimization.

[ Next Create Startup Profiles  arrow_forward  ](https://developer.android.com/topic/performance/startupprofiles/dex-layout-optimizations)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-19 UTC."],[],[]] 
