---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestAndroidResources/
title: TestAndroidResources \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:55:59.224016+00:00
---

# TestAndroidResources  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestAndroidResources/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestAndroidResources

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/TestAndroidResources.kt+class:com.android.build.api.dsl.TestAndroidResources)

Added in 8.1.0
    
    
    interface [TestAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestAndroidResources) : [AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources)

* * *

DSL object for configuring Android resource options for Test plugins.

This is accessed via `[TestExtension.androidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestExtension#androidResources\(kotlin.Function1\))`

## Summary

### Inherited functions  
  
---  
From [com.android.build.api.dsl.AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#additionalParameters\(kotlin.String\))~~(params: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property additionalParameters  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#additionalParameters\(kotlin.Array\))~~(vararg params: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property additionalParameters  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[noCompress](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#noCompress\(kotlin.String\))~~(noCompress: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property noCompress  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[noCompress](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#noCompress\(kotlin.Array\))~~(vararg noCompress: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property noCompress  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources) | `[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#additionalParameters\(\))` List of additional parameters to pass to `aapt`.  
---|---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[failOnMissingConfigEntry](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#failOnMissingConfigEntry\(\))` Forces aapt to return an error if it fails to find an entry for a configuration.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[ignoreAssetsPattern](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#ignoreAssetsPattern\(\))` Pattern describing assets to be ignored.  
`[MutableCollection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[ignoreAssetsPatterns](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#ignoreAssetsPatterns\(\))` Patterns describing assets to be ignored.  
`[MutableCollection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[noCompress](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#noCompress\(\))` File extensions of Android resources, assets, and Java resources to be stored uncompressed in the APK.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
