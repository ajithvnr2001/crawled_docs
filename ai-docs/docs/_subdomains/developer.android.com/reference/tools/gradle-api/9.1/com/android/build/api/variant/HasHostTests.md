---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasHostTests/
title: HasHostTests \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:09:23.110728+00:00
---

# HasHostTests  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasHostTests/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# HasHostTests

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/HasHostTests.kt+class:com.android.build.api.variant.HasHostTests)

Added in 8.5.0
    
    
    interface [HasHostTests](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasHostTests)

Known direct subclasses 

[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/ApplicationVariant), [LibraryVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/LibraryVariant)

`[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/ApplicationVariant)` |  Model for application components that only contains build-time properties.  
---|---  
`[LibraryVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/LibraryVariant)` |  Model for library components that only contains build-time properties.  
  
Known indirect subclasses 

[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)

`[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)` |  Properties for the main Variant of a kotlin multiplatform android library  
---|---  
  
* * *

`[Variant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/Variant)` that optionally have `[HostTest](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HostTest)` components like `[UnitTest](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/UnitTest)`.

## Summary

### Public properties  
  
---  
`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [HostTest](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HostTest)>` |  `[hostTests](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasHostTests#hostTests\(\))` `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)` of Variant's `[HostTest](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HostTest)`, or empty if all host tests (like unit test) for this variant are disabled.  
  
## Public properties

### hostTests

Added in 8.5.0
    
    
    val [hostTests](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasHostTests#hostTests\(\)): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [HostTest](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HostTest)>

`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)` of Variant's `[HostTest](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HostTest)`, or empty if all host tests (like unit test) for this variant are disabled. Map keys are the `[HostTest](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HostTest)` name, like HasHostTestsBuilder.UNIT_TEST_TYPE or HasHostTestsBuilder.SCREENSHOT_TEST_TYPE for default host tests.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
