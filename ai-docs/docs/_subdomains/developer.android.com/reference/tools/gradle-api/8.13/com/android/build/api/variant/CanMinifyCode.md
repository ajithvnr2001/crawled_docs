---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/CanMinifyCode/
title: CanMinifyCode \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:38:18.695123+00:00
---

# CanMinifyCode  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/CanMinifyCode/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# CanMinifyCode

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/CanMinifyCode.kt+class:com.android.build.api.variant.CanMinifyCode)

Added in 7.4.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [CanMinifyCode](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/CanMinifyCode)

Known direct subclasses 

[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ApplicationVariant), [LibraryVariant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/LibraryVariant)

`[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ApplicationVariant)` |  Model for application components that only contains build-time properties.  
---|---  
`[LibraryVariant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/LibraryVariant)` |  Model for library components that only contains build-time properties.  
  
Known indirect subclasses 

[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)

`[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)` |  Properties for the main Variant of a kotlin multiplatform android library  
---|---  
  
* * *

Build-time properties for `[Component](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Component)` that can minify code.

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isMinifyEnabled](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/CanMinifyCode#isMinifyEnabled\(\))` Specifies whether code will be minified.  
  
## Public properties

### isMinifyEnabled

Added in 7.4.0
    
    
    val [isMinifyEnabled](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/CanMinifyCode#isMinifyEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Specifies whether code will be minified. At this point the value is final. You can change it via `[AndroidComponentsExtension.beforeVariants](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` and `[CanMinifyCodeBuilder.isMinifyEnabled](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/CanMinifyCodeBuilder#isMinifyEnabled\(\))`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
