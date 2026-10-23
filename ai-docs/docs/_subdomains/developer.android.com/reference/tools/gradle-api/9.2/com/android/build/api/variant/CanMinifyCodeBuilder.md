---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/CanMinifyCodeBuilder/
title: CanMinifyCodeBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:52:24.734573+00:00
---

# CanMinifyCodeBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/CanMinifyCodeBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# CanMinifyCodeBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/CanMinifyCodeBuilder.kt+class:com.android.build.api.variant.CanMinifyCodeBuilder)

Added in 7.4.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [CanMinifyCodeBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/CanMinifyCodeBuilder)

Known direct subclasses 

[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApplicationVariantBuilder), [LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/LibraryVariantBuilder), [TestVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestVariantBuilder)

`[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApplicationVariantBuilder)` |  Model for application components that only contains configuration-time properties that impacts the build flow.  
---|---  
`[LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/LibraryVariantBuilder)` |  Model for library components that only contains configuration-time properties that impacts the build flow.  
`[TestVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestVariantBuilder)` |  Model for test components that only contains configuration-time properties that impacts the build flow.  
  
Known indirect subclasses 

[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)

`[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)` |  Model for kotlin multiplatform library components that only contains configuration-time properties that impacts the build flow.  
---|---  
  
* * *

Interface for component builder that can minify code

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isMinifyEnabled](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/CanMinifyCodeBuilder#isMinifyEnabled\(\))` Specifies whether code will be minified  
  
## Public properties

### isMinifyEnabled

Added in 7.4.0
    
    
    var [isMinifyEnabled](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/CanMinifyCodeBuilder#isMinifyEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Specifies whether code will be minified

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
