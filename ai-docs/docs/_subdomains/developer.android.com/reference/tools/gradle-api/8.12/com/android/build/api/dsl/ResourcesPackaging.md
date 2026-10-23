---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ResourcesPackaging/
title: ResourcesPackaging \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:02:58.991129+00:00
---

# ResourcesPackaging  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ResourcesPackaging/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ResourcesPackaging

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ResourcesPackaging.kt+class:com.android.build.api.dsl.ResourcesPackaging)

Added in 8.0.2
    
    
    interface [ResourcesPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ResourcesPackaging)

* * *

Packaging options for java resource files in the Android DSL
    
    
    android {  
        packaging {  
            resources {  
                excludes += "/..."  
            }  
        }  
    }

## Summary

### Public properties  
  
---  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[excludes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ResourcesPackaging#excludes\(\))` The set of excluded patterns.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[merges](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ResourcesPackaging#merges\(\))` The set of patterns for which matching java resources are merged.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[pickFirsts](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ResourcesPackaging#pickFirsts\(\))` The set of patterns for which the first occurrence is packaged in the APK.  
  
## Public properties

### excludes

Added in 8.0.2
    
    
    val [excludes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ResourcesPackaging#excludes\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The set of excluded patterns. Java resources matching any of these patterns do not get packaged in the APK.

Example: `android.packagingOptions.resources.excludes += "**`/`*.exclude"`

### merges

Added in 8.0.2
    
    
    val [merges](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ResourcesPackaging#merges\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The set of patterns for which matching java resources are merged. For each java resource APK entry path matching one of these patterns, all java resources with that path are concatenated and packaged as a single entry in the APK.

Example: `android.packagingOptions.resources.merges += "**`/`*.merge"`

### pickFirsts

Added in 8.0.2
    
    
    val [pickFirsts](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ResourcesPackaging#pickFirsts\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The set of patterns for which the first occurrence is packaged in the APK. For each java resource APK entry path matching one of these patterns, only the first java resource found with that path gets packaged in the APK.

Example: `android.packagingOptions.resources.pickFirsts += "**`/`*.pickFirst"`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
