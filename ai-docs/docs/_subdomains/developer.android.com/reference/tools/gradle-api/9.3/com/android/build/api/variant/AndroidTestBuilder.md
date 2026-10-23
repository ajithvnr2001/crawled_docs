---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidTestBuilder/
title: AndroidTestBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:34:05.018435+00:00
---

# AndroidTestBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidTestBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AndroidTestBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/AndroidTestBuilder.kt+class:com.android.build.api.variant.AndroidTestBuilder)

Added in 8.3.1
    
    
    interface [AndroidTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidTestBuilder) : [DeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DeviceTestBuilder)

* * *

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enable](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidTestBuilder#enable\(\))` Set to `true` if the variant's has any android tests, false otherwise.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[enableMultiDex](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidTestBuilder#enableMultiDex\(\))` Sets whether multi-dex is enabled for this variant.  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.DeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DeviceTestBuilder) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableCodeCoverage](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DeviceTestBuilder#enableCodeCoverage\(\))` Specifies host test code coverage data collection by configuring the JacocoPlugin.  
---|---  
  
From [com.android.build.api.variant.GeneratesApkBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/GeneratesApkBuilder) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[debuggable](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/GeneratesApkBuilder#debuggable\(\))` Sets the APK debuggable flag.  
---|---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/GeneratesApkBuilder#targetSdk\(\))` Sets the target SDK Version for this variant as an integer API level.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/GeneratesApkBuilder#targetSdkPreview\(\))` Sets the target SDK Version for this variant as an integer API level.  
  
## Public properties

### enable

Added in 8.3.1
    
    
    var [enable](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidTestBuilder#enable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Set to `true` if the variant's has any android tests, false otherwise. Value is Boolean#True by default.

### enableMultiDex

Added in 8.3.1

Deprecated in 8.3.1
    
    
    var [enableMultiDex](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidTestBuilder#enableMultiDex\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Sets whether multi-dex is enabled for this variant.

This can be null, in which case the default value is used.

It is not safe to read the value of this property as other plugins that were applied later can change this value so there is no guarantee you would get the final value. To get the final value, use the `[AndroidComponentsExtension.onVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` API :
    
    
    onVariants { variant ->  
      variant.dexing.isMultiDexEnabled  
    }

Note the a `[RuntimeException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/RuntimeException.html)` will be thrown at Runtime if a java or groovy code tries to read the property value.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
