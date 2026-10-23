---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkSpec/
title: MinSdkSpec \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:13:16.199255+00:00
---

# MinSdkSpec  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkSpec/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# MinSdkSpec

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/MinSdkSpec.kt+class:com.android.build.api.dsl.MinSdkSpec)

Added in 8.13.0
    
    
    interface [MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkSpec)

* * *

DSL object to configure min SDK version.

To set min SDK version with a released API level,
    
    
    android {  
      defaultConfig {  
        minSdk {  
          version = release(33)  
        }  
      }  
    }

or to set min SDK version with a preview API level
    
    
    android {  
      defaultConfig {  
        minSdk {  
          version = preview("Tiramisu")  
        }  
      }  
    }

## Summary

### Public functions  
  
---  
`[MinSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkVersion)` |  `@[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.5/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
[preview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkSpec#preview\(kotlin.String\))(codeName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` To set min SDK version with a preview API level, use this function to compute the `[MinSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkVersion)` and assign it to `[MinSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkSpec#version\(\))` property.  
`[MinSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkVersion)` |  `@[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.5/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
[release](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkSpec#release\(kotlin.Int\))(version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` To set min SDK version with a released API level, use this function to compute the `[MinSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkVersion)` and assign it to `[MinSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkSpec#version\(\))` property.  
  
### Public properties  
  
---  
`[MinSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkVersion)?` |  `[version](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkSpec#version\(\))` The min SDK version.  
  
## Public functions

### preview

Added in 8.13.0
    
    
    @[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.5/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
    fun [preview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkSpec#preview\(kotlin.String\))(codeName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [MinSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkVersion)

To set min SDK version with a preview API level, use this function to compute the `[MinSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkVersion)` and assign it to `[MinSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkSpec#version\(\))` property.

### release

Added in 8.13.0
    
    
    @[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.5/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
    fun [release](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkSpec#release\(kotlin.Int\))(version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [MinSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkVersion)

To set min SDK version with a released API level, use this function to compute the `[MinSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkVersion)` and assign it to `[MinSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkSpec#version\(\))` property.

## Public properties

### version

Added in 8.13.0
    
    
    var [version](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkSpec#version\(\)): [MinSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkVersion)?

The min SDK version.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
