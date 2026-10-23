---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkSpec/
title: TargetSdkSpec \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:03:19.839496+00:00
---

# TargetSdkSpec  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkSpec/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TargetSdkSpec

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/TargetSdkSpec.kt+class:com.android.build.api.dsl.TargetSdkSpec)

Added in 8.12.3
    
    
    interface [TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkSpec)

* * *

DSL object to configure the target SDK.

To configure target SDK with a release API level,
    
    
    android {  
      defaultConfig {  
        targetSdk {  
          version = release(33)  
        }  
      }  
    }

or with a preview API level
    
    
    android {  
      defaultConfig {  
        targetSdk {  
          version = preview("Tiramisu")  
        }  
      }  
    }

## Summary

### Public functions  
  
---  
`[TargetSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkVersion)` |  `[preview](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkSpec#preview\(kotlin.String\))(codeName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` To set target SDK version with a preview API level, use this function to compute the `[TargetSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkVersion)` and assign it to `[TargetSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkSpec#version\(\))` property.  
`[TargetSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkVersion)` |  `[release](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkSpec#release\(kotlin.Int\))(version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` To set target SDK version with a released API level, use this function to compute the `[TargetSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkVersion)` and assign it to `[TargetSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkSpec#version\(\))` property.  
  
### Public properties  
  
---  
`[TargetSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkVersion)?` |  `[version](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkSpec#version\(\))` The target SDK version.  
  
## Public functions

### preview

Added in 8.12.3
    
    
    fun [preview](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkSpec#preview\(kotlin.String\))(codeName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [TargetSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkVersion)

To set target SDK version with a preview API level, use this function to compute the `[TargetSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkVersion)` and assign it to `[TargetSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkSpec#version\(\))` property.

### release

Added in 8.12.3
    
    
    fun [release](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkSpec#release\(kotlin.Int\))(version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [TargetSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkVersion)

To set target SDK version with a released API level, use this function to compute the `[TargetSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkVersion)` and assign it to `[TargetSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkSpec#version\(\))` property.

## Public properties

### version

Added in 8.12.3
    
    
    var [version](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkSpec#version\(\)): [TargetSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkVersion)?

The target SDK version.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-09-11 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-11 UTC."],[],[]] 
