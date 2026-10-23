---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleDeviceGroup/
title: BundleDeviceGroup \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:27:36.733195+00:00
---

# BundleDeviceGroup  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleDeviceGroup/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BundleDeviceGroup

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/BundleDeviceGroup.kt+class:com.android.build.api.dsl.BundleDeviceGroup)

Added in 8.10.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [BundleDeviceGroup](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleDeviceGroup)

* * *

DSL object for configuring the App Bundle Device Group options

This is accessed via `[Bundle.deviceGroup](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Bundle#deviceGroup\(kotlin.Function1\))`

## Summary

### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[defaultGroup](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleDeviceGroup#defaultGroup\(\))` Specifies the default device group name for the bundle.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[enableSplit](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleDeviceGroup#enableSplit\(\))`  
  
## Public properties

### defaultGroup

Added in 8.10.1
    
    
    var [defaultGroup](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleDeviceGroup#defaultGroup\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Specifies the default device group name for the bundle. Used for local-testing and generating universal APKs.

### enableSplit

Added in 8.10.1
    
    
    var [enableSplit](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleDeviceGroup#enableSplit\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
