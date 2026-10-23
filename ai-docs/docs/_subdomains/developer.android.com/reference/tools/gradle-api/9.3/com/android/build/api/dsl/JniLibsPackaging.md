---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JniLibsPackaging/
title: JniLibsPackaging \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:29:39.911075+00:00
---

# JniLibsPackaging  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JniLibsPackaging/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# JniLibsPackaging

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/JniLibsPackaging.kt+class:com.android.build.api.dsl.JniLibsPackaging)

Added in 8.0.2
    
    
    interface [JniLibsPackaging](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JniLibsPackaging)

* * *

Packaging options for native library (.so) files in the Android DSL
    
    
    android {  
        packaging {  
            jniLibs {  
                excludes += ...  
            }  
        }  
    }

## Summary

### Public properties  
  
---  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[excludes](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JniLibsPackaging#excludes\(\))` The set of excluded patterns.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[keepDebugSymbols](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JniLibsPackaging#keepDebugSymbols\(\))` The set of patterns for native libraries that should not be stripped of debug symbols.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[pickFirsts](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JniLibsPackaging#pickFirsts\(\))` The set of patterns where the first occurrence is packaged in the APK.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[testOnly](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JniLibsPackaging#testOnly\(\))` The set of test-only patterns.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[useLegacyPackaging](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JniLibsPackaging#useLegacyPackaging\(\))` Whether to use the legacy convention of compressing all .so files in the APK.  
  
## Public properties

### excludes

Added in 8.0.2
    
    
    val [excludes](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JniLibsPackaging#excludes\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The set of excluded patterns. Native libraries matching any of these patterns do not get packaged.

Example: `android.packagingOptions.jniLibs.excludes += "**`/`exclude.so"`

### keepDebugSymbols

Added in 8.0.2
    
    
    val [keepDebugSymbols](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JniLibsPackaging#keepDebugSymbols\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The set of patterns for native libraries that should not be stripped of debug symbols.

Example: `android.packagingOptions.jniLibs.keepDebugSymbols += "**`/`doNotStrip.so"`

### pickFirsts

Added in 8.0.2
    
    
    val [pickFirsts](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JniLibsPackaging#pickFirsts\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The set of patterns where the first occurrence is packaged in the APK. For each native library APK entry path matching one of these patterns, only the first native library found with that path gets packaged.

Example: `android.packagingOptions.jniLibs.pickFirsts += "**`/`pickFirst.so"`

### testOnly

Added in 8.4.0
    
    
    val [testOnly](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JniLibsPackaging#testOnly\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The set of test-only patterns. Native libraries matching any of these patterns do not get packaged in the main APK or AAR, but they are included in the test APK.

Example: `android.packaging.jniLibs.testOnly += "**`/`testOnly.so"`

### useLegacyPackaging

Added in 8.0.2
    
    
    var [useLegacyPackaging](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JniLibsPackaging#useLegacyPackaging\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Whether to use the legacy convention of compressing all .so files in the APK. If null, .so files will be uncompressed and page-aligned when minSdk >= 23.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
