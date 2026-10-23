---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CompileSdkReleaseSpec/
title: CompileSdkReleaseSpec \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:28:06.707092+00:00
---

# CompileSdkReleaseSpec  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CompileSdkReleaseSpec/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# CompileSdkReleaseSpec

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/CompileSdkReleaseSpec.kt+class:com.android.build.api.dsl.CompileSdkReleaseSpec)

Added in 8.13.0
    
    
    interface [CompileSdkReleaseSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CompileSdkReleaseSpec)

* * *

Configures the compile sdk version when a released API level is used. See `[CompileSdkSpec.release](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CompileSdkSpec#release\(kotlin.Int,kotlin.Function1\))`

## Summary

### Public properties  
  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[minorApiLevel](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CompileSdkReleaseSpec#minorApiLevel\(\))` Set minor API version for compile SDK.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[sdkExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CompileSdkReleaseSpec#sdkExtension\(\))` Set the SDK Extension level to compile your project against.  
  
## Public properties

### minorApiLevel

Added in 8.13.0
    
    
    var [minorApiLevel](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CompileSdkReleaseSpec#minorApiLevel\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Set minor API version for compile SDK. This should be used with the main API version to specify a full SDK version.

### sdkExtension

Added in 8.13.0
    
    
    var [sdkExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CompileSdkReleaseSpec#sdkExtension\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Set the SDK Extension level to compile your project against.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
