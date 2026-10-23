---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources/
title: AndroidResources \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:00:11.272456+00:00
---

# AndroidResources  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AndroidResources

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/AndroidResources.kt+class:com.android.build.api.dsl.AndroidResources)

Added in 7.0.0
    
    
    interface [AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources)

Known direct subclasses 

[AaptOptions](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AaptOptions), [ApplicationAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationAndroidResources), [DynamicFeatureAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/DynamicFeatureAndroidResources), [LibraryAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/LibraryAndroidResources), [TestAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/TestAndroidResources)

`[AaptOptions](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AaptOptions)` |  **This interface is deprecated.** Renamed to AndroidResources  
---|---  
`[ApplicationAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationAndroidResources)` |  DSL object for configuring Android resource options for Application plugins.  
`[DynamicFeatureAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/DynamicFeatureAndroidResources)` |  DSL object for configuring Android resource options for Dynamic Feature plugins.  
`[LibraryAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/LibraryAndroidResources)` |  DSL object for configuring Android resource options for Library plugins.  
`[TestAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/TestAndroidResources)` |  DSL object for configuring Android resource options for Test plugins.  
  
* * *

DSL object for configuring Android resource options.

This is accessed via `[CommonExtension.androidResources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CommonExtension#androidResources\(\))`

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#additionalParameters\(kotlin.String\))~~(params: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property additionalParameters  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#additionalParameters\(kotlin.Array\))~~(vararg params: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property additionalParameters  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[noCompress](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#noCompress\(kotlin.String\))~~(noCompress: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property noCompress  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[noCompress](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#noCompress\(kotlin.Array\))~~(vararg noCompress: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property noCompress  
  
### Public properties  
  
---  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#additionalParameters\(\))` List of additional parameters to pass to `aapt`.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[failOnMissingConfigEntry](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#failOnMissingConfigEntry\(\))` Forces aapt to return an error if it fails to find an entry for a configuration.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[ignoreAssetsPattern](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#ignoreAssetsPattern\(\))` Pattern describing assets to be ignored.  
`[MutableCollection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[ignoreAssetsPatterns](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#ignoreAssetsPatterns\(\))` Patterns describing assets to be ignored.  
`[MutableCollection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[noCompress](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#noCompress\(\))` File extensions of Android resources, assets, and Java resources to be stored uncompressed in the APK.  
  
## Public functions

### additionalParameters

Added in 7.0.0

Deprecated in 8.0.2
    
    
    fun ~~[additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#additionalParameters\(kotlin.String\))~~(params: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced with property additionalParameters

Adds additional parameters to be passed to `aapt`.

### additionalParameters

Added in 7.0.0

Deprecated in 8.0.2
    
    
    fun ~~[additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#additionalParameters\(kotlin.Array\))~~(vararg params: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced with property additionalParameters

Adds additional parameters to be passed to `aapt`.

### noCompress

Added in 7.0.0

Deprecated in 8.0.2
    
    
    fun ~~[noCompress](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#noCompress\(kotlin.String\))~~(noCompress: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced with property noCompress

Adds a file extension of Android resources, assets, and Java resources to be stored uncompressed in the APK. Adding an empty extension (i.e., `noCompress('')`) will disable compression for all Android resources, assets, and Java resources.

### noCompress

Added in 7.0.0

Deprecated in 8.0.2
    
    
    fun ~~[noCompress](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#noCompress\(kotlin.Array\))~~(vararg noCompress: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced with property noCompress

Adds file extensions of Android resources, assets, and Java resources to be stored uncompressed in the APK. Adding an empty extension (e.g., `noCompress('')`) will disable compression for all Android resources, assets, and Java resources.

## Public properties

### additionalParameters

Added in 7.0.0
    
    
    val [additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#additionalParameters\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

List of additional parameters to pass to `aapt`.

### failOnMissingConfigEntry

Added in 7.0.0
    
    
    var [failOnMissingConfigEntry](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#failOnMissingConfigEntry\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Forces aapt to return an error if it fails to find an entry for a configuration.

See `aapt --help`

### ignoreAssetsPattern

Added in 7.0.0
    
    
    var [ignoreAssetsPattern](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#ignoreAssetsPattern\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Pattern describing assets to be ignored.

This is `[ignoreAssetsPatterns](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#ignoreAssetsPatterns\(\))` joined by ':'.

### ignoreAssetsPatterns

Added in 7.3.0
    
    
    val [ignoreAssetsPatterns](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#ignoreAssetsPatterns\(\)): [MutableCollection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Patterns describing assets to be ignored.

If empty, defaults to `["!.svn", "!.git", "!.ds_store", "!*.scc", ".*", "<dir>_*", "!CVS", "!thumbs.db", "!picasa.ini", "!*~"]`

### noCompress

Added in 7.0.0
    
    
    val [noCompress](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AndroidResources#noCompress\(\)): [MutableCollection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

File extensions of Android resources, assets, and Java resources to be stored uncompressed in the APK. Adding an empty extension (e.g., setting `noCompress ''`) will disable compression for all Android resources, assets, and Java resources.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
