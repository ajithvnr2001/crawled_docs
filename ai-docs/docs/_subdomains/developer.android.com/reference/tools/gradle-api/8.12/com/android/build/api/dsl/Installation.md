---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Installation/
title: Installation \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:59:20.506266+00:00
---

# Installation  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Installation/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Installation

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/Installation.kt+class:com.android.build.api.dsl.Installation)

Added in 7.0.0
    
    
    interface [Installation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Installation)

Known direct subclasses 

[AdbOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/AdbOptions), [ApplicationInstallation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApplicationInstallation), [DynamicFeatureInstallation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DynamicFeatureInstallation), [LibraryInstallation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/LibraryInstallation), [TestInstallation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TestInstallation)

`[AdbOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/AdbOptions)` |  **This interface is deprecated.** Renamed to Installation  
---|---  
`[ApplicationInstallation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApplicationInstallation)` |   
`[DynamicFeatureInstallation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DynamicFeatureInstallation)` |  DSL object for configuring installation options for Dynamic Feature plugins.  
`[LibraryInstallation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/LibraryInstallation)` |  DSL object for configuring installation options for Library plugins.  
`[TestInstallation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TestInstallation)` |  DSL object for configuring installation options for Test plugins.  
  
* * *

Local installation options for the adb tool.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[installOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Installation#installOptions\(kotlin.String\))~~(option: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** To be removed in AGP 9.0  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[installOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Installation#installOptions\(kotlin.Array\))~~(vararg options: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** To be removed in AGP 9.0  
  
### Public properties  
  
---  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[installOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Installation#installOptions\(\))` The list of FULL_APK installation options.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[timeOutInMs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Installation#timeOutInMs\(\))` The time out used for all adb operations.  
  
## Public functions

### installOptions

Added in 7.0.0

Deprecated in 8.0.2
    
    
    fun ~~[installOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Installation#installOptions\(kotlin.String\))~~(option: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
To be removed in AGP 9.0

Sets the list of FULL_APK installation options

### installOptions

Added in 7.0.0

Deprecated in 8.0.2
    
    
    fun ~~[installOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Installation#installOptions\(kotlin.Array\))~~(vararg options: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
To be removed in AGP 9.0

Sets the list of FULL_APK installation options

## Public properties

### installOptions

Added in 7.0.0
    
    
    val [installOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Installation#installOptions\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The list of FULL_APK installation options.

### timeOutInMs

Added in 7.0.0
    
    
    var [timeOutInMs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Installation#timeOutInMs\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

The time out used for all adb operations.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
