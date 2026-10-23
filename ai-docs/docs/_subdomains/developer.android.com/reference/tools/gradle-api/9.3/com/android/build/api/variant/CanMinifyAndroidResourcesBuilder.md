---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/CanMinifyAndroidResourcesBuilder/
title: CanMinifyAndroidResourcesBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:34:53.502889+00:00
---

# CanMinifyAndroidResourcesBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/CanMinifyAndroidResourcesBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# CanMinifyAndroidResourcesBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/CanMinifyAndroidResourcesBuilder.kt+class:com.android.build.api.variant.CanMinifyAndroidResourcesBuilder)

Added in 7.4.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [CanMinifyAndroidResourcesBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/CanMinifyAndroidResourcesBuilder)

Known direct subclasses 

[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ApplicationVariantBuilder)

`[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ApplicationVariantBuilder)` |  Model for application components that only contains configuration-time properties that impacts the build flow.  
---|---  
  
* * *

Interface for component builder that can shrink resources

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[shrinkResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/CanMinifyAndroidResourcesBuilder#shrinkResources\(\))` Specifies whether resources will be shrinked  
  
## Public properties

### shrinkResources

Added in 7.4.0
    
    
    var [shrinkResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/CanMinifyAndroidResourcesBuilder#shrinkResources\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Specifies whether resources will be shrinked

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
