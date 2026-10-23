---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder/
title: GeneratesApkBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:00:03.104934+00:00
---

# GeneratesApkBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# GeneratesApkBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/GeneratesApkBuilder.kt+class:com.android.build.api.variant.GeneratesApkBuilder)

Added in 7.4.0
    
    
    interface [GeneratesApkBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder)

Known direct subclasses 

[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApplicationVariantBuilder), [DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/DynamicFeatureVariantBuilder), [GeneratesTestApkBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesTestApkBuilder), [TestVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestVariantBuilder)

`[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApplicationVariantBuilder)` |  Model for application components that only contains configuration-time properties that impacts the build flow.  
---|---  
`[DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/DynamicFeatureVariantBuilder)` |  Model for dynamic feature components that only contains configuration-time properties that impacts the build flow.  
`[GeneratesTestApkBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesTestApkBuilder)` |  Configuration-time properties `[ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentBuilder)` that produce Test APKs.  
`[TestVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestVariantBuilder)` |  Model for test components that only contains configuration-time properties that impacts the build flow.  
  
Known indirect subclasses 

[AndroidTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidTestBuilder), [DeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/DeviceTestBuilder)

`[AndroidTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidTestBuilder)` |   
---|---  
`[DeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/DeviceTestBuilder)` |  Interface to turn tests on devices, `AndroidTest` being an example of device tests.  
  
* * *

Configuration-time properties `[ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentBuilder)` that produce APKs.

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[debuggable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder#debuggable\(\))` Sets the APK debuggable flag.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[enableMultiDex](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder#enableMultiDex\(\))` Sets whether multi-dex is enabled for this variant.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder#targetSdk\(\))` Sets the target SDK Version for this variant as an integer API level.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder#targetSdkPreview\(\))` Sets the target SDK Version for this variant as an integer API level.  
  
## Public properties

### debuggable

Added in 8.10.1

Deprecated in 8.10.1
    
    
    var [debuggable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder#debuggable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Sets the APK debuggable flag.

### enableMultiDex

Added in 8.3.1

Deprecated in 8.3.1
    
    
    var [enableMultiDex](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder#enableMultiDex\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Sets whether multi-dex is enabled for this variant.

This can be null, in which case the default value is used.

It is not safe to read the value of this property as other plugins that were applied later can change this value so there is no guarantee you would get the final value. To get the final value, use the `[AndroidComponentsExtension.onVariants](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` API :
    
    
    onVariants { variant ->  
      variant.dexing.isMultiDexEnabled  
    }

Note the a `[RuntimeException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/RuntimeException.html)` will be thrown at Runtime if a java or groovy code tries to read the property value.

### targetSdk

Added in 7.4.0
    
    
    var [targetSdk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder#targetSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Sets the target SDK Version for this variant as an integer API level. Setting this will override previous calls of `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder#targetSdk\(\))` and `[targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder#targetSdkPreview\(\))` setters. Only one of `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder#targetSdk\(\))` and `[targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder#targetSdkPreview\(\))` should be set.

It is not safe to read this value. Use `[GeneratesApk.targetSdk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApk#targetSdk\(\))` instead.

### targetSdkPreview

Added in 7.4.0
    
    
    var [targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder#targetSdkPreview\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Sets the target SDK Version for this variant as an integer API level. Setting this will override previous calls of `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder#targetSdk\(\))` and `[targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder#targetSdkPreview\(\))` setters. Only one of `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder#targetSdk\(\))` and `[targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApkBuilder#targetSdkPreview\(\))` should be set.

It is not safe to read this value. Use `[GeneratesApk.targetSdk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApk#targetSdk\(\))` instead.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
