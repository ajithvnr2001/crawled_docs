---
url: https://developer.android.com/topic/performance/rendering/
title: Rendering \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:11.048234+00:00
---

# Rendering  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/rendering/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Rendering Stay organized with collections  Save and categorize content based on your preferences. 

A key aspect of your app that influences your users' perception of quality is the smoothness with which it renders images and text to the screen. It's important to avoid jank and sluggish responsiveness when your app is drawing to the screen.

This section shows several ways to optimize your app's rendering performance: reducing overdraw, optimizing view hierarchies, and taking advantage of the Profile GPU tool. See [Jetpack Compose performance](https://developer.android.com/jetpack/compose/performance) to learn about rendering in Jetpack Compose.

## Render actions

**[Reduce overdraw](https://developer.android.com/topic/performance/rendering/overdraw)**
     Minimize the number of times your app redraws the same pixel in a single frame. 
**[Performance and view hierarchies](https://developer.android.com/topic/performance/rendering/optimizing-view-hierarchies)**
     Make sure your layout and measurement are executing efficiently, and avoid double taxation. 
**[Analyze with Profile GPU Rendering](https://developer.android.com/topic/performance/rendering/profile-gpu)**
     Take advantage of this on-device tool to identify bottlenecks that might slow your app's rendering. 

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-19 UTC."],[],[]] 
