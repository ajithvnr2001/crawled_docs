---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor/
title: BaseFlavor \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:16:22.897445+00:00
---

# BaseFlavor  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BaseFlavor

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/BaseFlavor.kt+class:com.android.build.api.dsl.BaseFlavor)

Added in 4.2.0
    
    
    interface [BaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor) : [VariantDimension](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension)

Known direct subclasses 

[ApplicationBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApplicationBaseFlavor), [DefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DefaultConfig), [DynamicFeatureBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBaseFlavor), [LibraryBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/LibraryBaseFlavor), [ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ProductFlavor), [TestBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestBaseFlavor)

`[ApplicationBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApplicationBaseFlavor)` |  Shared properties between `[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApplicationProductFlavor)` and `[ApplicationDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApplicationDefaultConfig)`  
---|---  
`[DefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DefaultConfig)` |  Specifies defaults for variant properties that the Android plugin applies to all build variants.  
`[DynamicFeatureBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureBaseFlavor)` |  Shared properties between DSL objects `[DynamicFeatureProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureProductFlavor)` and `[DynamicFeatureDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureDefaultConfig)`  
`[LibraryBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/LibraryBaseFlavor)` |  Shared properties between `[LibraryProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/LibraryProductFlavor)` and `[LibraryDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/LibraryDefaultConfig)`  
`[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ProductFlavor)` |  Encapsulates all product flavors properties for this project.  
`[TestBaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestBaseFlavor)` |  Shared properties between `[TestProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestProductFlavor)` and `[TestDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestDefaultConfig)`  
  
Known indirect subclasses 

[ApplicationDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApplicationDefaultConfig), [ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApplicationProductFlavor), [DynamicFeatureDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureDefaultConfig), [DynamicFeatureProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureProductFlavor), [LibraryDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/LibraryDefaultConfig), [LibraryProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/LibraryProductFlavor), [TestDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestDefaultConfig), [TestProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestProductFlavor)

`[ApplicationDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApplicationDefaultConfig)` |  Specifies defaults for properties that the Android application plugin applies to all build variants.  
---|---  
`[ApplicationProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ApplicationProductFlavor)` |  Encapsulates all product flavors properties for application projects.  
`[DynamicFeatureDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureDefaultConfig)` |  Specifies defaults for properties that the Android dynamic-feature plugin applies to all build variants.  
`[DynamicFeatureProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicFeatureProductFlavor)` |  Encapsulates all product flavors properties for dynamic feature projects.  
`[LibraryDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/LibraryDefaultConfig)` |  Specifies defaults for properties that the Android library plugin applies to all build variants.  
`[LibraryProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/LibraryProductFlavor)` |  Encapsulates all product flavors properties for library projects.  
`[TestDefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestDefaultConfig)` |  Specifies defaults for properties that the Android test plugin applies to all build variants.  
`[TestProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestProductFlavor)` |  Encapsulates all product flavors properties for test projects.  
  
* * *

Shared properties between DSL objects `[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ProductFlavor)` and `[DefaultConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DefaultConfig)`

## Summary

### Public functions  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#getName\(\))()` The name of the flavor.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[initWith](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#initWith\(com.android.build.api.dsl.BaseFlavor\))(that: [BaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor))` Copies all properties from the given flavor.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdk\(kotlin.Function1\))(action: [MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/MinSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding minSdk, see `[MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/MinSdkSpec)` for available options.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[minSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdkVersion\(kotlin.Int\))~~(minSdkVersion: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` **This function is deprecated.** Will be removed in AGP 10.0, replaced with the minSdk block  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[minSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdkVersion\(kotlin.String\))~~(minSdkVersion: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)` **This function is deprecated.** Will be removed in AGP 10.0, replaced with the minSdk block  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[missingDimensionStrategy](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#missingDimensionStrategy\(kotlin.String,kotlin.String\))(dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), requestedValue: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Specifies a flavor that the plugin should try to use from a given dimension in a dependency.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[missingDimensionStrategy](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#missingDimensionStrategy\(kotlin.String,kotlin.collections.List\))(  
dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),  
requestedValues: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>  
)` Specifies a sorted list of flavors that the plugin should try to use from a given dimension in a dependency.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[missingDimensionStrategy](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#missingDimensionStrategy\(kotlin.String,kotlin.Array\))(  
dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),  
vararg requestedValues: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)  
)` Specifies a sorted list of flavors that the plugin should try to use from a given dimension in a dependency.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[resConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#resConfig\(kotlin.String\))~~(config: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Support for resource configurations will be removed.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[resConfigs](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#resConfigs\(kotlin.collections.Collection\))~~(config: [Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>)` **This function is deprecated.** Support for resource configurations will be removed.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[resConfigs](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#resConfigs\(kotlin.Array\))~~(vararg config: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Support for resource configurations will be removed.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[setMinSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#setMinSdkVersion\(kotlin.Int\))~~(minSdkVersion: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` **This function is deprecated.** Will be removed in AGP 10.0, replaced with the minSdk block  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[setMinSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#setMinSdkVersion\(kotlin.String\))~~(minSdkVersion: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)` **This function is deprecated.** Will be removed in AGP 10.0, replaced with the minSdk block  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?` |  `~~[setTestFunctionalTest](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#setTestFunctionalTest\(kotlin.Boolean\))~~(testFunctionalTest: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` **This function is deprecated.** Replaced by testFunctionalTest property  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?` |  `~~[setTestHandleProfiling](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#setTestHandleProfiling\(kotlin.Boolean\))~~(testHandleProfiling: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` **This function is deprecated.** Replaced by testFunctionalTest property  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?` |  `~~[setTestInstrumentationRunnerArguments](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#setTestInstrumentationRunnerArguments\(kotlin.collections.MutableMap\))~~(  
testInstrumentationRunnerArguments: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>  
)` **This function is deprecated.** Replaced by testInstrumentationRunnerArguments property  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[testInstrumentationRunnerArgument](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#testInstrumentationRunnerArgument\(kotlin.String,kotlin.String\))~~(key: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by testInstrumentationRunnerArguments property  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[testInstrumentationRunnerArguments](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#testInstrumentationRunnerArguments\(kotlin.collections.Map\))~~(args: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>)` **This function is deprecated.** Replaced by testInstrumentationRunnerArguments property  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[vectorDrawables](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#vectorDrawables\(kotlin.Function1\))(action: [VectorDrawables](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VectorDrawables).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures `[VectorDrawables](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VectorDrawables)`.  
  
### Public properties  
  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdk\(\))` The minimum SDK version.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdkPreview\(\))` **This property is deprecated.** Will be removed in AGP 10.0, replaced with the minSdk block  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[renderscriptNdkModeEnabled](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#renderscriptNdkModeEnabled\(\))` Whether the renderscript code should be compiled to generate C/C++ bindings.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[renderscriptSupportModeBlasEnabled](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#renderscriptSupportModeBlasEnabled\(\))` Whether the renderscript BLAS support lib should be used to make it compatible with older versions of Android.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[renderscriptSupportModeEnabled](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#renderscriptSupportModeEnabled\(\))` Whether the renderscript code should be compiled in support mode to make it compatible with older versions of Android.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[renderscriptTargetApi](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#renderscriptTargetApi\(\))` The renderscript target api, or null if not specified.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[resourceConfigurations](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#resourceConfigurations\(\))` **This property is deprecated.** Support for resource configurations will be removed.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[testApplicationId](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#testApplicationId\(\))` Test application ID.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[testFunctionalTest](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#testFunctionalTest\(\))` See [instrumentation](http://developer.android.com/guide/topics/manifest/instrumentation-element.html).  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[testHandleProfiling](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#testHandleProfiling\(\))` See [instrumentation](http://developer.android.com/guide/topics/manifest/instrumentation-element.html).  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[testInstrumentationRunner](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#testInstrumentationRunner\(\))` Test instrumentation runner class name.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[testInstrumentationRunnerArguments](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#testInstrumentationRunnerArguments\(\))` Test instrumentation runner custom arguments.  
`[VectorDrawables](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VectorDrawables)` |  `[vectorDrawables](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#vectorDrawables\(\))` Options to configure the build-time support for `vector` drawables.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[wearAppUnbundled](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#wearAppUnbundled\(\))` Whether to enable unbundling mode for embedded wear app.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.VariantDimension](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[addManifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#addManifestPlaceholders\(kotlin.collections.Map\))(manifestPlaceholders: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>)` Adds manifest placeholders.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[buildConfigField](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#buildConfigField\(kotlin.String,kotlin.String,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds a new field to the generated BuildConfig class.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#externalNativeBuild\(kotlin.Function1\))(action: [ExternalNativeBuildFlags](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ExternalNativeBuildFlags).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates per-variant CMake and ndk-build configurations for your external native build.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[javaCompileOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#javaCompileOptions\(kotlin.Function1\))(action: [JavaCompileOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/JavaCompileOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Options for configuring Java compilation.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[ndk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#ndk\(kotlin.Function1\))(action: [Ndk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Ndk).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates per-variant configurations for the NDK, such as ABI filters.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[optimization](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#optimization\(kotlin.Function1\))~~(action: [Optimization](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Optimization).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Use ApplicationBuildType.optimization(action) instead  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[proguardFile](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#proguardFile\(kotlin.Any\))(proguardFile: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds a new ProGuard configuration file.  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[proguardFiles](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#proguardFiles\(kotlin.Array\))(vararg files: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds new ProGuard configuration files.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[resValue](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#resValue\(kotlin.String,kotlin.String,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds a new generated resource.  
`[Void](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Void.html)?` |  `~~[setManifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#setManifestPlaceholders\(kotlin.collections.Map\))~~(manifestPlaceholders: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>)` **This function is deprecated.** Use manifestPlaceholders property instead  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[setProguardFiles](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#setProguardFiles\(kotlin.collections.Iterable\))(proguardFileIterable: [Iterable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html)<*>)` Replaces the ProGuard configuration files.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#shaders\(kotlin.Function1\))(action: [Shaders](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Shaders).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configure the shader compiler options.  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[testProguardFile](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#testProguardFile\(kotlin.Any\))(proguardFile: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds a proguard rule file to be used when processing test code.  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[testProguardFiles](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#testProguardFiles\(kotlin.Array\))(vararg proguardFiles: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds proguard rule files to be used when processing test code.  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.VariantDimension](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension) | `[ExternalNativeBuildFlags](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/ExternalNativeBuildFlags)` |  `[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#externalNativeBuild\(\))` Encapsulates per-variant CMake and ndk-build configurations for your external native build.  
---|---  
`[JavaCompileOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/JavaCompileOptions)` |  `[javaCompileOptions](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#javaCompileOptions\(\))` Options for configuring Java compilation.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[manifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#manifestPlaceholders\(\))` The manifest placeholders.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[multiDexKeepFile](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#multiDexKeepFile\(\))` **This property is deprecated.** This property is deprecated.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[multiDexKeepProguard](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#multiDexKeepProguard\(\))` Text file with additional ProGuard rules to be used to determine which classes are compiled into the main dex file.  
`[Ndk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Ndk)` |  `[ndk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#ndk\(\))` Encapsulates per-variant configurations for the NDK, such as ABI filters.  
`[Optimization](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Optimization)` |  `[optimization](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#optimization\(\))` **This property is deprecated.** Use ApplicationBuildType.optimization instead  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>` |  `[proguardFiles](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#proguardFiles\(\))` Specifies the ProGuard configuration files that the plugin should use.  
`[Shaders](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/Shaders)` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#shaders\(\))` Options for configuring the shader compiler.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>` |  `[testProguardFiles](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VariantDimension#testProguardFiles\(\))` The collection of proguard rule files to be used when processing test code.  
  
## Public functions

### getName

Added in 4.2.0
    
    
    fun [getName](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#getName\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

The name of the flavor.

### initWith

Added in 7.1.0
    
    
    fun [initWith](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#initWith\(com.android.build.api.dsl.BaseFlavor\))(that: [BaseFlavor](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Copies all properties from the given flavor.

It can be used like this:
    
    
    android.productFlavors {  
        paid {  
            initWith free  
            // customize...  
        }  
    }

### minSdk

Added in 8.12.0
    
    
    fun [minSdk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdk\(kotlin.Function1\))(action: [MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/MinSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures all aspects regarding minSdk, see `[MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/MinSdkSpec)` for available options.

### minSdkVersion

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[minSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdkVersion\(kotlin.Int\))~~(minSdkVersion: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Will be removed in AGP 10.0, replaced with the minSdk block

### minSdkVersion

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[minSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdkVersion\(kotlin.String\))~~(minSdkVersion: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Will be removed in AGP 10.0, replaced with the minSdk block

### missingDimensionStrategy

Added in 7.0.0
    
    
    fun [missingDimensionStrategy](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#missingDimensionStrategy\(kotlin.String,kotlin.String\))(dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), requestedValue: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies a flavor that the plugin should try to use from a given dimension in a dependency.

Android plugin 3.0.0 and higher try to match each variant of your module with the same one from its dependencies. For example, consider if both your app and its dependencies include a "tier" /studio/build/build-variants.html#flavor-dimensions, with flavors "free" and "paid". When you build a "freeDebug" version of your app, the plugin tries to match it with "freeDebug" versions of the local library modules the app depends on.

However, there may be situations in which **a library dependency includes a flavor dimension that your app does not**. For example, consider if a library dependency includes flavors for a "minApi" dimension, but your app includes flavors for only the "tier" dimension. So, when you want to build the "freeDebug" version of your app, the plugin doesn't know whether to use the "minApi23Debug" or "minApi18Debug" version of the dependency, and you'll see an error message similar to the following:
    
    
    Error:Failed to resolve: Could not resolve project :mylibrary.  
    Required by:  
    project :app

In this type of situation, use `missingDimensionStrategy` in the com.android.build.gradle.internal.dsl.DefaultConfig.html block to specify the default flavor the plugin should select from each missing dimension, as shown in the sample below. You can also override your selection in the com.android.build.gradle.internal.dsl.ProductFlavor.html block, so each flavor can specify a different matching strategy for a missing dimension. (Tip: you can also use this property if you simply want to change the matching strategy for a dimension that exists in both the app and its dependencies.)
    
    
    // In the app's build.gradle file.  
    android {  
        defaultConfig {  
            // Specifies a flavor that the plugin should try to use from  
            // a given dimension. The following tells the plugin that, when encountering  
            // a dependency that includes a "minApi" dimension, it should select the  
            // "minApi18" flavor.  
            missingDimensionStrategy 'minApi', 'minApi18'  
            // You should specify a missingDimensionStrategy property for each  
            // dimension that exists in a local dependency but not in your app.  
            missingDimensionStrategy 'abi', 'x86'  
        }  
        flavorDimensions 'tier'  
        productFlavors {  
            free {  
                dimension 'tier'  
                // You can override the default selection at the product flavor  
                // level by configuring another missingDimensionStrategy property  
                // for the "minApi" dimension.  
                missingDimensionStrategy 'minApi', 'minApi23'  
            }  
            paid { }  
        }  
    }

### missingDimensionStrategy

Added in 7.0.0
    
    
    fun [missingDimensionStrategy](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#missingDimensionStrategy\(kotlin.String,kotlin.collections.List\))(  
        dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),  
        requestedValues: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies a sorted list of flavors that the plugin should try to use from a given dimension in a dependency.

Android plugin 3.0.0 and higher try to match each variant of your module with the same one from its dependencies. For example, consider if both your app and its dependencies include a "tier" /studio/build/build-variants.html#flavor-dimensions, with flavors "free" and "paid". When you build a "freeDebug" version of your app, the plugin tries to match it with "freeDebug" versions of the local library modules the app depends on.

However, there may be situations in which **a library dependency includes a flavor dimension that your app does not**. For example, consider if a library dependency includes flavors for a "minApi" dimension, but your app includes flavors for only the "tier" dimension. So, when you want to build the "freeDebug" version of your app, the plugin doesn't know whether to use the "minApi23Debug" or "minApi18Debug" version of the dependency, and you'll see an error message similar to the following:
    
    
    Error:Failed to resolve: Could not resolve project :mylibrary.  
    Required by:  
    project :app

In this type of situation, use `missingDimensionStrategy` in the com.android.build.gradle.internal.dsl.DefaultConfig.html block to specify the default flavor the plugin should select from each missing dimension, as shown in the sample below. You can also override your selection in the com.android.build.gradle.internal.dsl.ProductFlavor.html block, so each flavor can specify a different matching strategy for a missing dimension. (Tip: you can also use this property if you simply want to change the matching strategy for a dimension that exists in both the app and its dependencies.)
    
    
    // In the app's build.gradle file.  
    android {  
        defaultConfig {  
            // Specifies a flavor that the plugin should try to use from  
            // a given dimension. The following tells the plugin that, when encountering  
            // a dependency that includes a "minApi" dimension, it should select the  
            // "minApi18" flavor.  
            missingDimensionStrategy 'minApi', 'minApi18'  
            // You should specify a missingDimensionStrategy property for each  
            // dimension that exists in a local dependency but not in your app.  
            missingDimensionStrategy 'abi', 'x86'  
        }  
        flavorDimensions 'tier'  
        productFlavors {  
            free {  
                dimension 'tier'  
                // You can override the default selection at the product flavor  
                // level by configuring another missingDimensionStrategy property  
                // for the "minApi" dimension.  
                missingDimensionStrategy 'minApi', 'minApi23'  
            }  
            paid { }  
        }  
    }

### missingDimensionStrategy

Added in 7.0.0
    
    
    fun [missingDimensionStrategy](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#missingDimensionStrategy\(kotlin.String,kotlin.Array\))(  
        dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),  
        vararg requestedValues: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies a sorted list of flavors that the plugin should try to use from a given dimension in a dependency.

Android plugin 3.0.0 and higher try to match each variant of your module with the same one from its dependencies. For example, consider if both your app and its dependencies include a "tier" /studio/build/build-variants.html#flavor-dimensions, with flavors "free" and "paid". When you build a "freeDebug" version of your app, the plugin tries to match it with "freeDebug" versions of the local library modules the app depends on.

However, there may be situations in which **a library dependency includes a flavor dimension that your app does not**. For example, consider if a library dependency includes flavors for a "minApi" dimension, but your app includes flavors for only the "tier" dimension. So, when you want to build the "freeDebug" version of your app, the plugin doesn't know whether to use the "minApi23Debug" or "minApi18Debug" version of the dependency, and you'll see an error message similar to the following:
    
    
    Error:Failed to resolve: Could not resolve project :mylibrary.  
    Required by:  
    project :app

In this type of situation, use `missingDimensionStrategy` in the com.android.build.gradle.internal.dsl.DefaultConfig.html block to specify the default flavor the plugin should select from each missing dimension, as shown in the sample below. You can also override your selection in the com.android.build.gradle.internal.dsl.ProductFlavor.html block, so each flavor can specify a different matching strategy for a missing dimension. (Tip: you can also use this property if you simply want to change the matching strategy for a dimension that exists in both the app and its dependencies.)
    
    
    // In the app's build.gradle file.  
    android {  
        defaultConfig {  
            // Specifies a flavor that the plugin should try to use from  
            // a given dimension. The following tells the plugin that, when encountering  
            // a dependency that includes a "minApi" dimension, it should select the  
            // "minApi18" flavor.  
            missingDimensionStrategy 'minApi', 'minApi18'  
            // You should specify a missingDimensionStrategy property for each  
            // dimension that exists in a local dependency but not in your app.  
            missingDimensionStrategy 'abi', 'x86'  
        }  
        flavorDimensions 'tier'  
        productFlavors {  
            free {  
                dimension 'tier'  
                // You can override the default selection at the product flavor  
                // level by configuring another missingDimensionStrategy property  
                // for the "minApi" dimension.  
                missingDimensionStrategy 'minApi', 'minApi23'  
            }  
            paid { }  
        }  
    }

### resConfig

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[resConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#resConfig\(kotlin.String\))~~(config: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Support for resource configurations will be removed. For language resource configurations in applications, use androidResources.localeFilters.

### resConfigs

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[resConfigs](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#resConfigs\(kotlin.collections.Collection\))~~(config: [Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Support for resource configurations will be removed. For language resource configurations in applications, use androidResources.localeFilters.

### resConfigs

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[resConfigs](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#resConfigs\(kotlin.Array\))~~(vararg config: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Support for resource configurations will be removed. For language resource configurations in applications, use androidResources.localeFilters.

### setMinSdkVersion

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[setMinSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#setMinSdkVersion\(kotlin.Int\))~~(minSdkVersion: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Will be removed in AGP 10.0, replaced with the minSdk block

### setMinSdkVersion

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[setMinSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#setMinSdkVersion\(kotlin.String\))~~(minSdkVersion: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Will be removed in AGP 10.0, replaced with the minSdk block

### setTestFunctionalTest

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[setTestFunctionalTest](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#setTestFunctionalTest\(kotlin.Boolean\))~~(testFunctionalTest: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?

**This function is deprecated.**  
Replaced by testFunctionalTest property

### setTestHandleProfiling

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[setTestHandleProfiling](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#setTestHandleProfiling\(kotlin.Boolean\))~~(testHandleProfiling: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?

**This function is deprecated.**  
Replaced by testFunctionalTest property

### setTestInstrumentationRunnerArguments

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[setTestInstrumentationRunnerArguments](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#setTestInstrumentationRunnerArguments\(kotlin.collections.MutableMap\))~~(  
        testInstrumentationRunnerArguments: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>  
    ): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?

**This function is deprecated.**  
Replaced by testInstrumentationRunnerArguments property

### testInstrumentationRunnerArgument

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[testInstrumentationRunnerArgument](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#testInstrumentationRunnerArgument\(kotlin.String,kotlin.String\))~~(key: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by testInstrumentationRunnerArguments property

### testInstrumentationRunnerArguments

Added in 7.0.0

Deprecated in 7.0.0
    
    
    fun ~~[testInstrumentationRunnerArguments](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#testInstrumentationRunnerArguments\(kotlin.collections.Map\))~~(args: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by testInstrumentationRunnerArguments property

### vectorDrawables

Added in 4.2.0
    
    
    fun [vectorDrawables](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#vectorDrawables\(kotlin.Function1\))(action: [VectorDrawables](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VectorDrawables).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures `[VectorDrawables](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VectorDrawables)`.

## Public properties

### minSdk

Added in 4.2.0
    
    
    var [minSdk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

The minimum SDK version. Setting this it will override previous calls of `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdk\(kotlin.Function1\))` and `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdkPreview\(\))` setters. Only one of `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdk\(kotlin.Function1\))` and `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdkPreview\(\))` should be set.

See [uses-sdk element documentation](http://developer.android.com/guide/topics/manifest/uses-sdk-element.html).

### minSdkPreview

Added in 4.2.0

Deprecated in 8.12.0
    
    
    var [minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdkPreview\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

**This property is deprecated.**  
Will be removed in AGP 10.0, replaced with the minSdk block

The minimum SDK version. Setting this it will override previous calls of `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdk\(kotlin.Function1\))` and `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdkPreview\(\))` setters. Only one of `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdk\(kotlin.Function1\))` and `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdkPreview\(\))` should be set.

See [uses-sdk element documentation](http://developer.android.com/guide/topics/manifest/uses-sdk-element.html).

### renderscriptNdkModeEnabled

Added in 4.2.0
    
    
    var [renderscriptNdkModeEnabled](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#renderscriptNdkModeEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Whether the renderscript code should be compiled to generate C/C++ bindings. True for C/C++ generation, false for Java, null if not specified.

### renderscriptSupportModeBlasEnabled

Added in 4.2.0
    
    
    var [renderscriptSupportModeBlasEnabled](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#renderscriptSupportModeBlasEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Whether the renderscript BLAS support lib should be used to make it compatible with older versions of Android.

True if BLAS support lib is enabled, false if not, and null if not specified.

### renderscriptSupportModeEnabled

Added in 4.2.0
    
    
    var [renderscriptSupportModeEnabled](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#renderscriptSupportModeEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Whether the renderscript code should be compiled in support mode to make it compatible with older versions of Android.

True if support mode is enabled, false if not, and null if not specified.

### renderscriptTargetApi

Added in 4.2.0
    
    
    var [renderscriptTargetApi](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#renderscriptTargetApi\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

The renderscript target api, or null if not specified. This is only the value set on this product flavor.

### resourceConfigurations

Added in 4.2.0

Deprecated in 8.8.0
    
    
    val [resourceConfigurations](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#resourceConfigurations\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

**This property is deprecated.**  
Support for resource configurations will be removed. For language resource configurations in applications, use androidResources.localeFilters.

Specifies a list of [alternative resources](https://d.android.com/guide/topics/resources/providing-resources.html#AlternativeResources) to keep.

For example, if you are using a library that includes language resources (such as AppCompat or Google Play Services), then your APK includes all translated language strings for the messages in those libraries whether the rest of your app is translated to the same languages or not. If you'd like to keep only the languages that your app officially supports, you can specify those languages using the `resourceConfigurations` property, as shown in the sample below. Any resources for languages not specified are removed.
    
    
    android {  
        defaultConfig {  
            ...  
            // Keeps language resources for only the locales specified below.  
            resourceConfigurations += ["en", "fr"]  
        }  
    }

You can also use this property to filter resources for screen densities. For example, specifying `hdpi` removes all other screen density resources (such as `mdpi`, `xhdpi`, etc) from the final APK.

**Note:** `auto` is no longer supported because it created a number of issues with multi-module projects. Instead, you should specify a list of locales that your app supports, as shown in the sample above. Android plugin 3.1.0 and higher ignore the `auto` argument, and Gradle packages all string resources your app and its dependencies provide.

To learn more, see [Remove unused alternative resources](https://d.android.com/studio/build/shrink-code.html#unused-alt-resources).

### testApplicationId

Added in 4.2.0
    
    
    var [testApplicationId](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#testApplicationId\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Test application ID.

See [Set the Application ID](https://developer.android.com/studio/build/application-id.html)

### testFunctionalTest

Added in 4.2.0
    
    
    var [testFunctionalTest](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#testFunctionalTest\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

See [instrumentation](http://developer.android.com/guide/topics/manifest/instrumentation-element.html).

### testHandleProfiling

Added in 4.2.0
    
    
    var [testHandleProfiling](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#testHandleProfiling\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

See [instrumentation](http://developer.android.com/guide/topics/manifest/instrumentation-element.html).

### testInstrumentationRunner

Added in 4.2.0
    
    
    var [testInstrumentationRunner](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#testInstrumentationRunner\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Test instrumentation runner class name.

This is a fully qualified class name of the runner, e.g. `androidx.test.runner.AndroidJUnitRunner`

See [instrumentation](http://developer.android.com/guide/topics/manifest/instrumentation-element.html).

### testInstrumentationRunnerArguments

Added in 4.2.0
    
    
    val [testInstrumentationRunnerArguments](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#testInstrumentationRunnerArguments\(\)): [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Test instrumentation runner custom arguments.

e.g. `[key: "value"]` will give `adb shell am instrument -w -e key value com.example`...

See [instrumentation](http://developer.android.com/guide/topics/manifest/instrumentation-element.html).

Test runner arguments can also be specified from the command line:
    
    
    ./gradlew connectedAndroidTest -Pandroid.testInstrumentationRunnerArguments.size=medium  
    ./gradlew connectedAndroidTest -Pandroid.testInstrumentationRunnerArguments.foo=bar

### vectorDrawables

Added in 4.2.0
    
    
    val [vectorDrawables](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#vectorDrawables\(\)): [VectorDrawables](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/VectorDrawables)

Options to configure the build-time support for `vector` drawables.

### wearAppUnbundled

Added in 4.2.0
    
    
    var [wearAppUnbundled](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#wearAppUnbundled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Whether to enable unbundling mode for embedded wear app.

If true, this enables the app to transition from an embedded wear app to one distributed by the play store directly.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-09-11 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-11 UTC."],[],[]] 
