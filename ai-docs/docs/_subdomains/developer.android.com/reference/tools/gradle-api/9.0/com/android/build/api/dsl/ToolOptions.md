---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ToolOptions/
title: ToolOptions \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:21:39.373104+00:00
---

# ToolOptions  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ToolOptions/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ToolOptions

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ToolOptions.kt+class:com.android.build.api.dsl.ToolOptions)

Added in 7.4.0
    
    
    interface [ToolOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ToolOptions)

* * *

## Summary

### Public properties  
  
---  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[jvmOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ToolOptions#jvmOptions\(\))` Extra JVM options to give to the out of process worker JVM.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[runInSeparateProcess](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ToolOptions#runInSeparateProcess\(\))` If true, run tool workers out of process.  
  
## Public properties

### jvmOptions

Added in 7.4.0
    
    
    val [jvmOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ToolOptions#jvmOptions\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Extra JVM options to give to the out of process worker JVM. Useful for setting things like max memory usage

### runInSeparateProcess

Added in 7.4.0
    
    
    var [runInSeparateProcess](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ToolOptions#runInSeparateProcess\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

If true, run tool workers out of process.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
