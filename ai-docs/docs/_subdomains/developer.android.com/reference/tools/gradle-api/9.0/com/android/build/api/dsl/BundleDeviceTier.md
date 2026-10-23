---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BundleDeviceTier/
title: BundleDeviceTier \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:16:48.961599+00:00
---

# BundleDeviceTier  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BundleDeviceTier/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BundleDeviceTier

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/BundleDeviceTier.kt+class:com.android.build.api.dsl.BundleDeviceTier)

Added in 4.2.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [BundleDeviceTier](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BundleDeviceTier)

* * *

DSL object for configuring the App Bundle Device Tier options

This is accessed via `[Bundle.deviceTier](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Bundle#deviceTier\(kotlin.Function1\))`

## Summary

### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[defaultTier](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BundleDeviceTier#defaultTier\(\))` Specifies the default device tier value for the bundle.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[enableSplit](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BundleDeviceTier#enableSplit\(\))`  
  
## Public properties

### defaultTier

Added in 4.2.0
    
    
    var [defaultTier](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BundleDeviceTier#defaultTier\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Specifies the default device tier value for the bundle. Used for local-testing and generating universal APKs.

### enableSplit

Added in 4.2.0
    
    
    var [enableSplit](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BundleDeviceTier#enableSplit\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
