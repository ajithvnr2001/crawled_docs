---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidTestBuilder/
title: HasAndroidTestBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:00:14.896349+00:00
---

# HasAndroidTestBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidTestBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# HasAndroidTestBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/HasAndroidTestBuilder.kt+class:com.android.build.api.variant.HasAndroidTestBuilder)

Added in 7.0.0
    
    
    @[ReplacedByIncubating](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/annotations/ReplacedByIncubating)(message = "Replaced by the new interface HasDeviceTestsBuilder", bugId = 357083708)  
    interface [HasAndroidTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidTestBuilder)

Known direct subclasses 

[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApplicationVariantBuilder), [DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/DynamicFeatureVariantBuilder), [LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LibraryVariantBuilder)

`[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApplicationVariantBuilder)` |  Model for application components that only contains configuration-time properties that impacts the build flow.  
---|---  
`[DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/DynamicFeatureVariantBuilder)` |  Model for dynamic feature components that only contains configuration-time properties that impacts the build flow.  
`[LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LibraryVariantBuilder)` |  Model for library components that only contains configuration-time properties that impacts the build flow.  
  
Known indirect subclasses 

[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)

`[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)` |  Model for kotlin multiplatform library components that only contains configuration-time properties that impacts the build flow.  
---|---  
  
* * *

Interface that marks the potential existence of `[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidTest)` component on a `[Variant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Variant)`.

This is implemented by select subtypes of `[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantBuilder)`.

## Summary

### Public properties  
  
---  
`[AndroidTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidTestBuilder)` |  `[androidTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidTestBuilder#androidTest\(\))` Variant's `[AndroidTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidTestBuilder)` configuration to turn on or off android tests and set other android test related settings.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[androidTestEnabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidTestBuilder#androidTestEnabled\(\))` Set to `true` if the variant's has any android tests, false otherwise.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableAndroidTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidTestBuilder#enableAndroidTest\(\))` Set to `true` if the variant's has any android tests, false otherwise.  
  
## Public properties

### androidTest

Added in 8.3.1
    
    
    val [androidTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidTestBuilder#androidTest\(\)): [AndroidTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidTestBuilder)

Variant's `[AndroidTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidTestBuilder)` configuration to turn on or off android tests and set other android test related settings.

### androidTestEnabled

Added in 7.0.0
    
    
    var [androidTestEnabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidTestBuilder#androidTestEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Set to `true` if the variant's has any android tests, false otherwise. Value is Boolean#True by default.

### enableAndroidTest

Added in 7.0.0
    
    
    var [enableAndroidTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidTestBuilder#enableAndroidTest\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Set to `true` if the variant's has any android tests, false otherwise. Value is Boolean#True by default.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
