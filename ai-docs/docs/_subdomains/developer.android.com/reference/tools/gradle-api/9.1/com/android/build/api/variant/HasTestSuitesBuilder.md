---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasTestSuitesBuilder/
title: HasTestSuitesBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:09:33.736808+00:00
---

# HasTestSuitesBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasTestSuitesBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# HasTestSuitesBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/HasTestSuitesBuilder.kt+class:com.android.build.api.variant.HasTestSuitesBuilder)

Added in 9.1.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [HasTestSuitesBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasTestSuitesBuilder)

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

Container of `[TestSuiteBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/TestSuiteBuilder)`

## Summary

### Public properties  
  
---  
`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [TestSuiteBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/TestSuiteBuilder)>` |  `[suites](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasTestSuitesBuilder#suites\(\))` Variant's `[TestSuiteBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/TestSuiteBuilder)` configuration to configure test suites associated with this variant.  
  
## Public properties

### suites

Added in 9.1.1
    
    
    val [suites](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasTestSuitesBuilder#suites\(\)): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [TestSuiteBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/TestSuiteBuilder)>

Variant's `[TestSuiteBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/TestSuiteBuilder)` configuration to configure test suites associated with this variant.

Returns  
---  
`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [TestSuiteBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/TestSuiteBuilder)>` |  a `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)` which keys are unique names within the test suites  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-13 UTC."],[],[]] 
