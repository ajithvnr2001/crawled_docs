---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleAiModelVersion/
title: BundleAiModelVersion \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:31:02.883396+00:00
---

# BundleAiModelVersion  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleAiModelVersion/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BundleAiModelVersion

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/BundleAiModelVersion.kt+class:com.android.build.api.dsl.BundleAiModelVersion)

Added in 8.7.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [BundleAiModelVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleAiModelVersion)

* * *

DSL object for configuring the App Bundle AI model version targeting

This is accessed via `[Bundle.aiModelVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#aiModelVersion\(kotlin.Function1\))`

## Summary

### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[defaultVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleAiModelVersion#defaultVersion\(\))` Specifies the default AI model version value for the bundle.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[enableSplit](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleAiModelVersion#enableSplit\(\))`  
  
## Public properties

### defaultVersion

Added in 8.7.0
    
    
    var [defaultVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleAiModelVersion#defaultVersion\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Specifies the default AI model version value for the bundle. Used for filtering splits for standalone, system and universal APKs.

### enableSplit

Added in 8.7.0
    
    
    var [enableSplit](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleAiModelVersion#enableSplit\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
