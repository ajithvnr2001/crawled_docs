---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ResourcesPackaging/
title: ResourcesPackaging \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:55:04.130199+00:00
---

# ResourcesPackaging  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ResourcesPackaging/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ResourcesPackaging

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/ResourcesPackaging.kt+class:com.android.build.api.variant.ResourcesPackaging)

Added in 7.0.0
    
    
    interface [ResourcesPackaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ResourcesPackaging)

* * *

Build-time properties for packaging Java resources inside a `[Component](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component)`.

This is accessed via `[Packaging.resources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Packaging#resources\(\))`

## Summary

### Public properties  
  
---  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[excludes](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ResourcesPackaging#excludes\(\))` The set of excluded patterns.  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[merges](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ResourcesPackaging#merges\(\))` The set of patterns for which matching java resources are merged.  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[pickFirsts](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ResourcesPackaging#pickFirsts\(\))` The set of patterns for which the first occurrence is packaged in the APK.  
  
## Public properties

### excludes

Added in 7.0.0
    
    
    val [excludes](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ResourcesPackaging#excludes\(\)): [SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The set of excluded patterns. Java resources matching any of these patterns do not get packaged in the APK.

Example usage: `variant.packaging.resources.excludes.add("**`/`*.exclude")`

### merges

Added in 7.0.0
    
    
    val [merges](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ResourcesPackaging#merges\(\)): [SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The set of patterns for which matching java resources are merged. For each java resource APK entry path matching one of these patterns, all java resources with that path are concatenated and packaged as a single entry in the APK.

Example usage: `variant.packaging.resources.merges.add("**`/`*.merge")`

### pickFirsts

Added in 7.0.0
    
    
    val [pickFirsts](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ResourcesPackaging#pickFirsts\(\)): [SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The set of patterns for which the first occurrence is packaged in the APK. For each java resource APK entry path matching one of these patterns, only the first java resource found with that path gets packaged in the APK.

Example usage: `variant.packaging.resources.pickFirsts.add("**`/`*.pickFirst")`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
