---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationVariantDimension/
title: ApplicationVariantDimension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:00:55.829947+00:00
---

# ApplicationVariantDimension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationVariantDimension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ApplicationVariantDimension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ApplicationVariantDimension.kt+class:com.android.build.api.dsl.ApplicationVariantDimension)

Added in 4.2.0
    
    
    interface [ApplicationVariantDimension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationVariantDimension) : [VariantDimension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension)

Known direct subclasses 

[ApplicationBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationBaseFlavor), [ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationBuildType)

`[ApplicationBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationBaseFlavor)` |  Shared properties between `[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationProductFlavor)` and `[ApplicationDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationDefaultConfig)`  
---|---  
`[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationBuildType)` |  Build types define certain properties that Gradle uses when building and packaging your app, and are typically configured for different stages of your development lifecycle.  
  
Known indirect subclasses 

[ApplicationDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationDefaultConfig), [ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationProductFlavor)

`[ApplicationDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationDefaultConfig)` |  Specifies defaults for properties that the Android application plugin applies to all build variants.  
---|---  
`[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationProductFlavor)` |  Encapsulates all product flavors properties for application projects.  
  
* * *

Shared properties between DSL objects that contribute to an application variant.

That is, `[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationBuildType)` and `[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationProductFlavor)` and `[ApplicationDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationDefaultConfig)`.

## Summary

### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[applicationIdSuffix](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationVariantDimension#applicationIdSuffix\(\))` Application id suffix.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[multiDexEnabled](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationVariantDimension#multiDexEnabled\(\))` Returns whether multi-dex is enabled.  
`[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApkSigningConfig)?` |  `[signingConfig](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationVariantDimension#signingConfig\(\))` The associated signing config or null if none are set on the variant dimension.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[versionNameSuffix](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationVariantDimension#versionNameSuffix\(\))` Version name suffix.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.VariantDimension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[addManifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#addManifestPlaceholders\(kotlin.collections.Map\))(manifestPlaceholders: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>)` Adds manifest placeholders.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[buildConfigField](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#buildConfigField\(kotlin.String,kotlin.String,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds a new field to the generated BuildConfig class.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#externalNativeBuild\(kotlin.Function1\))(action: [ExternalNativeBuildFlags](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ExternalNativeBuildFlags).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates per-variant CMake and ndk-build configurations for your external native build.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[javaCompileOptions](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#javaCompileOptions\(kotlin.Function1\))(action: [JavaCompileOptions](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/JavaCompileOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Options for configuring Java compilation.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[ndk](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#ndk\(kotlin.Function1\))(action: [Ndk](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Ndk).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates per-variant configurations for the NDK, such as ABI filters.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[optimization](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#optimization\(kotlin.Function1\))~~(action: [Optimization](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Optimization).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Use ApplicationBuildType.optimization(action) instead  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[proguardFile](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#proguardFile\(kotlin.Any\))(proguardFile: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds a new ProGuard configuration file.  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[proguardFiles](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#proguardFiles\(kotlin.Array\))(vararg files: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds new ProGuard configuration files.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[resValue](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#resValue\(kotlin.String,kotlin.String,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds a new generated resource.  
`[Void](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Void.html)?` |  `~~[setManifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#setManifestPlaceholders\(kotlin.collections.Map\))~~(manifestPlaceholders: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>)` **This function is deprecated.** Use manifestPlaceholders property instead  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[setProguardFiles](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#setProguardFiles\(kotlin.collections.Iterable\))(proguardFileIterable: [Iterable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html)<*>)` Replaces the ProGuard configuration files.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#shaders\(kotlin.Function1\))(action: [Shaders](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Shaders).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configure the shader compiler options.  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[testProguardFile](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#testProguardFile\(kotlin.Any\))(proguardFile: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds a proguard rule file to be used when processing test code.  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[testProguardFiles](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#testProguardFiles\(kotlin.Array\))(vararg proguardFiles: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds proguard rule files to be used when processing test code.  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.VariantDimension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension) | `[ExternalNativeBuildFlags](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ExternalNativeBuildFlags)` |  `[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#externalNativeBuild\(\))` Encapsulates per-variant CMake and ndk-build configurations for your external native build.  
---|---  
`[JavaCompileOptions](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/JavaCompileOptions)` |  `[javaCompileOptions](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#javaCompileOptions\(\))` Options for configuring Java compilation.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[manifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#manifestPlaceholders\(\))` The manifest placeholders.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[multiDexKeepFile](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#multiDexKeepFile\(\))` **This property is deprecated.** This property is deprecated.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[multiDexKeepProguard](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#multiDexKeepProguard\(\))` Text file with additional ProGuard rules to be used to determine which classes are compiled into the main dex file.  
`[Ndk](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Ndk)` |  `[ndk](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#ndk\(\))` Encapsulates per-variant configurations for the NDK, such as ABI filters.  
`[Optimization](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Optimization)` |  `[optimization](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#optimization\(\))` **This property is deprecated.** Use ApplicationBuildType.optimization instead  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>` |  `[proguardFiles](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#proguardFiles\(\))` Specifies the ProGuard configuration files that the plugin should use.  
`[Shaders](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Shaders)` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#shaders\(\))` Options for configuring the shader compiler.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>` |  `[testProguardFiles](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/VariantDimension#testProguardFiles\(\))` The collection of proguard rule files to be used when processing test code.  
  
## Public properties

### applicationIdSuffix

Added in 4.2.0
    
    
    var [applicationIdSuffix](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationVariantDimension#applicationIdSuffix\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Application id suffix. It is appended to the "base" application id when calculating the final application id for a variant.

In case there are product flavor dimensions specified, the final application id suffix will contain the suffix from the default product flavor, followed by the suffix from product flavor of the first dimension, second dimension and so on. All of these will have a dot in between e.g. "defaultSuffix.dimension1Suffix.dimensions2Suffix".

### multiDexEnabled

Added in 4.2.0
    
    
    var [multiDexEnabled](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationVariantDimension#multiDexEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Returns whether multi-dex is enabled.

This can be null if the flag is not set, in which case the default value is used.

### signingConfig

Added in 4.2.0
    
    
    var [signingConfig](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationVariantDimension#signingConfig\(\)): [ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApkSigningConfig)?

The associated signing config or null if none are set on the variant dimension.

### versionNameSuffix

Added in 4.2.0
    
    
    var [versionNameSuffix](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ApplicationVariantDimension#versionNameSuffix\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Version name suffix. It is appended to the "base" version name when calculating the final version name for a variant.

In case there are product flavor dimensions specified, the final version name suffix will contain the suffix from the default product flavor, followed by the suffix from product flavor of the first dimension, second dimension and so on.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
