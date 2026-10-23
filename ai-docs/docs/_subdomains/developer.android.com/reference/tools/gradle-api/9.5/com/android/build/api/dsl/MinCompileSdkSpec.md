---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinCompileSdkSpec/
title: MinCompileSdkSpec \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:13:14.459178+00:00
---

# MinCompileSdkSpec  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinCompileSdkSpec/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# MinCompileSdkSpec

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/MinCompileSdkSpec.kt+class:com.android.build.api.dsl.MinCompileSdkSpec)

Added in 9.5.0-alpha10
    
    
    interface [MinCompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinCompileSdkSpec)

* * *

Specifies the minimum compileSdk this Gradle project imposes on projects that depend on it, both within the same build and when publishing AARs.

This defaults to the compile SDK of your project. If you set this value to lower than your compileSdk, you should take care to only use Android APIs from that lower API level to not create problems (such as with dexing and resource references) to projects that depend on your library.

## Summary

### Public functions  
  
---  
`[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CompileSdkVersion)` |  `@[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.5/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
[release](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinCompileSdkSpec#release\(kotlin.Int\))(version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` To set min compile SDK version with a released API level, use this function to compute the `[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CompileSdkVersion)` and assign it to `[MinCompileSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinCompileSdkSpec#version\(\))` property.  
`[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CompileSdkVersion)` |  `@[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.5/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
[release](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinCompileSdkSpec#release\(kotlin.Int,kotlin.Function1\))(version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), action: [CompileSdkReleaseSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CompileSdkReleaseSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` To set min compile SDK version with a released API level, use this function to compute the `[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CompileSdkVersion)` and assign it to `[MinCompileSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinCompileSdkSpec#version\(\))` property.  
  
### Public properties  
  
---  
`[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CompileSdkVersion)?` |  `[version](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinCompileSdkSpec#version\(\))` The min compile SDK version set for this project.  
  
## Public functions

### release

Added in 9.5.0-alpha10
    
    
    @[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.5/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
    fun [release](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinCompileSdkSpec#release\(kotlin.Int\))(version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CompileSdkVersion)

To set min compile SDK version with a released API level, use this function to compute the `[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CompileSdkVersion)` and assign it to `[MinCompileSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinCompileSdkSpec#version\(\))` property.

### release

Added in 9.5.0-alpha10
    
    
    @[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.5/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
    fun [release](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinCompileSdkSpec#release\(kotlin.Int,kotlin.Function1\))(version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), action: [CompileSdkReleaseSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CompileSdkReleaseSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CompileSdkVersion)

To set min compile SDK version with a released API level, use this function to compute the `[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CompileSdkVersion)` and assign it to `[MinCompileSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinCompileSdkSpec#version\(\))` property. You can also set minor API level and SDK extension level via `[CompileSdkReleaseSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CompileSdkReleaseSpec)` block.

## Public properties

### version

Added in 9.5.0-alpha10
    
    
    var [version](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinCompileSdkSpec#version\(\)): [CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CompileSdkVersion)?

The min compile SDK version set for this project.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
