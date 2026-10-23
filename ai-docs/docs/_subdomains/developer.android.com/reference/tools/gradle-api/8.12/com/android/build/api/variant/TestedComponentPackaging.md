---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/TestedComponentPackaging/
title: TestedComponentPackaging \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:09:44.706037+00:00
---

# TestedComponentPackaging  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/TestedComponentPackaging/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestedComponentPackaging

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/TestedComponentPackaging.kt+class:com.android.build.api.variant.TestedComponentPackaging)

Added in 8.4.0
    
    
    interface [TestedComponentPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/TestedComponentPackaging) : [Packaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Packaging)

Known direct subclasses 

[TestedApkPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/TestedApkPackaging)

`[TestedApkPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/TestedApkPackaging)` |  Build-time properties for packaging inside a tested APK `[Component](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component)`.  
---|---  
  
* * *

Build-time properties for packaging inside a tested `[Component](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component)`.

## Summary

### Public properties  
  
---  
`[JniLibsTestedComponentPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/JniLibsTestedComponentPackaging)` |  `[jniLibs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/TestedComponentPackaging#jniLibs\(\))` Packaging options for native libraries.  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.Packaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Packaging) | `[ResourcesPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ResourcesPackaging)` |  `[resources](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Packaging#resources\(\))` Packaging options for java resources.  
---|---  
  
## Public properties

### jniLibs
    
    
    val [jniLibs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/TestedComponentPackaging#jniLibs\(\)): [JniLibsTestedComponentPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/JniLibsTestedComponentPackaging)

Packaging options for native libraries. Initialized from the corresponding DSL.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
