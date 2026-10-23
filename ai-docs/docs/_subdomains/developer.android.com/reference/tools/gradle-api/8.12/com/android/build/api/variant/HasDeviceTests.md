---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasDeviceTests/
title: HasDeviceTests \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:08:00.395999+00:00
---

# HasDeviceTests  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasDeviceTests/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# HasDeviceTests

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/HasDeviceTests.kt+class:com.android.build.api.variant.HasDeviceTests)

Added in 8.4.0
    
    
    interface [HasDeviceTests](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasDeviceTests)

Known direct subclasses 

[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ApplicationVariant), [DynamicFeatureVariant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DynamicFeatureVariant), [LibraryVariant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/LibraryVariant)

`[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ApplicationVariant)` |  Model for application components that only contains build-time properties.  
---|---  
`[DynamicFeatureVariant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DynamicFeatureVariant)` |  Model for dynamic feature components that only contains build-time properties.  
`[LibraryVariant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/LibraryVariant)` |  Model for library components that only contains build-time properties.  
  
Known indirect subclasses 

[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)

`[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)` |  Properties for the main Variant of a kotlin multiplatform android library  
---|---  
  
* * *

`[Variant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant)` that optionally have `[DeviceTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTest)` components like `[AndroidTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AndroidTest)`.

## Summary

### Public properties  
  
---  
`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [DeviceTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTest)>` |  `[deviceTests](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasDeviceTests#deviceTests\(\))` Variant's `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)` of `[DeviceTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTest)` configurations, or empty if all devices tests (like android tests) are disabled for this variant.  
  
## Public properties

### deviceTests

Added in 8.4.0
    
    
    val [deviceTests](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasDeviceTests#deviceTests\(\)): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [DeviceTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTest)>

Variant's `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)` of `[DeviceTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTest)` configurations, or empty if all devices tests (like android tests) are disabled for this variant.

Returns  
---  
`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [DeviceTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTest)>` |  a `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)` which keys are unique names within the tested variant like `[DeviceTestBuilder.ANDROID_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTestBuilder.Companion#ANDROID_TEST_TYPE\(\))` and the values are `[DeviceTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTest)` for that host test suite.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
