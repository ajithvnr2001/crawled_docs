---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DynamicFeatureBuildType/
title: DynamicFeatureBuildType \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:32:11.984989+00:00
---

# DynamicFeatureBuildType  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DynamicFeatureBuildType/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DynamicFeatureBuildType

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/DynamicFeatureBuildType.kt+class:com.android.build.api.dsl.DynamicFeatureBuildType)

Added in 4.2.0
    
    
    interface [DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DynamicFeatureBuildType) : [BuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType), [DynamicFeatureVariantDimension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DynamicFeatureVariantDimension)

* * *

Build types define certain properties that Gradle uses when building and packaging your app, and are typically configured for different stages of your development lifecycle.

Dynamic features must have exactly the same build types (by name) as the app that includes them, however settings can be different between the application and the dynamic feature. Properties on dynamic feature build types fall in to three categories.

  * Properties global to the application that affect the build flow, and so must be explicitly set in the dynamic feature. For example, whether the build type is debuggable must match the application that includes this dynamic feature.

  * Properties global to the application that do not affect the build flow. These are set in the `com.android.application` project, and are automatically configured on the dynamic feature, they cannot be set on the dynamic feature. For example, application ID suffix and signing cannot be configured on the dynamic feature and are not present on this interface.

  * Properties that can vary between the app and the dynamic feature. For example, `resValues` can be used independently from the app in a dynamic feature.




See `[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationProductFlavor)`

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[isCrunchPngs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DynamicFeatureBuildType#isCrunchPngs\(\))` Whether to crunch PNGs.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isDebuggable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DynamicFeatureBuildType#isDebuggable\(\))` Whether this build type should generate a debuggable apk.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.BuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[initWith](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#initWith\(com.android.build.api.dsl.BuildType\))(that: [BuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType))` Copies all properties from the given build type.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[postprocessing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#postprocessing\(kotlin.Function1\))(action: [PostProcessing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PostProcessing).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[setMatchingFallbacks](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#setMatchingFallbacks\(kotlin.collections.List\))~~(fallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>)` **This function is deprecated.** Replaced with property matchingFallbacks  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[setMatchingFallbacks](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#setMatchingFallbacks\(kotlin.Array\))~~(vararg fallbacks: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property matchingFallbacks  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[vcsInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#vcsInfo\(kotlin.Function1\))(action: [VcsInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VcsInfo).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
  
From [org.gradle.api.plugins.ExtensionAware](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html) | `[ExtensionContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionContainer.html)` |  `@[Internal](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/Internal.html)  
[getExtensions](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html#getExtensions--)()`  
---|---  
  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
From [com.android.build.api.dsl.VariantDimension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[addManifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#addManifestPlaceholders\(kotlin.collections.Map\))(manifestPlaceholders: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>)` Adds manifest placeholders.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[buildConfigField](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#buildConfigField\(kotlin.String,kotlin.String,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds a new field to the generated BuildConfig class.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#externalNativeBuild\(kotlin.Function1\))(action: [ExternalNativeBuildFlags](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ExternalNativeBuildFlags).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates per-variant CMake and ndk-build configurations for your external native build.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[javaCompileOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#javaCompileOptions\(kotlin.Function1\))(action: [JavaCompileOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/JavaCompileOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Options for configuring Java compilation.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[ndk](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#ndk\(kotlin.Function1\))(action: [Ndk](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates per-variant configurations for the NDK, such as ABI filters.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[optimization](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#optimization\(kotlin.Function1\))~~(action: [Optimization](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Optimization).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Use ApplicationBuildType.optimization(action) instead  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[proguardFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#proguardFile\(kotlin.Any\))(proguardFile: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds a new ProGuard configuration file.  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[proguardFiles](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#proguardFiles\(kotlin.Array\))(vararg files: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds new ProGuard configuration files.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[resValue](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#resValue\(kotlin.String,kotlin.String,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds a new generated resource.  
`[Void](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Void.html)?` |  `~~[setManifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#setManifestPlaceholders\(kotlin.collections.Map\))~~(manifestPlaceholders: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>)` **This function is deprecated.** Use manifestPlaceholders property instead  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[setProguardFiles](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#setProguardFiles\(kotlin.collections.Iterable\))(proguardFileIterable: [Iterable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html)<*>)` Replaces the ProGuard configuration files.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#shaders\(kotlin.Function1\))(action: [Shaders](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Shaders).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configure the shader compiler options.  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[testProguardFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#testProguardFile\(kotlin.Any\))(proguardFile: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds a proguard rule file to be used when processing test code.  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[testProguardFiles](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#testProguardFiles\(kotlin.Array\))(vararg proguardFiles: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds proguard rule files to be used when processing test code.  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.BuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableAndroidTestCoverage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#enableAndroidTestCoverage\(\))` Specifies code coverage is enabled for module tests of type AndroidTest.  
---|---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableUnitTestCoverage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#enableUnitTestCoverage\(\))` Specifies unit test code coverage data collection by configuring the JacocoPlugin.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isJniDebuggable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#isJniDebuggable\(\))` Whether this build type is configured to generate an APK with debuggable native code.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isMinifyEnabled](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#isMinifyEnabled\(\))` Specifies whether to enable code shrinking for this build type.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isPseudoLocalesEnabled](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#isPseudoLocalesEnabled\(\))` Specifies whether the plugin should generate resources for pseudolocales.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isRenderscriptDebuggable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#isRenderscriptDebuggable\(\))` **This property is deprecated.** This dsl option has no effect and will be removed in AGP 9.0  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isShrinkResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#isShrinkResources\(\))` Specifies whether to enable shrinking resources for this build type.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isTestCoverageEnabled](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#isTestCoverageEnabled\(\))` **This property is deprecated.** Replaced with: enableUnitTestCoverage and or enableAndroidTestCoverage.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isZipAlignEnabled](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#isZipAlignEnabled\(\))` **This property is deprecated.** Changing the value of isZipAlignEnabled no longer has any effect (AGP produced artifacts are already aligned).  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[matchingFallbacks](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#matchingFallbacks\(\))` Specifies a sorted list of build types that the plugin should try to use when a direct variant match with a local module dependency is not possible.  
`[PostProcessing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PostProcessing)` |  `[postprocessing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#postprocessing\(\))`  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[renderscriptOptimLevel](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#renderscriptOptimLevel\(\))` Optimization level to use by the renderscript compiler.  
`[VcsInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VcsInfo)` |  `[vcsInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#vcsInfo\(\))`  
  
From [com.android.build.api.dsl.VariantDimension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension) | `[ExternalNativeBuildFlags](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ExternalNativeBuildFlags)` |  `[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#externalNativeBuild\(\))` Encapsulates per-variant CMake and ndk-build configurations for your external native build.  
---|---  
`[JavaCompileOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/JavaCompileOptions)` |  `[javaCompileOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#javaCompileOptions\(\))` Options for configuring Java compilation.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[manifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#manifestPlaceholders\(\))` The manifest placeholders.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[multiDexKeepFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#multiDexKeepFile\(\))` **This property is deprecated.** This property is deprecated.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[multiDexKeepProguard](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#multiDexKeepProguard\(\))` Text file with additional ProGuard rules to be used to determine which classes are compiled into the main dex file.  
`[Ndk](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk)` |  `[ndk](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#ndk\(\))` Encapsulates per-variant configurations for the NDK, such as ABI filters.  
`[Optimization](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Optimization)` |  `[optimization](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#optimization\(\))` **This property is deprecated.** Use ApplicationBuildType.optimization instead  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>` |  `[proguardFiles](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#proguardFiles\(\))` Specifies the ProGuard configuration files that the plugin should use.  
`[Shaders](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Shaders)` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#shaders\(\))` Options for configuring the shader compiler.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>` |  `[testProguardFiles](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension#testProguardFiles\(\))` The collection of proguard rule files to be used when processing test code.  
  
## Public properties

### isCrunchPngs

Added in 4.2.0
    
    
    var [isCrunchPngs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DynamicFeatureBuildType#isCrunchPngs\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Whether to crunch PNGs.

Setting this property to `true` reduces of PNG resources that are not already optimally compressed. However, this process increases build times.

PNG crunching is enabled by default in the release build type and disabled by default in the debug build type.

### isDebuggable

Added in 8.4.0
    
    
    var [isDebuggable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DynamicFeatureBuildType#isDebuggable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether this build type should generate a debuggable apk.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-31 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-31 UTC."],[],[]] 
