---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk/
title: GeneratesApk \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:24:25.282090+00:00
---

# GeneratesApk  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# GeneratesApk

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/GeneratesApk.kt+class:com.android.build.api.variant.GeneratesApk)

Added in 7.0.0
    
    
    interface [GeneratesApk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk)

Known direct subclasses 

[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApplicationVariant), [DynamicFeatureVariant](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DynamicFeatureVariant), [GeneratesTestApk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesTestApk)

`[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApplicationVariant)` |  Model for application components that only contains build-time properties.  
---|---  
`[DynamicFeatureVariant](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DynamicFeatureVariant)` |  Model for dynamic feature components that only contains build-time properties.  
`[GeneratesTestApk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesTestApk)` |  Build-time properties for `[Component](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Component)` that produce test APKs.  
  
Known indirect subclasses 

[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/AndroidTest), [DeviceTest](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceTest), [TestVariant](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestVariant)

`[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/AndroidTest)` |  Model for Android Test components that contains build-time properties  
---|---  
`[DeviceTest](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceTest)` |  Model for Device Test components that contains build-time properties  
`[TestVariant](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestVariant)` |  Model for test components that only contains build-time properties.  
  
* * *

Build-time properties for `[Component](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Component)` that produce APKs.

## Summary

### Public properties  
  
---  
`[AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/AndroidResources)` |  `[androidResources](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk#androidResources\(\))` Variant's android resources processing configuration, initialized by the corresponding global DSL element.  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[applicationId](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk#applicationId\(\))` Variant's application ID as present in the final manifest file of the APK.  
`[Dexing](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Dexing)` |  `[dexing](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk#dexing\(\))` Variant's specific dexing options  
`[AndroidVersion](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/AndroidVersion)` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk#minSdk\(\))` Min SDK version for this variant  
`[ApkOutputProviders](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApkOutputProviders)` |  `[outputProviders](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk#outputProviders\(\))` Provides access to built artifacts output(e.g. APK) produced by this Variant.  
`[ApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApkPackaging)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk#packaging\(\))` Variant's packagingOptions, initialized by the corresponding global DSL element.  
`[Renderscript](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Renderscript)?` |  `[renderscript](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk#renderscript\(\))` Variant specific settings for the renderscript compiler.  
`[AndroidVersion](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/AndroidVersion)` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk#targetSdk\(\))` Target SDK version for this variant.  
  
## Public properties

### androidResources

Added in 7.0.0
    
    
    val [androidResources](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk#androidResources\(\)): [AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/AndroidResources)

Variant's android resources processing configuration, initialized by the corresponding global DSL element.

### applicationId

Added in 7.0.0
    
    
    val [applicationId](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk#applicationId\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Variant's application ID as present in the final manifest file of the APK.

### dexing

Added in 8.3.1
    
    
    val [dexing](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk#dexing\(\)): [Dexing](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Dexing)

Variant's specific dexing options

### minSdk

Added in 8.8.0
    
    
    val [minSdk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk#minSdk\(\)): [AndroidVersion](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/AndroidVersion)

Min SDK version for this variant

### outputProviders

Added in 8.9.0
    
    
    val [outputProviders](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk#outputProviders\(\)): [ApkOutputProviders](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApkOutputProviders)

Provides access to built artifacts output(e.g. APK) produced by this Variant.

### packaging

Added in 7.0.0
    
    
    val [packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk#packaging\(\)): [ApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApkPackaging)

Variant's packagingOptions, initialized by the corresponding global DSL element.

### renderscript

Added in 7.0.0
    
    
    val [renderscript](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk#renderscript\(\)): [Renderscript](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Renderscript)?

Variant specific settings for the renderscript compiler. This will return null when `[com.android.build.api.dsl.BuildFeatures.renderScript](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BuildFeatures#renderScript\(\))` is false.

### targetSdk

Added in 8.1.0
    
    
    val [targetSdk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/GeneratesApk#targetSdk\(\)): [AndroidVersion](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/AndroidVersion)

Target SDK version for this variant.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-09-11 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-11 UTC."],[],[]] 
