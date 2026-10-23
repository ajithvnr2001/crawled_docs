---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestedApkPackaging/
title: TestedApkPackaging \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:02:55.781647+00:00
---

# TestedApkPackaging  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestedApkPackaging/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestedApkPackaging

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/TestedApkPackaging.kt+class:com.android.build.api.variant.TestedApkPackaging)

Added in 8.4.0
    
    
    interface [TestedApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestedApkPackaging) : [TestedComponentPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestedComponentPackaging), [ApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkPackaging)

* * *

Build-time properties for packaging inside a tested APK `[Component](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Component)`.

## Summary

### Public properties  
  
---  
`[JniLibsTestedApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsTestedApkPackaging)` |  `[jniLibs](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestedApkPackaging#jniLibs\(\))` Packaging options for native libraries.  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.ApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkPackaging) | `[DexPackagingOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/DexPackagingOptions)` |  `[dex](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkPackaging#dex\(\))` PackagingOptions for dex files.  
---|---  
  
From [com.android.build.api.variant.Packaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Packaging) | `[ResourcesPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ResourcesPackaging)` |  `[resources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Packaging#resources\(\))` Packaging options for java resources.  
---|---  
  
## Public properties

### jniLibs
    
    
    val [jniLibs](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestedApkPackaging#jniLibs\(\)): [JniLibsTestedApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JniLibsTestedApkPackaging)

Packaging options for native libraries. Initialized from the corresponding DSL.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
