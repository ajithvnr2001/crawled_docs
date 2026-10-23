---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasTestFixtures/
title: HasTestFixtures \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:53:45.648722+00:00
---

# HasTestFixtures  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasTestFixtures/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# HasTestFixtures

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/HasTestFixtures.kt+class:com.android.build.api.variant.HasTestFixtures)

Added in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [HasTestFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasTestFixtures)

Known direct subclasses 

[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApplicationVariant), [DynamicFeatureVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DynamicFeatureVariant), [LibraryVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/LibraryVariant)

`[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApplicationVariant)` |  Model for application components that only contains build-time properties.  
---|---  
`[DynamicFeatureVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DynamicFeatureVariant)` |  Model for dynamic feature components that only contains build-time properties.  
`[LibraryVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/LibraryVariant)` |  Model for library components that only contains build-time properties.  
  
Known indirect subclasses 

[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)

`[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)` |  Properties for the main Variant of a kotlin multiplatform android library  
---|---  
  
* * *

`[Variant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant)` that optionally have `[TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestFixtures)` component.

## Summary

### Public properties  
  
---  
`[TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestFixtures)?` |  `[testFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasTestFixtures#testFixtures\(\))` Variant's `[TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestFixtures)`, or null if the test fixtures for this variant are disabled.  
  
## Public properties

### testFixtures

Added in 7.1.0
    
    
    val [testFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasTestFixtures#testFixtures\(\)): [TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestFixtures)?

Variant's `[TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestFixtures)`, or null if the test fixtures for this variant are disabled.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
