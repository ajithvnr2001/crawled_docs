---
url: https://developer.android.com/develop/ui/views/layout/improving-layouts/
title: Improve layout performance \u00a0|\u00a0 Views \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:11.175501+00:00
---

# Improve layout performance  |  Views  |  Android Developers

> Source: https://developer.android.com/develop/ui/views/layout/improving-layouts/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ UI ](https://developer.android.com/develop/ui)
  * [ Views ](https://developer.android.com/develop/ui/views/layout/declaring-layout)



#  Improve layout performance Stay organized with collections  Save and categorize content based on your preferences. 

Try the Compose way 

Jetpack Compose is the recommended UI toolkit for Android. Learn how to work with layouts in Compose. 

[ Performance in Compose → ](https://developer.android.com/jetpack/compose/performance)

![](https://developer.android.com/static/images/android-compose-ui-logo.png)

Layouts are a key part of Android applications that directly affect the user experience. If implemented poorly, your layout can make your app memory-intensive with slow UIs. The Android SDK includes tools to help identify problems in your layout performance. With this documentation, you can implement smooth scrolling interfaces with a minimal memory footprint.

## Lessons

**[Optimize layout hierarchies](https://developer.android.com/develop/ui/views/layout/improving-layouts/optimizing-layouts)**
    In the same way that a complex web page can slow down load time, a complex layout hierarchy can also cause performance problems. This documentation shows how you can use SDK tools to inspect your layout and discover performance bottlenecks.
**[Reuse layouts with<include>](https://developer.android.com/develop/ui/views/layout/improving-layouts/reusing-layouts)**
    If your application UI repeats certain layout constructs in multiple places, this documentation shows you how to create efficient, reusable layout constructs and include them in the appropriate UI layouts.
**[Load views on demand](https://developer.android.com/develop/ui/views/layout/improving-layouts/loading-ondemand)**
    Beyond including one layout component within another layout, you might want to make the included layout visible only when it's needed after the activity is running. This documentation shows how you can improve your layout's initialization performance by loading portions of your layout on demand.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-28 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-28 UTC."],[],[]] 
