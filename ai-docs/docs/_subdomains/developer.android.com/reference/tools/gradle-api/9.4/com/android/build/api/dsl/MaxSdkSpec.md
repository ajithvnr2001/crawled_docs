---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/MaxSdkSpec/
title: MaxSdkSpec \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:54:34.033159+00:00
---

# MaxSdkSpec  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/MaxSdkSpec/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# MaxSdkSpec

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/MaxSdkSpec.kt+class:com.android.build.api.dsl.MaxSdkSpec)

Added in 8.13.0
    
    
    interface [MaxSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/MaxSdkSpec)

* * *

DSL object to configure max SDK version.

For example,
    
    
    android {  
      defaultConfig {  
        maxSdk {  
          version = release(33)  
        }  
      }  
    }

## Summary

### Public functions  
  
---  
`[MaxSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/MaxSdkVersion)` |  `[release](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/MaxSdkSpec#release\(kotlin.Int\))(version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` To set max SDK version, use this function to compute the `[MaxSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/MaxSdkVersion)` and assign it to `[MaxSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/MaxSdkSpec#version\(\))`.  
  
### Public properties  
  
---  
`[MaxSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/MaxSdkVersion)?` |  `[version](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/MaxSdkSpec#version\(\))` The Max SDK version.  
  
## Public functions

### release

Added in 8.13.0
    
    
    fun [release](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/MaxSdkSpec#release\(kotlin.Int\))(version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [MaxSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/MaxSdkVersion)

To set max SDK version, use this function to compute the `[MaxSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/MaxSdkVersion)` and assign it to `[MaxSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/MaxSdkSpec#version\(\))`.

## Public properties

### version

Added in 8.13.0
    
    
    var [version](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/MaxSdkSpec#version\(\)): [MaxSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/MaxSdkVersion)?

The Max SDK version.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
