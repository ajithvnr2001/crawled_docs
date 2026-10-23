---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension/
title: CommonExtension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:27:58.022629+00:00
---

# CommonExtension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# CommonExtension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/CommonExtension.kt+class:com.android.build.api.dsl.CommonExtension)

Added in 4.2.0
    
    
    interface [CommonExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension) : [ExtensionAware](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html)

Known direct subclasses 

[ApplicationExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApplicationExtension), [DynamicFeatureExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DynamicFeatureExtension), [LibraryExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryExtension), [TestExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestExtension)

`[ApplicationExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApplicationExtension)` |  Extension for the Android Gradle Plugin Application plugin.  
---|---  
`[DynamicFeatureExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DynamicFeatureExtension)` |  Extension for the Android Dynamic Feature Gradle Plugin.  
`[LibraryExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryExtension)` |  Extension for the Android Library Gradle Plugin.  
`[TestExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestExtension)` |  Extension for the Android Test Gradle Plugin.  
  
* * *

Common extension properties for the Android Application. Library and Dynamic Feature Plugins.

Only the Android Gradle Plugin should create instances of this interface.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#buildToolsVersion\(kotlin.String\))~~(buildToolsVersion: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by buildToolsVersion property  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileSdk\(kotlin.Function1\))(action: [CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CompileSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding compile Sdk version, see `[CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CompileSdkSpec)` for more details.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compileSdkAddon](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileSdkAddon\(kotlin.String,kotlin.String,kotlin.Int\))(vendor: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Specify an SDK add-on to compile your project against.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[compileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileSdkVersion\(kotlin.Int\))~~(apiLevel: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` **This function is deprecated.** Will be removed in AGP 10.0, replaced by the compileSdk block  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[compileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileSdkVersion\(kotlin.String\))~~(version: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Will be removed in AGP 10.0, replaced by the compileSdk block  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)` |  `[getDefaultProguardFile](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#getDefaultProguardFile\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[useLibrary](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#useLibrary\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Includes the specified library to the classpath.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[useLibrary](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#useLibrary\(kotlin.String,kotlin.Boolean\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), required: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Includes the specified library to the classpath.  
  
### Public properties  
  
---  
`[AaptOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AaptOptions)` |  `[aaptOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#aaptOptions\(\))` **This property is deprecated.** Replaced by androidResources  
`[AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AdbOptions)` |  `[adbOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#adbOptions\(\))` **This property is deprecated.** Replaced by installation  
`[AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidResources)` |  `[androidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#androidResources\(\))` Specifies options related to the processing of Android Resources.  
`[BuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BuildFeatures)` |  `[buildFeatures](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#buildFeatures\(\))` A list of build features that can be enabled or disabled on the Android Project.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#buildToolsVersion\(\))` Specifies the version of the [SDK Build Tools](https://developer.android.com/studio/releases/build-tools.html) to use when building your project.  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[BuildType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BuildType)>` |  `[buildTypes](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#buildTypes\(\))` Encapsulates all build type configurations for this project.  
`[CompileOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CompileOptions)` |  `[compileOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileOptions\(\))` Specifies Java compiler options, such as the language level of the Java source code and generated bytecode.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileSdk\(\))` Specifies the API level to compile your project against.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdkExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileSdkExtension\(\))` Specifies the SDK Extension level to compile your project against.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdkMinor](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileSdkMinor\(\))` Specify a minor API version for the compile SDK.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[compileSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileSdkPreview\(\))` Specify a preview API to compile your project against.  
`[ComposeOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ComposeOptions)` |  `[composeOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#composeOptions\(\))`  
`[DataBinding](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DataBinding)` |  `[dataBinding](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#dataBinding\(\))` Specifies options for the [Data Binding Library](https://developer.android.com/topic/libraries/data-binding/index.html).  
`[DefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DefaultConfig)` |  `[defaultConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#defaultConfig\(\))` Specifies defaults for variant properties that the Android plugin applies to all build variants.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableKotlin](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#enableKotlin\(\))` Enables the compilation of Kotlin sources.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[experimentalProperties](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#experimentalProperties\(\))` Additional per module experimental properties.  
`[ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ExternalNativeBuild)` |  `[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#externalNativeBuild\(\))` Specifies options for external native build using [CMake](https://cmake.org/) or [ndk-build](https://developer.android.com/ndk/guides/ndk-build.html).  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[flavorDimensions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#flavorDimensions\(\))` Specifies the names of product flavor dimensions for this project.  
`[Installation](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Installation)` |  `[installation](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#installation\(\))` Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.  
`[JacocoOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JacocoOptions)` |  `[jacoco](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#jacoco\(\))` **This property is deprecated.** Renamed to testCoverage  
`[Lint](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Lint)` |  `[lint](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#lint\(\))` Specifies options for the lint tool.  
`[LintOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LintOptions)` |  `[lintOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#lintOptions\(\))` **This property is deprecated.** Renamed to lint  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[namespace](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#namespace\(\))` The namespace of the generated R and BuildConfig classes.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[ndkPath](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#ndkPath\(\))` Requires the specified path to NDK be used.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[ndkVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#ndkVersion\(\))` Requires the specified NDK version to be used.  
`[Packaging](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Packaging)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#packaging\(\))` Specifies options and rules that determine which files the Android plugin packages into your APK.  
`[Packaging](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Packaging)` |  `[packagingOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#packagingOptions\(\))` **This property is deprecated.** Renamed to packaging  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ProductFlavor)>` |  `[productFlavors](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#productFlavors\(\))` Encapsulates all product flavors configurations for this project.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[resourcePrefix](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#resourcePrefix\(\))` Specifies this project's resource prefix to Android Studio for editor features, such as Lint checks.  
`[SdkComponents](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SdkComponents)` |  `[sdkComponents](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#sdkComponents\(\))`  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApkSigningConfig)>` |  `[signingConfigs](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#signingConfigs\(\))` Encapsulates signing configurations that you can apply to [ ] and [ ] configurations.  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet)>` |  `[sourceSets](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#sourceSets\(\))` Encapsulates source set configurations for all variants.  
`[Splits](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Splits)` |  `[splits](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#splits\(\))` Specifies configurations for [building multiple APKs](https://developer.android.com/studio/build/configure-apk-splits.html) or APK splits.  
`[TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestCoverage)` |  `[testCoverage](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#testCoverage\(\))` Configure the gathering of code-coverage from tests.  
`[TestOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestOptions)` |  `[testOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#testOptions\(\))` Specifies options for how the Android plugin should run local and instrumented tests.  
`[ViewBinding](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ViewBinding)` |  `[viewBinding](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#viewBinding\(\))` Specifies options for the [View Binding Library](https://developer.android.com/topic/libraries/view-binding/index.html).  
  
### Inherited functions  
  
---  
From [org.gradle.api.plugins.ExtensionAware](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html) | `[ExtensionContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionContainer.html)` |  `@[Internal](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/Internal.html)  
@[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.3/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
[getExtensions](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html#getExtensions--)()`  
---|---  
  
## Public functions

### buildToolsVersion

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#buildToolsVersion\(kotlin.String\))~~(buildToolsVersion: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by buildToolsVersion property

### compileSdk

Added in 8.12.0
    
    
    fun [compileSdk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileSdk\(kotlin.Function1\))(action: [CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CompileSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures all aspects regarding compile Sdk version, see `[CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CompileSdkSpec)` for more details.

### compileSdkAddon

Added in 4.2.0
    
    
    fun [compileSdkAddon](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileSdkAddon\(kotlin.String,kotlin.String,kotlin.Int\))(vendor: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specify an SDK add-on to compile your project against.

This can be set on all Gradle projects with `[com.android.build.api.dsl.SettingsExtension.compileSdkAddon](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SettingsExtension#compileSdkAddon\(kotlin.String,kotlin.String,kotlin.Int\))`

Parameters  
---  
`vendor: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the vendor name of the add-on.  
`name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the name of the add-on  
`version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  the integer API level of the add-on  
  
### compileSdkVersion

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[compileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileSdkVersion\(kotlin.Int\))~~(apiLevel: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Will be removed in AGP 10.0, replaced by the compileSdk block

### compileSdkVersion

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[compileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileSdkVersion\(kotlin.String\))~~(version: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Will be removed in AGP 10.0, replaced by the compileSdk block

### getDefaultProguardFile

Added in 7.0.0
    
    
    fun [getDefaultProguardFile](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#getDefaultProguardFile\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)

### useLibrary

Added in 4.2.0
    
    
    fun [useLibrary](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#useLibrary\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

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

Added in 4.2.0
    
    
    fun [useLibrary](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#useLibrary\(kotlin.String,kotlin.Boolean\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), required: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

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
  
## Public properties

### aaptOptions

Added in 4.2.0

Deprecated in 7.0.0
    
    
    val [aaptOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#aaptOptions\(\)): [AaptOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AaptOptions)

**This property is deprecated.**  
Replaced by androidResources

Specifies options for the Android Asset Packaging Tool (AAPT).

For more information about the properties you can configure in this block, see `[AaptOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AaptOptions)`.

### adbOptions

Added in 4.2.0

Deprecated in 7.0.0
    
    
    val [adbOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#adbOptions\(\)): [AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AdbOptions)

**This property is deprecated.**  
Replaced by installation

Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.

For more information about the properties you can configure in this block, see `[AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AdbOptions)`.

### androidResources

Added in 7.0.0
    
    
    val [androidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#androidResources\(\)): [AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidResources)

Specifies options related to the processing of Android Resources.

For more information about the properties you can configure in this block, see `[AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidResources)`.

### buildFeatures

Added in 4.2.0
    
    
    val [buildFeatures](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#buildFeatures\(\)): [BuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BuildFeatures)

A list of build features that can be enabled or disabled on the Android Project.

### buildToolsVersion

Added in 4.2.0
    
    
    var [buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#buildToolsVersion\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Specifies the version of the [SDK Build Tools](https://developer.android.com/studio/releases/build-tools.html) to use when building your project.

When using Android plugin 3.0.0 or later, configuring this property is optional. By default, the plugin uses the minimum version of the build tools required by the [version of the plugin](https://developer.android.com/studio/releases/gradle-plugin.html#revisions) you're using. To specify a different version of the build tools for the plugin to use, specify the version as follows:
    
    
    android {  
        // Specifying this property is optional.  
        buildToolsVersion "26.0.0"  
    }

For a list of build tools releases, read [the release notes](https://developer.android.com/studio/releases/build-tools.html#notes).

Note that the value assigned to this property is parsed and stored in a normalized form, so reading it back may give a slightly different result.

This can be set on all Gradle projects with `[com.android.build.api.dsl.SettingsExtension.buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SettingsExtension#buildToolsVersion\(\))`

### buildTypes

Added in 4.2.0
    
    
    val [buildTypes](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#buildTypes\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[BuildType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BuildType)>

Encapsulates all build type configurations for this project.

Unlike using `[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ProductFlavor)` to create different versions of your project that you expect to co-exist on a single device, build types determine how Gradle builds and packages each version of your project. Developers typically use them to configure projects for various stages of a development lifecycle. For example, when creating a new project from Android Studio, the Android plugin configures a 'debug' and 'release' build type for you. By default, the 'debug' build type enables debugging options and signs your APK with a generic debug keystore. Conversely, The 'release' build type strips out debug symbols and requires you to [create a release key and keystore](https://developer.android.com/studio/publish/app-signing.html#sign-apk) for your app. You can then combine build types with product flavors to [create build variants](https://developer.android.com/studio/build/build-variants.html).

See also  
---  
`[BuildType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BuildType)` |   
  
### compileOptions

Added in 4.2.0
    
    
    val [compileOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileOptions\(\)): [CompileOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CompileOptions)

Specifies Java compiler options, such as the language level of the Java source code and generated bytecode.

For more information about the properties you can configure in this block, see `[CompileOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CompileOptions)`.

### compileSdk

Added in 4.2.0
    
    
    var [compileSdk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Specifies the API level to compile your project against. The Android plugin requires you to configure this property.

This means your code can use only the Android APIs included in that API level and lower. You can configure the compile sdk version by adding the following to the `android` block: `compileSdk = 26`.

You should generally [use the most up-to-date API level](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels) available. If you are planning to also support older API levels, it's good practice to [use the Lint tool](https://developer.android.com/studio/write/lint.html) to check if you are using APIs that are not available in earlier API levels.

The value you assign to this property is parsed and stored in a normalized form, so reading it back may return a slightly different value.

This can be set on all Gradle projects with `[com.android.build.api.dsl.SettingsExtension.compileSdk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SettingsExtension#compileSdk\(kotlin.Function1\))`

### compileSdkExtension

Added in 7.1.0
    
    
    var [compileSdkExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileSdkExtension\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Specifies the SDK Extension level to compile your project against. This value is optional.

When not provided the base extension for the given `compileSdk` API level will be selected.

This can be set on all Gradle projects with `[com.android.build.api.dsl.SettingsExtension.compileSdkExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SettingsExtension#compileSdkExtension\(\))`

### compileSdkMinor

Added in 8.10.1
    
    
    var [compileSdkMinor](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileSdkMinor\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Specify a minor API version for the compile SDK. This should be used with the compileSdk property to specify a full SDK version.

### compileSdkPreview

Added in 4.2.0
    
    
    var [compileSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#compileSdkPreview\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Specify a preview API to compile your project against.

For example, to try out the Android S preview, rather than `compileSdk = 30` you can use `compileSdkPreview = "S"`

Once the preview APIs are finalized, they will be allocated a stable integer value.

This can be set on all Gradle projects with `[com.android.build.api.dsl.SettingsExtension.compileSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SettingsExtension#compileSdkPreview\(\))`

### composeOptions

Added in 4.2.0
    
    
    val [composeOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#composeOptions\(\)): [ComposeOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ComposeOptions)

### dataBinding

Added in 4.2.0
    
    
    val [dataBinding](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#dataBinding\(\)): [DataBinding](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DataBinding)

Specifies options for the [Data Binding Library](https://developer.android.com/topic/libraries/data-binding/index.html).

For more information about the properties you can configure in this block, see `[DataBinding](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DataBinding)`

### defaultConfig

Added in 4.2.0
    
    
    val [defaultConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#defaultConfig\(\)): [DefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DefaultConfig)

Specifies defaults for variant properties that the Android plugin applies to all build variants.

You can override any `defaultConfig` property when [configuring product flavors](https://developer.android.com/studio/build/build-variants.html#product-flavors)

For more information about the properties you can configure in this block, see `[DefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DefaultConfig)`.

### enableKotlin

Added in 9.3.3
    
    
    var [enableKotlin](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#enableKotlin\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Enables the compilation of Kotlin sources. The default value is `true`.

### experimentalProperties

Added in 7.0.0
    
    
    val [experimentalProperties](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#experimentalProperties\(\)): [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>

Additional per module experimental properties.

Values provided should not be based on a Task execution result, as most of these properties are read during configuration.

### externalNativeBuild

Added in 4.2.0
    
    
    val [externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#externalNativeBuild\(\)): [ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ExternalNativeBuild)

Specifies options for external native build using [CMake](https://cmake.org/) or [ndk-build](https://developer.android.com/ndk/guides/ndk-build.html).

When using [Android Studio 2.2 or higher](https://developer.android.com/studio/index.html) with [Android plugin 2.2.0 or higher](https://developer.android.com/studio/releases/gradle-plugin.html), you can compile C and C++ code into a native library that Gradle packages into your APK.

To learn more, read [Add C and C++ Code to Your Project](https://developer.android.com/studio/projects/add-native-code.html).

See also  
---  
`[ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ExternalNativeBuild)` |  since 2.2.0  
  
### flavorDimensions

Added in 4.2.0
    
    
    val [flavorDimensions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#flavorDimensions\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies the names of product flavor dimensions for this project.

When configuring product flavors with Android plugin 3.0.0 and higher, you must specify at least one flavor dimension, using the `[`flavorDimensions`](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#flavorDimensions\(\))` property, and then assign each flavor to a dimension. Otherwise, you will get the following build error:
    
    
    Error:All flavors must now belong to a named flavor dimension.  
    The flavor 'flavor_name' is not assigned to a flavor dimension.

By default, when you specify only one dimension, all flavors you configure automatically belong to that dimension. If you specify more than one dimension, you need to manually assign each flavor to a dimension, as shown in the sample below.

Flavor dimensions allow you to create groups of product flavors that you can combine with flavors from other flavor dimensions. For example, you can have one dimension that includes a 'free' and 'paid' version of your app, and another dimension for flavors that support different API levels, such as 'minApi21' and 'minApi24'. The Android plugin can then combine flavors from these dimensions—including their settings, code, and resources—to create variants such as 'debugFreeMinApi21' and 'releasePaidMinApi24', and so on. The sample below shows you how to specify flavor dimensions and add product flavors to them.
    
    
    android {  
        ...  
        // Specifies the flavor dimensions you want to use. The order in which you  
        // list each dimension determines its priority, from highest to lowest,  
        // when Gradle merges variant sources and configurations. You must assign  
        // each product flavor you configure to one of the flavor dimensions.  
        flavorDimensions 'api', 'version'  
      
        productFlavors {  
          demo {  
            // Assigns this product flavor to the 'version' flavor dimension.  
            dimension 'version'  
            ...  
        }  
      
          full {  
            dimension 'version'  
            ...  
          }  
      
          minApi24 {  
            // Assigns this flavor to the 'api' dimension.  
            dimension 'api'  
            minSdkVersion '24'  
            versionNameSuffix "-minApi24"  
            ...  
          }  
      
          minApi21 {  
            dimension "api"  
            minSdkVersion '21'  
            versionNameSuffix "-minApi21"  
            ...  
          }  
       }  
    }

To learn more, read [Combine multiple flavors](https://developer.android.com/studio/build/build-variants.html#flavor-dimensions).

### installation

Added in 7.0.0
    
    
    val [installation](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#installation\(\)): [Installation](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Installation)

Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.

For more information about the properties you can configure in this block, see `[AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AdbOptions)`.

### jacoco

Added in 4.2.0

Deprecated in 7.0.0
    
    
    val [jacoco](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#jacoco\(\)): [JacocoOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JacocoOptions)

**This property is deprecated.**  
Renamed to testCoverage

Configure the gathering of code-coverage from tests.

This is replaced by `[testCoverage](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#testCoverage\(\))`.

### lint

Added in 7.0.0
    
    
    val [lint](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#lint\(\)): [Lint](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Lint)

Specifies options for the lint tool.

For more information about the properties you can configure in this block, see `[Lint](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Lint)`.

### lintOptions

Added in 4.2.0

Deprecated in 7.0.0
    
    
    val [lintOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#lintOptions\(\)): [LintOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LintOptions)

**This property is deprecated.**  
Renamed to lint

Specifies options for the lint tool.

For more information about the properties you can configure in this block, see `[LintOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LintOptions)`.

### namespace

Added in 4.2.0
    
    
    var [namespace](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#namespace\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The namespace of the generated R and BuildConfig classes. Also, the namespace used to resolve any relative class names that are declared in the AndroidManifest.xml.

### ndkPath

Added in 4.2.0
    
    
    var [ndkPath](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#ndkPath\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Requires the specified path to NDK be used.

Use this to specify a path to the NDK folder to be used for C and C++ builds.
    
    
    android {  
        // Path to custom NDK location  
        ndkPath '/path/to/ndk'  
    }

If this field is specified, then the version it refers to need to match the one specified in ndkVersion. If ndkVersion is not specified, ndkPath need to match the default ndkVersion

For additional information about NDK installation see [Install and configure the NDK](https://developer.android.com/studio/projects/install-ndk).

This can be set on all Gradle projects with `[com.android.build.api.dsl.SettingsExtension.ndkPath](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SettingsExtension#ndkPath\(\))`

### ndkVersion

Added in 4.2.0
    
    
    var [ndkVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#ndkVersion\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Requires the specified NDK version to be used.

Use this to specify a fixed NDK version. Without this, each new version of the Android Gradle Plugin will choose a specific version of NDK to use, so upgrading the plugin also means upgrading the NDK. Locking to a specific version can increase repeatability of the build.
    
    
    android {  
        // Use a fixed NDK version  
        ndkVersion '20.1.5948944'  
    }

If this field is specified then android.ndkPath may not be specified. If this field is not specified, a default value will be provided depending on the AGP version

The required format of the version is `major.minor.build`. It's not legal to specify less precision. If `ndk.dir` is specified in `local.properties` file then the NDK that it points to must match the `android.ndkVersion`.

Prior to Android Gradle Plugin version 3.5, the highest installed version of NDK will be used. In Android Gradle Plugin 3.4, specifying `android.ndkVersion` was not an error, but the value would be ignored. Prior to Android Gradle Plugin version 3.4, it was illegal to specify `android.ndkVersion`.

For additional information about NDK installation see [Install and configure the NDK](https://developer.android.com/studio/projects/install-ndk).

This can be set on all Gradle projects with `[com.android.build.api.dsl.SettingsExtension.ndkVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SettingsExtension#ndkVersion\(\))`

### packaging

Added in 8.0.2
    
    
    val [packaging](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#packaging\(\)): [Packaging](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Packaging)

Specifies options and rules that determine which files the Android plugin packages into your APK.

For more information about the properties you can configure in this block, see `[Packaging](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Packaging)`.

### packagingOptions

Added in 4.2.0

Deprecated in 8.0.2
    
    
    val [packagingOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#packagingOptions\(\)): [Packaging](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Packaging)

**This property is deprecated.**  
Renamed to packaging

Specifies options and rules that determine which files the Android plugin packages into your APK.

For more information about the properties you can configure in this block, see `[Packaging](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Packaging)`.

### productFlavors

Added in 4.2.0
    
    
    val [productFlavors](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#productFlavors\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ProductFlavor)>

Encapsulates all product flavors configurations for this project.

Product flavors represent different versions of your project that you expect to co-exist on a single device, the Google Play store, or repository. For example, you can configure 'demo' and 'full' product flavors for your app, and each of those flavors can specify different features, device requirements, resources, and application ID's--while sharing common source code and resources. So, product flavors allow you to output different versions of your project by simply changing only the components and settings that are different between them.

Configuring product flavors is similar to [configuring build types](https://developer.android.com/studio/build/build-variants.html#build-types): add them to the `productFlavors` block of your project's `build.gradle` file and configure the settings you want. Product flavors support the same properties as the `defaultConfig` block--this is because `defaultConfig` defines an object that the plugin uses as the base configuration for all other flavors. Each flavor you configure can then override any of the default values in `defaultConfig`, such as the [`applicationId`](https://d.android.com/studio/build/application-id.html).

When using Android plugin 3.0.0 and higher, _each flavor must belong to a com.android.build.gradle.BaseExtension.html#com.android.build.gradle.BaseExtension:flavorDimensions(java.lang.String[]) value_. By default, when you specify only one dimension, all flavors you configure belong to that dimension. If you specify more than one flavor dimension, you need to manually assign each flavor to a dimension. To learn more, read [Use Flavor Dimensions for variant-aware dependency management](https://developer.android.com/studio/build/gradle-plugin-3-0-0-migration.html#variant_aware).

When you configure product flavors, the Android plugin automatically combines them with your `[BuildType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BuildType)` configurations to [create build variants](https://developer.android.com/studio/build/build-variants.html). If the plugin creates certain build variants that you don't want, you can [filter variants](https://developer.android.com/studio/build/build-variants.html#filter-variants).

See also  
---  
`[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ProductFlavor)` |   
  
### resourcePrefix

Added in 4.2.0
    
    
    var [resourcePrefix](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#resourcePrefix\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Specifies this project's resource prefix to Android Studio for editor features, such as Lint checks. This property is useful only when using Android Studio.

Including unique prefixes for project resources helps avoid naming collisions with resources from other projects.

For example, when creating a library with String resources, you may want to name each resource with a unique prefix, such as "`mylib_`" to avoid naming collisions with similar resources that the consumer defines.

You can then specify this prefix, as shown below, so that Android Studio expects this prefix when you name project resources:
    
    
    // This property is useful only when developing your project in Android Studio.  
    resourcePrefix 'mylib_'

### sdkComponents

Added in 4.2.0

Deprecated in 4.2.0
    
    
    val [sdkComponents](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#sdkComponents\(\)): [SdkComponents](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SdkComponents)

### signingConfigs

Added in 4.2.0
    
    
    val [signingConfigs](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#signingConfigs\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApkSigningConfig)>

Encapsulates signing configurations that you can apply to [ ] and [ ] configurations.

Android requires that all APKs be digitally signed with a certificate before they can be installed onto a device. When deploying a debug version of your project from Android Studio, the Android plugin automatically signs your APK with a generic debug certificate. However, to build an APK for release, you must [sign the APK](https://developer.android.com/studio/publish/app-signing.html) with a release key and keystore. You can do this by either [using the Android Studio UI](https://developer.android.com/studio/publish/app-signing.html#sign-apk) or manually [configuring your `build.gradle` file](https://developer.android.com/studio/publish/app-signing.html#gradle-sign).

See also  
---  
`[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApkSigningConfig)` |   
  
### sourceSets

Added in 4.2.0
    
    
    val [sourceSets](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#sourceSets\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet)>

Encapsulates source set configurations for all variants.

Note that the Android plugin uses its own implementation of source sets. For more information about the properties you can configure in this block, see `[AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet)`.

### splits

Added in 4.2.0
    
    
    val [splits](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#splits\(\)): [Splits](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Splits)

Specifies configurations for [building multiple APKs](https://developer.android.com/studio/build/configure-apk-splits.html) or APK splits.

For more information about the properties you can configure in this block, see `[Splits](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Splits)`.

### testCoverage

Added in 7.0.0
    
    
    val [testCoverage](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#testCoverage\(\)): [TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestCoverage)

Configure the gathering of code-coverage from tests.

To override the JaCoCo version that is used for offline instrumentation and coverage report, add the following to `build.gradle` file:
    
    
    android {  
        testCoverage {  
            jacocoVersion "<jacoco-version>"  
        }  
    }

For more information about the properties you can configure in this block, see `[TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestCoverage)`.

### testOptions

Added in 4.2.0
    
    
    val [testOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#testOptions\(\)): [TestOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestOptions)

Specifies options for how the Android plugin should run local and instrumented tests.

For more information about the properties you can configure in this block, see `[TestOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestOptions)`.

### viewBinding

Added in 7.3.0
    
    
    val [viewBinding](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension#viewBinding\(\)): [ViewBinding](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ViewBinding)

Specifies options for the [View Binding Library](https://developer.android.com/topic/libraries/view-binding/index.html).

For more information about the properties you can configure in this block, see `[ViewBinding](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ViewBinding)`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
