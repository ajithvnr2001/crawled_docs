---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ApkOutput/
title: ApkOutput \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:16:41.323930+00:00
---

# ApkOutput  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ApkOutput/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ApkOutput

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/ApkOutput.kt+class:com.android.build.api.variant.ApkOutput)

Added in 8.8.0
    
    
    interface [ApkOutput](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ApkOutput)

* * *

Provides an ordered collection of APK batches, each intended for local installation, facilitating staged installations.

An instance of `[ApkOutput](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ApkOutput)` can be obtained via `[ApplicationVariant.outputProviders](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ApplicationVariant#outputProviders\(\))`

See example at `[ApkOutputProviders](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ApkOutputProviders)`

## Summary

### Public properties  
  
---  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[ApkInstallGroup](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ApkInstallGroup)>` |  `[apkInstallGroups](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ApkOutput#apkInstallGroups\(\))` Returns an ordered collection of co-installable APK batches targeted for a specific device.  
  
## Public properties

### apkInstallGroups

Added in 8.8.0
    
    
    val [apkInstallGroups](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ApkOutput#apkInstallGroups\(\)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[ApkInstallGroup](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ApkInstallGroup)>

Returns an ordered collection of co-installable APK batches targeted for a specific device.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
