---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension/
title: ApplicationExtension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:44:38.484244+00:00
---

# ApplicationExtension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ApplicationExtension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ApplicationExtension.kt+class:com.android.build.api.dsl.ApplicationExtension)

Added in 4.2.0
    
    
    interface [ApplicationExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension) : [CommonExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension), [ApkExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApkExtension), [TestedExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension)

* * *

Extension for the Android Gradle Plugin Application plugin.

This is the `android` block when the `com.android.application` plugin is applied.

Only the Android Gradle Plugin should create instances of interfaces in com.android.build.api.dsl.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[aaptOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#aaptOptions\(kotlin.Function1\))~~(action: [AaptOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AaptOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Replaced by   
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[adbOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#adbOptions\(kotlin.Function1\))~~(action: [AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AdbOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Replaced by installation  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[androidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#androidResources\(kotlin.Function1\))(action: [ApplicationAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationAndroidResources).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options related to the processing of Android Resources.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[buildFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#buildFeatures\(kotlin.Function1\))(action: [ApplicationBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildFeatures).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` A list of build features that can be enabled or disabled on the Android Project.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.2/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
[buildTypes](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#buildTypes\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates all build type configurations for this project.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[bundle](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#bundle\(kotlin.Function1\))(action: [Bundle](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Bundle).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compileOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#compileOptions\(kotlin.Function1\))(action: [CompileOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies Java compiler options, such as the language level of the Java source code and generated bytecode.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[composeOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#composeOptions\(kotlin.Function1\))(action: [ComposeOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ComposeOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[dataBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#dataBinding\(kotlin.Function1\))(action: [DataBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DataBinding).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the [Data Binding Library](https://developer.android.com/topic/libraries/data-binding/index.html).  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType)>.[debug](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#\(org.gradle.api.NamedDomainObjectContainer\).debug\(kotlin.Function1\))(  
action: [ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
)` Shortcut extension method to allow easy access to the predefined `debug` `[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[defaultConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#defaultConfig\(kotlin.Function1\))(action: [ApplicationDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationDefaultConfig).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies defaults for variant properties that the Android plugin applies to all build variants.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[dependenciesInfo](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#dependenciesInfo\(kotlin.Function1\))(action: [DependenciesInfo](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DependenciesInfo).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specify whether to include SDK dependency information in APKs and Bundles.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#externalNativeBuild\(kotlin.Function1\))(action: [ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ExternalNativeBuild).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for external native build using [CMake](https://cmake.org/) or [ndk-build](https://developer.android.com/ndk/guides/ndk-build.html).  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[installation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#installation\(kotlin.Function1\))(action: [ApplicationInstallation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationInstallation).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[jacoco](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#jacoco\(kotlin.Function1\))~~(action: [JacocoOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/JacocoOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Renamed to testCoverage  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#lint\(kotlin.Function1\))(action: [Lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Lint).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the lint tool.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[lintOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#lintOptions\(kotlin.Function1\))~~(action: [LintOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LintOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Renamed to lint  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#packaging\(kotlin.Function1\))(action: [Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options and rules that determine which files the Android plugin packages into your APK.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[packagingOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#packagingOptions\(kotlin.Function1\))~~(action: [Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Renamed to packaging  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.2/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
[productFlavors](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#productFlavors\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationProductFlavor)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates all product flavors configurations for this project.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[publishing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#publishing\(kotlin.Function1\))(action: [ApplicationPublishing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationPublishing).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Customizes publishing build variant artifacts from app module to a Maven repository.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType)>.[release](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#\(org.gradle.api.NamedDomainObjectContainer\).release\(kotlin.Function1\))(  
action: [ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
)` Shortcut extension method to allow easy access to the predefined `release` `[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.2/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
[signingConfigs](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#signingConfigs\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApkSigningConfig)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates signing configurations that you can apply to `[BuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildType)` and `[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ProductFlavor)` configurations.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.2/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
[sourceSets](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#sourceSets\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AndroidSourceSet)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates source set configurations for all variants.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[splits](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#splits\(kotlin.Function1\))(action: [Splits](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Splits).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies configurations for [building multiple APKs](https://developer.android.com/studio/build/configure-apk-splits.html) or APK splits.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[testCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#testCoverage\(kotlin.Function1\))(action: [TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestCoverage).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configure the gathering of code-coverage from tests.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[testOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#testOptions\(kotlin.Function1\))(action: [TestOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for how the Android plugin should run local and instrumented tests.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[viewBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#viewBinding\(kotlin.Function1\))(action: [ViewBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ViewBinding).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the [View Binding Library](https://developer.android.com/topic/libraries/view-binding/index.html).  
  
### Public properties  
  
---  
`[AaptOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AaptOptions)` |  `[aaptOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#aaptOptions\(\))` **This property is deprecated.** Replaced by   
`[AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AdbOptions)` |  `[adbOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#adbOptions\(\))` **This property is deprecated.** Replaced by installation  
`[ApplicationAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationAndroidResources)` |  `[androidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#androidResources\(\))` Specifies options related to the processing of Android Resources.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[assetPacks](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#assetPacks\(\))` Set of asset pack subprojects to be included in the app's bundle.  
`[ApplicationBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildFeatures)` |  `[buildFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#buildFeatures\(\))` A list of build features that can be enabled or disabled on the Android Project.  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType)>` |  `[buildTypes](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#buildTypes\(\))` Encapsulates all build type configurations for this project.  
`[Bundle](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Bundle)` |  `[bundle](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#bundle\(\))`  
`[CompileOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileOptions)` |  `[compileOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#compileOptions\(\))` Specifies Java compiler options, such as the language level of the Java source code and generated bytecode.  
`[ComposeOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ComposeOptions)` |  `[composeOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#composeOptions\(\))`  
`[DataBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DataBinding)` |  `[dataBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#dataBinding\(\))` Specifies options for the [Data Binding Library](https://developer.android.com/topic/libraries/data-binding/index.html).  
`[ApplicationDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationDefaultConfig)` |  `[defaultConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#defaultConfig\(\))` Specifies defaults for variant properties that the Android plugin applies to all build variants.  
`[DependenciesInfo](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DependenciesInfo)` |  `[dependenciesInfo](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#dependenciesInfo\(\))` Specify whether to include SDK dependency information in APKs and Bundles.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[dynamicFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#dynamicFeatures\(\))`  
`[ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ExternalNativeBuild)` |  `[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#externalNativeBuild\(\))` Specifies options for external native build using [CMake](https://cmake.org/) or [ndk-build](https://developer.android.com/ndk/guides/ndk-build.html).  
`[ApplicationInstallation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationInstallation)` |  `[installation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#installation\(\))` Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.  
`[JacocoOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/JacocoOptions)` |  `[jacoco](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#jacoco\(\))` **This property is deprecated.** Renamed to testCoverage  
`[Lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Lint)` |  `[lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#lint\(\))` Specifies options for the lint tool.  
`[LintOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LintOptions)` |  `[lintOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#lintOptions\(\))` **This property is deprecated.** Renamed to lint  
`[Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#packaging\(\))` Specifies options and rules that determine which files the Android plugin packages into your APK.  
`[Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging)` |  `[packagingOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#packagingOptions\(\))` **This property is deprecated.** Renamed to packaging  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationProductFlavor)>` |  `[productFlavors](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#productFlavors\(\))` Encapsulates all product flavors configurations for this project.  
`[ApplicationPublishing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationPublishing)` |  `[publishing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#publishing\(\))` Customizes publishing build variant artifacts from app module to a Maven repository.  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApkSigningConfig)>` |  `[signingConfigs](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#signingConfigs\(\))` Encapsulates signing configurations that you can apply to [ ] and [ ] configurations.  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AndroidSourceSet)>` |  `[sourceSets](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#sourceSets\(\))` Encapsulates source set configurations for all variants.  
`[Splits](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Splits)` |  `[splits](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#splits\(\))` Specifies configurations for [building multiple APKs](https://developer.android.com/studio/build/configure-apk-splits.html) or APK splits.  
`[TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestCoverage)` |  `[testCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#testCoverage\(\))` Configure the gathering of code-coverage from tests.  
`[TestOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestOptions)` |  `[testOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#testOptions\(\))` Specifies options for how the Android plugin should run local and instrumented tests.  
`[ViewBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ViewBinding)` |  `[viewBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#viewBinding\(\))` Specifies options for the [View Binding Library](https://developer.android.com/topic/libraries/view-binding/index.html).  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.CommonExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#buildToolsVersion\(kotlin.String\))~~(buildToolsVersion: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by buildToolsVersion property  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#compileSdk\(kotlin.Function1\))(action: [CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding compile Sdk version, see `[CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkSpec)` for more details.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compileSdkAddon](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#compileSdkAddon\(kotlin.String,kotlin.String,kotlin.Int\))(vendor: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Specify an SDK add-on to compile your project against.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[compileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#compileSdkVersion\(kotlin.Int\))~~(apiLevel: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` **This function is deprecated.** Will be removed in AGP 10.0, replaced by the compileSdk block  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[compileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#compileSdkVersion\(kotlin.String\))~~(version: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Will be removed in AGP 10.0, replaced by the compileSdk block  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)` |  `[getDefaultProguardFile](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#getDefaultProguardFile\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[useLibrary](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#useLibrary\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Includes the specified library to the classpath.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[useLibrary](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#useLibrary\(kotlin.String,kotlin.Boolean\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), required: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Includes the specified library to the classpath.  
  
From [org.gradle.api.plugins.ExtensionAware](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html) | `[ExtensionContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionContainer.html)` |  `@[Internal](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/Internal.html)  
@[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.2/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
[getExtensions](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html#getExtensions--)()`  
---|---  
  
From [com.android.build.api.dsl.TestedExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[testFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension#testFixtures\(kotlin.Function1\))(action: [TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestFixtures).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Options to configure the test fixtures.  
---|---  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.CommonExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#buildToolsVersion\(\))` Specifies the version of the [SDK Build Tools](https://developer.android.com/studio/releases/build-tools.html) to use when building your project.  
---|---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#compileSdk\(\))` Specifies the API level to compile your project against.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdkExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#compileSdkExtension\(\))` Specifies the SDK Extension level to compile your project against.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdkMinor](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#compileSdkMinor\(\))` Specify a minor API version for the compile SDK.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[compileSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#compileSdkPreview\(\))` Specify a preview API to compile your project against.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableKotlin](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#enableKotlin\(\))` Enables the compilation of Kotlin sources.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[experimentalProperties](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#experimentalProperties\(\))` Additional per module experimental properties.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[flavorDimensions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#flavorDimensions\(\))` Specifies the names of product flavor dimensions for this project.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[namespace](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#namespace\(\))` The namespace of the generated R and BuildConfig classes.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[ndkPath](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#ndkPath\(\))` Requires the specified path to NDK be used.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[ndkVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#ndkVersion\(\))` Requires the specified NDK version to be used.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[resourcePrefix](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#resourcePrefix\(\))` Specifies this project's resource prefix to Android Studio for editor features, such as Lint checks.  
`[SdkComponents](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/SdkComponents)` |  `[sdkComponents](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#sdkComponents\(\))`  
  
From [com.android.build.api.dsl.TestedExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[testBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension#testBuildType\(\))` Specifies the [build type](https://developer.android.com/studio/build/build-variants.html#build-types) that the plugin should use to test the module.  
---|---  
`[TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestFixtures)` |  `[testFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension#testFixtures\(\))` Options to configure the test fixtures.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[testNamespace](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension#testNamespace\(\))` The namespace used by the android test and unit test components for the generated R and BuildConfig classes.  
  
## Public functions

### aaptOptions
    
    
    fun ~~[aaptOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#aaptOptions\(kotlin.Function1\))~~(action: [AaptOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AaptOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by 

Specifies options for the Android Asset Packaging Tool (AAPT).

For more information about the properties you can configure in this block, see `[AaptOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AaptOptions)`.

### adbOptions
    
    
    fun ~~[adbOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#adbOptions\(kotlin.Function1\))~~(action: [AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AdbOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by installation

Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.

For more information about the properties you can configure in this block, see `[AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AdbOptions)`.

### androidResources

Added in 9.2.1
    
    
    fun [androidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#androidResources\(kotlin.Function1\))(action: [ApplicationAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationAndroidResources).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options related to the processing of Android Resources.

For more information about the properties you can configure in this block, see `[ApplicationAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationAndroidResources)`.

### buildFeatures

Added in 9.2.1
    
    
    fun [buildFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#buildFeatures\(kotlin.Function1\))(action: [ApplicationBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildFeatures).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

A list of build features that can be enabled or disabled on the Android Project.

### buildTypes

Added in 9.2.1
    
    
    @[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.2/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
    fun [buildTypes](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#buildTypes\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Encapsulates all build type configurations for this project.

For more information about the properties you can configure in this block, see `[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType)`

### bundle

Added in 4.2.0
    
    
    fun [bundle](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#bundle\(kotlin.Function1\))(action: [Bundle](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Bundle).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### compileOptions
    
    
    fun [compileOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#compileOptions\(kotlin.Function1\))(action: [CompileOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies Java compiler options, such as the language level of the Java source code and generated bytecode.

For more information about the properties you can configure in this block, see `[CompileOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileOptions)`.

### composeOptions
    
    
    fun [composeOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#composeOptions\(kotlin.Function1\))(action: [ComposeOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ComposeOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### dataBinding
    
    
    fun [dataBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#dataBinding\(kotlin.Function1\))(action: [DataBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DataBinding).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for the [Data Binding Library](https://developer.android.com/topic/libraries/data-binding/index.html).

For more information about the properties you can configure in this block, see `[DataBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DataBinding)`

### debug

Added in 9.2.1
    
    
    fun [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType)>.[debug](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#\(org.gradle.api.NamedDomainObjectContainer\).debug\(kotlin.Function1\))(  
        action: [ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Shortcut extension method to allow easy access to the predefined `debug` `[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType)`

For example:
    
    
     android {  
         buildTypes {  
             debug {  
                 // ...  
             }  
         }  
    }

### defaultConfig

Added in 9.2.1
    
    
    fun [defaultConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#defaultConfig\(kotlin.Function1\))(action: [ApplicationDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationDefaultConfig).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies defaults for variant properties that the Android plugin applies to all build variants.

You can override any `defaultConfig` property when [configuring product flavors](https://developer.android.com/studio/build/build-variants.html#product-flavors)

For more information about the properties you can configure in this block, see `[DefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DefaultConfig)`.

### dependenciesInfo

Added in 4.2.0
    
    
    fun [dependenciesInfo](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#dependenciesInfo\(kotlin.Function1\))(action: [DependenciesInfo](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DependenciesInfo).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specify whether to include SDK dependency information in APKs and Bundles.

### externalNativeBuild
    
    
    fun [externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#externalNativeBuild\(kotlin.Function1\))(action: [ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ExternalNativeBuild).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for external native build using [CMake](https://cmake.org/) or [ndk-build](https://developer.android.com/ndk/guides/ndk-build.html).

When using [Android Studio 2.2 or higher](https://developer.android.com/studio/index.html) with [Android plugin 2.2.0 or higher](https://developer.android.com/studio/releases/gradle-plugin.html), you can compile C and C++ code into a native library that Gradle packages into your APK.

To learn more, read [Add C and C++ Code to Your Project](https://developer.android.com/studio/projects/add-native-code.html).

See also  
---  
`[ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ExternalNativeBuild)` |  since 2.2.0  
  
### installation

Added in 9.2.1
    
    
    fun [installation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#installation\(kotlin.Function1\))(action: [ApplicationInstallation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationInstallation).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.

For more information about the properties you can configure in this block, see `[AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AdbOptions)`.

### jacoco
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[jacoco](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#jacoco\(kotlin.Function1\))~~(action: [JacocoOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/JacocoOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Renamed to testCoverage

Configure the gathering of code-coverage from tests.

This is replaced by `[testCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#testCoverage\(kotlin.Function1\))`.

### lint
    
    
    fun [lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#lint\(kotlin.Function1\))(action: [Lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Lint).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for the lint tool.

For more information about the properties you can configure in this block, see `[Lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Lint)`.

### lintOptions
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[lintOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#lintOptions\(kotlin.Function1\))~~(action: [LintOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LintOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Renamed to lint

Specifies options for the lint tool.

For more information about the properties you can configure in this block, see `[LintOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LintOptions)`.

### packaging
    
    
    fun [packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#packaging\(kotlin.Function1\))(action: [Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options and rules that determine which files the Android plugin packages into your APK.

For more information about the properties you can configure in this block, see `[Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging)`.

### packagingOptions
    
    
    fun ~~[packagingOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#packagingOptions\(kotlin.Function1\))~~(action: [Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Renamed to packaging

Specifies options and rules that determine which files the Android plugin packages into your APK.

For more information about the properties you can configure in this block, see `[Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging)`.

### productFlavors

Added in 9.2.1
    
    
    @[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.2/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
    fun [productFlavors](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#productFlavors\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationProductFlavor)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Encapsulates all product flavors configurations for this project.

For more information about the properties you can configure in this block, see `[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationProductFlavor)`

### publishing

Added in 7.1.0
    
    
    fun [publishing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#publishing\(kotlin.Function1\))(action: [ApplicationPublishing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationPublishing).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Customizes publishing build variant artifacts from app module to a Maven repository.

For more information about the properties you can configure in this block, see `[ApplicationPublishing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationPublishing)`

### release

Added in 9.2.1
    
    
    fun [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType)>.[release](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#\(org.gradle.api.NamedDomainObjectContainer\).release\(kotlin.Function1\))(  
        action: [ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Shortcut extension method to allow easy access to the predefined `release` `[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType)`

For example:
    
    
     android {  
         buildTypes {  
             release {  
                 // ...  
             }  
         }  
    }

### signingConfigs
    
    
    @[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.2/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
    fun [signingConfigs](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#signingConfigs\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApkSigningConfig)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Encapsulates signing configurations that you can apply to `[BuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildType)` and `[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ProductFlavor)` configurations.

For more information about the properties you can configure in this block, see `[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApkSigningConfig)`.

### sourceSets
    
    
    @[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.2/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
    fun [sourceSets](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#sourceSets\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AndroidSourceSet)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Encapsulates source set configurations for all variants.

Note that the Android plugin uses its own implementation of source sets. For more information about the properties you can configure in this block, see `[AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AndroidSourceSet)`.

### splits
    
    
    fun [splits](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#splits\(kotlin.Function1\))(action: [Splits](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Splits).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies configurations for [building multiple APKs](https://developer.android.com/studio/build/configure-apk-splits.html) or APK splits.

For more information about the properties you can configure in this block, see `[Splits](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Splits)`.

### testCoverage
    
    
    fun [testCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#testCoverage\(kotlin.Function1\))(action: [TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestCoverage).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configure the gathering of code-coverage from tests.

To override the JaCoCo version that is used for offline instrumentation and coverage report, add the following to `build.gradle` file:
    
    
    android {  
        testCoverage {  
            jacocoVersion "<jacoco-version>"  
        }  
    }

For more information about the properties you can configure in this block, see `[TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestCoverage)`.

### testOptions
    
    
    fun [testOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#testOptions\(kotlin.Function1\))(action: [TestOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for how the Android plugin should run local and instrumented tests.

For more information about the properties you can configure in this block, see `[TestOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestOptions)`.

### viewBinding
    
    
    fun [viewBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#viewBinding\(kotlin.Function1\))(action: [ViewBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ViewBinding).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for the [View Binding Library](https://developer.android.com/topic/libraries/view-binding/index.html).

For more information about the properties you can configure in this block, see `[ViewBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ViewBinding)`

## Public properties

### aaptOptions
    
    
    val [aaptOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#aaptOptions\(\)): [AaptOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AaptOptions)

**This property is deprecated.**  
Replaced by 

Specifies options for the Android Asset Packaging Tool (AAPT).

For more information about the properties you can configure in this block, see `[AaptOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AaptOptions)`.

### adbOptions
    
    
    val [adbOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#adbOptions\(\)): [AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AdbOptions)

**This property is deprecated.**  
Replaced by installation

Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.

For more information about the properties you can configure in this block, see `[AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AdbOptions)`.

### androidResources
    
    
    val [androidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#androidResources\(\)): [ApplicationAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationAndroidResources)

Specifies options related to the processing of Android Resources.

For more information about the properties you can configure in this block, see `[ApplicationAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationAndroidResources)`.

### assetPacks

Added in 4.2.0
    
    
    val [assetPacks](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#assetPacks\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Set of asset pack subprojects to be included in the app's bundle.

### buildFeatures
    
    
    val [buildFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#buildFeatures\(\)): [ApplicationBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildFeatures)

A list of build features that can be enabled or disabled on the Android Project.

### buildTypes
    
    
    val [buildTypes](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#buildTypes\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType)>

Encapsulates all build type configurations for this project.

Unlike using `[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationProductFlavor)` to create different versions of your project that you expect to co-exist on a single device, build types determine how Gradle builds and packages each version of your project. Developers typically use them to configure projects for various stages of a development lifecycle. For example, when creating a new project from Android Studio, the Android plugin configures a 'debug' and 'release' build type for you. By default, the 'debug' build type enables debugging options and signs your APK with a generic debug keystore. Conversely, The 'release' build type strips out debug symbols and requires you to [create a release key and keystore](https://developer.android.com/studio/publish/app-signing.html#sign-apk) for your app. You can then combine build types with product flavors to [create build variants](https://developer.android.com/studio/build/build-variants.html).

See also  
---  
`[BuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BuildType)` |   
  
### bundle

Added in 4.2.0
    
    
    val [bundle](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#bundle\(\)): [Bundle](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Bundle)

### compileOptions
    
    
    val [compileOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#compileOptions\(\)): [CompileOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileOptions)

Specifies Java compiler options, such as the language level of the Java source code and generated bytecode.

For more information about the properties you can configure in this block, see `[CompileOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileOptions)`.

### composeOptions
    
    
    val [composeOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#composeOptions\(\)): [ComposeOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ComposeOptions)

### dataBinding
    
    
    val [dataBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#dataBinding\(\)): [DataBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DataBinding)

Specifies options for the [Data Binding Library](https://developer.android.com/topic/libraries/data-binding/index.html).

For more information about the properties you can configure in this block, see `[DataBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DataBinding)`

### defaultConfig
    
    
    val [defaultConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#defaultConfig\(\)): [ApplicationDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationDefaultConfig)

Specifies defaults for variant properties that the Android plugin applies to all build variants.

You can override any `defaultConfig` property when [configuring product flavors](https://developer.android.com/studio/build/build-variants.html#product-flavors)

For more information about the properties you can configure in this block, see `[ApplicationDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationDefaultConfig)`.

### dependenciesInfo

Added in 4.2.0
    
    
    val [dependenciesInfo](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#dependenciesInfo\(\)): [DependenciesInfo](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DependenciesInfo)

Specify whether to include SDK dependency information in APKs and Bundles.

### dynamicFeatures

Added in 4.2.0
    
    
    val [dynamicFeatures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#dynamicFeatures\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

### externalNativeBuild
    
    
    val [externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#externalNativeBuild\(\)): [ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ExternalNativeBuild)

Specifies options for external native build using [CMake](https://cmake.org/) or [ndk-build](https://developer.android.com/ndk/guides/ndk-build.html).

When using [Android Studio 2.2 or higher](https://developer.android.com/studio/index.html) with [Android plugin 2.2.0 or higher](https://developer.android.com/studio/releases/gradle-plugin.html), you can compile C and C++ code into a native library that Gradle packages into your APK.

To learn more, read [Add C and C++ Code to Your Project](https://developer.android.com/studio/projects/add-native-code.html).

See also  
---  
`[ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ExternalNativeBuild)` |  since 2.2.0  
  
### installation
    
    
    val [installation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#installation\(\)): [ApplicationInstallation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationInstallation)

Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.

For more information about the properties you can configure in this block, see `[AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AdbOptions)`.

### jacoco
    
    
    val [jacoco](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#jacoco\(\)): [JacocoOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/JacocoOptions)

**This property is deprecated.**  
Renamed to testCoverage

Configure the gathering of code-coverage from tests.

This is replaced by `[testCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#testCoverage\(kotlin.Function1\))`.

### lint
    
    
    val [lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#lint\(\)): [Lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Lint)

Specifies options for the lint tool.

For more information about the properties you can configure in this block, see `[Lint](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Lint)`.

### lintOptions
    
    
    val [lintOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#lintOptions\(\)): [LintOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LintOptions)

**This property is deprecated.**  
Renamed to lint

Specifies options for the lint tool.

For more information about the properties you can configure in this block, see `[LintOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LintOptions)`.

### packaging
    
    
    val [packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#packaging\(\)): [Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging)

Specifies options and rules that determine which files the Android plugin packages into your APK.

For more information about the properties you can configure in this block, see `[Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging)`.

### packagingOptions
    
    
    val [packagingOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#packagingOptions\(\)): [Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging)

**This property is deprecated.**  
Renamed to packaging

Specifies options and rules that determine which files the Android plugin packages into your APK.

For more information about the properties you can configure in this block, see `[Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Packaging)`.

### productFlavors
    
    
    val [productFlavors](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#productFlavors\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationProductFlavor)>

Encapsulates all product flavors configurations for this project.

Product flavors represent different versions of your project that you expect to co-exist on a single device, the Google Play store, or repository. For example, you can configure 'demo' and 'full' product flavors for your app, and each of those flavors can specify different features, device requirements, resources, and application ID's--while sharing common source code and resources. So, product flavors allow you to output different versions of your project by simply changing only the components and settings that are different between them.

Configuring product flavors is similar to [configuring build types](https://developer.android.com/studio/build/build-variants.html#build-types): add them to the `productFlavors` block of your project's `build.gradle` file and configure the settings you want. Product flavors support the same properties as the `defaultConfig` block--this is because `defaultConfig` defines an object that the plugin uses as the base configuration for all other flavors. Each flavor you configure can then override any of the default values in `defaultConfig`, such as the [`applicationId`](https://d.android.com/studio/build/application-id.html).

When using Android plugin 3.0.0 and higher, _each flavor must belong to a com.android.build.gradle.BaseExtension.html#com.android.build.gradle.BaseExtension:flavorDimensions(java.lang.String[]) value_. By default, when you specify only one dimension, all flavors you configure belong to that dimension. If you specify more than one flavor dimension, you need to manually assign each flavor to a dimension. To learn more, read [Use Flavor Dimensions for variant-aware dependency management](https://developer.android.com/studio/build/gradle-plugin-3-0-0-migration.html#variant_aware).

When you configure product flavors, the Android plugin automatically combines them with your `[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationBuildType)` configurations to [create build variants](https://developer.android.com/studio/build/build-variants.html). If the plugin creates certain build variants that you don't want, you can [filter variants](https://developer.android.com/studio/build/build-variants.html#filter-variants).

See also  
---  
`[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationProductFlavor)` |   
  
### publishing

Added in 7.1.0
    
    
    val [publishing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#publishing\(\)): [ApplicationPublishing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationPublishing)

Customizes publishing build variant artifacts from app module to a Maven repository.

For more information about the properties you can configure in this block, see `[ApplicationPublishing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationPublishing)`

### signingConfigs
    
    
    val [signingConfigs](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#signingConfigs\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApkSigningConfig)>

Encapsulates signing configurations that you can apply to [ ] and [ ] configurations.

Android requires that all APKs be digitally signed with a certificate before they can be installed onto a device. When deploying a debug version of your project from Android Studio, the Android plugin automatically signs your APK with a generic debug certificate. However, to build an APK for release, you must [sign the APK](https://developer.android.com/studio/publish/app-signing.html) with a release key and keystore. You can do this by either [using the Android Studio UI](https://developer.android.com/studio/publish/app-signing.html#sign-apk) or manually [configuring your `build.gradle` file](https://developer.android.com/studio/publish/app-signing.html#gradle-sign).

See also  
---  
`[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApkSigningConfig)` |   
  
### sourceSets
    
    
    val [sourceSets](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#sourceSets\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AndroidSourceSet)>

Encapsulates source set configurations for all variants.

Note that the Android plugin uses its own implementation of source sets. For more information about the properties you can configure in this block, see `[AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AndroidSourceSet)`.

### splits
    
    
    val [splits](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#splits\(\)): [Splits](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Splits)

Specifies configurations for [building multiple APKs](https://developer.android.com/studio/build/configure-apk-splits.html) or APK splits.

For more information about the properties you can configure in this block, see `[Splits](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Splits)`.

### testCoverage
    
    
    val [testCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#testCoverage\(\)): [TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestCoverage)

Configure the gathering of code-coverage from tests.

To override the JaCoCo version that is used for offline instrumentation and coverage report, add the following to `build.gradle` file:
    
    
    android {  
        testCoverage {  
            jacocoVersion "<jacoco-version>"  
        }  
    }

For more information about the properties you can configure in this block, see `[TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestCoverage)`.

### testOptions
    
    
    val [testOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#testOptions\(\)): [TestOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestOptions)

Specifies options for how the Android plugin should run local and instrumented tests.

For more information about the properties you can configure in this block, see `[TestOptions](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestOptions)`.

### viewBinding
    
    
    val [viewBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension#viewBinding\(\)): [ViewBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ViewBinding)

Specifies options for the [View Binding Library](https://developer.android.com/topic/libraries/view-binding/index.html).

For more information about the properties you can configure in this block, see `[ViewBinding](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ViewBinding)`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
