---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DependencyVariantSelection/
title: DependencyVariantSelection \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:31:51.980818+00:00
---

# DependencyVariantSelection  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DependencyVariantSelection/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DependencyVariantSelection

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/DependencyVariantSelection.kt+class:com.android.build.api.dsl.DependencyVariantSelection)

Added in 8.2.0

Deprecated in 8.13.2
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [DependencyVariantSelection](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DependencyVariantSelection)

* * *

**This interface is deprecated.**  
Replaced by LocalDependencySelection

Specifies options for doing variant selection for external Android dependencies based on build types and product flavors

## Summary

### Public properties  
  
---  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[buildTypes](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DependencyVariantSelection#buildTypes\(\))` **This property is deprecated.** Replaced by LocalDependencySelection.selectBuildTypeFrom  
`[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>>` |  `[productFlavors](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DependencyVariantSelection#productFlavors\(\))` **This property is deprecated.** Replaced by LocalDependencySelection.productFlavorDimension  
  
## Public properties

### buildTypes

Added in 8.2.0

Deprecated in 8.13.2
    
    
    val [buildTypes](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DependencyVariantSelection#buildTypes\(\)): [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

**This property is deprecated.**  
Replaced by LocalDependencySelection.selectBuildTypeFrom

Specifies a list of build types that the plugin should try to use when a direct variant match with a dependency is not possible.

If the list is left empty, the default variant for the dependencies being consumed will be of build type "debug"

### productFlavors

Added in 8.2.0

Deprecated in 8.13.2
    
    
    val [productFlavors](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DependencyVariantSelection#productFlavors\(\)): [MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>>

**This property is deprecated.**  
Replaced by LocalDependencySelection.productFlavorDimension

Specifies a map of product flavors that the plugin should try to use when a direct variant match with a dependency is not possible.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-11 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-11 UTC."],[],[]] 
