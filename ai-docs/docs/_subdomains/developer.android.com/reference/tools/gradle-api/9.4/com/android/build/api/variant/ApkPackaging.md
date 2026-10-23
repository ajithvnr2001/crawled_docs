---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkPackaging/
title: ApkPackaging \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:58:26.015559+00:00
---

# ApkPackaging  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkPackaging/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ApkPackaging

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/ApkPackaging.kt+class:com.android.build.api.variant.ApkPackaging)

Added in 7.0.0
    
    
    interface [ApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkPackaging) : [Packaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Packaging)

Known direct subclasses 

[TestedApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestedApkPackaging)

`[TestedApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestedApkPackaging)` |  Build-time properties for packaging inside a tested APK `[Component](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Component)`.  
---|---  
  
* * *

Build-time properties for APK packaging inside a `[Component](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Component)`.

This is accessed via `[GeneratesApk.packaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApk#packaging\(\))`

## Summary

### Public properties  
  
---  
`[DexPackagingOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/DexPackagingOptions)` |  `[dex](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkPackaging#dex\(\))` PackagingOptions for dex files.  
`[JniLibsApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsApkPackaging)` |  `[jniLibs](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkPackaging#jniLibs\(\))` Packaging options for native libraries.  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.Packaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Packaging) | `[ResourcesPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ResourcesPackaging)` |  `[resources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Packaging#resources\(\))` Packaging options for java resources.  
---|---  
  
## Public properties

### dex

Added in 7.0.0
    
    
    val [dex](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkPackaging#dex\(\)): [DexPackagingOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/DexPackagingOptions)

PackagingOptions for dex files. Initialized from the corresponding DSL.

### jniLibs
    
    
    val [jniLibs](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkPackaging#jniLibs\(\)): [JniLibsApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsApkPackaging)

Packaging options for native libraries. Initialized from the corresponding DSL.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
