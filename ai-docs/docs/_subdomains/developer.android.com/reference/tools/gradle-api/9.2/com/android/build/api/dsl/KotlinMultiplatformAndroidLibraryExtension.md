---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension/
title: KotlinMultiplatformAndroidLibraryExtension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:35.638481+00:00
---

# KotlinMultiplatformAndroidLibraryExtension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# KotlinMultiplatformAndroidLibraryExtension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension.kt+class:com.android.build.api.dsl.KotlinMultiplatformAndroidLibraryExtension)

Added in 8.8.0
    
    
    interface [KotlinMultiplatformAndroidLibraryExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension)

Known direct subclasses 

[KotlinMultiplatformAndroidLibraryTarget](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryTarget)

`[KotlinMultiplatformAndroidLibraryTarget](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryTarget)` |   
---|---  
  
* * *

Extension properties for Kotlin multiplatform Android libraries.

Only the Kotlin Multiplatform Android Plugin should create instances of this interface.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[aarMetadata](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#aarMetadata\(kotlin.Function1\))(action: [AarMetadata](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AarMetadata).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Options for configuring AAR metadata.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[androidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#androidResources\(kotlin.Function1\))(action: [LibraryAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryAndroidResources).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for configuring android resources and assets for KMP  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#compileSdk\(kotlin.Function1\))(action: [CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding compile Sdk version, see `[CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkSpec)` for more details.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#lint\(kotlin.Function1\))(action: [Lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Lint).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the lint tool.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[localDependencySelection](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#localDependencySelection\(kotlin.Function1\))(action: [DependencySelection](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DependencySelection).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for doing variant selection for external Android dependencies based on build types and product flavors  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#minSdk\(kotlin.Function1\))(action: [MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/MinSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding minSdk, see `[MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/MinSdkSpec)` for available options.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[optimization](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#optimization\(kotlin.Function1\))(action: [KmpOptimization](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KmpOptimization).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the R8/D8 optimization tool.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#packaging\(kotlin.Function1\))(action: [Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options and rules that determine which files the Android plugin packages into your AAR.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[testCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#testCoverage\(kotlin.Function1\))(action: [TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestCoverage).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[useLibrary](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#useLibrary\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Includes the specified library to the classpath.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[useLibrary](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#useLibrary\(kotlin.String,kotlin.Boolean\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), required: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Includes the specified library to the classpath.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[withDeviceTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#withDeviceTest\(kotlin.Function1\))(action: [KotlinMultiplatformAndroidDeviceTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Creates and configures a compilation for tests that run on the device (previously referred to as instrumented tests).  
`[HasConfigurableValue](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/HasConfigurableValue)<[KotlinMultiplatformAndroidDeviceTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest)>` |  `[withDeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#withDeviceTestBuilder\(kotlin.Function1\))(action: [KotlinMultiplatformAndroidCompilationBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Creates and configures a compilation for tests that run on the device (previously referred to as instrumented tests).  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[withHostTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#withHostTest\(kotlin.Function1\))(action: [KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Creates and configures a compilation for tests that run on the JVM (previously referred to as unit tests).  
`[HasConfigurableValue](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/HasConfigurableValue)<[KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest)>` |  `[withHostTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#withHostTestBuilder\(kotlin.Function1\))(action: [KotlinMultiplatformAndroidCompilationBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Creates and configures a compilation for tests that run on the JVM (previously referred to as unit tests).  
  
### Public properties  
  
---  
`[AarMetadata](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AarMetadata)` |  `[aarMetadata](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#aarMetadata\(\))` Options for configuring AAR metadata.  
`[LibraryAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryAndroidResources)` |  `[androidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#androidResources\(\))` Specifies options for configuring android resources and assets for KMP  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#buildToolsVersion\(\))` Specifies the version of the [SDK Build Tools](https://developer.android.com/studio/releases/build-tools.html) to use when building your project.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#compileSdk\(\))` Specifies the API level to compile your project against.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdkExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#compileSdkExtension\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[compileSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#compileSdkPreview\(\))`  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableCoreLibraryDesugaring](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#enableCoreLibraryDesugaring\(\))` Whether core library desugaring is enabled.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[experimentalProperties](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#experimentalProperties\(\))` Additional per module experimental properties.  
`[Lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Lint)` |  `[lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#lint\(\))` Specifies options for the lint tool.  
`[DependencySelection](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DependencySelection)` |  `[localDependencySelection](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#localDependencySelection\(\))` Specifies options for doing variant selection for external Android dependencies based on build types and product flavors  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#minSdk\(\))` The minimum SDK version.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#minSdkPreview\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[namespace](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#namespace\(\))` The namespace of the generated R and BuildConfig classes.  
`[KmpOptimization](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KmpOptimization)` |  `[optimization](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#optimization\(\))` Specifies options for the R8/D8 optimization tool.  
`[Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#packaging\(\))` Specifies options and rules that determine which files the Android plugin packages into your AAR.  
`[TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestCoverage)` |  `[testCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#testCoverage\(\))` Configure the gathering of code-coverage from tests.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[testNamespace](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#testNamespace\(\))` The namespace used by the android test and unit test components for the generated R and BuildConfig classes.  
  
## Public functions

### aarMetadata

Added in 8.8.0
    
    
    fun [aarMetadata](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#aarMetadata\(kotlin.Function1\))(action: [AarMetadata](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AarMetadata).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Options for configuring AAR metadata.

### androidResources

Added in 8.11.0
    
    
    fun [androidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#androidResources\(kotlin.Function1\))(action: [LibraryAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryAndroidResources).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for configuring android resources and assets for KMP

### compileSdk

Added in 8.13.0
    
    
    fun [compileSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#compileSdk\(kotlin.Function1\))(action: [CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures all aspects regarding compile Sdk version, see `[CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkSpec)` for more details.

### lint

Added in 8.8.0
    
    
    fun [lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#lint\(kotlin.Function1\))(action: [Lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Lint).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for the lint tool.

For more information about the properties you can configure in this block, see `[Lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Lint)`.

### localDependencySelection

Added in 8.12.0
    
    
    fun [localDependencySelection](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#localDependencySelection\(kotlin.Function1\))(action: [DependencySelection](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DependencySelection).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for doing variant selection for external Android dependencies based on build types and product flavors

Note that this only affects dependency selection within this gradle project and does not affect the resolution of dependencies in other Gradle projects that depend on this project or the artifacts published from this project

For more information about the properties you can configure in this block, see `[DependencySelection](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DependencySelection)`.

### minSdk

Added in 8.13.0
    
    
    fun [minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#minSdk\(kotlin.Function1\))(action: [MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/MinSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures all aspects regarding minSdk, see `[MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/MinSdkSpec)` for available options.

### optimization

Added in 8.8.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [optimization](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#optimization\(kotlin.Function1\))(action: [KmpOptimization](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KmpOptimization).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for the R8/D8 optimization tool.

For more information about the properties you can configure in this block, see `[KmpOptimization](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KmpOptimization)`.

### packaging

Added in 8.8.0
    
    
    fun [packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#packaging\(kotlin.Function1\))(action: [Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options and rules that determine which files the Android plugin packages into your AAR.

For more information about the properties you can configure in this block, see `[Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging)`.

### testCoverage

Added in 9.2.1
    
    
    fun [testCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#testCoverage\(kotlin.Function1\))(action: [TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestCoverage).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### useLibrary

Added in 8.8.0
    
    
    fun [useLibrary](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#useLibrary\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Includes the specified library to the classpath.

You typically use this property to support optional platform libraries that ship with the Android SDK. The following sample adds the Apache HTTP API library to the project classpath:
    
    
    android {  
        // Adds a platform library that ships with the Android SDK.  
        useLibrary 'org.apache.http.legacy'  
    }

To include libraries that do not ship with the SDK, such as local library modules or binaries from remote repositories, [add the libraries as dependencies](https://developer.android.com/studio/build/dependencies.html) in the `dependencies` block. Note that Android plugin 3.0.0 and later introduce [new dependency configurations](https://developer.android.com/studio/build/gradle-plugin-3-0-0-migration.html#new_configurations). To learn more about Gradle dependencies, read [Dependency Management Basics](https://docs.gradle.org/current/userguide/artifact_dependencies_tutorial.html).

Parameters  
---  
`name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the name of the library.  
  
### useLibrary

Added in 8.8.0
    
    
    fun [useLibrary](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#useLibrary\(kotlin.String,kotlin.Boolean\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), required: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Includes the specified library to the classpath.

You typically use this property to support optional platform libraries that ship with the Android SDK. The following sample adds the Apache HTTP API library to the project classpath:
    
    
    android {  
        // Adds a platform library that ships with the Android SDK.  
        useLibrary 'org.apache.http.legacy'  
    }

To include libraries that do not ship with the SDK, such as local library modules or binaries from remote repositories, "https://developer.android.com/studio/build/dependencies.html in the `dependencies` block. Note that Android plugin 3.0.0 and later introduce new dependency configurations. To learn more about Gradle dependencies, read [Dependency Management Basics](https://docs.gradle.org/current/userguide/artifact_dependencies_tutorial.html)

Parameters  
---  
`name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the name of the library.  
`required: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  if using the library requires a manifest entry, the entry will indicate that the library is not required.  
  
### withDeviceTest

Added in 8.8.0
    
    
    fun [withDeviceTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#withDeviceTest\(kotlin.Function1\))(action: [KotlinMultiplatformAndroidDeviceTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Creates and configures a compilation for tests that run on the device (previously referred to as instrumented tests). Invoking this method will create a `[KotlinMultiplatformAndroidDeviceTestCompilation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTestCompilation)` object with the following defaults:

  * compilation name is "deviceTest"

  * default sourceSet name is "androidDeviceTest" (sources would be located at `$project/src/androidDeviceTest`)

  * sourceSet tree is `null`, which means that the `commonTest` sourceSet will **not** be included in the compilation.




Only a single compilation of this test type can be created. If you want to configure `[KotlinMultiplatformAndroidDeviceTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest)` options, you can modify it on the kotlin compilation as follows:
    
    
    kotlin {  
      android {  
        compilations.withType(com.android.build.api.dsl.KotlinMultiplatformAndroidDeviceTestCompilation::class.java) {  
          // configure options  
        }  
      }  
    }

### withDeviceTestBuilder

Added in 8.8.0
    
    
    fun [withDeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#withDeviceTestBuilder\(kotlin.Function1\))(action: [KotlinMultiplatformAndroidCompilationBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [HasConfigurableValue](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/HasConfigurableValue)<[KotlinMultiplatformAndroidDeviceTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest)>

Creates and configures a compilation for tests that run on the device (previously referred to as instrumented tests). Invoking this method will create a `[KotlinMultiplatformAndroidDeviceTestCompilation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTestCompilation)` object using the values set in the `[KotlinMultiplatformAndroidCompilationBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder)`.

The returned object can be used to configure `[KotlinMultiplatformAndroidDeviceTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest)` as follows:
    
    
    kotlin {  
      android {  
        withDeviceTestBuilder {  
        }.configure {  
          instrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"  
        }  
      }  
    }

Only a single compilation of this test type can be created. If you want to configure `[KotlinMultiplatformAndroidDeviceTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest)` options, you can modify it on the kotlin compilation as follows:
    
    
    kotlin {  
      android {  
        compilations.withType(com.android.build.api.dsl.KotlinMultiplatformAndroidDeviceTestCompilation::class.java) {  
          // configure options  
        }  
      }  
    }

### withHostTest

Added in 8.8.0
    
    
    fun [withHostTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#withHostTest\(kotlin.Function1\))(action: [KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Creates and configures a compilation for tests that run on the JVM (previously referred to as unit tests). Invoking this method will create a `[KotlinMultiplatformAndroidHostTestCompilation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTestCompilation)` object with the following defaults (You can change these defaults by using `[withHostTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#withHostTestBuilder\(kotlin.Function1\))` instead):

  * compilation name is "hostTest"

  * default sourceSet name is "androidHostTest" (sources would be located at `$project/src/androidHostTest`)

  * sourceSet tree is `test`, which means that the `commonTest` sourceSet would be included in the compilation.




Only a single compilation of this test type can be created. If you want to configure `[KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest)` options, you can modify it on the kotlin compilation as follows:
    
    
    kotlin {  
      android {  
        compilations.withType(com.android.build.api.dsl.KotlinMultiplatformAndroidHostTestCompilation::class.java) {  
          // configure options  
        }  
      }  
    }

### withHostTestBuilder

Added in 8.8.0
    
    
    fun [withHostTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#withHostTestBuilder\(kotlin.Function1\))(action: [KotlinMultiplatformAndroidCompilationBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [HasConfigurableValue](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/HasConfigurableValue)<[KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest)>

Creates and configures a compilation for tests that run on the JVM (previously referred to as unit tests). Invoking this method will create a `[KotlinMultiplatformAndroidHostTestCompilation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTestCompilation)` object using the values set in the `[KotlinMultiplatformAndroidCompilationBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder)`.

The returned object can be used to configure `[KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest)` as follows:
    
    
    kotlin {  
      android {  
        withHostTestBuilder {  
        }.configure {  
          isIncludeAndroidResources = true  
        }  
      }  
    }

Only a single compilation of this test type can be created. If you want to configure `[KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest)` options, you can modify it on the kotlin compilation as follows:
    
    
    kotlin {  
      android {  
        compilations.withType(com.android.build.api.dsl.KotlinMultiplatformAndroidHostTestCompilation::class.java) {  
          // configure options  
        }  
      }  
    }

## Public properties

### aarMetadata

Added in 8.8.0
    
    
    val [aarMetadata](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#aarMetadata\(\)): [AarMetadata](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AarMetadata)

Options for configuring AAR metadata.

### androidResources

Added in 8.11.0
    
    
    val [androidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#androidResources\(\)): [LibraryAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryAndroidResources)

Specifies options for configuring android resources and assets for KMP

### buildToolsVersion

Added in 8.8.0
    
    
    var [buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#buildToolsVersion\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Specifies the version of the [SDK Build Tools](https://developer.android.com/studio/releases/build-tools.html) to use when building your project.

By default, the plugin uses the minimum version of the build tools required by the [version of the plugin](https://developer.android.com/studio/releases/gradle-plugin.html#revisions) you're using. To specify a different version of the build tools for the plugin to use, specify the version as follows:
    
    
    android {  
        // Specifying this property is optional.  
        buildToolsVersion "26.0.0"  
    }

For a list of build tools releases, read [the release notes](https://developer.android.com/studio/releases/build-tools.html#notes).

Note that the value assigned to this property is parsed and stored in a normalized form, so reading it back may give a slightly different result.

### compileSdk

Added in 8.8.0
    
    
    var [compileSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#compileSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Specifies the API level to compile your project against. The Android plugin requires you to configure this property.

This means your code can use only the Android APIs included in that API level and lower. You can configure the compile sdk version by adding the following to the `android` block: `compileSdk = 26`.

You should generally [use the most up-to-date API level](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels) available. If you are planning to also support older API levels, it's good practice to [use the Lint tool](https://developer.android.com/studio/write/lint.html) to check if you are using APIs that are not available in earlier API levels.

The value you assign to this property is parsed and stored in a normalized form, so reading it back may return a slightly different value.

### compileSdkExtension

Added in 8.8.0
    
    
    var [compileSdkExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#compileSdkExtension\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

### compileSdkPreview

Added in 8.8.0
    
    
    var [compileSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#compileSdkPreview\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

### enableCoreLibraryDesugaring

Added in 8.8.0
    
    
    var [enableCoreLibraryDesugaring](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#enableCoreLibraryDesugaring\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether core library desugaring is enabled.

### experimentalProperties

Added in 8.8.0
    
    
    val [experimentalProperties](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#experimentalProperties\(\)): [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>

Additional per module experimental properties.

### lint

Added in 8.8.0
    
    
    val [lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#lint\(\)): [Lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Lint)

Specifies options for the lint tool.

For more information about the properties you can configure in this block, see `[Lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Lint)`.

### localDependencySelection

Added in 8.12.0
    
    
    val [localDependencySelection](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#localDependencySelection\(\)): [DependencySelection](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DependencySelection)

Specifies options for doing variant selection for external Android dependencies based on build types and product flavors

Note that this only affects dependency selection within this gradle project and does not affect the resolution of dependencies in other Gradle projects that depend on this project or the artifacts published from this project

For more information about the properties you can configure in this block, see `[DependencySelection](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DependencySelection)`.

### minSdk

Added in 8.8.0
    
    
    var [minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#minSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

The minimum SDK version. Setting this it will override previous calls of `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#minSdk\(kotlin.Function1\))` and `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#minSdkPreview\(\))` setters. Only one of `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#minSdk\(kotlin.Function1\))` and `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#minSdkPreview\(\))` should be set.

See [uses-sdk element documentation](http://developer.android.com/guide/topics/manifest/uses-sdk-element.html).

### minSdkPreview

Added in 8.8.0
    
    
    var [minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#minSdkPreview\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

### namespace

Added in 8.8.0
    
    
    var [namespace](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#namespace\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The namespace of the generated R and BuildConfig classes. Also, the namespace used to resolve any relative class names that are declared in the AndroidManifest.xml.

### optimization

Added in 8.8.0
    
    
    val [optimization](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#optimization\(\)): [KmpOptimization](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KmpOptimization)

Specifies options for the R8/D8 optimization tool.

For more information about the properties you can configure in this block, see `[KmpOptimization](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KmpOptimization)`.

### packaging

Added in 8.8.0
    
    
    val [packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#packaging\(\)): [Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging)

Specifies options and rules that determine which files the Android plugin packages into your AAR.

For more information about the properties you can configure in this block, see `[Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging)`.

### testCoverage

Added in 8.8.0
    
    
    val [testCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#testCoverage\(\)): [TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestCoverage)

Configure the gathering of code-coverage from tests.

### testNamespace

Added in 8.8.0
    
    
    var [testNamespace](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension#testNamespace\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The namespace used by the android test and unit test components for the generated R and BuildConfig classes.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
