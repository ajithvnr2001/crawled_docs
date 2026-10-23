---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DexPackagingOptions/
title: DexPackagingOptions \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:52:50.297200+00:00
---

# DexPackagingOptions  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DexPackagingOptions/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DexPackagingOptions

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/DexPackagingOptions.kt+class:com.android.build.api.variant.DexPackagingOptions)

Added in 4.2.0
    
    
    interface [DexPackagingOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DexPackagingOptions)

* * *

Build-time properties for packaging dex files inside an APK `[Component](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component)`.

This is accessed via `[ApkPackaging.dex](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApkPackaging#dex\(\))`

## Summary

### Public properties  
  
---  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[useLegacyPackaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DexPackagingOptions#useLegacyPackaging\(\))` Whether to use the legacy convention of compressing all dex files in the APK.  
  
## Public properties

### useLegacyPackaging

Added in 4.2.0
    
    
    val [useLegacyPackaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DexPackagingOptions#useLegacyPackaging\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>

Whether to use the legacy convention of compressing all dex files in the APK.

This property is initialized from the `[com.android.build.api.dsl.DexPackaging.useLegacyPackaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DexPackaging#useLegacyPackaging\(\))` DSL element, if set. If this property and the DSL are unset, dex files will be uncompressed when minSdk >= 28. If this property is set, the value will be fed directly to the corresponding Gradle tasks without extra logic.

This property does not affect dex file compression in APKs produced from app bundles.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
