---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestBuildFeatures/
title: TestBuildFeatures \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:20:59.644052+00:00
---

# TestBuildFeatures  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestBuildFeatures/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestBuildFeatures

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/TestBuildFeatures.kt+class:com.android.build.api.dsl.TestBuildFeatures)

Added in 4.2.0
    
    
    interface [TestBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestBuildFeatures) : [BuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BuildFeatures)

* * *

A list of build features that can be disabled or enabled in an Android Test project.

## Summary

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
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-22 UTC."],[],[]] 
