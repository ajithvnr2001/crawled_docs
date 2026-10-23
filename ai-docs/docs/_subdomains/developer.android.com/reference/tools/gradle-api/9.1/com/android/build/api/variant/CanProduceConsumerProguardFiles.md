---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/CanProduceConsumerProguardFiles/
title: CanProduceConsumerProguardFiles \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:08:11.114347+00:00
---

# CanProduceConsumerProguardFiles  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/CanProduceConsumerProguardFiles/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# CanProduceConsumerProguardFiles

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/CanProduceConsumerProguardFiles.kt+class:com.android.build.api.variant.CanProduceConsumerProguardFiles)

Added in 9.1.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [CanProduceConsumerProguardFiles](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/CanProduceConsumerProguardFiles)

Known direct subclasses 

[LibraryVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/LibraryVariant)

`[LibraryVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/LibraryVariant)` |  Model for library components that only contains build-time properties.  
---|---  
  
Known indirect subclasses 

[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)

`[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)` |  Properties for the main Variant of a kotlin multiplatform android library  
---|---  
  
* * *

Component that optionally produces consumer proguard files.

## Summary

### Public properties  
  
---  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>` |  `[consumerProguardFiles](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/CanProduceConsumerProguardFiles#consumerProguardFiles\(\))` The collection of proguard rule files for consumers of the library to use.  
  
## Public properties

### consumerProguardFiles

Added in 9.1.1
    
    
    val [consumerProguardFiles](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/CanProduceConsumerProguardFiles#consumerProguardFiles\(\)): [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>

The collection of proguard rule files for consumers of the library to use. The list is initialized from the corresponding DSL element, and cannot be queried at configuration time. At configuration time, you can only add new elements to the list.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-13 UTC."],[],[]] 
