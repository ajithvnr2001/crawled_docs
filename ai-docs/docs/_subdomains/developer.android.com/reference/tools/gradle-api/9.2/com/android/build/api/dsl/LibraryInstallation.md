---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryInstallation/
title: LibraryInstallation \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:48:00.580408+00:00
---

# LibraryInstallation  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryInstallation/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# LibraryInstallation

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/LibraryInstallation.kt+class:com.android.build.api.dsl.LibraryInstallation)

Added in 8.3.1
    
    
    interface [LibraryInstallation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryInstallation) : [Installation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Installation)

* * *

DSL object for configuring installation options for Library plugins.

This is accessed via `[LibraryExtension.installation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryExtension#installation\(kotlin.Function1\))`

## Summary

### Inherited properties  
  
---  
From [com.android.build.api.dsl.Installation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Installation) | `[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[installOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Installation#installOptions\(\))` The list of FULL_APK installation options.  
---|---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[timeOutInMs](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Installation#timeOutInMs\(\))` The time out used for all adb operations.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
