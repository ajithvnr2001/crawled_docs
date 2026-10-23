---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTestCompilation/
title: KotlinMultiplatformAndroidHostTestCompilation \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:12:13.878825+00:00
---

# KotlinMultiplatformAndroidHostTestCompilation  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTestCompilation/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# KotlinMultiplatformAndroidHostTestCompilation

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/KotlinMultiplatformAndroidHostTestCompilation.kt+class:com.android.build.api.dsl.KotlinMultiplatformAndroidHostTestCompilation)

Added in 8.8.0
    
    
    interface [KotlinMultiplatformAndroidHostTestCompilation](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTestCompilation) : [KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest), [KotlinMultiplatformAndroidCompilation](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation)

* * *

## Summary

### Inherited functions  
  
---  
From [org.gradle.api.attributes.HasAttributes](https://docs.gradle.org/current/javadoc/org/gradle/api/attributes/HasAttributes.html) | `[AttributeContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/attributes/AttributeContainer.html)` |  `@[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.5/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
[getAttributes](https://docs.gradle.org/current/javadoc/org/gradle/api/attributes/HasAttributes.html#getAttributes--)()`  
---|---  
  
From [org.jetbrains.kotlin.gradle.plugin.HasKotlinDependencies](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/HasKotlinDependencies) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[dependencies](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/HasKotlinDependencies#dependencies\(org.gradle.api.Action\))(configure: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<[KotlinDependencyHandler](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinDependencyHandler)>)`  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[dependencies](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/HasKotlinDependencies#dependencies\(kotlin.Function1\))(configure: [KotlinDependencyHandler](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinDependencyHandler).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
  
From [org.jetbrains.kotlin.gradle.plugin.KotlinCompilation](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[associateWith](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#associateWith\(org.jetbrains.kotlin.gradle.plugin.KotlinCompilation\))(other: [KotlinCompilation](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation)<*>)`  
---|---  
`open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[attributes](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#attributes\(org.gradle.api.Action\))(configure: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<[AttributeContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/attributes/AttributeContainer.html)>)`  
`open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[attributes](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#attributes\(kotlin.Function1\))(configure: [AttributeContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/attributes/AttributeContainer.html).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[defaultSourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#defaultSourceSet\(org.gradle.api.Action\))(configure: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<[KotlinSourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinSourceSet)>)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[defaultSourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#defaultSourceSet\(kotlin.Function1\))(configure: [KotlinSourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinSourceSet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#getName\(\))()`  
`open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[kotlinOptions](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#kotlinOptions\(org.gradle.api.Action\))~~(configure: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<[KotlinCommonOptions](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/dsl/KotlinCommonOptions)>)` **This function is deprecated.** Please migrate to the compilerOptions DSL.  
`open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[kotlinOptions](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#kotlinOptions\(kotlin.Function1\))~~(configure: [KotlinCommonOptions](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/dsl/KotlinCommonOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Please migrate to the compilerOptions DSL.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[source](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#source\(org.jetbrains.kotlin.gradle.plugin.KotlinSourceSet\))~~(sourceSet: [KotlinSourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinSourceSet))` **This function is deprecated.** Scheduled for removal with Kotlin 2.3.  
  
From [com.android.build.api.dsl.KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest#targetSdk\(kotlin.Function1\))(action: [TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TargetSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding target sdk for host tests, see `[TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TargetSdkSpec)` for available options.  
---|---  
  
### Inherited properties  
  
---  
From [org.jetbrains.kotlin.gradle.plugin.HasKotlinDependencies](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/HasKotlinDependencies) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[apiConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/HasKotlinDependencies#apiConfigurationName\(\))`  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[compileOnlyConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/HasKotlinDependencies#compileOnlyConfigurationName\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[implementationConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/HasKotlinDependencies#implementationConfigurationName\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[runtimeOnlyConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/HasKotlinDependencies#runtimeOnlyConfigurationName\(\))`  
  
From [org.jetbrains.kotlin.tooling.core.HasMutableExtras](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/tooling/core/HasMutableExtras) | `[MutableExtras](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/tooling/core/MutableExtras)` |  `[extras](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/tooling/core/HasMutableExtras#extras\(\))`  
---|---  
  
From [org.jetbrains.kotlin.gradle.plugin.HasProject](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/HasProject) | `[Project](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html)` |  `[project](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/HasProject#project\(\))`  
---|---  
  
From [org.jetbrains.kotlin.gradle.plugin.KotlinCompilation](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation) | `[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[KotlinCompilation](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation)<*>>` |  `@[ExperimentalKotlinGradlePluginApi](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/ExperimentalKotlinGradlePluginApi)  
[allAssociatedCompilations](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#allAssociatedCompilations\(\))`  
---|---  
`[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[KotlinSourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinSourceSet)>` |  `[allKotlinSourceSets](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#allKotlinSourceSets\(\))`  
`open [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[KotlinCompilation](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation)<*>>` |  `[associateWith](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#associateWith\(\))` **This property is deprecated.** Use 'associatedCompilations' instead  
`[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[KotlinCompilation](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation)<*>>` |  `[associatedCompilations](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#associatedCompilations\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[compilationName](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#compilationName\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[compileAllTaskName](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#compileAllTaskName\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[compileDependencyConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#compileDependencyConfigurationName\(\))`  
`[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)` |  `[compileDependencyFiles](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#compileDependencyFiles\(\))`  
`[KotlinCompile](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/dsl/KotlinCompile)<[KotlinCommonOptions](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/dsl/KotlinCommonOptions)>` |  `[compileKotlinTask](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#compileKotlinTask\(\))` **This property is deprecated.** Accessing task instance directly is deprecated.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[compileKotlinTaskName](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#compileKotlinTaskName\(\))`  
`[TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<[KotlinCompile](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/dsl/KotlinCompile)<[KotlinCommonOptions](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/dsl/KotlinCommonOptions)>>` |  `[compileKotlinTaskProvider](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#compileKotlinTaskProvider\(\))` **This property is deprecated.** Replaced with compileTaskProvider.  
`[HasCompilerOptions](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/HasCompilerOptions)<*>` |  `[compilerOptions](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#compilerOptions\(\))` **This property is deprecated.** To configure compilation compiler options use 'compileTaskProvider': compilation.compileTaskProvider.configure{ compilerOptions {} }  
`[KotlinSourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinSourceSet)` |  `[defaultSourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#defaultSourceSet\(\))`  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[defaultSourceSetName](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#defaultSourceSetName\(\))` **This property is deprecated.** Use defaultSourceSet.name instead.  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[disambiguatedName](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#disambiguatedName\(\))`  
`[KotlinCommonOptions](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/dsl/KotlinCommonOptions)` |  `[kotlinOptions](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#kotlinOptions\(\))` **This property is deprecated.** Please migrate to the compilerOptions DSL.  
`[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[KotlinSourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinSourceSet)>` |  `[kotlinSourceSets](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#kotlinSourceSets\(\))`  
`[KotlinCompilationOutput](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilationOutput)` |  `[output](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#output\(\))`  
`open [KotlinPlatformType](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinPlatformType)` |  `[platformType](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#platformType\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[runtimeDependencyConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#runtimeDependencyConfigurationName\(\))`  
`[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)?` |  `[runtimeDependencyFiles](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#runtimeDependencyFiles\(\))`  
`[KotlinTarget](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinTarget)` |  `[target](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation#target\(\))`  
  
From [com.android.build.api.dsl.KotlinMultiplatformAndroidCompilation](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation) | `[TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<[KotlinCompilationTask](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/tasks/KotlinCompilationTask)<[KotlinJvmCompilerOptions](https://developer.android.com/reference/tools/gradle-api/9.5/org/jetbrains/kotlin/gradle/dsl/KotlinJvmCompilerOptions)>>` |  `[compileTaskProvider](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#compileTaskProvider\(\))`  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[componentName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#componentName\(\))` The name of the component corresponding to this Android compilation.  
  
From [com.android.build.api.dsl.KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableCoverage](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest#enableCoverage\(\))` Specifies unit test code coverage data collection by configuring the JacocoPlugin.  
---|---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isIncludeAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest#isIncludeAndroidResources\(\))` Enables unit tests to use Android resources, assets, and manifests.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isReturnDefaultValues](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest#isReturnDefaultValues\(\))` Whether unmocked methods from android.jar should throw exceptions or return default values (i.e. zero or null).  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
