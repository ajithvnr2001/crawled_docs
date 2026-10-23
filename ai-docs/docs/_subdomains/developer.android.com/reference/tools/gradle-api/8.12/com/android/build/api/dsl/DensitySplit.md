---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DensitySplit/
title: DensitySplit \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:57:47.573657+00:00
---

# DensitySplit  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DensitySplit/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DensitySplit

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/DensitySplit.kt+class:com.android.build.api.dsl.DensitySplit)

Added in 4.2.0

Deprecated in 8.1.0
    
    
    interface [DensitySplit](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DensitySplit) : [Split](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Split)

* * *

**This interface is deprecated.**  
Density-based apk split feature is deprecated and will be removed in AGP 10.0.Use Android App Bundle (https://developer.android.com/guide/app-bundle)to generate optimized APKs.

DSL object for configuring per-density splits options.

See [APK Splits](https://developer.android.com/studio/build/configure-apk-splits.html).

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compatibleScreens](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DensitySplit#compatibleScreens\(kotlin.Array\))(vararg sizes: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds a new compatible screen.  
  
### Public properties  
  
---  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[compatibleScreens](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DensitySplit#compatibleScreens\(\))` A list of compatible screens.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isStrict](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DensitySplit#isStrict\(\))` TODO: Document.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.Split](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Split) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[exclude](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Split#exclude\(kotlin.Array\))(vararg excludes: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Excludes some values  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[include](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Split#include\(kotlin.Array\))(vararg includes: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Includes some values  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[reset](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Split#reset\(\))()` Resets the list of included split configuration.  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.Split](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Split) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isEnable](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Split#isEnable\(\))` Whether to split in this dimension.  
---|---  
  
## Public functions

### compatibleScreens

Added in 4.2.0

Deprecated in 8.1.0
    
    
    fun [compatibleScreens](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DensitySplit#compatibleScreens\(kotlin.Array\))(vararg sizes: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds a new compatible screen.

## Public properties

### compatibleScreens

Added in 4.2.0

Deprecated in 8.1.0
    
    
    val [compatibleScreens](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DensitySplit#compatibleScreens\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

A list of compatible screens.

This will inject a matching `<compatible-screens><screen ...>` node in the manifest. This is optional.

### isStrict

Added in 4.2.0

Deprecated in 8.1.0
    
    
    var [isStrict](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DensitySplit#isStrict\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

TODO: Document.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
