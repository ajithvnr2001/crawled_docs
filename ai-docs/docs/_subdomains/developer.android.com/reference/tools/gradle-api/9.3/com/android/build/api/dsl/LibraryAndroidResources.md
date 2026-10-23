---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryAndroidResources/
title: LibraryAndroidResources \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:30:10.948903+00:00
---

# LibraryAndroidResources  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryAndroidResources/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# LibraryAndroidResources

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/LibraryAndroidResources.kt+class:com.android.build.api.dsl.LibraryAndroidResources)

Added in 8.1.0
    
    
    interface [LibraryAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryAndroidResources) : [AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidResources)

* * *

DSL object for configuring Android resource options for Library plugins. This is accessed via `[LibraryExtension.androidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryExtension#androidResources\(kotlin.Function1\))`

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enable](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryAndroidResources#enable\(\))` Flag to enable Android resource processing in this library module Default value is 'true' for plain android libraries and 'false' for multiplatform libraries.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[resourcePrefix](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryAndroidResources#resourcePrefix\(\))` Specifies this project's resource prefix to Android Studio for editor features, such as Lint checks.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidResources) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidResources#additionalParameters\(kotlin.String\))~~(params: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property additionalParameters  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidResources#additionalParameters\(kotlin.Array\))~~(vararg params: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property additionalParameters  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[noCompress](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidResources#noCompress\(kotlin.String\))~~(noCompress: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property noCompress  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[noCompress](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidResources#noCompress\(kotlin.Array\))~~(vararg noCompress: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property noCompress  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidResources) | `[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidResources#additionalParameters\(\))` List of additional parameters to pass to `aapt`.  
---|---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[failOnMissingConfigEntry](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidResources#failOnMissingConfigEntry\(\))` Forces aapt to return an error if it fails to find an entry for a configuration.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[ignoreAssetsPattern](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidResources#ignoreAssetsPattern\(\))` Pattern describing assets to be ignored.  
`[MutableCollection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[ignoreAssetsPatterns](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidResources#ignoreAssetsPatterns\(\))` Patterns describing assets to be ignored.  
`[MutableCollection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[noCompress](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidResources#noCompress\(\))` File extensions of Android resources, assets, and Java resources to be stored uncompressed in the APK.  
  
## Public properties

### enable

Added in 8.11.0
    
    
    var [enable](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryAndroidResources#enable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Flag to enable Android resource processing in this library module Default value is 'true' for plain android libraries and 'false' for multiplatform libraries.

### resourcePrefix

Added in 9.3.3
    
    
    var [resourcePrefix](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryAndroidResources#resourcePrefix\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Specifies this project's resource prefix to Android Studio for editor features, such as Lint checks. This property is useful only when using Android Studio.

Including unique prefixes for project resources helps avoid naming collisions with resources from other projects.

For example, when creating a library with String resources, you may want to name each resource with a unique prefix, such as "`mylib_`" to avoid naming collisions with similar resources that the consumer defines.

You can then specify this prefix, as shown below, so that Android Studio expects this prefix when you name project resources:
    
    
    // This property is useful only when developing your project in Android Studio.  
    resourcePrefix = "mylib_"

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
