---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/BundleStoreArchive/
title: BundleStoreArchive \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:01:36.419234+00:00
---

# BundleStoreArchive  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/BundleStoreArchive/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BundleStoreArchive

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/BundleStoreArchive.kt+class:com.android.build.api.dsl.BundleStoreArchive)

Added in 7.3.0
    
    
    interface [BundleStoreArchive](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/BundleStoreArchive)

* * *

DSL object for configuring the App Bundle Store Archive options

This is accessed via `[Bundle.storeArchive](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Bundle#storeArchive\(kotlin.Function1\))`

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[enable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/BundleStoreArchive#enable\(\))` Archive is an app state that allows an official app store to reclaim device storage and disable app functionality temporarily until the user interacts with the app again.  
  
## Public properties

### enable

Added in 7.3.0
    
    
    var [enable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/BundleStoreArchive#enable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Archive is an app state that allows an official app store to reclaim device storage and disable app functionality temporarily until the user interacts with the app again. Upon interaction the latest available version of the app will be restored while leaving user data unaffected.

Enabled by default. 

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
