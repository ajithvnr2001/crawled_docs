---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HasUnitTestBuilder/
title: HasUnitTestBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:18:59.606714+00:00
---

# HasUnitTestBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HasUnitTestBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# HasUnitTestBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/HasUnitTestBuilder.kt+class:com.android.build.api.variant.HasUnitTestBuilder)

Added in 8.1.0
    
    
    interface [HasUnitTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HasUnitTestBuilder)

Known direct subclasses 

[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ApplicationVariantBuilder), [DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/DynamicFeatureVariantBuilder), [LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/LibraryVariantBuilder)

`[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ApplicationVariantBuilder)` |  Model for application components that only contains configuration-time properties that impacts the build flow.  
---|---  
`[DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/DynamicFeatureVariantBuilder)` |  Model for dynamic feature components that only contains configuration-time properties that impacts the build flow.  
`[LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/LibraryVariantBuilder)` |  Model for library components that only contains configuration-time properties that impacts the build flow.  
  
Known indirect subclasses 

[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)

`[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)` |  Model for kotlin multiplatform library components that only contains configuration-time properties that impacts the build flow.  
---|---  
  
* * *

Interface that marks the potential existence of `[UnitTest](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/UnitTest)` component on a `[Variant](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/Variant)`.

This is implemented by select subtypes of `[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantBuilder)`.

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableUnitTest](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HasUnitTestBuilder#enableUnitTest\(\))` Set to `true` if the variant's has any unit tests, false otherwise.  
  
## Public properties

### enableUnitTest

Added in 8.1.0
    
    
    var [enableUnitTest](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HasUnitTestBuilder#enableUnitTest\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Set to `true` if the variant's has any unit tests, false otherwise. Value is Boolean#True by default.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
