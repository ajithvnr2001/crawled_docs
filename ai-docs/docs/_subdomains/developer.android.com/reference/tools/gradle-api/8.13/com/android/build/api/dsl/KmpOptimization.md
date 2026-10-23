---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KmpOptimization/
title: KmpOptimization \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:32:56.014524+00:00
---

# KmpOptimization  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KmpOptimization/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# KmpOptimization

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/KmpOptimization.kt+class:com.android.build.api.dsl.KmpOptimization)

Added in 8.2.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [KmpOptimization](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KmpOptimization)

* * *

DSL object for configurations aimed for optimizing build process(e.g. speed, correctness)

## Summary

### Public properties  
  
---  
`[ConsumerKeepRules](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ConsumerKeepRules)` |  `[consumerKeepRules](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KmpOptimization#consumerKeepRules\(\))` The collection of keep rule files for consumers of the library to use.  
`[LibraryKeepRules](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LibraryKeepRules)` |  `[keepRules](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KmpOptimization#keepRules\(\))` The collection of keep rule files that the plugin should use when optimizing the AAR  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[minify](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KmpOptimization#minify\(\))` Specifies whether to enable code shrinking for this build type.  
`[ConfigurableFiles](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ConfigurableFiles)` |  `[testKeepRules](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KmpOptimization#testKeepRules\(\))` The collection of keep rule files to use for the test APK.  
  
## Public properties

### consumerKeepRules

Added in 8.2.0
    
    
    val [consumerKeepRules](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KmpOptimization#consumerKeepRules\(\)): [ConsumerKeepRules](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ConsumerKeepRules)

The collection of keep rule files for consumers of the library to use.

### keepRules

Added in 8.2.0
    
    
    val [keepRules](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KmpOptimization#keepRules\(\)): [LibraryKeepRules](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LibraryKeepRules)

The collection of keep rule files that the plugin should use when optimizing the AAR

### minify

Added in 8.2.0
    
    
    var [minify](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KmpOptimization#minify\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Specifies whether to enable code shrinking for this build type.

By default, when you enable code shrinking by setting this property to `true`, the Android plugin uses ProGuard.

To learn more, read [Shrink Your Code and Resources](https://developer.android.com/studio/build/shrink-code.html).

### testKeepRules

Added in 8.2.0
    
    
    val [testKeepRules](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KmpOptimization#testKeepRules\(\)): [ConfigurableFiles](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ConfigurableFiles)

The collection of keep rule files to use for the test APK.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
