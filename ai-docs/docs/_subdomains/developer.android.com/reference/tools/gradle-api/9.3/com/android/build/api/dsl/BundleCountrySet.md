---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCountrySet/
title: BundleCountrySet \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:27:30.970314+00:00
---

# BundleCountrySet  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCountrySet/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BundleCountrySet

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/BundleCountrySet.kt+class:com.android.build.api.dsl.BundleCountrySet)

Added in 8.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [BundleCountrySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCountrySet)

* * *

DSL object for configuring the App Bundle Country Set options

This is accessed via `[Bundle.countrySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Bundle#countrySet\(kotlin.Function1\))`

## Summary

### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[defaultSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCountrySet#defaultSet\(\))` Specifies the default country set value for the bundle.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[enableSplit](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCountrySet#enableSplit\(\))`  
  
## Public properties

### defaultSet

Added in 8.1.0
    
    
    var [defaultSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCountrySet#defaultSet\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Specifies the default country set value for the bundle. Used for filtering splits for standalone, system and universal APKs.

### enableSplit

Added in 8.1.0
    
    
    var [enableSplit](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCountrySet#enableSplit\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
