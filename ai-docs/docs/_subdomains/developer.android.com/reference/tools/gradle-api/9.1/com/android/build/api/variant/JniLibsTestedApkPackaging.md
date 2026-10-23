---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/JniLibsTestedApkPackaging/
title: JniLibsTestedApkPackaging \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:10:00.242973+00:00
---

# JniLibsTestedApkPackaging  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/JniLibsTestedApkPackaging/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# JniLibsTestedApkPackaging

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/JniLibsTestedApkPackaging.kt+class:com.android.build.api.variant.JniLibsTestedApkPackaging)

Added in 8.4.0
    
    
    interface [JniLibsTestedApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/JniLibsTestedApkPackaging) : [JniLibsTestedComponentPackaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/JniLibsTestedComponentPackaging), [JniLibsApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/JniLibsApkPackaging)

* * *

Build-time properties for packaging native libraries (.so) inside a tested APK `[Component](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/Component)`.

## Summary

### Inherited properties  
  
---  
From [com.android.build.api.variant.JniLibsApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/JniLibsApkPackaging) | `[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[useLegacyPackaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/JniLibsApkPackaging#useLegacyPackaging\(\))` Whether to use the legacy convention of compressing all .so files in the APK.  
---|---  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[useLegacyPackagingFromBundle](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/JniLibsApkPackaging#useLegacyPackagingFromBundle\(\))` Whether to use the legacy convention of compressing all .so files when generating APKs from the app bundle.  
  
From [com.android.build.api.variant.JniLibsPackaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/JniLibsPackaging) | `[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[excludes](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/JniLibsPackaging#excludes\(\))` The set of excluded patterns.  
---|---  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[keepDebugSymbols](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/JniLibsPackaging#keepDebugSymbols\(\))` The set of patterns for native libraries that should not be stripped of debug symbols.  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[pickFirsts](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/JniLibsPackaging#pickFirsts\(\))` The set of patterns for which the first occurrence is packaged in the APK.  
  
From [com.android.build.api.variant.JniLibsTestedComponentPackaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/JniLibsTestedComponentPackaging) | `[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[testOnly](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/JniLibsTestedComponentPackaging#testOnly\(\))` The set of test-only patterns.  
---|---  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
