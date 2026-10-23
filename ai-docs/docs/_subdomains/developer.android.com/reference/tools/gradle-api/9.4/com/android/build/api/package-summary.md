---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/package-summary/
title: com.android.build.api \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:38.514179+00:00
---

# com.android.build.api  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/package-summary/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# com.android.build.api

## Classes

`[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/AndroidPluginVersion)` |  Represents a version of the Android Gradle Plugin  
---|---  
  
## Extension functions summary

`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[KotlinHierarchyBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/org/jetbrains/kotlin/gradle/plugin/KotlinHierarchyBuilder).[withAndroid](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/package-summary#\(org.jetbrains.kotlin.gradle.plugin.KotlinHierarchyBuilder\).withAndroid\(\))()` Creates an extension for android support in applyDefaultHierarchyTemplate, for example:  
---|---  
  
## Extension functions

### withAndroid

Added in 9.4.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [KotlinHierarchyBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/org/jetbrains/kotlin/gradle/plugin/KotlinHierarchyBuilder).[withAndroid](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/package-summary#\(org.jetbrains.kotlin.gradle.plugin.KotlinHierarchyBuilder\).withAndroid\(\))(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Creates an extension for android support in applyDefaultHierarchyTemplate, for example:

applyDefaultHierarchyTemplate { common { group("androidJvm") { withJvm() withAndroid() } } }

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
