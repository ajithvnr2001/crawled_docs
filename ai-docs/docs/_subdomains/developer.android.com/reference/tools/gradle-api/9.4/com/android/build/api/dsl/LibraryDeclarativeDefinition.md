---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition/
title: LibraryDeclarativeDefinition \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:53:59.640356+00:00
---

# LibraryDeclarativeDefinition  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# LibraryDeclarativeDefinition

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/LibraryDeclarativeDefinition.kt+class:com.android.build.api.dsl.LibraryDeclarativeDefinition)

Added in 9.4.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [LibraryDeclarativeDefinition](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition) : [CommonDeclarativeDefinition](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CommonDeclarativeDefinition), [TestedDeclarativeDefinition](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestedDeclarativeDefinition), [Definition](https://developer.android.com/reference/tools/gradle-api/9.4/org/gradle/features/binding/Definition)

* * *

A declarative definition for the Android Library Gradle Plugin.

This interface contains all properties and functions from `[LibraryExtension](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryExtension)` and its parent interfaces.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DeclarativeLibraryBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DeclarativeLibraryBuildType)>.[debug](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#\(org.gradle.api.NamedDomainObjectContainer\).debug\(kotlin.Function1\))(  
action: [DeclarativeLibraryBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DeclarativeLibraryBuildType).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DeclarativeLibraryBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DeclarativeLibraryBuildType)>.[release](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#\(org.gradle.api.NamedDomainObjectContainer\).release\(kotlin.Function1\))(  
action: [DeclarativeLibraryBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DeclarativeLibraryBuildType).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
)`  
  
### Public properties  
  
---  
`[MutableCollection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>?` |  `[aidlPackagedList](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#aidlPackagedList\(\))` Aidl files to package in the aar.  
`[LibraryAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryAndroidResources)` |  `[androidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#androidResources\(\))` Specifies options related to the processing of Android Resources.  
`[LibraryBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryBuildFeatures)` |  `[buildFeatures](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#buildFeatures\(\))` A list of build features that can be enabled or disabled on the Android Project.  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DeclarativeLibraryBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DeclarativeLibraryBuildType)>` |  `[buildTypes](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#buildTypes\(\))` Encapsulates all build type configurations for this project.  
`[CompileOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CompileOptions)` |  `[compileOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#compileOptions\(\))` Specifies Java compiler options.  
`[ComposeOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ComposeOptions)` |  `[composeOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#composeOptions\(\))`  
`[DataBinding](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding)` |  `[dataBinding](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#dataBinding\(\))` Specifies options for the Data Binding Library.  
`[LibraryDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDefaultConfig)` |  `[defaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#defaultConfig\(\))` Specifies defaults for variant properties.  
`[DependenciesExtension](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DependenciesExtension)` |  `[dependencies](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#dependencies\(\))`  
`[ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuild)` |  `[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#externalNativeBuild\(\))` Specifies options for external native build using CMake or ndk-build.  
`[LibraryInstallation](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryInstallation)` |  `[installation](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#installation\(\))` Specifies options for the Android Debug Bridge (ADB).  
`[Lint](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Lint)` |  `[lint](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#lint\(\))` Specifies options for the lint tool.  
`[Packaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Packaging)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#packaging\(\))`  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[Prefab](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Prefab)>` |  `[prefab](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#prefab\(\))` container of Prefab options  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DeclarativeLibraryFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DeclarativeLibraryFlavor)>` |  `[productFlavors](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#productFlavors\(\))` Encapsulates all product flavors configurations for this project.  
`[LibraryPublishing](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryPublishing)` |  `[publishing](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#publishing\(\))` Customizes publishing build variant artifacts from library module to a Maven repository.  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApkSigningConfig)>` |  `[signingConfigs](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#signingConfigs\(\))` Encapsulates signing configurations.  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[AndroidLibrarySourceSet](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidLibrarySourceSet)>` |  `[sourceSets](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#sourceSets\(\))` Encapsulates source set configurations for all variants.  
`[Splits](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Splits)` |  `[splits](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#splits\(\))` Specifies configurations for building multiple APKs or APK splits.  
`[TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestCoverage)` |  `[testCoverage](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#testCoverage\(\))` Configure the gathering of code-coverage from tests.  
`[TestOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions)` |  `[testOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#testOptions\(\))` Specifies options for how the Android plugin should run local and instrumented tests.  
`[ViewBinding](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ViewBinding)` |  `[viewBinding](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#viewBinding\(\))` Specifies options for the View Binding Library.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.CommonDeclarativeDefinition](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CommonDeclarativeDefinition) | `[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[getDefaultProguardFile](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CommonDeclarativeDefinition#getDefaultProguardFile\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))`  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[useLibrary](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CommonDeclarativeDefinition#useLibrary\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Includes the specified library to the classpath.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[useLibrary](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CommonDeclarativeDefinition#useLibrary\(kotlin.String,kotlin.Boolean\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), required: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))`  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.CommonDeclarativeDefinition](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CommonDeclarativeDefinition) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CommonDeclarativeDefinition#buildToolsVersion\(\))` Specifies the version of the SDK Build Tools to use.  
---|---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CommonDeclarativeDefinition#compileSdk\(\))` Specifies the API level to compile your project against.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableKotlin](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CommonDeclarativeDefinition#enableKotlin\(\))` Enables the compilation of Kotlin sources.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[experimentalProperties](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CommonDeclarativeDefinition#experimentalProperties\(\))` Additional per module experimental properties.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[flavorDimensions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CommonDeclarativeDefinition#flavorDimensions\(\))` Specifies the names of product flavor dimensions for this project.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[namespace](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CommonDeclarativeDefinition#namespace\(\))` The namespace of the generated R and BuildConfig classes.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[ndkPath](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CommonDeclarativeDefinition#ndkPath\(\))` Requires the specified path to NDK be used.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[ndkVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CommonDeclarativeDefinition#ndkVersion\(\))` Requires the specified NDK version to be used.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[resourcePrefix](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CommonDeclarativeDefinition#resourcePrefix\(\))` Specifies this project's resource prefix to Android Studio for editor features.  
  
From [com.android.build.api.dsl.TestedDeclarativeDefinition](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestedDeclarativeDefinition) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[testBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestedDeclarativeDefinition#testBuildType\(\))` Specifies the build type that the plugin should use to test the module.  
---|---  
`[TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestFixtures)` |  `[testFixtures](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestedDeclarativeDefinition#testFixtures\(\))` Options to configure the test fixtures.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[testNamespace](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestedDeclarativeDefinition#testNamespace\(\))` The namespace used by the android test and unit test components.  
  
## Public functions

### debug

Added in 9.4.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DeclarativeLibraryBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DeclarativeLibraryBuildType)>.[debug](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#\(org.gradle.api.NamedDomainObjectContainer\).debug\(kotlin.Function1\))(  
        action: [DeclarativeLibraryBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DeclarativeLibraryBuildType).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### release

Added in 9.4.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DeclarativeLibraryBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DeclarativeLibraryBuildType)>.[release](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#\(org.gradle.api.NamedDomainObjectContainer\).release\(kotlin.Function1\))(  
        action: [DeclarativeLibraryBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DeclarativeLibraryBuildType).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

## Public properties

### aidlPackagedList

Added in 9.4.1
    
    
    val [aidlPackagedList](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#aidlPackagedList\(\)): [MutableCollection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>?

Aidl files to package in the aar.

### androidResources

Added in 9.4.1
    
    
    val [androidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#androidResources\(\)): [LibraryAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryAndroidResources)

Specifies options related to the processing of Android Resources.

### buildFeatures

Added in 9.4.1
    
    
    val [buildFeatures](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#buildFeatures\(\)): [LibraryBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryBuildFeatures)

A list of build features that can be enabled or disabled on the Android Project.

### buildTypes

Added in 9.4.1
    
    
    val [buildTypes](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#buildTypes\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DeclarativeLibraryBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DeclarativeLibraryBuildType)>

Encapsulates all build type configurations for this project.

### compileOptions

Added in 9.4.1
    
    
    val [compileOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#compileOptions\(\)): [CompileOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CompileOptions)

Specifies Java compiler options.

### composeOptions

Added in 9.4.1
    
    
    val [composeOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#composeOptions\(\)): [ComposeOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ComposeOptions)

### dataBinding

Added in 9.4.1
    
    
    val [dataBinding](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#dataBinding\(\)): [DataBinding](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding)

Specifies options for the Data Binding Library.

### defaultConfig

Added in 9.4.1
    
    
    val [defaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#defaultConfig\(\)): [LibraryDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDefaultConfig)

Specifies defaults for variant properties.

### dependencies

Added in 9.4.1
    
    
    val [dependencies](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#dependencies\(\)): [DependenciesExtension](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DependenciesExtension)

### externalNativeBuild

Added in 9.4.1
    
    
    val [externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#externalNativeBuild\(\)): [ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuild)

Specifies options for external native build using CMake or ndk-build.

### installation

Added in 9.4.1
    
    
    val [installation](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#installation\(\)): [LibraryInstallation](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryInstallation)

Specifies options for the Android Debug Bridge (ADB).

### lint

Added in 9.4.1
    
    
    val [lint](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#lint\(\)): [Lint](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Lint)

Specifies options for the lint tool.

### packaging

Added in 9.4.1
    
    
    val [packaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#packaging\(\)): [Packaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Packaging)

### prefab

Added in 9.4.1
    
    
    val [prefab](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#prefab\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[Prefab](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Prefab)>

container of Prefab options

### productFlavors

Added in 9.4.1
    
    
    val [productFlavors](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#productFlavors\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DeclarativeLibraryFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DeclarativeLibraryFlavor)>

Encapsulates all product flavors configurations for this project.

### publishing

Added in 9.4.1
    
    
    val [publishing](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#publishing\(\)): [LibraryPublishing](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryPublishing)

Customizes publishing build variant artifacts from library module to a Maven repository.

### signingConfigs

Added in 9.4.1
    
    
    val [signingConfigs](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#signingConfigs\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApkSigningConfig)>

Encapsulates signing configurations.

### sourceSets

Added in 9.4.1
    
    
    val [sourceSets](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#sourceSets\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[AndroidLibrarySourceSet](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidLibrarySourceSet)>

Encapsulates source set configurations for all variants.

### splits

Added in 9.4.1
    
    
    val [splits](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#splits\(\)): [Splits](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Splits)

Specifies configurations for building multiple APKs or APK splits.

### testCoverage

Added in 9.4.1
    
    
    val [testCoverage](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#testCoverage\(\)): [TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestCoverage)

Configure the gathering of code-coverage from tests.

### testOptions

Added in 9.4.1
    
    
    val [testOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#testOptions\(\)): [TestOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions)

Specifies options for how the Android plugin should run local and instrumented tests.

### viewBinding

Added in 9.4.1
    
    
    val [viewBinding](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDeclarativeDefinition#viewBinding\(\)): [ViewBinding](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ViewBinding)

Specifies options for the View Binding Library.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
