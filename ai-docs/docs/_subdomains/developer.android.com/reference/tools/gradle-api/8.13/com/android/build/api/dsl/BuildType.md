---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType/
title: BuildType \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:30:54.016043+00:00
---

# BuildType  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BuildType

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/BuildType.kt+class:com.android.build.api.dsl.BuildType)

Added in 4.2.0
    
    
    interface [BuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html), [VariantDimension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VariantDimension), [ExtensionAware](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html)

Known direct subclasses 

[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationBuildType), [DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DynamicFeatureBuildType), [LibraryBuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LibraryBuildType), [TestBuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestBuildType)

`[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationBuildType)` |  Build types define certain properties that Gradle uses when building and packaging your app, and are typically configured for different stages of your development lifecycle.  
---|---  
`[DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DynamicFeatureBuildType)` |  Build types define certain properties that Gradle uses when building and packaging your app, and are typically configured for different stages of your development lifecycle.  
`[LibraryBuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LibraryBuildType)` |  Build types define certain properties that Gradle uses when building and packaging your library, and are typically configured for different stages of your development lifecycle.  
`[TestBuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestBuildType)` |  Build types define certain properties that Gradle uses when building and packaging your library, and are typically configured for different stages of your development lifecycle.  
  
* * *

Build types define certain properties that Gradle uses when building and packaging your app, and are typically configured for different stages of your development lifecycle.

There are two build types defined by default, `debug` and `release`, and you can customize them and create additional build types.

The default debug build type enables debug options and signs the APK with the debug key, while the release build type is not debuggable and can be configured to shrink, obfuscate, and sign your APK with a release key for distribution.

See [configuring build types](https://developer.android.com/studio/build#build-config) for more information.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[initWith](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#initWith\(com.android.build.api.dsl.BuildType\))(that: [BuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType))` Copies all properties from the given build type.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[postprocessing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#postprocessing\(kotlin.Function1\))(action: [PostProcessing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PostProcessing).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[setMatchingFallbacks](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#setMatchingFallbacks\(kotlin.collections.List\))~~(fallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>)` **This function is deprecated.** Replaced with property matchingFallbacks  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[setMatchingFallbacks](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#setMatchingFallbacks\(kotlin.Array\))~~(vararg fallbacks: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property matchingFallbacks  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[vcsInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#vcsInfo\(kotlin.Function1\))(action: [VcsInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VcsInfo).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
  
### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableAndroidTestCoverage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#enableAndroidTestCoverage\(\))` Specifies code coverage is enabled for module tests of type AndroidTest.  
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
  
### Inherited functions  
  
---  
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
  
## Public functions

### initWith

Added in 7.0.0
    
    
    fun [initWith](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#initWith\(com.android.build.api.dsl.BuildType\))(that: [BuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Copies all properties from the given build type.

It can be used like this:
    
    
    android.buildTypes {  
        customBuildType {  
            initWith debug  
            // customize...  
        }  
    }

### postprocessing

Added in 7.0.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [postprocessing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#postprocessing\(kotlin.Function1\))(action: [PostProcessing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PostProcessing).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### setMatchingFallbacks

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[setMatchingFallbacks](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#setMatchingFallbacks\(kotlin.collections.List\))~~(fallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced with property matchingFallbacks

### setMatchingFallbacks

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[setMatchingFallbacks](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#setMatchingFallbacks\(kotlin.Array\))~~(vararg fallbacks: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced with property matchingFallbacks

### vcsInfo

Added in 8.3.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [vcsInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#vcsInfo\(kotlin.Function1\))(action: [VcsInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VcsInfo).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

## Public properties

### enableAndroidTestCoverage

Added in 7.3.0
    
    
    var [enableAndroidTestCoverage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#enableAndroidTestCoverage\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Specifies code coverage is enabled for module tests of type AndroidTest.

If enabled, prepares module class files for code coverage collection such as instrumenting dependent library classes and module classes. This allows for code coverage reports to be generated.

### enableUnitTestCoverage

Added in 7.2.0
    
    
    var [enableUnitTestCoverage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#enableUnitTestCoverage\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Specifies unit test code coverage data collection by configuring the JacocoPlugin.

When enabled, the Jacoco plugin is applied and coverage data is collected by the Jacoco plugin. This can avoid unwanted build time instrumentation required to collect coverage data from other test types such as connected tests.

### isJniDebuggable

Added in 4.2.0
    
    
    var [isJniDebuggable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#isJniDebuggable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether this build type is configured to generate an APK with debuggable native code.

### isMinifyEnabled

Added in 4.2.0
    
    
    var [isMinifyEnabled](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#isMinifyEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Specifies whether to enable code shrinking for this build type.

By default, when you enable code shrinking by setting this property to `true`, the Android plugin uses ProGuard.

To learn more, read [Shrink Your Code and Resources](https://developer.android.com/studio/build/shrink-code.html).

### isPseudoLocalesEnabled

Added in 4.2.0
    
    
    var [isPseudoLocalesEnabled](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#isPseudoLocalesEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Specifies whether the plugin should generate resources for pseudolocales.

A pseudolocale is a locale that simulates characteristics of languages that cause UI, layout, and other translation-related problems when an app is localized. Pseudolocales can aid your development workflow because you can test and make adjustments to your UI before you finalize text for translation.

When you set this property to `true` as shown below, the plugin generates resources for the following pseudo locales and makes them available in your connected device's language preferences: `en-XA` and `ar-XB`.
    
    
    android {  
        buildTypes {  
            debug {  
                pseudoLocalesEnabled true  
            }  
        }  
    }

When you build your app, the plugin includes the pseudolocale resources in your APK. If you notice that your APK does not include those locale resources, make sure your build configuration isn't limiting which locale resources are packaged with your APK, such as using the `resourceConfigurations` property to [remove unused locale resources](https://d.android.com/studio/build/shrink-code.html#unused-alt-resources).

To learn more, read [Test Your App with Pseudolocales](https://d.android.com/guide/topics/resources/pseudolocales.html).

### isRenderscriptDebuggable

Added in 4.2.0

Deprecated in 8.2.0
    
    
    var [isRenderscriptDebuggable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#isRenderscriptDebuggable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
This dsl option has no effect and will be removed in AGP 9.0

Whether the build type is configured to generate an apk with debuggable RenderScript code.

RenderScript APIs are deprecated starting in Android 12. For more information about how to migrate, see https://developer.android.com/guide/topics/renderscript/migrate

### isShrinkResources

Added in 7.0.0
    
    
    var [isShrinkResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#isShrinkResources\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Specifies whether to enable shrinking resources for this build type.

To learn more, read [Shrink Your Code and Resources](https://developer.android.com/studio/build/shrink-code.html).

### isTestCoverageEnabled

Added in 4.2.0

Deprecated in 7.3.0
    
    
    var [isTestCoverageEnabled](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#isTestCoverageEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Replaced with: enableUnitTestCoverage and or enableAndroidTestCoverage.

Whether test coverage is enabled for this build type.

If enabled this uses Jacoco to capture coverage and creates a report in the build directory.

The version of Jacoco can be configured with:
    
    
    android {  
        testCoverage {  
            jacocoVersion = '0.6.2.201302030002'  
        }  
    }

isTestCoverageEnabled is deprecated. Use enableUnitTestCoverage and enableAndroidTestCoverage instead which allow you to enable coverage separately for unit and instrumentation tests.

### isZipAlignEnabled

Added in 7.0.0

Deprecated in 7.0.0
    
    
    var [isZipAlignEnabled](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#isZipAlignEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Changing the value of isZipAlignEnabled no longer has any effect (AGP produced artifacts are already aligned).

### matchingFallbacks

Added in 4.2.0
    
    
    val [matchingFallbacks](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#matchingFallbacks\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies a sorted list of build types that the plugin should try to use when a direct variant match with a local module dependency is not possible.

Android plugin 3.0.0 and higher try to match each variant of your module with the same one from its dependencies. For example, when you build a "freeDebug" version of your app, the plugin tries to match it with "freeDebug" versions of the local library modules the app depends on.

However, there may be situations in which **your app includes build types that a dependency does not**. For example, consider if your app includes a "stage" build type, but a dependency includes only a "debug" and "release" build type. When the plugin tries to build the "stage" version of your app, it won't know which version of the dependency to use, and you'll see an error message similar to the following:
    
    
    Error:Failed to resolve: Could not resolve project :mylibrary.  
    Required by:  
    project :app

In this situation, you can use `matchingFallbacks` to specify alternative matches for the app's "stage" build type, as shown below:
    
    
    // In the app's build.gradle file.  
    android {  
        buildTypes {  
            release {  
                // Because the dependency already includes a "release" build type,  
                // you don't need to provide a list of fallbacks here.  
            }  
            stage {  
                // Specifies a sorted list of fallback build types that the  
                // plugin should try to use when a dependency does not include a  
                // "stage" build type. You may specify as many fallbacks as you  
                // like, and the plugin selects the first build type that's  
                // available in the dependency.  
                matchingFallbacks = ['debug', 'qa', 'release']  
            }  
        }  
    }

Note that there is no issue when a library dependency includes a build type that your app does not. That's because the plugin simply never requests that build type from the dependency.

Returns  
---  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  the names of product flavors to use, in descending priority order  
  
### postprocessing

Added in 7.0.0
    
    
    val [postprocessing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#postprocessing\(\)): [PostProcessing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PostProcessing)

### renderscriptOptimLevel

Added in 4.2.0
    
    
    var [renderscriptOptimLevel](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#renderscriptOptimLevel\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Optimization level to use by the renderscript compiler. RenderScript APIs are deprecated starting in Android 12. For more information about how to migrate, see https://developer.android.com/guide/topics/renderscript/migrate

### vcsInfo

Added in 8.3.1
    
    
    val [vcsInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#vcsInfo\(\)): [VcsInfo](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/VcsInfo)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-31 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-31 UTC."],[],[]] 
