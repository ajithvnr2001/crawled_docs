---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion/
title: CompileSdkVersion \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:45:54.216729+00:00
---

# CompileSdkVersion  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# CompileSdkVersion

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/CompileSdkSpec.kt+class:com.android.build.api.dsl.CompileSdkVersion)

Added in 8.13.0
    
    
    @[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.2/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
    interface [CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion)

* * *

DSL object to represent compile sdk version.

## Summary

### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[addonName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion#addonName\(\))` The add-on name of the SDK to compile your project against.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[apiLevel](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion#apiLevel\(\))` The API level to compile your project against.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[betaVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion#betaVersion\(\))` The beta version of the SDK.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[canaryDate](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion#canaryDate\(\))` The canary version's date.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[codeName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion#codeName\(\))` The preview API to compile your project against.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[minorApiLevel](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion#minorApiLevel\(\))` Minor API version for compile SDK.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[sdkExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion#sdkExtension\(\))` The SDK Extension level to compile your project against.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[vendorName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion#vendorName\(\))` The vendor name of the SDK to compile your project against.  
  
## Public properties

### addonName

Added in 8.13.0
    
    
    val [addonName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion#addonName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The add-on name of the SDK to compile your project against.

### apiLevel

Added in 8.13.0
    
    
    val [apiLevel](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion#apiLevel\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

The API level to compile your project against.

### betaVersion

Added in 9.2.1
    
    
    val [betaVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion#betaVersion\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

The beta version of the SDK.

### canaryDate

Added in 9.2.1
    
    
    val [canaryDate](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion#canaryDate\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The canary version's date.

### codeName

Added in 8.13.0
    
    
    val [codeName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion#codeName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The preview API to compile your project against. Once the preview APIs are finalized, they will be allocated a stable integer value.

### minorApiLevel

Added in 8.13.0
    
    
    val [minorApiLevel](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion#minorApiLevel\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Minor API version for compile SDK. This should be used with the `[apiLevel](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion#apiLevel\(\))` property to specify a full SDK version.

### sdkExtension

Added in 8.13.0
    
    
    val [sdkExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion#sdkExtension\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

The SDK Extension level to compile your project against.

### vendorName

Added in 8.13.0
    
    
    val [vendorName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion#vendorName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The vendor name of the SDK to compile your project against.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
