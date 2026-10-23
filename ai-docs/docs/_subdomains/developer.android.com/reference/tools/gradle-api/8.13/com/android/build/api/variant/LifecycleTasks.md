---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/LifecycleTasks/
title: LifecycleTasks \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:40:19.786404+00:00
---

# LifecycleTasks  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/LifecycleTasks/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# LifecycleTasks

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/LifecycleTasks.kt+class:com.android.build.api.variant.LifecycleTasks)

Added in 8.3.1
    
    
    interface [LifecycleTasks](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/LifecycleTasks)

* * *

Lifecycle tasks created by the AGP plugins.

A lifecycle task usually does not have any processing associated with it but represent a specific location in the build process that can be used to register dependent tasks. These are also `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)`s that can be invoked by users which provide a consumable output.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[registerPreBuild](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/LifecycleTasks#registerPreBuild\(kotlin.Array\))(vararg objects: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Register PreBuild lifecycle task dependencies.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[registerPreInstallation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/LifecycleTasks#registerPreInstallation\(kotlin.Array\))(vararg objects: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Register a Install task dependencies.  
  
## Public functions

### registerPreBuild

Added in 8.3.1
    
    
    fun [registerPreBuild](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/LifecycleTasks#registerPreBuild\(kotlin.Array\))(vararg objects: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Register PreBuild lifecycle task dependencies.

Parameters  
---  
`vararg objects: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  must comply to Gradle's task dependency rules defined [there](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html#dependencies)  
  
### registerPreInstallation

Added in 8.13.2
    
    
    fun [registerPreInstallation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/LifecycleTasks#registerPreInstallation\(kotlin.Array\))(vararg objects: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Register a Install task dependencies.

Parameters  
---  
`vararg objects: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  must comply to Gradle's task dependency rules defined [there](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html#dependencies)  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-11 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-11 UTC."],[],[]] 
