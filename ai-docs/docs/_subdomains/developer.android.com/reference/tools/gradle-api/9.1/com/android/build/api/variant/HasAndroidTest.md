---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasAndroidTest/
title: HasAndroidTest \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:09:12.449635+00:00
---

# HasAndroidTest  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasAndroidTest/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# HasAndroidTest

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/HasAndroidTest.kt+class:com.android.build.api.variant.HasAndroidTest)

Added in 7.1.0
    
    
    interface [HasAndroidTest](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasAndroidTest)

Known direct subclasses 

[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/ApplicationVariant), [DynamicFeatureVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DynamicFeatureVariant), [LibraryVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/LibraryVariant)

`[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/ApplicationVariant)` |  Model for application components that only contains build-time properties.  
---|---  
`[DynamicFeatureVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DynamicFeatureVariant)` |  Model for dynamic feature components that only contains build-time properties.  
`[LibraryVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/LibraryVariant)` |  Model for library components that only contains build-time properties.  
  
Known indirect subclasses 

[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)

`[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)` |  Properties for the main Variant of a kotlin multiplatform android library  
---|---  
  
* * *

`[Variant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/Variant)` that optionally have `[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidTest)` component.

## Summary

### Public properties  
  
---  
`[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidTest)?` |  `[androidTest](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasAndroidTest#androidTest\(\))` Variant's `[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidTest)` configuration, or null if android tests are disabled for this variant.  
`[TestedComponentPackaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/TestedComponentPackaging)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasAndroidTest#packaging\(\))` Variant's packagingOptions, initialized by the corresponding global DSL element.  
  
## Public properties

### androidTest

Added in 7.1.0
    
    
    val [androidTest](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasAndroidTest#androidTest\(\)): [AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidTest)?

Variant's `[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidTest)` configuration, or null if android tests are disabled for this variant.

### packaging

Added in 8.4.0
    
    
    val [packaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasAndroidTest#packaging\(\)): [TestedComponentPackaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/TestedComponentPackaging)

Variant's packagingOptions, initialized by the corresponding global DSL element.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
