---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidResources/
title: HasAndroidResources \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:00:10.067249+00:00
---

# HasAndroidResources  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidResources/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# HasAndroidResources

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/HasAndroidResources.kt+class:com.android.build.api.variant.HasAndroidResources)

Added in 7.0.0
    
    
    interface [HasAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidResources)

Known direct subclasses 

[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidTest), [DeviceTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/DeviceTest), [TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestFixtures), [Variant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Variant)

`[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidTest)` |  Model for Android Test components that contains build-time properties  
---|---  
`[DeviceTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/DeviceTest)` |  Model for Device Test components that contains build-time properties  
`[TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestFixtures)` |  Model for Test Fixtures components that contains build-time properties  
`[Variant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Variant)` |  Model for variant components that only contains build-time properties  
  
Known indirect subclasses 

[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidTest), [ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApplicationVariant), [DynamicFeatureVariant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/DynamicFeatureVariant), [KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/KotlinMultiplatformAndroidVariant), [LibraryVariant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LibraryVariant), [TestVariant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestVariant)

`[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidTest)` |  Model for Android Test components that contains build-time properties  
---|---  
`[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApplicationVariant)` |  Model for application components that only contains build-time properties.  
`[DynamicFeatureVariant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/DynamicFeatureVariant)` |  Model for dynamic feature components that only contains build-time properties.  
`[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)` |  Properties for the main Variant of a kotlin multiplatform android library  
`[LibraryVariant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LibraryVariant)` |  Model for library components that only contains build-time properties.  
`[TestVariant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestVariant)` |  Model for test components that only contains build-time properties.  
  
* * *

Build-time properties for `[Component](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Component)` that have Android resources.

## Summary

### Public functions  
  
---  
`[ResValue.Key](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ResValue.Key)` |  `[makeResValueKey](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidResources#makeResValueKey\(kotlin.String,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Make a `[ResValue.Key](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ResValue.Key)` to interact with `[resValues](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidResources#resValues\(\))`'s `[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)`  
  
### Public properties  
  
---  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[pseudoLocalesEnabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidResources#pseudoLocalesEnabled\(\))` Variant's is pseudo locales enabled, initialized by the corresponding DSL elements.  
`[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[ResValue.Key](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ResValue.Key), [ResValue](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ResValue)>` |  `[resValues](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidResources#resValues\(\))` Variant's `[ResValue](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ResValue)` which will be generated.  
  
## Public functions

### makeResValueKey

Added in 7.0.0
    
    
    fun [makeResValueKey](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidResources#makeResValueKey\(kotlin.String,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [ResValue.Key](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ResValue.Key)

Make a `[ResValue.Key](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ResValue.Key)` to interact with `[resValues](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidResources#resValues\(\))`'s `[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)`

## Public properties

### pseudoLocalesEnabled

Added in 7.0.0
    
    
    val [pseudoLocalesEnabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidResources#pseudoLocalesEnabled\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>

Variant's is pseudo locales enabled, initialized by the corresponding DSL elements.

### resValues

Added in 7.0.0
    
    
    val [resValues](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidResources#resValues\(\)): [MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[ResValue.Key](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ResValue.Key), [ResValue](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ResValue)>

Variant's `[ResValue](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ResValue)` which will be generated.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
