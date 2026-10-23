---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JniLibsApkPackaging/
title: JniLibsApkPackaging \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:54:17.637545+00:00
---

# JniLibsApkPackaging  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JniLibsApkPackaging/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# JniLibsApkPackaging

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/JniLibsApkPackaging.kt+class:com.android.build.api.variant.JniLibsApkPackaging)

Added in 7.0.0
    
    
    interface [JniLibsApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JniLibsApkPackaging) : [JniLibsPackaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JniLibsPackaging)

Known direct subclasses 

[JniLibsTestedApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JniLibsTestedApkPackaging)

`[JniLibsTestedApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JniLibsTestedApkPackaging)` |  Build-time properties for packaging native libraries (.so) inside a tested APK `[Component](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component)`.  
---|---  
  
* * *

Build-time properties for packaging native libraries (.so) inside an APK `[Component](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component)`.

This is accessed via `[ApkPackaging.jniLibs](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApkPackaging#jniLibs\(\))`

## Summary

### Public properties  
  
---  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[useLegacyPackaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JniLibsApkPackaging#useLegacyPackaging\(\))` Whether to use the legacy convention of compressing all .so files in the APK.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[useLegacyPackagingFromBundle](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JniLibsApkPackaging#useLegacyPackagingFromBundle\(\))` Whether to use the legacy convention of compressing all .so files when generating APKs from the app bundle.  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.JniLibsPackaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JniLibsPackaging) | `[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[excludes](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JniLibsPackaging#excludes\(\))` The set of excluded patterns.  
---|---  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[keepDebugSymbols](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JniLibsPackaging#keepDebugSymbols\(\))` The set of patterns for native libraries that should not be stripped of debug symbols.  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[pickFirsts](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JniLibsPackaging#pickFirsts\(\))` The set of patterns for which the first occurrence is packaged in the APK.  
  
## Public properties

### useLegacyPackaging

Added in 7.0.0
    
    
    val [useLegacyPackaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JniLibsApkPackaging#useLegacyPackaging\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>

Whether to use the legacy convention of compressing all .so files in the APK. This does not affect APKs generated from the app bundle; see `[useLegacyPackagingFromBundle](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JniLibsApkPackaging#useLegacyPackagingFromBundle\(\))`.

This property is initialized from the `[com.android.build.api.dsl.JniLibsPackaging.useLegacyPackaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/JniLibsPackaging#useLegacyPackaging\(\))` DSL element, if set. If this property and the DSL are unset, .so files will be uncompressed and page-aligned when minSdk >= 23. If this property is set, the value will be fed directly to the corresponding Gradle tasks without extra logic.

If setting this property, consider also setting `[useLegacyPackagingFromBundle](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JniLibsApkPackaging#useLegacyPackagingFromBundle\(\))` to the same value so that .so files are packaged consistently when API level >= 23, whether an APK is generated from the app bundle or not.

### useLegacyPackagingFromBundle

Added in 7.0.0
    
    
    val [useLegacyPackagingFromBundle](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JniLibsApkPackaging#useLegacyPackagingFromBundle\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>

Whether to use the legacy convention of compressing all .so files when generating APKs from the app bundle. If true, .so files will always be compressed when generating APKs from the app bundle, regardless of the API level of the target device. If false, .so files will be compressed only when targeting devices with API level < 23.

This property is initialized from the `[com.android.build.api.dsl.JniLibsPackaging.useLegacyPackaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/JniLibsPackaging#useLegacyPackaging\(\))` DSL element, if set. If this property and the DSL are unset, this property's value defaults to false.

If setting this property to true, consider also setting `[useLegacyPackaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JniLibsApkPackaging#useLegacyPackaging\(\))` to true so that .so files are packaged consistently, whether an APK is generated from the app bundle or not.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
