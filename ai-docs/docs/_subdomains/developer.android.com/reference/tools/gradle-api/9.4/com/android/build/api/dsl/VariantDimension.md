---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension/
title: VariantDimension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:56:51.646465+00:00
---

# VariantDimension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# VariantDimension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/VariantDimension.kt+class:com.android.build.api.dsl.VariantDimension)

Added in 4.2.0
    
    
    interface [VariantDimension](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension)

Known direct subclasses 

[ApplicationVariantDimension](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationVariantDimension), [BaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/BaseFlavor), [BuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/BuildType), [DynamicFeatureVariantDimension](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DynamicFeatureVariantDimension), [LibraryVariantDimension](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryVariantDimension), [TestVariantDimension](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestVariantDimension)

`[ApplicationVariantDimension](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationVariantDimension)` |  Shared properties between DSL objects that contribute to an application variant.  
---|---  
`[BaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/BaseFlavor)` |  Shared properties between DSL objects `[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ProductFlavor)` and `[DefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DefaultConfig)`  
`[BuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/BuildType)` |  Build types define certain properties that Gradle uses when building and packaging your app, and are typically configured for different stages of your development lifecycle.  
`[DynamicFeatureVariantDimension](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DynamicFeatureVariantDimension)` |  Shared properties between DSL objects that contribute to an dynamic feature variant.  
`[LibraryVariantDimension](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryVariantDimension)` |  Shared properties between DSL objects that contribute to a library variant.  
`[TestVariantDimension](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestVariantDimension)` |  Shared properties between DSL objects that contribute to a separate-test-project variant.  
  
Known indirect subclasses 

[ApplicationBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationBaseFlavor), [ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationBuildType), [ApplicationDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationDefaultConfig), [ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationProductFlavor), [DefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DefaultConfig), [DynamicFeatureBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DynamicFeatureBaseFlavor), [DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DynamicFeatureBuildType), [DynamicFeatureDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DynamicFeatureDefaultConfig), [DynamicFeatureProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DynamicFeatureProductFlavor), [LibraryBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryBaseFlavor), [LibraryBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryBuildType), [LibraryDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDefaultConfig), [LibraryProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryProductFlavor), [ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ProductFlavor), [TestBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestBaseFlavor), [TestBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestBuildType), [TestDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestDefaultConfig), [TestProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestProductFlavor)

`[ApplicationBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationBaseFlavor)` |  Shared properties between `[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationProductFlavor)` and `[ApplicationDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationDefaultConfig)`  
---|---  
`[ApplicationBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationBuildType)` |  Build types define certain properties that Gradle uses when building and packaging your app, and are typically configured for different stages of your development lifecycle.  
`[ApplicationDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationDefaultConfig)` |  Specifies defaults for properties that the Android application plugin applies to all build variants.  
`[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationProductFlavor)` |  Encapsulates all product flavors properties for application projects.  
`[DefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DefaultConfig)` |  Specifies defaults for variant properties that the Android plugin applies to all build variants.  
`[DynamicFeatureBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DynamicFeatureBaseFlavor)` |  Shared properties between DSL objects `[DynamicFeatureProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DynamicFeatureProductFlavor)` and `[DynamicFeatureDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DynamicFeatureDefaultConfig)`  
`[DynamicFeatureBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DynamicFeatureBuildType)` |  Build types define certain properties that Gradle uses when building and packaging your app, and are typically configured for different stages of your development lifecycle.  
`[DynamicFeatureDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DynamicFeatureDefaultConfig)` |  Specifies defaults for properties that the Android dynamic-feature plugin applies to all build variants.  
`[DynamicFeatureProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DynamicFeatureProductFlavor)` |  Encapsulates all product flavors properties for dynamic feature projects.  
`[LibraryBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryBaseFlavor)` |  Shared properties between `[LibraryProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryProductFlavor)` and `[LibraryDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDefaultConfig)`  
`[LibraryBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryBuildType)` |  Build types define certain properties that Gradle uses when building and packaging your library, and are typically configured for different stages of your development lifecycle.  
`[LibraryDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryDefaultConfig)` |  Specifies defaults for properties that the Android library plugin applies to all build variants.  
`[LibraryProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryProductFlavor)` |  Encapsulates all product flavors properties for library projects.  
`[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ProductFlavor)` |  Encapsulates all product flavors properties for this project.  
`[TestBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestBaseFlavor)` |  Shared properties between `[TestProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestProductFlavor)` and `[TestDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestDefaultConfig)`  
`[TestBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestBuildType)` |  Build types define certain properties that Gradle uses when building and packaging your library, and are typically configured for different stages of your development lifecycle.  
`[TestDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestDefaultConfig)` |  Specifies defaults for properties that the Android test plugin applies to all build variants.  
`[TestProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestProductFlavor)` |  Encapsulates all product flavors properties for test projects.  
  
* * *

Shared properties between DSL objects that contribute to a variant.

That is, `[BuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/BuildType)` and `[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ProductFlavor)` and `[DefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DefaultConfig)`.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[addManifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#addManifestPlaceholders\(kotlin.collections.Map\))(manifestPlaceholders: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>)` Adds manifest placeholders.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[buildConfigField](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#buildConfigField\(kotlin.String,kotlin.String,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds a new field to the generated BuildConfig class.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#externalNativeBuild\(kotlin.Function1\))(action: [ExternalNativeBuildFlags](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuildFlags).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates per-variant CMake and ndk-build configurations for your external native build.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[javaCompileOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#javaCompileOptions\(kotlin.Function1\))(action: [JavaCompileOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/JavaCompileOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Options for configuring Java compilation.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[ndk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#ndk\(kotlin.Function1\))(action: [Ndk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Ndk).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates per-variant configurations for the NDK, such as ABI filters.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[optimization](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#optimization\(kotlin.Function1\))~~(action: [Optimization](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Optimization).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Use ApplicationBuildType.optimization(action) instead  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[proguardFile](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#proguardFile\(kotlin.Any\))(proguardFile: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds a new ProGuard configuration file.  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[proguardFiles](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#proguardFiles\(kotlin.Array\))(vararg files: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds new ProGuard configuration files.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[resValue](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#resValue\(kotlin.String,kotlin.String,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds a new generated resource.  
`[Void](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Void.html)?` |  `@[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.4/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
~~[setManifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#setManifestPlaceholders\(kotlin.collections.Map\))~~(manifestPlaceholders: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>)` **This function is deprecated.** Use manifestPlaceholders property instead  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[setProguardFiles](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#setProguardFiles\(kotlin.collections.Iterable\))(proguardFileIterable: [Iterable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html)<*>)` Replaces the ProGuard configuration files.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#shaders\(kotlin.Function1\))(action: [Shaders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Shaders).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configure the shader compiler options.  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[testProguardFile](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#testProguardFile\(kotlin.Any\))(proguardFile: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds a proguard rule file to be used when processing test code.  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[testProguardFiles](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#testProguardFiles\(kotlin.Array\))(vararg proguardFiles: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds proguard rule files to be used when processing test code.  
  
### Public properties  
  
---  
`[ExternalNativeBuildFlags](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuildFlags)` |  `[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#externalNativeBuild\(\))` Encapsulates per-variant CMake and ndk-build configurations for your external native build.  
`[JavaCompileOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/JavaCompileOptions)` |  `[javaCompileOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#javaCompileOptions\(\))` Options for configuring Java compilation.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[manifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#manifestPlaceholders\(\))` The manifest placeholders.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[multiDexKeepFile](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#multiDexKeepFile\(\))` **This property is deprecated.** This property is deprecated.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[multiDexKeepProguard](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#multiDexKeepProguard\(\))` Text file with additional ProGuard rules to be used to determine which classes are compiled into the main dex file.  
`[Ndk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Ndk)` |  `[ndk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#ndk\(\))` Encapsulates per-variant configurations for the NDK, such as ABI filters.  
`[Optimization](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Optimization)` |  `[optimization](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#optimization\(\))` **This property is deprecated.** Use ApplicationBuildType.optimization instead  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>` |  `[proguardFiles](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#proguardFiles\(\))` Specifies the ProGuard configuration files that the plugin should use.  
`[Shaders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Shaders)` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#shaders\(\))` Options for configuring the shader compiler.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>` |  `[testProguardFiles](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#testProguardFiles\(\))` The collection of proguard rule files to be used when processing test code.  
  
## Public functions

### addManifestPlaceholders
    
    
    fun [addManifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#addManifestPlaceholders\(kotlin.collections.Map\))(manifestPlaceholders: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds manifest placeholders.

See [Inject Build Variables into the Manifest](https://developer.android.com/studio/build/manifest-build-variables.html).

### buildConfigField

Added in 4.2.0
    
    
    fun [buildConfigField](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#buildConfigField\(kotlin.String,kotlin.String,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds a new field to the generated BuildConfig class.

The field is generated as: `<type> <name> = <value>;`

This means each of these must have valid Java content. If the type is a String, then the value should include quotes.

Parameters  
---  
`type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the type of the field  
`name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the name of the field  
`value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the value of the field  
  
### externalNativeBuild

Added in 8.0.2
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#externalNativeBuild\(kotlin.Function1\))(action: [ExternalNativeBuildFlags](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuildFlags).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Encapsulates per-variant CMake and ndk-build configurations for your external native build.

To learn more, see [Add C and C++ Code to Your Project](http://developer.android.com/studio/projects/add-native-code.html).

### javaCompileOptions

Added in 4.2.0
    
    
    fun [javaCompileOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#javaCompileOptions\(kotlin.Function1\))(action: [JavaCompileOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/JavaCompileOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Options for configuring Java compilation.

### ndk

Added in 4.2.0
    
    
    fun [ndk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#ndk\(kotlin.Function1\))(action: [Ndk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Ndk).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Encapsulates per-variant configurations for the NDK, such as ABI filters.

### optimization

Added in 7.3.0

Deprecated in 8.13.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[optimization](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#optimization\(kotlin.Function1\))~~(action: [Optimization](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Optimization).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Use ApplicationBuildType.optimization(action) instead

### proguardFile

Added in 4.2.0
    
    
    fun [proguardFile](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#proguardFile\(kotlin.Any\))(proguardFile: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)

Adds a new ProGuard configuration file.

`proguardFile getDefaultProguardFile('proguard-android-optimize.txt')`

There are two ProGuard rules files that ship with the Android plugin and are used by default:

  * proguard-android.txt

  * proguard-android-optimize.txt




`proguard-android-optimize.txt` is identical to `proguard-android.txt`, except with optimizations enabled. You can use getDefaultProguardFile(String) to return the full path of the files.

This method has a return value for legacy reasons.

### proguardFiles

Added in 4.2.0
    
    
    fun [proguardFiles](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#proguardFiles\(kotlin.Array\))(vararg files: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)

Adds new ProGuard configuration files.

There are two ProGuard rules files that ship with the Android plugin and are used by default:

  * proguard-android.txt

  * proguard-android-optimize.txt




`proguard-android-optimize.txt` is identical to `proguard-android.txt`, except with optimizations enabled. You can use getDefaultProguardFile(String) to return the full path of the files.

This method has a return value for legacy reasons.

### resValue

Added in 4.2.0
    
    
    fun [resValue](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#resValue\(kotlin.String,kotlin.String,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds a new generated resource.

This is equivalent to specifying a resource in res/values.

See [Resource Types](http://developer.android.com/guide/topics/resources/available-resources.html).

Parameters  
---  
`type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the type of the resource  
`name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the name of the resource  
`value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the value of the resource  
  
### setManifestPlaceholders
    
    
    @[HiddenInDefinition](https://developer.android.com/reference/tools/gradle-api/9.4/org/gradle/declarative/dsl/model/annotations/HiddenInDefinition)  
    fun ~~[setManifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#setManifestPlaceholders\(kotlin.collections.Map\))~~(manifestPlaceholders: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>): [Void](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Void.html)?

**This function is deprecated.**  
Use manifestPlaceholders property instead

### setProguardFiles

Added in 7.0.0
    
    
    fun [setProguardFiles](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#setProguardFiles\(kotlin.collections.Iterable\))(proguardFileIterable: [Iterable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html)<*>): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)

Replaces the ProGuard configuration files.

This method has a return value for legacy reasons.

### shaders

Added in 4.2.0
    
    
    fun [shaders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#shaders\(kotlin.Function1\))(action: [Shaders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Shaders).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configure the shader compiler options.

### testProguardFile

Added in 4.2.0
    
    
    fun [testProguardFile](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#testProguardFile\(kotlin.Any\))(proguardFile: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)

Adds a proguard rule file to be used when processing test code.

Test code needs to be processed to apply the same obfuscation as was done to main code.

This method has a return value for legacy reasons.

### testProguardFiles

Added in 4.2.0
    
    
    fun [testProguardFiles](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#testProguardFiles\(kotlin.Array\))(vararg proguardFiles: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)

Adds proguard rule files to be used when processing test code.

Test code needs to be processed to apply the same obfuscation as was done to main code.

This method has a return value for legacy reasons.

## Public properties

### externalNativeBuild

Added in 4.2.0
    
    
    val [externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#externalNativeBuild\(\)): [ExternalNativeBuildFlags](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuildFlags)

Encapsulates per-variant CMake and ndk-build configurations for your external native build.

To learn more, see [Add C and C++ Code to Your Project](http://developer.android.com/studio/projects/add-native-code.html).

### javaCompileOptions

Added in 4.2.0
    
    
    val [javaCompileOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#javaCompileOptions\(\)): [JavaCompileOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/JavaCompileOptions)

Options for configuring Java compilation.

### manifestPlaceholders

Added in 4.2.0
    
    
    val [manifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#manifestPlaceholders\(\)): [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>

The manifest placeholders.

See [Inject Build Variables into the Manifest](https://developer.android.com/studio/build/manifest-build-variables.html).

### multiDexKeepFile

Added in 4.2.0

Deprecated in 7.0.0
    
    
    var [multiDexKeepFile](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#multiDexKeepFile\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?

**This property is deprecated.**  
This property is deprecated. Migrate to multiDexKeepProguard.

Text file that specifies additional classes that will be compiled into the main dex file.

Classes specified in the file are appended to the main dex classes computed using `aapt`.

If set, the file should contain one class per line, in the following format: `com/example/MyClass.class`

### multiDexKeepProguard

Added in 4.2.0
    
    
    var [multiDexKeepProguard](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#multiDexKeepProguard\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?

Text file with additional ProGuard rules to be used to determine which classes are compiled into the main dex file.

If set, rules from this file are used in combination with the default rules used by the build system.

### ndk

Added in 4.2.0
    
    
    val [ndk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#ndk\(\)): [Ndk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Ndk)

Encapsulates per-variant configurations for the NDK, such as ABI filters.

### optimization

Added in 7.3.0

Deprecated in 8.13.0
    
    
    val [optimization](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#optimization\(\)): [Optimization](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Optimization)

**This property is deprecated.**  
Use ApplicationBuildType.optimization instead

### proguardFiles

Added in 4.2.0
    
    
    val [proguardFiles](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#proguardFiles\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>

Specifies the ProGuard configuration files that the plugin should use.

There are two ProGuard rules files that ship with the Android plugin and are used by default:

  * proguard-android.txt

  * proguard-android-optimize.txt




`proguard-android-optimize.txt` is identical to `proguard-android.txt`, except with optimizations enabled. You can use getDefaultProguardFile(String) to return the full path of the files.

Returns  
---  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>` |  a non-null collection of files.  
  
### shaders

Added in 4.2.0
    
    
    val [shaders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#shaders\(\)): [Shaders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Shaders)

Options for configuring the shader compiler.

### testProguardFiles

Added in 4.2.0
    
    
    val [testProguardFiles](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/VariantDimension#testProguardFiles\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>

The collection of proguard rule files to be used when processing test code.

Test code needs to be processed to apply the same obfuscation as was done to main code.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
