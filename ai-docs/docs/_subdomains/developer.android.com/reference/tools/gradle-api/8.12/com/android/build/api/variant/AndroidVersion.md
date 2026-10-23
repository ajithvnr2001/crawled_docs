---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AndroidVersion/
title: AndroidVersion \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:06:09.084669+00:00
---

# AndroidVersion  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AndroidVersion/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AndroidVersion

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/AndroidVersion.kt+class:com.android.build.api.variant.AndroidVersion)

Added in 4.2.0
    
    
    interface [AndroidVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AndroidVersion)

* * *

A version of the Android platform.

This includes support for preview versions that don't have a final API level, but instead use a `[codename](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AndroidVersion#codename\(\))`.

## Summary

### Public properties  
  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[apiLevel](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AndroidVersion#apiLevel\(\))` SDK version codes mirroring ones found in Build#VERSION_CODES on Android.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[codename](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AndroidVersion#codename\(\))` Preview versions of the platform are identified by a code name.  
  
## Public properties

### apiLevel

Added in 4.2.0
    
    
    val [apiLevel](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AndroidVersion#apiLevel\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

SDK version codes mirroring ones found in Build#VERSION_CODES on Android.

### codename

Added in 4.2.0
    
    
    val [codename](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AndroidVersion#codename\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Preview versions of the platform are identified by a code name. Their API level is usually set to the value of the previous platform.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
