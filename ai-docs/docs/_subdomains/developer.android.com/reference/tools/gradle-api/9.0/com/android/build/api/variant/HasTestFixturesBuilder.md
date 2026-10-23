---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/HasTestFixturesBuilder/
title: HasTestFixturesBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:24:52.705845+00:00
---

# HasTestFixturesBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/HasTestFixturesBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# HasTestFixturesBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/HasTestFixturesBuilder.kt+class:com.android.build.api.variant.HasTestFixturesBuilder)

Added in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [HasTestFixturesBuilder](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/HasTestFixturesBuilder)

Known direct subclasses 

[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApplicationVariantBuilder), [DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DynamicFeatureVariantBuilder), [LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/LibraryVariantBuilder)

`[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApplicationVariantBuilder)` |  Model for application components that only contains configuration-time properties that impacts the build flow.  
---|---  
`[DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DynamicFeatureVariantBuilder)` |  Model for dynamic feature components that only contains configuration-time properties that impacts the build flow.  
`[LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/LibraryVariantBuilder)` |  Model for library components that only contains configuration-time properties that impacts the build flow.  
  
Known indirect subclasses 

[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)

`[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)` |  Model for kotlin multiplatform library components that only contains configuration-time properties that impacts the build flow.  
---|---  
  
* * *

Interface that marks the potential existence of `[TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestFixtures)` component on a `[Variant](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Variant)`.

This is implemented by select subtypes of `[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/VariantBuilder)`.

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableTestFixtures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/HasTestFixturesBuilder#enableTestFixtures\(\))` Set to `true` if the variant's has test fixtures, `false` otherwise.  
  
## Public properties

### enableTestFixtures

Added in 7.1.0
    
    
    var [enableTestFixtures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/HasTestFixturesBuilder#enableTestFixtures\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Set to `true` if the variant's has test fixtures, `false` otherwise.

Default value will match `[com.android.build.api.dsl.TestFixtures.enable](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestFixtures#enable\(\))` value that is set through the extension via `[com.android.build.api.dsl.TestedExtension.testFixtures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestedExtension#testFixtures\(kotlin.Function1\))`.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
