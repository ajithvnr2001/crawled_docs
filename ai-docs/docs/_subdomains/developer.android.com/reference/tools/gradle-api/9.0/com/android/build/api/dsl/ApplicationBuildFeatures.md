---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApplicationBuildFeatures/
title: ApplicationBuildFeatures \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:15:53.994170+00:00
---

# ApplicationBuildFeatures  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApplicationBuildFeatures/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ApplicationBuildFeatures

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ApplicationBuildFeatures.kt+class:com.android.build.api.dsl.ApplicationBuildFeatures)

Added in 4.2.0
    
    
    interface [ApplicationBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApplicationBuildFeatures) : [BuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BuildFeatures)

* * *

A list of build features that can be disabled or enabled in an Android Application project.

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[dataBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApplicationBuildFeatures#dataBinding\(\))` Flag to enable Data Binding.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[mlModelBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApplicationBuildFeatures#mlModelBinding\(\))` Flag to enable Machine Learning Model Binding.  
  
### Inherited functions  
  
---  
From [org.gradle.api.plugins.ExtensionAware](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html) | `[ExtensionContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionContainer.html)` |  `@[Internal](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/Internal.html)  
[getExtensions](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html#getExtensions--)()`  
---|---  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.BuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BuildFeatures) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[aidl](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BuildFeatures#aidl\(\))` Flag to enable AIDL compilation.  
---|---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[buildConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BuildFeatures#buildConfig\(\))` Flag to enable/disable generation of the `BuildConfig` class.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[compose](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BuildFeatures#compose\(\))` Flag to enable Compose feature.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[prefab](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BuildFeatures#prefab\(\))` Flag to enable/disable import of Prefab dependencies from AARs.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[renderScript](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BuildFeatures#renderScript\(\))` **This property is deprecated.** This property and renderScript support will be removed in AGP 10.0  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[resValues](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BuildFeatures#resValues\(\))` Flag to enable Resource Values generation.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BuildFeatures#shaders\(\))` Flag to enable Shader compilation.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[viewBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BuildFeatures#viewBinding\(\))` Flag to enable View Binding.  
  
## Public properties

### dataBinding

Added in 4.2.0
    
    
    var [dataBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApplicationBuildFeatures#dataBinding\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Flag to enable Data Binding.

Setting the value to `null` resets to the default value. Default value is `false`.

You can override the default for this for all projects in your build by adding the line `android.defaults.buildfeatures.databinding=true` in the `gradle.properties` file at the root project of your build.

More information about this feature at: TBD

### mlModelBinding

Added in 4.2.0
    
    
    var [mlModelBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApplicationBuildFeatures#mlModelBinding\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Flag to enable Machine Learning Model Binding.

Setting the value to `null` resets to the default value. Default value is `false`.

You can override the default for this for all projects in your build by adding the line `android.defaults.buildfeatures.mlmodelbinding=true` in the `gradle.properties` file at the root project of your build.

More information about this feature at: TBD

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-22 UTC."],[],[]] 
