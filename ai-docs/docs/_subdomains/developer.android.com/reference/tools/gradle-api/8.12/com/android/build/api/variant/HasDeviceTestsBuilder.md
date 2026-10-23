---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasDeviceTestsBuilder/
title: HasDeviceTestsBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:08:02.839254+00:00
---

# HasDeviceTestsBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasDeviceTestsBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# HasDeviceTestsBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/HasDeviceTestsBuilder.kt+class:com.android.build.api.variant.HasDeviceTestsBuilder)

Added in 8.4.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [HasDeviceTestsBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasDeviceTestsBuilder)

Known direct subclasses 

[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ApplicationVariantBuilder), [DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DynamicFeatureVariantBuilder), [LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/LibraryVariantBuilder)

`[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ApplicationVariantBuilder)` |  Model for application components that only contains configuration-time properties that impacts the build flow.  
---|---  
`[DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DynamicFeatureVariantBuilder)` |  Model for dynamic feature components that only contains configuration-time properties that impacts the build flow.  
`[LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/LibraryVariantBuilder)` |  Model for library components that only contains configuration-time properties that impacts the build flow.  
  
Known indirect subclasses 

[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)

`[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)` |  Model for kotlin multiplatform library components that only contains configuration-time properties that impacts the build flow.  
---|---  
  
* * *

Interface that marks the potential existence of `[DeviceTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTest)` component on a `[Variant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant)`.

This is implemented by select subtypes of `[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantBuilder)`.

## Summary

### Public properties  
  
---  
`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [DeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTestBuilder)>` |  `[deviceTests](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasDeviceTestsBuilder#deviceTests\(\))` List of `[DeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTestBuilder)` for this variant.  
  
## Public properties

### deviceTests

Added in 8.4.0
    
    
    val [deviceTests](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasDeviceTestsBuilder#deviceTests\(\)): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [DeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTestBuilder)>

List of `[DeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTestBuilder)` for this variant.

The creation of `[DeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTestBuilder)` elements is handled by the AGP Plugin and there is no way to add or remove from the list as of now.

Returns  
---  
`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [DeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTestBuilder)>` |  a `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)` which keys are unique names within the tested variant like `[DeviceTestBuilder.ANDROID_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTestBuilder.Companion#ANDROID_TEST_TYPE\(\))` and the values are `[DeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTestBuilder)` for that host test suite.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
