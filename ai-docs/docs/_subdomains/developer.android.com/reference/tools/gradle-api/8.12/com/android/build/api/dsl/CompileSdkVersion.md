---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion/
title: CompileSdkVersion \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:57:28.773820+00:00
---

# CompileSdkVersion  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# CompileSdkVersion

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/CompileSdkSpec.kt+class:com.android.build.api.dsl.CompileSdkVersion)

Added in 8.12.3
    
    
    interface [CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion)

* * *

DSL object to represent compile sdk version.

## Summary

### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[addonName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion#addonName\(\))` The add-on name of the SDK to compile your project against.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[apiLevel](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion#apiLevel\(\))` The API level to compile your project against.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[codeName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion#codeName\(\))` The preview API to compile your project against.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[minorApiLevel](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion#minorApiLevel\(\))` Minor API version for compile SDK.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[sdkExtension](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion#sdkExtension\(\))` The SDK Extension level to compile your project against.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[vendorName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion#vendorName\(\))` The vendor name of the SDK to compile your project against.  
  
## Public properties

### addonName

Added in 8.12.3
    
    
    val [addonName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion#addonName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The add-on name of the SDK to compile your project against.

### apiLevel

Added in 8.12.3
    
    
    val [apiLevel](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion#apiLevel\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

The API level to compile your project against.

### codeName

Added in 8.12.3
    
    
    val [codeName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion#codeName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The preview API to compile your project against. Once the preview APIs are finalized, they will be allocated a stable integer value.

### minorApiLevel

Added in 8.12.3
    
    
    val [minorApiLevel](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion#minorApiLevel\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Minor API version for compile SDK. This should be used with the `[apiLevel](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion#apiLevel\(\))` property to specify a full SDK version.

### sdkExtension

Added in 8.12.3
    
    
    val [sdkExtension](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion#sdkExtension\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

The SDK Extension level to compile your project against.

### vendorName

Added in 8.12.3
    
    
    val [vendorName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion#vendorName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The vendor name of the SDK to compile your project against.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-09-11 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-11 UTC."],[],[]] 
