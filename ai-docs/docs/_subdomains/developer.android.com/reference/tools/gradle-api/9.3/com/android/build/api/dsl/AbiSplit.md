---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AbiSplit/
title: AbiSplit \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:25:56.649423+00:00
---

# AbiSplit  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AbiSplit/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AbiSplit

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/AbiSplit.kt+class:com.android.build.api.dsl.AbiSplit)

Added in 4.2.0
    
    
    interface [AbiSplit](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AbiSplit) : [Split](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Split)

* * *

DSL object for configuring per-abi splits options.

See [FULL_APK Splits](https://developer.android.com/studio/build/configure-apk-splits.html).

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isUniversalApk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AbiSplit#isUniversalApk\(\))` Whether to create an FULL_APK with all available ABIs.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.Split](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Split) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[exclude](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Split#exclude\(kotlin.Array\))(vararg excludes: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Excludes some values  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[include](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Split#include\(kotlin.Array\))(vararg includes: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Includes some values  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[reset](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Split#reset\(\))()` Resets the list of included split configuration.  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.Split](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Split) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isEnable](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Split#isEnable\(\))` Whether to split in this dimension.  
---|---  
  
## Public properties

### isUniversalApk

Added in 4.2.0
    
    
    var [isUniversalApk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AbiSplit#isUniversalApk\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether to create an FULL_APK with all available ABIs.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
