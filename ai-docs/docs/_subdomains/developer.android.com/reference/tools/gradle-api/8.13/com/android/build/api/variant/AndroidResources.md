---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidResources/
title: AndroidResources \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:37:27.840972+00:00
---

# AndroidResources  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidResources/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AndroidResources

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/AndroidResources.kt+class:com.android.build.api.variant.AndroidResources)

Added in 7.0.0
    
    
    interface [AndroidResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidResources)

Known direct subclasses 

[ApplicationAndroidResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ApplicationAndroidResources)

`[ApplicationAndroidResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ApplicationAndroidResources)` |  Build-time properties for Android Resources inside a `[Component](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Component)`.  
---|---  
  
* * *

Build-time properties for Android Resources inside a `[Component](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Component)`.

This is accessed via `[GeneratesApk.androidResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/GeneratesApk#androidResources\(\))`

## Summary

### Public properties  
  
---  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[aaptAdditionalParameters](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidResources#aaptAdditionalParameters\(\))` The list of additional parameters to pass to aapt.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[dataBinding](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidResources#dataBinding\(\))` Flag indicating whether databinding feature is on  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[ignoreAssetsPatterns](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidResources#ignoreAssetsPatterns\(\))` The list of patterns describing assets to be ignored.  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[noCompress](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidResources#noCompress\(\))` File extensions of Android resources, assets, and Java resources to be stored uncompressed in the APK.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[viewBinding](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidResources#viewBinding\(\))` Flag indicating whether viewbinding feature is on  
  
## Public properties

### aaptAdditionalParameters

Added in 7.0.0
    
    
    val [aaptAdditionalParameters](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidResources#aaptAdditionalParameters\(\)): [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The list of additional parameters to pass to aapt.

This property will be initialized using the corresponding DSL value.

### dataBinding

Added in 8.4.0
    
    
    val [dataBinding](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidResources#dataBinding\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Flag indicating whether databinding feature is on

### ignoreAssetsPatterns

Added in 7.0.0
    
    
    val [ignoreAssetsPatterns](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidResources#ignoreAssetsPatterns\(\)): [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The list of patterns describing assets to be ignored.

See aapt's --ignore-assets flag via `aapt --help`. Note: the --ignore-assets flag accepts a single string of colon-delimited patterns, whereas this property is a list of patterns.

This property will be initialized using the corresponding DSL value.

### noCompress

Added in 7.2.0
    
    
    val [noCompress](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidResources#noCompress\(\)): [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

File extensions of Android resources, assets, and Java resources to be stored uncompressed in the APK. Adding an empty extension (e.g., `noCompress.add("")`) will disable compression for all Android resources, assets, and Java resources.

### viewBinding

Added in 8.4.0
    
    
    val [viewBinding](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidResources#viewBinding\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Flag indicating whether viewbinding feature is on

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
