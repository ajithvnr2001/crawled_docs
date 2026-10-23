---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension/
title: DynamicFeatureExtension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:17:55.333745+00:00
---

# DynamicFeatureExtension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DynamicFeatureExtension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/DynamicFeatureExtension.kt+class:com.android.build.api.dsl.DynamicFeatureExtension)

Added in 4.2.0
    
    
    interface [DynamicFeatureExtension](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension) : [CommonExtension](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension), [ApkExtension](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApkExtension), [TestedExtension](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestedExtension)

* * *

Extension for the Android Dynamic Feature Gradle Plugin.

This is the `android` block when the `com.android.dynamic-feature` plugin is applied.

Only the Android Gradle Plugin should create instances of interfaces in com.android.build.api.dsl.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[aaptOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#aaptOptions\(kotlin.Function1\))~~(action: [AaptOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AaptOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Replaced by   
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[adbOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#adbOptions\(kotlin.Function1\))~~(action: [AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AdbOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Replaced by installation  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[androidResources](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#androidResources\(kotlin.Function1\))(action: [DynamicFeatureAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureAndroidResources).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options related to the processing of Android Resources.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[buildFeatures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#buildFeatures\(kotlin.Function1\))(action: [DynamicFeatureBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildFeatures).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` A list of build features that can be enabled or disabled on the Android Project.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[buildTypes](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#buildTypes\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates all build type configurations for this project.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compileOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#compileOptions\(kotlin.Function1\))(action: [CompileOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CompileOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies Java compiler options, such as the language level of the Java source code and generated bytecode.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[composeOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#composeOptions\(kotlin.Function1\))(action: [ComposeOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ComposeOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[dataBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#dataBinding\(kotlin.Function1\))(action: [DataBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DataBinding).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the [Data Binding Library](https://developer.android.com/topic/libraries/data-binding/index.html).  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType)>.[debug](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#\(org.gradle.api.NamedDomainObjectContainer\).debug\(kotlin.Function1\))(  
action: [DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
)` Shortcut extension method to allow easy access to the predefined `debug` `[DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[defaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#defaultConfig\(kotlin.Function1\))(action: [DynamicFeatureDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureDefaultConfig).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies defaults for variant properties that the Android plugin applies to all build variants.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#externalNativeBuild\(kotlin.Function1\))(action: [ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ExternalNativeBuild).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for external native build using [CMake](https://cmake.org/) or [ndk-build](https://developer.android.com/ndk/guides/ndk-build.html).  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[installation](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#installation\(kotlin.Function1\))(action: [DynamicFeatureInstallation](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureInstallation).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[jacoco](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#jacoco\(kotlin.Function1\))~~(action: [JacocoOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/JacocoOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Renamed to testCoverage  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[lint](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#lint\(kotlin.Function1\))(action: [Lint](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Lint).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the lint tool.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[lintOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#lintOptions\(kotlin.Function1\))~~(action: [LintOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/LintOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Renamed to lint  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#packaging\(kotlin.Function1\))(action: [Packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Packaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options and rules that determine which files the Android plugin packages into your APK.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[packagingOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#packagingOptions\(kotlin.Function1\))~~(action: [Packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Packaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Renamed to packaging  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[privacySandbox](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#privacySandbox\(kotlin.Function1\))(action: [PrivacySandbox](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/PrivacySandbox).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[productFlavors](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#productFlavors\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DynamicFeatureProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureProductFlavor)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates all product flavors configurations for this project.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType)>.[release](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#\(org.gradle.api.NamedDomainObjectContainer\).release\(kotlin.Function1\))(  
action: [DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
)` Shortcut extension method to allow easy access to the predefined `release` `[DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[signingConfigs](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#signingConfigs\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApkSigningConfig)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates signing configurations that you can apply to `[BuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BuildType)` and `[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ProductFlavor)` configurations.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[sourceSets](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#sourceSets\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidSourceSet)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates source set configurations for all variants.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[splits](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#splits\(kotlin.Function1\))(action: [Splits](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Splits).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies configurations for [building multiple APKs](https://developer.android.com/studio/build/configure-apk-splits.html) or APK splits.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[testCoverage](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#testCoverage\(kotlin.Function1\))(action: [TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestCoverage).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configure the gathering of code-coverage from tests.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[testOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#testOptions\(kotlin.Function1\))(action: [TestOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for how the Android plugin should run local and instrumented tests.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[viewBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#viewBinding\(kotlin.Function1\))(action: [ViewBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ViewBinding).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the [View Binding Library](https://developer.android.com/topic/libraries/view-binding/index.html).  
  
### Public properties  
  
---  
`[AaptOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AaptOptions)` |  `[aaptOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#aaptOptions\(\))` **This property is deprecated.** Replaced by   
`[AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AdbOptions)` |  `[adbOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#adbOptions\(\))` **This property is deprecated.** Replaced by installation  
`[DynamicFeatureAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureAndroidResources)` |  `[androidResources](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#androidResources\(\))` Specifies options related to the processing of Android Resources.  
`[DynamicFeatureBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildFeatures)` |  `[buildFeatures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#buildFeatures\(\))` A list of build features that can be enabled or disabled on the Android Project.  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType)>` |  `[buildTypes](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#buildTypes\(\))` Encapsulates all build type configurations for this project.  
`[CompileOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CompileOptions)` |  `[compileOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#compileOptions\(\))` Specifies Java compiler options, such as the language level of the Java source code and generated bytecode.  
`[ComposeOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ComposeOptions)` |  `[composeOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#composeOptions\(\))`  
`[DataBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DataBinding)` |  `[dataBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#dataBinding\(\))` Specifies options for the [Data Binding Library](https://developer.android.com/topic/libraries/data-binding/index.html).  
`[DynamicFeatureDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureDefaultConfig)` |  `[defaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#defaultConfig\(\))` Specifies defaults for variant properties that the Android plugin applies to all build variants.  
`[ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ExternalNativeBuild)` |  `[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#externalNativeBuild\(\))` Specifies options for external native build using [CMake](https://cmake.org/) or [ndk-build](https://developer.android.com/ndk/guides/ndk-build.html).  
`[DynamicFeatureInstallation](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureInstallation)` |  `[installation](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#installation\(\))` Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.  
`[JacocoOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/JacocoOptions)` |  `[jacoco](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#jacoco\(\))` **This property is deprecated.** Renamed to testCoverage  
`[Lint](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Lint)` |  `[lint](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#lint\(\))` Specifies options for the lint tool.  
`[LintOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/LintOptions)` |  `[lintOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#lintOptions\(\))` **This property is deprecated.** Renamed to lint  
`[Packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Packaging)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#packaging\(\))` Specifies options and rules that determine which files the Android plugin packages into your APK.  
`[Packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Packaging)` |  `[packagingOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#packagingOptions\(\))` **This property is deprecated.** Renamed to packaging  
`[PrivacySandbox](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/PrivacySandbox)` |  `[privacySandbox](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#privacySandbox\(\))`  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DynamicFeatureProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureProductFlavor)>` |  `[productFlavors](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#productFlavors\(\))` Encapsulates all product flavors configurations for this project.  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApkSigningConfig)>` |  `[signingConfigs](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#signingConfigs\(\))` Encapsulates signing configurations that you can apply to [ ] and [ ] configurations.  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidSourceSet)>` |  `[sourceSets](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#sourceSets\(\))` Encapsulates source set configurations for all variants.  
`[Splits](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Splits)` |  `[splits](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#splits\(\))` Specifies configurations for [building multiple APKs](https://developer.android.com/studio/build/configure-apk-splits.html) or APK splits.  
`[TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestCoverage)` |  `[testCoverage](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#testCoverage\(\))` Configure the gathering of code-coverage from tests.  
`[TestOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestOptions)` |  `[testOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#testOptions\(\))` Specifies options for how the Android plugin should run local and instrumented tests.  
`[ViewBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ViewBinding)` |  `[viewBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#viewBinding\(\))` Specifies options for the [View Binding Library](https://developer.android.com/topic/libraries/view-binding/index.html).  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.CommonExtension](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#buildToolsVersion\(kotlin.String\))~~(buildToolsVersion: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by buildToolsVersion property  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#compileSdk\(kotlin.Function1\))(action: [CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CompileSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding compile Sdk version, see `[CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CompileSdkSpec)` for more details.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compileSdkAddon](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#compileSdkAddon\(kotlin.String,kotlin.String,kotlin.Int\))(vendor: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Specify an SDK add-on to compile your project against.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[compileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#compileSdkVersion\(kotlin.Int\))~~(apiLevel: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` **This function is deprecated.** Will be removed in AGP 10.0, replaced by the compileSdk block  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[compileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#compileSdkVersion\(kotlin.String\))~~(version: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Will be removed in AGP 10.0, replaced by the compileSdk block  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)` |  `[getDefaultProguardFile](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#getDefaultProguardFile\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[useLibrary](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#useLibrary\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Includes the specified library to the classpath.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[useLibrary](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#useLibrary\(kotlin.String,kotlin.Boolean\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), required: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Includes the specified library to the classpath.  
  
From [org.gradle.api.plugins.ExtensionAware](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html) | `[ExtensionContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionContainer.html)` |  `@[Internal](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/Internal.html)  
[getExtensions](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html#getExtensions--)()`  
---|---  
  
From [com.android.build.api.dsl.TestedExtension](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestedExtension) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[testFixtures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestedExtension#testFixtures\(kotlin.Function1\))(action: [TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestFixtures).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Options to configure the test fixtures.  
---|---  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.CommonExtension](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#buildToolsVersion\(\))` Specifies the version of the [SDK Build Tools](https://developer.android.com/studio/releases/build-tools.html) to use when building your project.  
---|---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#compileSdk\(\))` Specifies the API level to compile your project against.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdkExtension](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#compileSdkExtension\(\))` Specifies the SDK Extension level to compile your project against.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdkMinor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#compileSdkMinor\(\))` Specify a minor API version for the compile SDK.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[compileSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#compileSdkPreview\(\))` Specify a preview API to compile your project against.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableKotlin](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#enableKotlin\(\))` Enables the compilation of Kotlin sources.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[experimentalProperties](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#experimentalProperties\(\))` Additional per module experimental properties.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[flavorDimensions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#flavorDimensions\(\))` Specifies the names of product flavor dimensions for this project.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[namespace](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#namespace\(\))` The namespace of the generated R and BuildConfig classes.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[ndkPath](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#ndkPath\(\))` Requires the specified path to NDK be used.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[ndkVersion](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#ndkVersion\(\))` Requires the specified NDK version to be used.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[resourcePrefix](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#resourcePrefix\(\))` Specifies this project's resource prefix to Android Studio for editor features, such as Lint checks.  
`[SdkComponents](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/SdkComponents)` |  `[sdkComponents](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CommonExtension#sdkComponents\(\))`  
  
From [com.android.build.api.dsl.TestedExtension](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestedExtension) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[testBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestedExtension#testBuildType\(\))` Specifies the [build type](https://developer.android.com/studio/build/build-variants.html#build-types) that the plugin should use to test the module.  
---|---  
`[TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestFixtures)` |  `[testFixtures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestedExtension#testFixtures\(\))` Options to configure the test fixtures.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[testNamespace](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestedExtension#testNamespace\(\))` The namespace used by the android test and unit test components for the generated R and BuildConfig classes.  
  
## Public functions

### aaptOptions
    
    
    fun ~~[aaptOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#aaptOptions\(kotlin.Function1\))~~(action: [AaptOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AaptOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by 

Specifies options for the Android Asset Packaging Tool (AAPT).

For more information about the properties you can configure in this block, see `[AaptOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AaptOptions)`.

### adbOptions
    
    
    fun ~~[adbOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#adbOptions\(kotlin.Function1\))~~(action: [AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AdbOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by installation

Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.

For more information about the properties you can configure in this block, see `[AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AdbOptions)`.

### androidResources

Added in 9.0.1
    
    
    fun [androidResources](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#androidResources\(kotlin.Function1\))(action: [DynamicFeatureAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureAndroidResources).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options related to the processing of Android Resources.

For more information about the properties you can configure in this block, see `[DynamicFeatureAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureAndroidResources)`.

### buildFeatures

Added in 9.0.1
    
    
    fun [buildFeatures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#buildFeatures\(kotlin.Function1\))(action: [DynamicFeatureBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildFeatures).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

A list of build features that can be enabled or disabled on the Android Project.

### buildTypes

Added in 9.0.1
    
    
    fun [buildTypes](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#buildTypes\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Encapsulates all build type configurations for this project.

For more information about the properties you can configure in this block, see `[DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType)`

### compileOptions
    
    
    fun [compileOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#compileOptions\(kotlin.Function1\))(action: [CompileOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CompileOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies Java compiler options, such as the language level of the Java source code and generated bytecode.

For more information about the properties you can configure in this block, see `[CompileOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CompileOptions)`.

### composeOptions
    
    
    fun [composeOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#composeOptions\(kotlin.Function1\))(action: [ComposeOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ComposeOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### dataBinding
    
    
    fun [dataBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#dataBinding\(kotlin.Function1\))(action: [DataBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DataBinding).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for the [Data Binding Library](https://developer.android.com/topic/libraries/data-binding/index.html).

For more information about the properties you can configure in this block, see `[DataBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DataBinding)`

### debug

Added in 9.0.1
    
    
    fun [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType)>.[debug](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#\(org.gradle.api.NamedDomainObjectContainer\).debug\(kotlin.Function1\))(  
        action: [DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Shortcut extension method to allow easy access to the predefined `debug` `[DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType)`

For example:
    
    
     android {  
         buildTypes {  
             debug {  
                 // ...  
             }  
         }  
    }

### defaultConfig

Added in 9.0.1
    
    
    fun [defaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#defaultConfig\(kotlin.Function1\))(action: [DynamicFeatureDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureDefaultConfig).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies defaults for variant properties that the Android plugin applies to all build variants.

You can override any `defaultConfig` property when [configuring product flavors](https://developer.android.com/studio/build/build-variants.html#product-flavors)

For more information about the properties you can configure in this block, see `[DynamicFeatureDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureDefaultConfig)`.

### externalNativeBuild
    
    
    fun [externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#externalNativeBuild\(kotlin.Function1\))(action: [ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ExternalNativeBuild).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for external native build using [CMake](https://cmake.org/) or [ndk-build](https://developer.android.com/ndk/guides/ndk-build.html).

When using [Android Studio 2.2 or higher](https://developer.android.com/studio/index.html) with [Android plugin 2.2.0 or higher](https://developer.android.com/studio/releases/gradle-plugin.html), you can compile C and C++ code into a native library that Gradle packages into your APK.

To learn more, read [Add C and C++ Code to Your Project](https://developer.android.com/studio/projects/add-native-code.html).

See also  
---  
`[ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ExternalNativeBuild)` |  since 2.2.0  
  
### installation

Added in 9.0.1
    
    
    fun [installation](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#installation\(kotlin.Function1\))(action: [DynamicFeatureInstallation](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureInstallation).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.

For more information about the properties you can configure in this block, see `[AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AdbOptions)`.

### jacoco
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[jacoco](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#jacoco\(kotlin.Function1\))~~(action: [JacocoOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/JacocoOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Renamed to testCoverage

Configure the gathering of code-coverage from tests.

This is replaced by `[testCoverage](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#testCoverage\(kotlin.Function1\))`.

### lint
    
    
    fun [lint](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#lint\(kotlin.Function1\))(action: [Lint](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Lint).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for the lint tool.

For more information about the properties you can configure in this block, see `[Lint](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Lint)`.

### lintOptions
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[lintOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#lintOptions\(kotlin.Function1\))~~(action: [LintOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/LintOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Renamed to lint

Specifies options for the lint tool.

For more information about the properties you can configure in this block, see `[LintOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/LintOptions)`.

### packaging
    
    
    fun [packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#packaging\(kotlin.Function1\))(action: [Packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Packaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options and rules that determine which files the Android plugin packages into your APK.

For more information about the properties you can configure in this block, see `[Packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Packaging)`.

### packagingOptions
    
    
    fun ~~[packagingOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#packagingOptions\(kotlin.Function1\))~~(action: [Packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Packaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Renamed to packaging

Specifies options and rules that determine which files the Android plugin packages into your APK.

For more information about the properties you can configure in this block, see `[Packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Packaging)`.

### privacySandbox

Added in 8.3.1
    
    
    fun [privacySandbox](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#privacySandbox\(kotlin.Function1\))(action: [PrivacySandbox](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/PrivacySandbox).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### productFlavors

Added in 9.0.1
    
    
    fun [productFlavors](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#productFlavors\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DynamicFeatureProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureProductFlavor)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Encapsulates all product flavors configurations for this project.

For more information about the properties you can configure in this block, see `[DynamicFeatureProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureProductFlavor)`

### release

Added in 9.0.1
    
    
    fun [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType)>.[release](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#\(org.gradle.api.NamedDomainObjectContainer\).release\(kotlin.Function1\))(  
        action: [DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Shortcut extension method to allow easy access to the predefined `release` `[DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType)`

For example:
    
    
     android {  
         buildTypes {  
             release {  
                 // ...  
             }  
         }  
    }

### signingConfigs
    
    
    fun [signingConfigs](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#signingConfigs\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApkSigningConfig)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Encapsulates signing configurations that you can apply to `[BuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BuildType)` and `[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ProductFlavor)` configurations.

For more information about the properties you can configure in this block, see `[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApkSigningConfig)`.

### sourceSets
    
    
    fun [sourceSets](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#sourceSets\(kotlin.Function1\))(action: [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidSourceSet)>.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Encapsulates source set configurations for all variants.

Note that the Android plugin uses its own implementation of source sets. For more information about the properties you can configure in this block, see `[AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidSourceSet)`.

### splits
    
    
    fun [splits](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#splits\(kotlin.Function1\))(action: [Splits](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Splits).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies configurations for [building multiple APKs](https://developer.android.com/studio/build/configure-apk-splits.html) or APK splits.

For more information about the properties you can configure in this block, see `[Splits](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Splits)`.

### testCoverage
    
    
    fun [testCoverage](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#testCoverage\(kotlin.Function1\))(action: [TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestCoverage).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configure the gathering of code-coverage from tests.

To override the JaCoCo version that is used for offline instrumentation and coverage report, add the following to `build.gradle` file:
    
    
    android {  
        testCoverage {  
            jacocoVersion "<jacoco-version>"  
        }  
    }

For more information about the properties you can configure in this block, see `[TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestCoverage)`.

### testOptions
    
    
    fun [testOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#testOptions\(kotlin.Function1\))(action: [TestOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for how the Android plugin should run local and instrumented tests.

For more information about the properties you can configure in this block, see `[TestOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestOptions)`.

### viewBinding
    
    
    fun [viewBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#viewBinding\(kotlin.Function1\))(action: [ViewBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ViewBinding).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for the [View Binding Library](https://developer.android.com/topic/libraries/view-binding/index.html).

For more information about the properties you can configure in this block, see `[ViewBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ViewBinding)`

## Public properties

### aaptOptions
    
    
    val [aaptOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#aaptOptions\(\)): [AaptOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AaptOptions)

**This property is deprecated.**  
Replaced by 

Specifies options for the Android Asset Packaging Tool (AAPT).

For more information about the properties you can configure in this block, see `[AaptOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AaptOptions)`.

### adbOptions
    
    
    val [adbOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#adbOptions\(\)): [AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AdbOptions)

**This property is deprecated.**  
Replaced by installation

Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.

For more information about the properties you can configure in this block, see `[AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AdbOptions)`.

### androidResources
    
    
    val [androidResources](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#androidResources\(\)): [DynamicFeatureAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureAndroidResources)

Specifies options related to the processing of Android Resources.

For more information about the properties you can configure in this block, see `[DynamicFeatureAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureAndroidResources)`.

### buildFeatures
    
    
    val [buildFeatures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#buildFeatures\(\)): [DynamicFeatureBuildFeatures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildFeatures)

A list of build features that can be enabled or disabled on the Android Project.

### buildTypes
    
    
    val [buildTypes](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#buildTypes\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType)>

Encapsulates all build type configurations for this project.

Unlike using `[DynamicFeatureProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureProductFlavor)` to create different versions of your project that you expect to co-exist on a single device, build types determine how Gradle builds and packages each version of your project. Developers typically use them to configure projects for various stages of a development lifecycle. For example, when creating a new project from Android Studio, the Android plugin configures a 'debug' and 'release' build type for you. You can then combine build types with product flavors to [create build variants](https://developer.android.com/studio/build/build-variants.html).

See also  
---  
`[BuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BuildType)` |   
  
### compileOptions
    
    
    val [compileOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#compileOptions\(\)): [CompileOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CompileOptions)

Specifies Java compiler options, such as the language level of the Java source code and generated bytecode.

For more information about the properties you can configure in this block, see `[CompileOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/CompileOptions)`.

### composeOptions
    
    
    val [composeOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#composeOptions\(\)): [ComposeOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ComposeOptions)

### dataBinding
    
    
    val [dataBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#dataBinding\(\)): [DataBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DataBinding)

Specifies options for the [Data Binding Library](https://developer.android.com/topic/libraries/data-binding/index.html).

For more information about the properties you can configure in this block, see `[DataBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DataBinding)`

### defaultConfig
    
    
    val [defaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#defaultConfig\(\)): [DynamicFeatureDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureDefaultConfig)

Specifies defaults for variant properties that the Android plugin applies to all build variants.

You can override any `defaultConfig` property when [configuring product flavors](https://developer.android.com/studio/build/build-variants.html#product-flavors)

For more information about the properties you can configure in this block, see `[DynamicFeatureDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureDefaultConfig)`.

### externalNativeBuild
    
    
    val [externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#externalNativeBuild\(\)): [ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ExternalNativeBuild)

Specifies options for external native build using [CMake](https://cmake.org/) or [ndk-build](https://developer.android.com/ndk/guides/ndk-build.html).

When using [Android Studio 2.2 or higher](https://developer.android.com/studio/index.html) with [Android plugin 2.2.0 or higher](https://developer.android.com/studio/releases/gradle-plugin.html), you can compile C and C++ code into a native library that Gradle packages into your APK.

To learn more, read [Add C and C++ Code to Your Project](https://developer.android.com/studio/projects/add-native-code.html).

See also  
---  
`[ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ExternalNativeBuild)` |  since 2.2.0  
  
### installation
    
    
    val [installation](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#installation\(\)): [DynamicFeatureInstallation](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureInstallation)

Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.

For more information about the properties you can configure in this block, see `[AdbOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AdbOptions)`.

### jacoco
    
    
    val [jacoco](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#jacoco\(\)): [JacocoOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/JacocoOptions)

**This property is deprecated.**  
Renamed to testCoverage

Configure the gathering of code-coverage from tests.

This is replaced by `[testCoverage](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#testCoverage\(kotlin.Function1\))`.

### lint
    
    
    val [lint](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#lint\(\)): [Lint](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Lint)

Specifies options for the lint tool.

For more information about the properties you can configure in this block, see `[Lint](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Lint)`.

### lintOptions
    
    
    val [lintOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#lintOptions\(\)): [LintOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/LintOptions)

**This property is deprecated.**  
Renamed to lint

Specifies options for the lint tool.

For more information about the properties you can configure in this block, see `[LintOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/LintOptions)`.

### packaging
    
    
    val [packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#packaging\(\)): [Packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Packaging)

Specifies options and rules that determine which files the Android plugin packages into your APK.

For more information about the properties you can configure in this block, see `[Packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Packaging)`.

### packagingOptions
    
    
    val [packagingOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#packagingOptions\(\)): [Packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Packaging)

**This property is deprecated.**  
Renamed to packaging

Specifies options and rules that determine which files the Android plugin packages into your APK.

For more information about the properties you can configure in this block, see `[Packaging](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Packaging)`.

### privacySandbox

Added in 8.3.1
    
    
    val [privacySandbox](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#privacySandbox\(\)): [PrivacySandbox](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/PrivacySandbox)

### productFlavors
    
    
    val [productFlavors](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#productFlavors\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DynamicFeatureProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureProductFlavor)>

Encapsulates all product flavors configurations for this project.

Product flavors represent different versions of your project that you expect to co-exist on a single device, the Google Play store, or repository. For example, you can configure 'demo' and 'full' product flavors for your app, and each of those flavors can specify different features, device requirements, resources, and application ID's--while sharing common source code and resources. So, product flavors allow you to output different versions of your project by simply changing only the components and settings that are different between them.

Configuring product flavors is similar to [configuring build types](https://developer.android.com/studio/build/build-variants.html#build-types): add them to the `productFlavors` block of your project's `build.gradle` file and configure the settings you want. Product flavors support the same properties as the `defaultConfig` block--this is because `defaultConfig` defines an object that the plugin uses as the base configuration for all other flavors. Each flavor you configure can then override any of the default values in `defaultConfig`, such as the [`applicationId`](https://d.android.com/studio/build/application-id.html).

When using Android plugin 3.0.0 and higher, _each flavor must belong to a com.android.build.gradle.BaseExtension.html#com.android.build.gradle.BaseExtension:flavorDimensions(java.lang.String[]) value_. By default, when you specify only one dimension, all flavors you configure belong to that dimension. If you specify more than one flavor dimension, you need to manually assign each flavor to a dimension. To learn more, read [Use Flavor Dimensions for variant-aware dependency management](https://developer.android.com/studio/build/gradle-plugin-3-0-0-migration.html#variant_aware).

When you configure product flavors, the Android plugin automatically combines them with your `[DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBuildType)` configurations to [create build variants](https://developer.android.com/studio/build/build-variants.html). If the plugin creates certain build variants that you don't want, you can [filter variants](https://developer.android.com/studio/build/build-variants.html#filter-variants).

See also  
---  
`[DynamicFeatureProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureProductFlavor)` |   
  
### signingConfigs
    
    
    val [signingConfigs](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#signingConfigs\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApkSigningConfig)>

Encapsulates signing configurations that you can apply to [ ] and [ ] configurations.

Android requires that all APKs be digitally signed with a certificate before they can be installed onto a device. When deploying a debug version of your project from Android Studio, the Android plugin automatically signs your APK with a generic debug certificate. However, to build an APK for release, you must [sign the APK](https://developer.android.com/studio/publish/app-signing.html) with a release key and keystore. You can do this by either [using the Android Studio UI](https://developer.android.com/studio/publish/app-signing.html#sign-apk) or manually [configuring your `build.gradle` file](https://developer.android.com/studio/publish/app-signing.html#gradle-sign).

See also  
---  
`[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApkSigningConfig)` |   
  
### sourceSets
    
    
    val [sourceSets](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#sourceSets\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidSourceSet)>

Encapsulates source set configurations for all variants.

Note that the Android plugin uses its own implementation of source sets. For more information about the properties you can configure in this block, see `[AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidSourceSet)`.

### splits
    
    
    val [splits](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#splits\(\)): [Splits](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Splits)

Specifies configurations for [building multiple APKs](https://developer.android.com/studio/build/configure-apk-splits.html) or APK splits.

For more information about the properties you can configure in this block, see `[Splits](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Splits)`.

### testCoverage
    
    
    val [testCoverage](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#testCoverage\(\)): [TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestCoverage)

Configure the gathering of code-coverage from tests.

To override the JaCoCo version that is used for offline instrumentation and coverage report, add the following to `build.gradle` file:
    
    
    android {  
        testCoverage {  
            jacocoVersion "<jacoco-version>"  
        }  
    }

For more information about the properties you can configure in this block, see `[TestCoverage](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestCoverage)`.

### testOptions
    
    
    val [testOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#testOptions\(\)): [TestOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestOptions)

Specifies options for how the Android plugin should run local and instrumented tests.

For more information about the properties you can configure in this block, see `[TestOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestOptions)`.

### viewBinding
    
    
    val [viewBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureExtension#viewBinding\(\)): [ViewBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ViewBinding)

Specifies options for the [View Binding Library](https://developer.android.com/topic/libraries/view-binding/index.html).

For more information about the properties you can configure in this block, see `[ViewBinding](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ViewBinding)`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-13 UTC."],[],[]] 
