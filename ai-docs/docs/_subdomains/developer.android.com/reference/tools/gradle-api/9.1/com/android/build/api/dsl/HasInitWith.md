---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/HasInitWith/
title: HasInitWith \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:03:03.535858+00:00
---

# HasInitWith  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/HasInitWith/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# HasInitWith

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/HasInitWith.kt+class:com.android.build.api.dsl.HasInitWith)

Added in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [HasInitWith](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/HasInitWith)<T : [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>

* * *

For build types and product flavors, they can be initialized from the current state of another.

This can be useful to save repeating configuration in the build file when two build types or flavors should be almost identical.

Custom extensions attached to build type and product flavor should implement this, so that they can also be initialized when Android Gradle plugin initialized the build type or product flavor too. Note that this will only work with Android Gradle Plugin 7.1 or higher, for older versions this will have no effect.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[initWith](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/HasInitWith#initWith\(kotlin.Any\))(that: T)` Copy the properties of the given build type, product flavor or custom extension to this  
  
## Public functions

### initWith

Added in 7.1.0
    
    
    fun [initWith](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/HasInitWith#initWith\(kotlin.Any\))(that: T): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Copy the properties of the given build type, product flavor or custom extension to this

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
