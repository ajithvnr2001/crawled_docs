---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationInstallation/
title: ApplicationInstallation \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:30:39.725223+00:00
---

# ApplicationInstallation  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationInstallation/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ApplicationInstallation

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ApplicationInstallation.kt+class:com.android.build.api.dsl.ApplicationInstallation)

Added in 8.3.1
    
    
    interface [ApplicationInstallation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationInstallation) : [Installation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Installation)

* * *

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableBaselineProfile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationInstallation#enableBaselineProfile\(\))` Whether to generate per-SDK level baseline profiles to install with an APK.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[installOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationInstallation#installOptions\(\))` The list of FULL_APK installation options.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.Installation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Installation) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[installOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Installation#installOptions\(kotlin.String\))~~(option: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** To be removed in AGP 9.0  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[installOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Installation#installOptions\(kotlin.Array\))~~(vararg options: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** To be removed in AGP 9.0  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.Installation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Installation) | `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[timeOutInMs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Installation#timeOutInMs\(\))` The time out used for all adb operations.  
---|---  
  
## Public properties

### enableBaselineProfile

Added in 8.3.1
    
    
    var [enableBaselineProfile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationInstallation#enableBaselineProfile\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether to generate per-SDK level baseline profiles to install with an APK.

### installOptions
    
    
    val [installOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationInstallation#installOptions\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The list of FULL_APK installation options.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
