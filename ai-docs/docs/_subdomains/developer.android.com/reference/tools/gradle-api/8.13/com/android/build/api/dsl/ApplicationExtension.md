---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension/
title: ApplicationExtension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:30:37.639967+00:00
---

# ApplicationExtension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ApplicationExtension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ApplicationExtension.kt+class:com.android.build.api.dsl.ApplicationExtension)

Added in 4.2.0
    
    
    interface [ApplicationExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension) : [CommonExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension), [ApkExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApkExtension), [TestedExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestedExtension)

* * *

Extension for the Android Gradle Plugin Application plugin.

This is the `android` block when the `com.android.application` plugin is applied.

Only the Android Gradle Plugin should create instances of interfaces in com.android.build.api.dsl.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[bundle](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#bundle\(kotlin.Function1\))(action: [Bundle](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[dependenciesInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#dependenciesInfo\(kotlin.Function1\))(action: [DependenciesInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DependenciesInfo).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specify whether to include SDK dependency information in APKs and Bundles.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[privacySandbox](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#privacySandbox\(kotlin.Function1\))(action: [PrivacySandbox](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PrivacySandbox).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[publishing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#publishing\(kotlin.Function1\))(action: [ApplicationPublishing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationPublishing).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Customizes publishing build variant artifacts from app module to a Maven repository.  
  
### Public properties  
  
---  
`[ApplicationAndroidResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationAndroidResources)` |  `[androidResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#androidResources\(\))` Specifies options related to the processing of Android Resources.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[assetPacks](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#assetPacks\(\))` Set of asset pack subprojects to be included in the app's bundle.  
`[Bundle](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle)` |  `[bundle](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#bundle\(\))`  
`[DependenciesInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DependenciesInfo)` |  `[dependenciesInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#dependenciesInfo\(\))` Specify whether to include SDK dependency information in APKs and Bundles.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[dynamicFeatures](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#dynamicFeatures\(\))`  
`[ApplicationInstallation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationInstallation)` |  `[installation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#installation\(\))` Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.  
`[PrivacySandbox](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PrivacySandbox)` |  `[privacySandbox](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#privacySandbox\(\))` Options related to the consumption of privacy sandbox libraries  
`[ApplicationPublishing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationPublishing)` |  `[publishing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#publishing\(\))` Customizes publishing build variant artifacts from app module to a Maven repository.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.CommonExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[aaptOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#aaptOptions\(kotlin.Function1\))~~(action: [AaptOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AaptOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Replaced by   
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[adbOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#adbOptions\(kotlin.Function1\))~~(action: [AdbOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AdbOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Replaced by installation  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[androidResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#androidResources\(kotlin.Function1\))(action: [ApplicationAndroidResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationAndroidResources).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options related to the processing of Android Resources.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[buildFeatures](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#buildFeatures\(kotlin.Function1\))(action: [ApplicationBuildFeatures](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationBuildFeatures).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` A list of build features that can be enabled or disabled on the Android Project.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#buildToolsVersion\(kotlin.String\))~~(buildToolsVersion: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by buildToolsVersion property  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[buildTypes](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#buildTypes\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationBuildType)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates all build type configurations for this project.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compileOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#compileOptions\(kotlin.Function1\))(action: [CompileOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CompileOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies Java compiler options, such as the language level of the Java source code and generated bytecode.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#compileSdk\(kotlin.Function1\))(action: [CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CompileSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding compile Sdk version, see `[CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CompileSdkSpec)` for more details.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compileSdkAddon](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#compileSdkAddon\(kotlin.String,kotlin.String,kotlin.Int\))(vendor: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Specify an SDK add-on to compile your project against.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[compileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#compileSdkVersion\(kotlin.Int\))~~(apiLevel: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` **This function is deprecated.** Will be removed in AGP 10.0, replaced by the compileSdk block  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[compileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#compileSdkVersion\(kotlin.String\))~~(version: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Will be removed in AGP 10.0, replaced by the compileSdk block  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[composeOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#composeOptions\(kotlin.Function1\))(action: [ComposeOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ComposeOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[dataBinding](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#dataBinding\(kotlin.Function1\))(action: [DataBinding](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DataBinding).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the [Data Binding Library](https://developer.android.com/topic/libraries/data-binding/index.html).  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationBuildType)>.[debug](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#\(org.gradle.api.NamedDomainObjectContainer\).debug\(kotlin.Function1\))(  
action: [ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationBuildType).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
)` Shortcut extension method to allow easy access to the predefined `debug` `[BuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[defaultConfig](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#defaultConfig\(kotlin.Function1\))(action: [ApplicationDefaultConfig](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationDefaultConfig).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies defaults for variant properties that the Android plugin applies to all build variants.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#externalNativeBuild\(kotlin.Function1\))(action: [ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ExternalNativeBuild).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for external native build using [CMake](https://cmake.org/) or [ndk-build](https://developer.android.com/ndk/guides/ndk-build.html).  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[flavorDimensions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#flavorDimensions\(kotlin.Array\))~~(vararg dimensions: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by flavorDimensions property  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)` |  `[getDefaultProguardFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#getDefaultProguardFile\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[installation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#installation\(kotlin.Function1\))(action: [ApplicationInstallation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationInstallation).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[jacoco](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#jacoco\(kotlin.Function1\))~~(action: [JacocoOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/JacocoOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Renamed to testCoverage  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[lint](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#lint\(kotlin.Function1\))(action: [Lint](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Lint).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the lint tool.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[lintOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#lintOptions\(kotlin.Function1\))~~(action: [LintOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Renamed to lint  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#packaging\(kotlin.Function1\))(action: [Packaging](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Packaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options and rules that determine which files the Android plugin packages into your APK.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[packagingOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#packagingOptions\(kotlin.Function1\))~~(action: [Packaging](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Packaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Renamed to packaging  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[productFlavors](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#productFlavors\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationProductFlavor)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates all product flavors configurations for this project.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationBuildType)>.[release](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#\(org.gradle.api.NamedDomainObjectContainer\).release\(kotlin.Function1\))(  
action: [ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationBuildType).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
)` Shortcut extension method to allow easy access to the predefined `release` `[BuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[signingConfigs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#signingConfigs\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApkSigningConfig)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates signing configurations that you can apply to `[BuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType)` and `[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ProductFlavor)` configurations.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[sourceSets](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#sourceSets\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AndroidSourceSet)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates source set configurations for all variants.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[splits](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#splits\(kotlin.Function1\))(action: [Splits](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies configurations for [building multiple APKs](https://developer.android.com/studio/build/configure-apk-splits.html) or APK splits.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[testCoverage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#testCoverage\(kotlin.Function1\))(action: [TestCoverage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestCoverage).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configure the gathering of code-coverage from tests.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[testOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#testOptions\(kotlin.Function1\))(action: [TestOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for how the Android plugin should run local and instrumented tests.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[useLibrary](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#useLibrary\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Includes the specified library to the classpath.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[useLibrary](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#useLibrary\(kotlin.String,kotlin.Boolean\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), required: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Includes the specified library to the classpath.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[viewBinding](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#viewBinding\(kotlin.Function1\))(action: [ViewBinding](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ViewBinding).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the [View Binding Library](https://developer.android.com/topic/libraries/view-binding/index.html).  
  
From [com.android.build.api.dsl.TestedExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestedExtension) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[testFixtures](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestedExtension#testFixtures\(kotlin.Function1\))(action: [TestFixtures](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestFixtures).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Options to configure the test fixtures.  
---|---  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.CommonExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension) | `[AaptOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AaptOptions)` |  `[aaptOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#aaptOptions\(\))` **This property is deprecated.** Replaced by   
---|---  
`[AdbOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AdbOptions)` |  `[adbOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#adbOptions\(\))` **This property is deprecated.** Replaced by installation  
`[ApplicationBuildFeatures](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationBuildFeatures)` |  `[buildFeatures](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#buildFeatures\(\))` A list of build features that can be enabled or disabled on the Android Project.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#buildToolsVersion\(\))` Specifies the version of the [SDK Build Tools](https://developer.android.com/studio/releases/build-tools.html) to use when building your project.  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationBuildType)>` |  `[buildTypes](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#buildTypes\(\))` Encapsulates all build type configurations for this project.  
`[CompileOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CompileOptions)` |  `[compileOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#compileOptions\(\))` Specifies Java compiler options, such as the language level of the Java source code and generated bytecode.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#compileSdk\(\))` Specifies the API level to compile your project against.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdkExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#compileSdkExtension\(\))` Specifies the SDK Extension level to compile your project against.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdkMinor](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#compileSdkMinor\(\))` Specify a minor API version for the compile SDK.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[compileSdkPreview](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#compileSdkPreview\(\))` Specify a preview API to compile your project against.  
`[ComposeOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ComposeOptions)` |  `[composeOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#composeOptions\(\))`  
`[DataBinding](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DataBinding)` |  `[dataBinding](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#dataBinding\(\))` Specifies options for the [Data Binding Library](https://developer.android.com/topic/libraries/data-binding/index.html).  
`[ApplicationDefaultConfig](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationDefaultConfig)` |  `[defaultConfig](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#defaultConfig\(\))` Specifies defaults for variant properties that the Android plugin applies to all build variants.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[experimentalProperties](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#experimentalProperties\(\))` Additional per module experimental properties.  
`[ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ExternalNativeBuild)` |  `[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#externalNativeBuild\(\))` Specifies options for external native build using [CMake](https://cmake.org/) or [ndk-build](https://developer.android.com/ndk/guides/ndk-build.html).  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[flavorDimensions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#flavorDimensions\(\))` Specifies the names of product flavor dimensions for this project.  
`[JacocoOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/JacocoOptions)` |  `[jacoco](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#jacoco\(\))` **This property is deprecated.** Renamed to testCoverage  
`[Lint](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Lint)` |  `[lint](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#lint\(\))` Specifies options for the lint tool.  
`[LintOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions)` |  `[lintOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#lintOptions\(\))` **This property is deprecated.** Renamed to lint  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[namespace](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#namespace\(\))` The namespace of the generated R and BuildConfig classes.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[ndkPath](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#ndkPath\(\))` Requires the specified path to NDK be used.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[ndkVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#ndkVersion\(\))` Requires the specified NDK version to be used.  
`[Packaging](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Packaging)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#packaging\(\))` Specifies options and rules that determine which files the Android plugin packages into your APK.  
`[Packaging](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Packaging)` |  `[packagingOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#packagingOptions\(\))` **This property is deprecated.** Renamed to packaging  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationProductFlavor)>` |  `[productFlavors](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#productFlavors\(\))` Encapsulates all product flavors configurations for this project.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[resourcePrefix](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#resourcePrefix\(\))` Specifies this project's resource prefix to Android Studio for editor features, such as Lint checks.  
`[SdkComponents](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/SdkComponents)` |  `[sdkComponents](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#sdkComponents\(\))`  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApkSigningConfig)>` |  `[signingConfigs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#signingConfigs\(\))` Encapsulates signing configurations that you can apply to [ ] and [ ] configurations.  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AndroidSourceSet)>` |  `[sourceSets](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#sourceSets\(\))` Encapsulates source set configurations for all variants.  
`[Splits](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits)` |  `[splits](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#splits\(\))` Specifies configurations for [building multiple APKs](https://developer.android.com/studio/build/configure-apk-splits.html) or APK splits.  
`[TestCoverage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestCoverage)` |  `[testCoverage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#testCoverage\(\))` Configure the gathering of code-coverage from tests.  
`[TestOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestOptions)` |  `[testOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#testOptions\(\))` Specifies options for how the Android plugin should run local and instrumented tests.  
`[ViewBinding](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ViewBinding)` |  `[viewBinding](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/CommonExtension#viewBinding\(\))` Specifies options for the [View Binding Library](https://developer.android.com/topic/libraries/view-binding/index.html).  
  
From [com.android.build.api.dsl.TestedExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestedExtension) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[testBuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestedExtension#testBuildType\(\))` Specifies the [build type](https://developer.android.com/studio/build/build-variants.html#build-types) that the plugin should use to test the module.  
---|---  
`[TestFixtures](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestFixtures)` |  `[testFixtures](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestedExtension#testFixtures\(\))` Options to configure the test fixtures.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[testNamespace](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestedExtension#testNamespace\(\))` The namespace used by the android test and unit test components for the generated R and BuildConfig classes.  
  
## Public functions

### bundle

Added in 4.2.0
    
    
    fun [bundle](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#bundle\(kotlin.Function1\))(action: [Bundle](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### dependenciesInfo

Added in 4.2.0
    
    
    fun [dependenciesInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#dependenciesInfo\(kotlin.Function1\))(action: [DependenciesInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DependenciesInfo).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specify whether to include SDK dependency information in APKs and Bundles.

### privacySandbox

Added in 8.3.1
    
    
    fun [privacySandbox](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#privacySandbox\(kotlin.Function1\))(action: [PrivacySandbox](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PrivacySandbox).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### publishing

Added in 7.1.0
    
    
    fun [publishing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#publishing\(kotlin.Function1\))(action: [ApplicationPublishing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationPublishing).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Customizes publishing build variant artifacts from app module to a Maven repository.

For more information about the properties you can configure in this block, see `[ApplicationPublishing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationPublishing)`

## Public properties

### androidResources
    
    
    val [androidResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#androidResources\(\)): [ApplicationAndroidResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationAndroidResources)

Specifies options related to the processing of Android Resources.

For more information about the properties you can configure in this block, see `[AndroidResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AndroidResources)`.

### assetPacks

Added in 4.2.0
    
    
    val [assetPacks](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#assetPacks\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Set of asset pack subprojects to be included in the app's bundle.

### bundle

Added in 4.2.0
    
    
    val [bundle](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#bundle\(\)): [Bundle](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle)

### dependenciesInfo

Added in 4.2.0
    
    
    val [dependenciesInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#dependenciesInfo\(\)): [DependenciesInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DependenciesInfo)

Specify whether to include SDK dependency information in APKs and Bundles.

### dynamicFeatures

Added in 4.2.0
    
    
    val [dynamicFeatures](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#dynamicFeatures\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

### installation
    
    
    val [installation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#installation\(\)): [ApplicationInstallation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationInstallation)

Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.

For more information about the properties you can configure in this block, see `[AdbOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AdbOptions)`.

### privacySandbox

Added in 8.3.1
    
    
    val [privacySandbox](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#privacySandbox\(\)): [PrivacySandbox](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PrivacySandbox)

Options related to the consumption of privacy sandbox libraries

### publishing

Added in 7.1.0
    
    
    val [publishing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#publishing\(\)): [ApplicationPublishing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationPublishing)

Customizes publishing build variant artifacts from app module to a Maven repository.

For more information about the properties you can configure in this block, see `[ApplicationPublishing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationPublishing)`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
