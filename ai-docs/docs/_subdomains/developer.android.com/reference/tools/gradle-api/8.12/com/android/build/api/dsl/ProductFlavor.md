---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ProductFlavor/
title: ProductFlavor \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:02:46.575567+00:00
---

# ProductFlavor  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ProductFlavor/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ProductFlavor

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ProductFlavor.kt+class:com.android.build.api.dsl.ProductFlavor)

Added in 4.2.0
    
    
    interface [ProductFlavor](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ProductFlavor) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html), [BaseFlavor](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor), [ExtensionAware](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html)

Known direct subclasses 

[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApplicationProductFlavor), [DynamicFeatureProductFlavor](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DynamicFeatureProductFlavor), [LibraryProductFlavor](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/LibraryProductFlavor), [TestProductFlavor](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TestProductFlavor)

`[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApplicationProductFlavor)` |  Encapsulates all product flavors properties for application projects.  
---|---  
`[DynamicFeatureProductFlavor](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DynamicFeatureProductFlavor)` |  Encapsulates all product flavors properties for dynamic feature projects.  
`[LibraryProductFlavor](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/LibraryProductFlavor)` |  Encapsulates all product flavors properties for library projects.  
`[TestProductFlavor](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TestProductFlavor)` |  Encapsulates all product flavors properties for test projects.  
  
* * *

Encapsulates all product flavors properties for this project.

Product flavors represent different versions of your project that you expect to co-exist on a single device, the Google Play store, or repository. For example, you can configure 'demo' and 'full' product flavors for your app, and each of those flavors can specify different features, device requirements, resources, and application ID's--while sharing common source code and resources. So, product flavors allow you to output different versions of your project by simply changing only the components and settings that are different between them.

Configuring product flavors is similar to [configuring build types](https://developer.android.com/studio/build/build-variants.html#build-types): add them to the `productFlavors` block of your project's `build.gradle` file and configure the settings you want.

Product flavors support the same properties as the `[DefaultConfig](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DefaultConfig)` block—this is because `defaultConfig` defines a `[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ProductFlavor)` object that the plugin uses as the base configuration for all other flavors. Each flavor you configure can then override any of the default values in `defaultConfig`, such as the [`applicationId`](https://d.android.com/studio/build/application-id.html).

When using Android plugin 3.0.0 and higher, _`[each flavor must belong to a`dimension`](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ProductFlavor#dimension\(\))`_.

When you configure product flavors, the Android plugin automatically combines them with your `[BuildType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BuildType)` configurations to [create build variants](https://developer.android.com/studio/build/build-variants.html). If the plugin creates certain build variants that you don't want, you can [filter variants using `android.variantFilter`](https://developer.android.com/studio/build/build-variants.html#filter-variants).

## Summary

### Public functions  
  
---  
`[Void](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Void.html)?` |  `~~[setDimension](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ProductFlavor#setDimension\(kotlin.String\))~~(dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)` **This function is deprecated.** Replaced with the dimension property  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[setMatchingFallbacks](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ProductFlavor#setMatchingFallbacks\(kotlin.collections.List\))~~(fallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>)` **This function is deprecated.** Replaced with property matchingFallbacks  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[setMatchingFallbacks](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ProductFlavor#setMatchingFallbacks\(kotlin.Array\))~~(vararg fallbacks: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property matchingFallbacks  
  
### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[dimension](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ProductFlavor#dimension\(\))` Specifies the flavor dimension that this product flavor belongs to.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[matchingFallbacks](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ProductFlavor#matchingFallbacks\(\))` Specifies a sorted list of product flavors that the plugin should try to use when a direct variant match with a local module dependency is not possible.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.BaseFlavor](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[initWith](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#initWith\(com.android.build.api.dsl.BaseFlavor\))(that: [BaseFlavor](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor))` Copies all properties from the given flavor.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#minSdk\(kotlin.Function1\))(action: [MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/MinSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding minSdk, see `[MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/MinSdkSpec)` for available options.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[minSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#minSdkVersion\(kotlin.Int\))~~(minSdkVersion: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` **This function is deprecated.** Will be removed in AGP 10.0, replaced with the minSdk block  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[minSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#minSdkVersion\(kotlin.String\))~~(minSdkVersion: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)` **This function is deprecated.** Will be removed in AGP 10.0, replaced with the minSdk block  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[missingDimensionStrategy](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#missingDimensionStrategy\(kotlin.String,kotlin.String\))(dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), requestedValue: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Specifies a flavor that the plugin should try to use from a given dimension in a dependency.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[missingDimensionStrategy](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#missingDimensionStrategy\(kotlin.String,kotlin.collections.List\))(  
dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),  
requestedValues: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>  
)` Specifies a sorted list of flavors that the plugin should try to use from a given dimension in a dependency.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[missingDimensionStrategy](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#missingDimensionStrategy\(kotlin.String,kotlin.Array\))(  
dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),  
vararg requestedValues: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)  
)` Specifies a sorted list of flavors that the plugin should try to use from a given dimension in a dependency.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[resConfig](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#resConfig\(kotlin.String\))~~(config: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Support for resource configurations will be removed.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[resConfigs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#resConfigs\(kotlin.collections.Collection\))~~(config: [Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>)` **This function is deprecated.** Support for resource configurations will be removed.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[resConfigs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#resConfigs\(kotlin.Array\))~~(vararg config: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Support for resource configurations will be removed.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[setMinSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#setMinSdkVersion\(kotlin.Int\))~~(minSdkVersion: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` **This function is deprecated.** Will be removed in AGP 10.0, replaced with the minSdk block  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[setMinSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#setMinSdkVersion\(kotlin.String\))~~(minSdkVersion: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)` **This function is deprecated.** Will be removed in AGP 10.0, replaced with the minSdk block  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?` |  `~~[setTestFunctionalTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#setTestFunctionalTest\(kotlin.Boolean\))~~(testFunctionalTest: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` **This function is deprecated.** Replaced by testFunctionalTest property  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?` |  `~~[setTestHandleProfiling](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#setTestHandleProfiling\(kotlin.Boolean\))~~(testHandleProfiling: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` **This function is deprecated.** Replaced by testFunctionalTest property  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?` |  `~~[setTestInstrumentationRunnerArguments](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#setTestInstrumentationRunnerArguments\(kotlin.collections.MutableMap\))~~(  
testInstrumentationRunnerArguments: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>  
)` **This function is deprecated.** Replaced by testInstrumentationRunnerArguments property  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[testInstrumentationRunnerArgument](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#testInstrumentationRunnerArgument\(kotlin.String,kotlin.String\))~~(key: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by testInstrumentationRunnerArguments property  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[testInstrumentationRunnerArguments](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#testInstrumentationRunnerArguments\(kotlin.collections.Map\))~~(args: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>)` **This function is deprecated.** Replaced by testInstrumentationRunnerArguments property  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[vectorDrawables](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#vectorDrawables\(kotlin.Function1\))(action: [VectorDrawables](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VectorDrawables).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures `[VectorDrawables](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VectorDrawables)`.  
  
From [org.gradle.api.plugins.ExtensionAware](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html) | `[ExtensionContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionContainer.html)` |  `@[Internal](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/Internal.html)  
[getExtensions](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionAware.html#getExtensions--)()`  
---|---  
  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
From [com.android.build.api.dsl.VariantDimension](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[addManifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#addManifestPlaceholders\(kotlin.collections.Map\))(manifestPlaceholders: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>)` Adds manifest placeholders.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[buildConfigField](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#buildConfigField\(kotlin.String,kotlin.String,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds a new field to the generated BuildConfig class.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#externalNativeBuild\(kotlin.Function1\))(action: [ExternalNativeBuildFlags](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ExternalNativeBuildFlags).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates per-variant CMake and ndk-build configurations for your external native build.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[javaCompileOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#javaCompileOptions\(kotlin.Function1\))(action: [JavaCompileOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/JavaCompileOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Options for configuring Java compilation.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[ndk](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#ndk\(kotlin.Function1\))(action: [Ndk](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Ndk).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates per-variant configurations for the NDK, such as ABI filters.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[optimization](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#optimization\(kotlin.Function1\))(action: [Optimization](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Optimization).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[proguardFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#proguardFile\(kotlin.Any\))(proguardFile: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds a new ProGuard configuration file.  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[proguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#proguardFiles\(kotlin.Array\))(vararg files: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds new ProGuard configuration files.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[resValue](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#resValue\(kotlin.String,kotlin.String,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds a new generated resource.  
`[Void](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Void.html)?` |  `~~[setManifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#setManifestPlaceholders\(kotlin.collections.Map\))~~(manifestPlaceholders: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>)` **This function is deprecated.** Use manifestPlaceholders property instead  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[setProguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#setProguardFiles\(kotlin.collections.Iterable\))(proguardFileIterable: [Iterable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html)<*>)` Replaces the ProGuard configuration files.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#shaders\(kotlin.Function1\))(action: [Shaders](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Shaders).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configure the shader compiler options.  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[testProguardFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#testProguardFile\(kotlin.Any\))(proguardFile: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds a proguard rule file to be used when processing test code.  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[testProguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#testProguardFiles\(kotlin.Array\))(vararg proguardFiles: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds proguard rule files to be used when processing test code.  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.BaseFlavor](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor) | `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#minSdk\(\))` The minimum SDK version.  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#minSdkPreview\(\))` **This property is deprecated.** Will be removed in AGP 10.0, replaced with the minSdk block  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[renderscriptNdkModeEnabled](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#renderscriptNdkModeEnabled\(\))` Whether the renderscript code should be compiled to generate C/C++ bindings.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[renderscriptSupportModeBlasEnabled](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#renderscriptSupportModeBlasEnabled\(\))` Whether the renderscript BLAS support lib should be used to make it compatible with older versions of Android.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[renderscriptSupportModeEnabled](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#renderscriptSupportModeEnabled\(\))` Whether the renderscript code should be compiled in support mode to make it compatible with older versions of Android.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[renderscriptTargetApi](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#renderscriptTargetApi\(\))` The renderscript target api, or null if not specified.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[resourceConfigurations](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#resourceConfigurations\(\))` **This property is deprecated.** Support for resource configurations will be removed.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[testApplicationId](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#testApplicationId\(\))` Test application ID.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[testFunctionalTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#testFunctionalTest\(\))` See [instrumentation](http://developer.android.com/guide/topics/manifest/instrumentation-element.html).  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[testHandleProfiling](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#testHandleProfiling\(\))` See [instrumentation](http://developer.android.com/guide/topics/manifest/instrumentation-element.html).  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[testInstrumentationRunner](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#testInstrumentationRunner\(\))` Test instrumentation runner class name.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[testInstrumentationRunnerArguments](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#testInstrumentationRunnerArguments\(\))` Test instrumentation runner custom arguments.  
`[VectorDrawables](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VectorDrawables)` |  `[vectorDrawables](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#vectorDrawables\(\))` Options to configure the build-time support for `vector` drawables.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[wearAppUnbundled](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#wearAppUnbundled\(\))` Whether to enable unbundling mode for embedded wear app.  
  
From [com.android.build.api.dsl.VariantDimension](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension) | `[ExternalNativeBuildFlags](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ExternalNativeBuildFlags)` |  `[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#externalNativeBuild\(\))` Encapsulates per-variant CMake and ndk-build configurations for your external native build.  
---|---  
`[JavaCompileOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/JavaCompileOptions)` |  `[javaCompileOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#javaCompileOptions\(\))` Options for configuring Java compilation.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[manifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#manifestPlaceholders\(\))` The manifest placeholders.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[multiDexKeepFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#multiDexKeepFile\(\))` **This property is deprecated.** This property is deprecated.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[multiDexKeepProguard](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#multiDexKeepProguard\(\))` Text file with additional ProGuard rules to be used to determine which classes are compiled into the main dex file.  
`[Ndk](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Ndk)` |  `[ndk](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#ndk\(\))` Encapsulates per-variant configurations for the NDK, such as ABI filters.  
`[Optimization](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Optimization)` |  `[optimization](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#optimization\(\))`  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>` |  `[proguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#proguardFiles\(\))` Specifies the ProGuard configuration files that the plugin should use.  
`[Shaders](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Shaders)` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#shaders\(\))` Options for configuring the shader compiler.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>` |  `[testProguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/VariantDimension#testProguardFiles\(\))` The collection of proguard rule files to be used when processing test code.  
  
## Public functions

### setDimension

Added in 4.2.0

Deprecated in 8.12.3
    
    
    fun ~~[setDimension](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ProductFlavor#setDimension\(kotlin.String\))~~(dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?): [Void](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Void.html)?

**This function is deprecated.**  
Replaced with the dimension property

### setMatchingFallbacks

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[setMatchingFallbacks](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ProductFlavor#setMatchingFallbacks\(kotlin.collections.List\))~~(fallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced with property matchingFallbacks

### setMatchingFallbacks

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[setMatchingFallbacks](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ProductFlavor#setMatchingFallbacks\(kotlin.Array\))~~(vararg fallbacks: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced with property matchingFallbacks

## Public properties

### dimension

Added in 4.2.0
    
    
    var [dimension](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ProductFlavor#dimension\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Specifies the flavor dimension that this product flavor belongs to.

When configuring product flavors with Android plugin 3.0.0 and higher, you must specify at least one flavor dimension, using the `flavorDimensions` property, and then assign each flavor to a dimension. Otherwise, you will get the following build error:
    
    
    Error:All flavors must now belong to a named flavor dimension.  
    The flavor 'flavor_name' is not assigned to a flavor dimension.

By default, when you specify only one dimension, all flavors you configure automatically belong to that dimension. If you specify more than one dimension, you need to manually assign each flavor to a dimension, as shown in the sample below:
    
    
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

To learn more about configuring flavor dimensions, read [Combine multiple flavors](https://developer.android.com/studio/build/build-variants.html#flavor-dimensions).

### matchingFallbacks

Added in 4.2.0
    
    
    val [matchingFallbacks](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ProductFlavor#matchingFallbacks\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies a sorted list of product flavors that the plugin should try to use when a direct variant match with a local module dependency is not possible.

Android plugin 3.0.0 and higher try to match each variant of your module with the same one from its dependencies. For example, when you build a "freeDebug" version of your app, the plugin tries to match it with "freeDebug" versions of the local library modules the app depends on.

However, there may be situations in which, for a given flavor dimension that exists in both the app and its library dependencies, **your app includes flavors that a dependency does not**. For example, consider if both your app and its library dependencies include a "tier" flavor dimension. However, the "tier" dimension in the app includes "free" and "paid" flavors, but one of its dependencies includes only "demo" and "paid" flavors for the same dimension. When the plugin tries to build the "free" version of your app, it won't know which version of the dependency to use, and you'll see an error message similar to the following:
    
    
    Error:Failed to resolve: Could not resolve project :mylibrary.  
    Required by:  
    project :app

In this situation, you should use `matchingFallbacks` to specify alternative matches for the app's "free" product flavor, as shown below:
    
    
    // In the app's build.gradle file.  
    android {  
        flavorDimensions 'tier'  
        productFlavors {  
            paid {  
                dimension 'tier'  
                // Because the dependency already includes a "paid" flavor in its  
                // "tier" dimension, you don't need to provide a list of fallbacks  
                // for the "paid" flavor.  
            }  
            free {  
                dimension 'tier'  
                // Specifies a sorted list of fallback flavors that the plugin  
                // should try to use when a dependency's matching dimension does  
                // not include a "free" flavor. You may specify as many  
                // fallbacks as you like, and the plugin selects the first flavor  
                // that's available in the dependency's "tier" dimension.  
                matchingFallbacks = ['demo', 'trial']  
            }  
        }  
    }

Note that, for a given flavor dimension that exists in both the app and its library dependencies, there is no issue when a library includes a product flavor that your app does not. That's because the plugin simply never requests that flavor from the dependency.

If instead you are trying to resolve an issue in which **a library dependency includes a flavor dimension that your app does not** , use `[BaseFlavor.missingDimensionStrategy](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BaseFlavor#missingDimensionStrategy\(kotlin.String,kotlin.String\))`.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-09-11 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-11 UTC."],[],[]] 
