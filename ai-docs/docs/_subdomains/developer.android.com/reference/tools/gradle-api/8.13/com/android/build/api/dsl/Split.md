---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Split/
title: Split \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:35:08.192488+00:00
---

# Split  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Split/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Split

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/Split.kt+class:com.android.build.api.dsl.Split)

Added in 7.1.0
    
    
    interface [Split](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Split)

Known direct subclasses 

[AbiSplit](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AbiSplit), [DensitySplit](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DensitySplit)

`[AbiSplit](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AbiSplit)` |  DSL object for configuring per-abi splits options.  
---|---  
`[DensitySplit](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DensitySplit)` |  **This interface is deprecated.** Density-based apk split feature is deprecated and will be removed in AGP 10.0.Use Android App Bundle (https://developer.android.com/guide/app-bundle)to generate optimized APKs.  
  
* * *

Base data representing how an APK should be split for a given dimension (density, abi).

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[exclude](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Split#exclude\(kotlin.Array\))(vararg excludes: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Excludes some values  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[include](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Split#include\(kotlin.Array\))(vararg includes: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Includes some values  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[reset](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Split#reset\(\))()` Resets the list of included split configuration.  
  
### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isEnable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Split#isEnable\(\))` Whether to split in this dimension.  
  
## Public functions

### exclude

Added in 7.1.0
    
    
    fun [exclude](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Split#exclude\(kotlin.Array\))(vararg excludes: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Excludes some values

### include

Added in 7.1.0
    
    
    fun [include](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Split#include\(kotlin.Array\))(vararg includes: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Includes some values

### reset

Added in 7.1.0
    
    
    fun [reset](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Split#reset\(\))(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Resets the list of included split configuration.

Use this before calling include, in order to manually configure the list of configuration to split on, rather than excluding from the default list.

## Public properties

### isEnable

Added in 7.1.0
    
    
    var [isEnable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Split#isEnable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether to split in this dimension.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
