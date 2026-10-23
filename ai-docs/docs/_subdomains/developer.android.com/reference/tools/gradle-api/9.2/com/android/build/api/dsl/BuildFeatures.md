---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures/
title: BuildFeatures \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:45:03.036861+00:00
---

# BuildFeatures  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BuildFeatures

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/BuildFeatures.kt+class:com.android.build.api.dsl.BuildFeatures)

Added in 4.2.0
    
    
    interface [BuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures) : [ExtensionAware](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html)

Known direct subclasses 

[ApplicationBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildFeatures), [DynamicFeatureBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DynamicFeatureBuildFeatures), [LibraryBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryBuildFeatures), [TestBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestBuildFeatures)

`[ApplicationBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildFeatures)` |  A list of build features that can be disabled or enabled in an Android Application project.  
---|---  
`[DynamicFeatureBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DynamicFeatureBuildFeatures)` |  A list of build features that can be disabled or enabled in an Android Dynamic Feature project.  
`[LibraryBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryBuildFeatures)` |  A list of build features that can be disabled or enabled in an Android Library project.  
`[TestBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestBuildFeatures)` |  A list of build features that can be disabled or enabled in an Android Test project.  
  
* * *

A list of build features that can be disabled or enabled in an Android project.

This list applies to all plugin types.

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[aidl](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures#aidl\(\))` Flag to enable AIDL compilation.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[buildConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures#buildConfig\(\))` Flag to enable/disable generation of the `BuildConfig` class.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[compose](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures#compose\(\))` Flag to enable Compose feature.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[prefab](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures#prefab\(\))` Flag to enable/disable import of Prefab dependencies from AARs.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[renderScript](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures#renderScript\(\))` **This property is deprecated.** This property and renderScript support will be removed in AGP 10.0  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[resValues](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures#resValues\(\))` Flag to enable Resource Values generation.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures#shaders\(\))` Flag to enable Shader compilation.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[viewBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures#viewBinding\(\))` Flag to enable View Binding.  
  
### Inherited functions  
  
---  
From [org.gradle.api.plugins.ExtensionAware](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html) | `[ExtensionContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionContainer.html)` |  `@[Internal](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/Internal.html)  
@[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.2/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
[getExtensions](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html#getExtensions--)()`  
---|---  
  
## Public properties

### aidl

Added in 4.2.0
    
    
    var [aidl](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures#aidl\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Flag to enable AIDL compilation.

Setting the value to `null` resets to the default value. Default value is `false`.

See [AIDL](http://developer.android.com/r/tools/reference/dsl/buildfeatures/aidl).

### buildConfig

Added in 4.2.0
    
    
    var [buildConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures#buildConfig\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Flag to enable/disable generation of the `BuildConfig` class.

Setting the value to `null` resets to the default value. Default value is `false`.

See [build config fields](http://developer.android.com/r/tools/build-config-fields).

### compose

Added in 4.2.0
    
    
    var [compose](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures#compose\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Flag to enable Compose feature. Setting the value to `null` resets to the default value

Default value is `false`.

See [Compose](http://developer.android.com/compose).

### prefab

Added in 4.2.0
    
    
    var [prefab](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures#prefab\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Flag to enable/disable import of Prefab dependencies from AARs.

Setting the value to `null` resets to the default value. Default value is `false`.

You can override the default for this in your module by setting android { buildFeatures { prefab true } } in the module's build.gradle file.

See [Prefab](http://developer.android.com/r/tools/prefab).

### renderScript

Added in 4.2.0

Deprecated in 9.2.1
    
    
    var [renderScript](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures#renderScript\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

**This property is deprecated.**  
This property and renderScript support will be removed in AGP 10.0

Flag to enable RenderScript compilation.

Setting the value to `null` resets to the default value. Default value is `false`.

### resValues

Added in 4.2.0
    
    
    var [resValues](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures#resValues\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Flag to enable Resource Values generation.

Setting the value to `null` resets to the default value. Default value is `false`. See [Resources](http://developer.android.com/r/tools/res-values).

### shaders

Added in 4.2.0
    
    
    var [shaders](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures#shaders\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Flag to enable Shader compilation.

Setting the value to `null` resets to the default value. Default value is `false`.

You can override the default for this for all projects in your build by adding the line `android.defaults.buildfeatures.shaders=true` in the gradle.properties file at the root project of your build.

See [Shader Compilers](https://developer.android.com/r/tools/shader-compilers)

### viewBinding

Added in 4.2.0
    
    
    var [viewBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildFeatures#viewBinding\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Flag to enable View Binding.

Setting the value to `null` resets to the default value. Default value is `false`.

You can override the default for this for all projects in your build by adding the line `android.defaults.buildfeatures.viewbinding=true` in the gradle.properties file at the root project of your build.

See [View Binding Library](https://developer.android.com/viewbinding)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
