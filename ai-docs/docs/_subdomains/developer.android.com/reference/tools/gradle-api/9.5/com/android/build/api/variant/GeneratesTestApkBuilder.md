---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/GeneratesTestApkBuilder/
title: GeneratesTestApkBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:18:24.349376+00:00
---

# GeneratesTestApkBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/GeneratesTestApkBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# GeneratesTestApkBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/GeneratesTestApkBuilder.kt+class:com.android.build.api.variant.GeneratesTestApkBuilder)

Added in 8.8.0
    
    
    interface [GeneratesTestApkBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/GeneratesTestApkBuilder) : [GeneratesApkBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/GeneratesApkBuilder)

Known direct subclasses 

[DeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/DeviceTestBuilder)

`[DeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/DeviceTestBuilder)` |  Interface to turn tests on devices, `AndroidTest` being an example of device tests.  
---|---  
  
Known indirect subclasses 

[AndroidTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidTestBuilder)

`[AndroidTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidTestBuilder)` |   
---|---  
  
* * *

Configuration-time properties `[ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ComponentBuilder)` that produce Test APKs.

## Summary

### Inherited properties  
  
---  
From [com.android.build.api.variant.GeneratesApkBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/GeneratesApkBuilder) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[debuggable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/GeneratesApkBuilder#debuggable\(\))` Sets the APK debuggable flag.  
---|---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[enableMultiDex](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/GeneratesApkBuilder#enableMultiDex\(\))` Sets whether multi-dex is enabled for this variant.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/GeneratesApkBuilder#targetSdk\(\))` Sets the target SDK Version for this variant as an integer API level.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/GeneratesApkBuilder#targetSdkPreview\(\))` Sets the target SDK Version for this variant as an integer API level.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
