---
url: https://developer.android.com/studio/profile/chart-glossary/flame-chart/
title: Flame chart \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:45:09.168070+00:00
---

# Flame chart  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/studio/profile/chart-glossary/flame-chart/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ IDE guides ](https://developer.android.com/studio/intro)



#  Flame chart Stay organized with collections  Save and categorize content based on your preferences. 

The **Flame Chart** tab provides an inverted call chart that aggregates identical call stacks. That is, identical methods or functions that share the same sequence of callers are collected and represented as one longer bar in a flame chart (rather than displaying them as multiple shorter bars, as shown in a call chart). This makes it easier to see which methods or functions consume the most time. However, this also means that the horizontal axis doesn't represent a timeline; instead, it indicates the relative amount of time each method or function takes to execute.

To help illustrate this concept, consider the call chart in Figure 1. Note that method D makes multiple calls to B (B1, B2, and B3), and some of those calls to B make a call to C (C1 and C3).

![](https://developer.android.com/static/studio/images/profile/call_chart_2-2X.png)

**Figure 1.** A call chart with multiple method calls that share a common sequence of callers.

Because B1, B2, and B3 share the same sequence of callers (A → D → B) they are aggregated, as shown in Figure 2. Similarly, C1 and C3 are aggregated because they share the same sequence of callers (A → D → B → C); note that C2 is not included because it has a different sequence of callers (A → D → C).

![](https://developer.android.com/static/studio/images/profile/flame_chart_aggregation-2X.png)

**Figure 2.** Aggregating identical methods that share the same call stack.

The aggregated calls are used to create the flame chart, as shown in Figure 3. Note that, for any given call in a flame chart, the callees that consume the most CPU time appear first.

![](https://developer.android.com/static/studio/images/profile/flame_chart-2X.png)

**Figure 3.** A flame chart representation of the call chart shown in figure 5.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-06 UTC."],[],[]] 
