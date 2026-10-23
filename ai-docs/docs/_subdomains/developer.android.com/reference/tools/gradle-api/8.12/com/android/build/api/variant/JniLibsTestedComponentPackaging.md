---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/JniLibsTestedComponentPackaging/
title: JniLibsTestedComponentPackaging \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:08:36.710995+00:00
---

# JniLibsTestedComponentPackaging  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/JniLibsTestedComponentPackaging/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# JniLibsTestedComponentPackaging

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/JniLibsTestedComponentPackaging.kt+class:com.android.build.api.variant.JniLibsTestedComponentPackaging)

Added in 8.4.0
    
    
    interface [JniLibsTestedComponentPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/JniLibsTestedComponentPackaging) : [JniLibsPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/JniLibsPackaging)

Known direct subclasses 

[JniLibsTestedApkPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/JniLibsTestedApkPackaging)

`[JniLibsTestedApkPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/JniLibsTestedApkPackaging)` |  Build-time properties for packaging native libraries (.so) inside a tested APK `[Component](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component)`.  
---|---  
  
* * *

Build-time properties for packaging native libraries (.so) inside a tested `[Component](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component)`.

This is accessed via `[TestedComponentPackaging.jniLibs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/TestedComponentPackaging#jniLibs\(\))`

## Summary

### Public properties  
  
---  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[testOnly](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/JniLibsTestedComponentPackaging#testOnly\(\))` The set of test-only patterns.  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.JniLibsPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/JniLibsPackaging) | `[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[excludes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/JniLibsPackaging#excludes\(\))` The set of excluded patterns.  
---|---  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[keepDebugSymbols](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/JniLibsPackaging#keepDebugSymbols\(\))` The set of patterns for native libraries that should not be stripped of debug symbols.  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[pickFirsts](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/JniLibsPackaging#pickFirsts\(\))` The set of patterns for which the first occurrence is packaged in the APK.  
  
## Public properties

### testOnly

Added in 8.4.0
    
    
    val [testOnly](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/JniLibsTestedComponentPackaging#testOnly\(\)): [SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The set of test-only patterns. Native libraries matching any of these patterns do not get packaged in the main APK or AAR, but they are included in the test APK.

Example: `packaging.jniLibs.testOnly.add("**`/`testOnly.so")`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
