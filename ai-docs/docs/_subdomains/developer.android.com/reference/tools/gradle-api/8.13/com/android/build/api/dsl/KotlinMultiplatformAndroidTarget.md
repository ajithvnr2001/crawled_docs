---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidTarget/
title: KotlinMultiplatformAndroidTarget \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:33:18.452063+00:00
---

# KotlinMultiplatformAndroidTarget  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidTarget/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# KotlinMultiplatformAndroidTarget

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryTarget.kt+class:com.android.build.api.dsl.KotlinMultiplatformAndroidTarget)

Added in 8.2.0

Deprecated in 8.8.0
    
    
    interface [KotlinMultiplatformAndroidTarget](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidTarget) : [KotlinMultiplatformAndroidLibraryExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension)

Known direct subclasses 

[KotlinMultiplatformAndroidLibraryTarget](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryTarget)

`[KotlinMultiplatformAndroidLibraryTarget](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryTarget)` |   
---|---  
  
* * *

**This interface is deprecated.**  
Use KotlinMultiplatformAndroidLibraryTarget. This interface will be removed in AGP 9.0

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[withJava](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidTarget#withJava\(\))()` Enables compilation of java sources.  
  
### Public properties  
  
---  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[KotlinMultiplatformAndroidCompilation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation)>` |  `[compilations](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidTarget#compilations\(\))`  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.KotlinMultiplatformAndroidLibraryExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[aarMetadata](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#aarMetadata\(kotlin.Function1\))(action: [AarMetadata](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AarMetadata).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Options for configuring AAR metadata.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[androidResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#androidResources\(kotlin.Function1\))(action: [LibraryAndroidResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LibraryAndroidResources).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for configuring android resources and assets for KMP  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#compileSdk\(kotlin.Function1\))(action: [CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CompileSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding compile Sdk version, see `[CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CompileSdkSpec)` for more details.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[dependencyVariantSelection](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#dependencyVariantSelection\(kotlin.Function1\))~~(action: [DependencyVariantSelection](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DependencyVariantSelection).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Use localDependencySelection instead.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[lint](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#lint\(kotlin.Function1\))(action: [Lint](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Lint).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the lint tool.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[localDependencySelection](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#localDependencySelection\(kotlin.Function1\))(action: [DependencySelection](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DependencySelection).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for doing variant selection for external Android dependencies based on build types and product flavors  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#minSdk\(kotlin.Function1\))(action: [MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/MinSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding minSdk, see `[MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/MinSdkSpec)` for available options.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[optimization](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#optimization\(kotlin.Function1\))(action: [KmpOptimization](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KmpOptimization).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the R8/D8 optimization tool.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#packaging\(kotlin.Function1\))(action: [Packaging](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Packaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options and rules that determine which files the Android plugin packages into your AAR.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[useLibrary](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#useLibrary\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Includes the specified library to the classpath.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[useLibrary](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#useLibrary\(kotlin.String,kotlin.Boolean\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), required: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Includes the specified library to the classpath.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[withAndroidTestOnDevice](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#withAndroidTestOnDevice\(kotlin.Function1\))~~(action: [KotlinMultiplatformAndroidDeviceTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Use withDeviceTest.  
`[HasConfigurableValue](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/HasConfigurableValue)<[KotlinMultiplatformAndroidDeviceTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest)>` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[withAndroidTestOnDeviceBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#withAndroidTestOnDeviceBuilder\(kotlin.Function1\))~~(action: [KotlinMultiplatformAndroidCompilationBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Use withDeviceTestBuilder.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[withAndroidTestOnJvm](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#withAndroidTestOnJvm\(kotlin.Function1\))~~(action: [KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Use withHostTest.  
`[HasConfigurableValue](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/HasConfigurableValue)<[KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest)>` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[withAndroidTestOnJvmBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#withAndroidTestOnJvmBuilder\(kotlin.Function1\))~~(action: [KotlinMultiplatformAndroidCompilationBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Use withHostTestBuilder.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[withDeviceTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#withDeviceTest\(kotlin.Function1\))(action: [KotlinMultiplatformAndroidDeviceTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Creates and configures a compilation for tests that run on the device (previously referred to as instrumented tests).  
`[HasConfigurableValue](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/HasConfigurableValue)<[KotlinMultiplatformAndroidDeviceTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest)>` |  `[withDeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#withDeviceTestBuilder\(kotlin.Function1\))(action: [KotlinMultiplatformAndroidCompilationBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Creates and configures a compilation for tests that run on the device (previously referred to as instrumented tests).  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[withHostTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#withHostTest\(kotlin.Function1\))(action: [KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Creates and configures a compilation for tests that run on the JVM (previously referred to as unit tests).  
`[HasConfigurableValue](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/HasConfigurableValue)<[KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest)>` |  `[withHostTestBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#withHostTestBuilder\(kotlin.Function1\))(action: [KotlinMultiplatformAndroidCompilationBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Creates and configures a compilation for tests that run on the JVM (previously referred to as unit tests).  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.KotlinMultiplatformAndroidLibraryExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension) | `[AarMetadata](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AarMetadata)` |  `[aarMetadata](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#aarMetadata\(\))` Options for configuring AAR metadata.  
---|---  
`[LibraryAndroidResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LibraryAndroidResources)` |  `[androidResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#androidResources\(\))` Specifies options for configuring android resources and assets for KMP  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#buildToolsVersion\(\))` Specifies the version of the [SDK Build Tools](https://developer.android.com/studio/releases/build-tools.html) to use when building your project.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#compileSdk\(\))` Specifies the API level to compile your project against.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdkExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#compileSdkExtension\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[compileSdkPreview](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#compileSdkPreview\(\))`  
`[DependencyVariantSelection](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DependencyVariantSelection)` |  `[dependencyVariantSelection](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#dependencyVariantSelection\(\))` **This property is deprecated.** Use localDependencySelection instead.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableCoreLibraryDesugaring](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#enableCoreLibraryDesugaring\(\))` Whether core library desugaring is enabled.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[experimentalProperties](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#experimentalProperties\(\))` Additional per module experimental properties.  
`[Lint](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Lint)` |  `[lint](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#lint\(\))` Specifies options for the lint tool.  
`[DependencySelection](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DependencySelection)` |  `[localDependencySelection](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#localDependencySelection\(\))` Specifies options for doing variant selection for external Android dependencies based on build types and product flavors  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#minSdk\(\))` The minimum SDK version.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#minSdkPreview\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[namespace](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#namespace\(\))` The namespace of the generated R and BuildConfig classes.  
`[KmpOptimization](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KmpOptimization)` |  `[optimization](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#optimization\(\))` Specifies options for the R8/D8 optimization tool.  
`[Packaging](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Packaging)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#packaging\(\))` Specifies options and rules that determine which files the Android plugin packages into your AAR.  
`[TestCoverage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestCoverage)` |  `[testCoverage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#testCoverage\(\))` Configure the gathering of code-coverage from tests.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[testNamespace](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#testNamespace\(\))` The namespace used by the android test and unit test components for the generated R and BuildConfig classes.  
  
## Public functions

### withJava

Added in 8.2.0

Deprecated in 8.8.0
    
    
    fun [withJava](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidTarget#withJava\(\))(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Enables compilation of java sources.

## Public properties

### compilations

Added in 8.2.0

Deprecated in 8.8.0
    
    
    val [compilations](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidTarget#compilations\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[KotlinMultiplatformAndroidCompilation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation)>

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-31 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-31 UTC."],[],[]] 
