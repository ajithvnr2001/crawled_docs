---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DependencySelection/
title: DependencySelection \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:28:31.331995+00:00
---

# DependencySelection  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DependencySelection/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DependencySelection

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/DependencySelection.kt+class:com.android.build.api.dsl.DependencySelection)

Added in 8.12.0
    
    
    interface [DependencySelection](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DependencySelection)

* * *

Specifies options for doing Gradle variant selection for external Android dependencies based on build types and product flavors.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[productFlavorDimension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DependencySelection#productFlavorDimension\(kotlin.String,org.gradle.api.Action\))(  
dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),  
action: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<[ProductFlavorDimensionSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ProductFlavorDimensionSpec)>  
)` Configures a single product flavor dimension that the plugin should try to use when a direct variant match with a dependency is not possible.  
  
### Public properties  
  
---  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[selectBuildTypeFrom](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DependencySelection#selectBuildTypeFrom\(\))` Specifies a list of build types that the plugin should try to use when a direct variant match with a dependency is not possible.  
  
## Public functions

### productFlavorDimension

Added in 8.12.0
    
    
    fun [productFlavorDimension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DependencySelection#productFlavorDimension\(kotlin.String,org.gradle.api.Action\))(  
        dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),  
        action: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<[ProductFlavorDimensionSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ProductFlavorDimensionSpec)>  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures a single product flavor dimension that the plugin should try to use when a direct variant match with a dependency is not possible.

## Public properties

### selectBuildTypeFrom

Added in 8.12.0
    
    
    val [selectBuildTypeFrom](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DependencySelection#selectBuildTypeFrom\(\)): [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies a list of build types that the plugin should try to use when a direct variant match with a dependency is not possible.

If the list is left empty, the default variant for the dependencies being consumed will be of build type "release"

If you want to preserve the default value use `selectBuildTypeFrom.add()` and if you would like to set your own list of build types use `selectBuildTypeFrom.set()`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
