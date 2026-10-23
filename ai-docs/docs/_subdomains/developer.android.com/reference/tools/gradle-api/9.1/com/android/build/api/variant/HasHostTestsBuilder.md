---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasHostTestsBuilder/
title: HasHostTestsBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:09:25.533949+00:00
---

# HasHostTestsBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasHostTestsBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# HasHostTestsBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/HasHostTestsBuilder.kt+class:com.android.build.api.variant.HasHostTestsBuilder)

Added in 8.5.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [HasHostTestsBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasHostTestsBuilder)

Known direct subclasses 

[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/ApplicationVariantBuilder), [DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DynamicFeatureVariantBuilder), [LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/LibraryVariantBuilder)

`[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/ApplicationVariantBuilder)` |  Model for application components that only contains configuration-time properties that impacts the build flow.  
---|---  
`[DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DynamicFeatureVariantBuilder)` |  Model for dynamic feature components that only contains configuration-time properties that impacts the build flow.  
`[LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/LibraryVariantBuilder)` |  Model for library components that only contains configuration-time properties that impacts the build flow.  
  
Known indirect subclasses 

[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)

`[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)` |  Model for kotlin multiplatform library components that only contains configuration-time properties that impacts the build flow.  
---|---  
  
* * *

Interface that marks the potential existence of `[HostTest](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HostTest)` components on a `[Variant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/Variant)`.

This is implemented by select subtypes of `[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantBuilder)`.

## Summary

### Public properties  
  
---  
`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [HostTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HostTestBuilder)>` |  `[hostTests](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasHostTestsBuilder#hostTests\(\))` Variant's `[HostTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HostTestBuilder)` configuration to turn on or off screenshot tests and set other screenshot test related settings.  
  
## Public properties

### hostTests

Added in 8.5.0
    
    
    val [hostTests](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasHostTestsBuilder#hostTests\(\)): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [HostTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HostTestBuilder)>

Variant's `[HostTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HostTestBuilder)` configuration to turn on or off screenshot tests and set other screenshot test related settings.

Returns  
---  
`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [HostTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HostTestBuilder)>` |  a `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)` which keys are unique names within the tested variant like `[HostTestBuilder.UNIT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HostTestBuilder.Companion#UNIT_TEST_TYPE\(\))` or `[HostTestBuilder.SCREENSHOT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HostTestBuilder.Companion#SCREENSHOT_TEST_TYPE\(\))` and the values are `[HostTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HostTestBuilder)` for that host test suite.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
