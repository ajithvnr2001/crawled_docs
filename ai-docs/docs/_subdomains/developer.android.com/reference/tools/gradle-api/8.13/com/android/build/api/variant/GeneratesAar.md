---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/GeneratesAar/
title: GeneratesAar \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:39:05.705902+00:00
---

# GeneratesAar  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/GeneratesAar/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# GeneratesAar

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/GeneratesAar.kt+class:com.android.build.api.variant.GeneratesAar)

Added in 7.0.0
    
    
    interface [GeneratesAar](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/GeneratesAar)

Known direct subclasses 

[LibraryVariant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/LibraryVariant), [TestFixtures](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/TestFixtures)

`[LibraryVariant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/LibraryVariant)` |  Model for library components that only contains build-time properties.  
---|---  
`[TestFixtures](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/TestFixtures)` |  Model for Test Fixtures components that contains build-time properties  
  
Known indirect subclasses 

[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)

`[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)` |  Properties for the main Variant of a kotlin multiplatform android library  
---|---  
  
* * *

Build-time properties for `[Component](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Component)` that generate AARs.

## Summary

### Public properties  
  
---  
`[AarMetadata](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AarMetadata)` |  `[aarMetadata](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/GeneratesAar#aarMetadata\(\))` Variant's aar metadata, initialized by merging the corresponding `[com.android.build.api.dsl.AarMetadata](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AarMetadata)` DSL elements.  
  
## Public properties

### aarMetadata

Added in 7.0.0
    
    
    val [aarMetadata](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/GeneratesAar#aarMetadata\(\)): [AarMetadata](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AarMetadata)

Variant's aar metadata, initialized by merging the corresponding `[com.android.build.api.dsl.AarMetadata](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AarMetadata)` DSL elements.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
