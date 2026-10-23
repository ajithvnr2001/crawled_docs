---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DexPackaging/
title: DexPackaging \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:58:10.412780+00:00
---

# DexPackaging  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DexPackaging/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DexPackaging

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/DexPackaging.kt+class:com.android.build.api.dsl.DexPackaging)

Added in 8.0.2
    
    
    interface [DexPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DexPackaging)

* * *

Packaging options for Dex (Android Dalvik Executable) files in the Android DSL
    
    
    android {  
        packaging {  
            dex {  
                useLegacyPackaging = ...  
            }  
        }  
    }

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[useLegacyPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DexPackaging#useLegacyPackaging\(\))` Whether to use the legacy convention of compressing all dex files in the APK.  
  
## Public properties

### useLegacyPackaging

Added in 8.0.2
    
    
    var [useLegacyPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DexPackaging#useLegacyPackaging\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Whether to use the legacy convention of compressing all dex files in the APK. If null, dex files will be uncompressed when minSdk >= 28.

This property does not affect dex file compression in APKs produced from app bundles.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
