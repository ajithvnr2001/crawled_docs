---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsPackaging/
title: JniLibsPackaging \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:01:09.793376+00:00
---

# JniLibsPackaging  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsPackaging/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# JniLibsPackaging

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/JniLibsPackaging.kt+class:com.android.build.api.variant.JniLibsPackaging)

Added in 7.0.0
    
    
    interface [JniLibsPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsPackaging)

Known direct subclasses 

[JniLibsApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsApkPackaging), [JniLibsTestedComponentPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsTestedComponentPackaging)

`[JniLibsApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsApkPackaging)` |  Build-time properties for packaging native libraries (.so) inside an APK `[Component](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Component)`.  
---|---  
`[JniLibsTestedComponentPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsTestedComponentPackaging)` |  Build-time properties for packaging native libraries (.so) inside a tested `[Component](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Component)`.  
  
Known indirect subclasses 

[JniLibsTestedApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsTestedApkPackaging)

`[JniLibsTestedApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsTestedApkPackaging)` |  Build-time properties for packaging native libraries (.so) inside a tested APK `[Component](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Component)`.  
---|---  
  
* * *

Build-time properties for packaging native libraries (.so) inside a `[Component](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Component)`.

This is accessed via `[Packaging.jniLibs](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Packaging#jniLibs\(\))`

## Summary

### Public properties  
  
---  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[excludes](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsPackaging#excludes\(\))` The set of excluded patterns.  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[keepDebugSymbols](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsPackaging#keepDebugSymbols\(\))` The set of patterns for native libraries that should not be stripped of debug symbols.  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[pickFirsts](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsPackaging#pickFirsts\(\))` The set of patterns for which the first occurrence is packaged in the APK.  
  
## Public properties

### excludes

Added in 7.0.0
    
    
    val [excludes](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsPackaging#excludes\(\)): [SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The set of excluded patterns. Native libraries matching any of these patterns do not get packaged.

Example usage: `packaging.jniLibs.excludes.add("**`/`exclude.so")`

### keepDebugSymbols

Added in 7.0.0
    
    
    val [keepDebugSymbols](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsPackaging#keepDebugSymbols\(\)): [SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The set of patterns for native libraries that should not be stripped of debug symbols.

Example: `packaging.jniLibs.keepDebugSymbols.add("**`/`doNotStrip.so")`

### pickFirsts

Added in 7.0.0
    
    
    val [pickFirsts](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsPackaging#pickFirsts\(\)): [SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The set of patterns for which the first occurrence is packaged in the APK. For each native library APK entry path matching one of these patterns, only the first native library found with that path gets packaged.

Example usage: `packaging.jniLibs.pickFirsts.add("**`/`pickFirst.so")`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
