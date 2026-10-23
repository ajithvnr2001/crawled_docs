---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/CanMinifyAndroidResources/
title: CanMinifyAndroidResources \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:17:14.594939+00:00
---

# CanMinifyAndroidResources  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/CanMinifyAndroidResources/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# CanMinifyAndroidResources

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/CanMinifyAndroidResources.kt+class:com.android.build.api.variant.CanMinifyAndroidResources)

Added in 7.4.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [CanMinifyAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/CanMinifyAndroidResources)

Known direct subclasses 

[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ApplicationVariant)

`[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ApplicationVariant)` |  Model for application components that only contains build-time properties.  
---|---  
  
* * *

Build-time properties for `[Component](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/Component)` that can minify Android resources.

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[shrinkResources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/CanMinifyAndroidResources#shrinkResources\(\))` Specifies whether resources will be shrinked.  
  
## Public properties

### shrinkResources

Added in 7.4.0
    
    
    val [shrinkResources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/CanMinifyAndroidResources#shrinkResources\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Specifies whether resources will be shrinked. At this point the value is final. You can change it via `[AndroidComponentsExtension.beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` and `[CanMinifyAndroidResourcesBuilder.shrinkResources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/CanMinifyAndroidResourcesBuilder#shrinkResources\(\))`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
