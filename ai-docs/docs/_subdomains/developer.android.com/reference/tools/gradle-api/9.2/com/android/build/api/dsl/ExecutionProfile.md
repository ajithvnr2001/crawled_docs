---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ExecutionProfile/
title: ExecutionProfile \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:51.398741+00:00
---

# ExecutionProfile  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ExecutionProfile/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ExecutionProfile

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ExecutionProfile.kt+class:com.android.build.api.dsl.ExecutionProfile)

Added in 7.4.0
    
    
    interface [ExecutionProfile](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ExecutionProfile) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html)

* * *

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[r8](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ExecutionProfile#r8\(kotlin.Function1\))(action: [ToolOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ToolOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specify R8 execution options.  
  
### Public properties  
  
---  
`[ToolOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ToolOptions)` |  `[r8](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ExecutionProfile#r8\(\))` Specify R8 execution options.  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
## Public functions

### r8

Added in 7.4.0
    
    
    fun [r8](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ExecutionProfile#r8\(kotlin.Function1\))(action: [ToolOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ToolOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specify R8 execution options.

## Public properties

### r8

Added in 7.4.0
    
    
    val [r8](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ExecutionProfile#r8\(\)): [ToolOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ToolOptions)

Specify R8 execution options.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
