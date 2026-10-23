---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant/
title: Variant \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:56:11.311606+00:00
---

# Variant  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Variant

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/Variant.kt+class:com.android.build.api.variant.Variant)

Added in 4.2.0
    
    
    interface [Variant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant) : [Component](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component), [HasAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasAndroidResources)

Known direct subclasses 

[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApplicationVariant), [DynamicFeatureVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DynamicFeatureVariant), [LibraryVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/LibraryVariant), [TestVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestVariant)

`[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApplicationVariant)` |  Model for application components that only contains build-time properties.  
---|---  
`[DynamicFeatureVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DynamicFeatureVariant)` |  Model for dynamic feature components that only contains build-time properties.  
`[LibraryVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/LibraryVariant)` |  Model for library components that only contains build-time properties.  
`[TestVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestVariant)` |  Model for test components that only contains build-time properties.  
  
Known indirect subclasses 

[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)

`[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)` |  Properties for the main Variant of a kotlin multiplatform android library  
---|---  
  
* * *

Model for variant components that only contains build-time properties

Variant components are the main output of the plugin (e.g. APKs, AARs). They contain references to optional secondary components (tests, fixtures)

It is the object passed to the `[AndroidComponentsExtension.onVariants](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` method, like this:
    
    
    androidComponents {  
      onVariants(selector().all()) { variant: Variant ->  
      }  
    }

Note that depending on the actual implementation of `[AndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension)`, the object received may be of a child type. For instance `[ApplicationAndroidComponentsExtension.onVariants](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApplicationAndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` will pass `[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApplicationVariant)` to the lambda.

See [here](https://developer.android.com/build/extend-agp#variant-api-artifacts-tasks) for more information

## Summary

### Public functions  
  
---  
`T?` |  `<T : [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?> [getExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#getExtension\(java.lang.Class\))(type: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<T>)` Returns an extension object registered via the `[VariantBuilder.registerExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#registerExtension\(java.lang.Class,kotlin.Any\))` API or null if none were registered under the passed `[type](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#getExtension\(java.lang.Class\))`.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[missingDimensionStrategy](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#missingDimensionStrategy\(kotlin.String,kotlin.Array\))(  
dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),  
vararg requestedValues: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)  
)` Set up a new matching request for a given flavor dimension and value.  
  
### Public properties  
  
---  
`[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [BuildConfigField](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/BuildConfigField)<[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)>>?` |  `[buildConfigFields](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#buildConfigFields\(\))` Variant's `[BuildConfigField](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/BuildConfigField)` which will be generated in the BuildConfig class.  
`[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion)` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#compileSdk\(\))` Gets the compile SDK Version for this variant.  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Component](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component)>` |  `[components](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#components\(\))` List containing this variant and all of its `[nestedComponents](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#nestedComponents\(\))`  
`[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[experimentalProperties](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#experimentalProperties\(\))` Additional per variant experimental properties.  
`[ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNativeBuild)?` |  `[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#externalNativeBuild\(\))` Variant's cmake `[ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNativeBuild)`, initialized by merging the product flavor values or null if no cmake external build is configured for this variant.  
`[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[manifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#manifestPlaceholders\(\))` `[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)` of the variant's manifest placeholders.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[maxSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#maxSdk\(\))` Gets the maximum supported SDK Version for this variant.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[maxSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#maxSdkVersion\(\))`  
`[AndroidVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidVersion)` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#minSdk\(\))` Gets the minimum supported SDK Version for this variant.  
`[AndroidVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidVersion)` |  `[minSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#minSdkVersion\(\))`  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Component](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component)>` |  `[nestedComponents](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#nestedComponents\(\))` List of the components nested in this variant, the returned list will contain:  
`[Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Packaging)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#packaging\(\))` Variant's packagingOptions, initialized by the corresponding global DSL element.  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>` |  `[proguardFiles](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#proguardFiles\(\))` List of proguard configuration files for this variant.  
`[AndroidVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidVersion)` |  `[targetSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#targetSdkVersion\(\))` Gets the target SDK Version for this variant.  
`[UnitTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/component/UnitTest)?` |  `[unitTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#unitTest\(\))` Variant's `[UnitTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/component/UnitTest)`, or null if the unit tests for this variant are disabled.  
  
### Inherited functions  
  
---  
From [com.android.build.api.variant.Component](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[computeTaskName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#computeTaskName\(kotlin.String,kotlin.String\))(action: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), subject: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Utility method to create unique task name for component.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[configureJavaCompileTask](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#configureJavaCompileTask\(kotlin.Function1\))(action: ([JavaCompile](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/compile/JavaCompile.html)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Runs an action to configure Components's java compilation `[JavaCompile](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/compile/JavaCompile.html)` task.  
`[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[getResolvableConfiguration](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#getResolvableConfiguration\(kotlin.String\))(sourceSetConfigurationsAffix: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Access to the component's resolvable configuration corresponding to the source set configurations added via `[AndroidComponentsExtension.addSourceSetConfigurations](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#addSourceSetConfigurations\(kotlin.String\))`.  
  
From [com.android.build.api.variant.HasAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasAndroidResources) | `[ResValue.Key](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ResValue.Key)` |  `[makeResValueKey](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasAndroidResources#makeResValueKey\(kotlin.String,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Make a `[ResValue.Key](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ResValue.Key)` to interact with `[resValues](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasAndroidResources#resValues\(\))`'s `[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)`  
---|---  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.Component](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component) | `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` |  `[annotationProcessorConfiguration](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#annotationProcessorConfiguration\(\))` Access to the variant's annotation processor `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)`; for example, the debugAnnotationProcessor `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` for the debug variant.  
---|---  
`[Artifacts](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts)` |  `[artifacts](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#artifacts\(\))` Access to the variant's buildable artifacts for build customization.  
`[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)` |  `[compileClasspath](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#compileClasspath\(\))` Access to the variant's compile classpath.  
`[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` |  `[compileConfiguration](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#compileConfiguration\(\))` Access to the variant's compile `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)`; for example, the debugCompileClasspath `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` for the debug variant.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[debuggable](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#debuggable\(\))` Whether the produced artifacts will be debuggable  
`[Instrumentation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Instrumentation)` |  `[instrumentation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#instrumentation\(\))` Access to the variant's instrumentation options.  
`[JavaCompilation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JavaCompilation)?` |  `[javaCompilation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#javaCompilation\(\))` Access to the variant's java compilation options.  
`[LifecycleTasks](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/LifecycleTasks)` |  `[lifecycleTasks](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#lifecycleTasks\(\))` Provides access to the `[LifecycleTasks](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/LifecycleTasks)` created for this component.  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[namespace](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#namespace\(\))` The namespace of the generated R and BuildConfig classes.  
`[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` |  `[runtimeConfiguration](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#runtimeConfiguration\(\))` Access to the variant's runtime `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)`; for example, the debugRuntimeClasspath `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` for the debug variant.  
`[Sources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Sources)` |  `[sources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#sources\(\))` Access to variant's source files.  
  
From [com.android.build.api.variant.ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[buildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity#buildType\(\))` Build type name.  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[flavorName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity#flavorName\(\))` The multi-flavor name of the variant.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity#name\(\))` Component's name.  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>>` |  `[productFlavors](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity#productFlavors\(\))` List of flavor names.  
  
From [com.android.build.api.variant.HasAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasAndroidResources) | `[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[pseudoLocalesEnabled](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasAndroidResources#pseudoLocalesEnabled\(\))` Variant's is pseudo locales enabled, initialized by the corresponding DSL elements.  
---|---  
`[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[ResValue.Key](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ResValue.Key), [ResValue](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ResValue)>` |  `[resValues](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasAndroidResources#resValues\(\))` Variant's `[ResValue](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ResValue)` which will be generated.  
  
## Public functions

### getExtension

Added in 7.0.0
    
    
    fun <T : [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?> [getExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#getExtension\(java.lang.Class\))(type: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<T>): T?

Returns an extension object registered via the `[VariantBuilder.registerExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#registerExtension\(java.lang.Class,kotlin.Any\))` API or null if none were registered under the passed `[type](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#getExtension\(java.lang.Class\))`.

Returns  
---  
`T?` |  the registered object or null.  
  
### missingDimensionStrategy

Added in 8.2.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [missingDimensionStrategy](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#missingDimensionStrategy\(kotlin.String,kotlin.Array\))(  
        dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),  
        vararg requestedValues: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Set up a new matching request for a given flavor dimension and value.

Parameters  
---  
`dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the flavor dimension  
`vararg requestedValues: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the flavor name(s)  
  
See also  
---  
`[missingDimensionStrategy](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BaseFlavor#missingDimensionStrategy\(kotlin.String,kotlin.String\))` |  To learn more, read d.android.com//build/build-variants.  
  
## Public properties

### buildConfigFields

Added in 4.2.0
    
    
    val [buildConfigFields](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#buildConfigFields\(\)): [MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [BuildConfigField](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/BuildConfigField)<[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)>>?

Variant's `[BuildConfigField](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/BuildConfigField)` which will be generated in the BuildConfig class.

### compileSdk

Added in 9.2.1
    
    
    val [compileSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#compileSdk\(\)): [CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileSdkVersion)

Gets the compile SDK Version for this variant.

### components

Added in 7.3.0
    
    
    val [components](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#components\(\)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Component](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component)>

List containing this variant and all of its `[nestedComponents](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#nestedComponents\(\))`

Example:
    
    
    androidComponents.onVariants(selector().withName("debug")) {  
        // components contains the debug variant along with its unitTests, androidTests, and  
        // testFixtures (if enabled).  
        components.forEach { component ->  
            component.runtimeConfiguration  
                .resolutionStrategy  
                .dependencySubstitution {  
                    substitute(project(":foo")).using(project(":bar"))  
                }  
        }  
    }

### experimentalProperties

Added in 7.0.0
    
    
    val [experimentalProperties](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#experimentalProperties\(\)): [MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>

Additional per variant experimental properties.

Initialized from `[com.android.build.api.dsl.CommonExtension.experimentalProperties](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CommonExtension#experimentalProperties\(\))`

Values provided should not be based on a Task execution result, as most of these properties are read during configuration.

### externalNativeBuild

Added in 7.0.0
    
    
    val [externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#externalNativeBuild\(\)): [ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNativeBuild)?

Variant's cmake `[ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNativeBuild)`, initialized by merging the product flavor values or null if no cmake external build is configured for this variant.

### manifestPlaceholders

Added in 4.2.0
    
    
    val [manifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#manifestPlaceholders\(\)): [MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

`[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)` of the variant's manifest placeholders.

Placeholders are organized with a key and a value. The value is a `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` that will be used as is in the merged manifest.

Returns  
---  
`[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  the `[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)` with keys as `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`  
  
### maxSdk

Added in 8.1.0
    
    
    val [maxSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#maxSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Gets the maximum supported SDK Version for this variant.

### maxSdkVersion
    
    
    val [maxSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#maxSdkVersion\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

### minSdk

Added in 8.1.0
    
    
    val [minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#minSdk\(\)): [AndroidVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidVersion)

Gets the minimum supported SDK Version for this variant.

### minSdkVersion
    
    
    val [minSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#minSdkVersion\(\)): [AndroidVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidVersion)

### nestedComponents

Added in 7.1.0
    
    
    val [nestedComponents](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#nestedComponents\(\)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Component](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component)>

List of the components nested in this variant, the returned list will contain:

  * `[UnitTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/component/UnitTest)` component if the unit tests for this variant are enabled,

  * `[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidTest)` component if this variant `[HasDeviceTests](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasDeviceTests)` and android tests for this variant are enabled,

  * `[TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestFixtures)` component if this variant `[HasTestFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasTestFixtures)` and test fixtures for this variant are enabled.




Use this list to do operations on all nested components of this variant without having to manually check whether the variant has each component.

Example:
    
    
    androidComponents.onVariants(selector().withName("debug")) {  
        // will return unitTests, androidTests, testFixtures for the debug variant (if enabled).  
        nestedComponents.forEach { component ->  
            component.instrumentation.transformClassesWith(NestedComponentsClassVisitorFactory::class.java,  
                                           InstrumentationScope.Project) {}  
        }  
    }

### packaging

Added in 7.0.0
    
    
    val [packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#packaging\(\)): [Packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Packaging)

Variant's packagingOptions, initialized by the corresponding global DSL element.

### proguardFiles

Added in 7.0.0
    
    
    val [proguardFiles](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#proguardFiles\(\)): [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>

List of proguard configuration files for this variant. The list is initialized from the corresponding DSL element, and cannot be queried at configuration time. At configuration time, you can only add new elements to the list.

This list will be initialized from com.android.build.api.dsl.VariantDimension#proguardFile for non test related variants and from `[com.android.build.api.dsl.VariantDimension.testProguardFiles](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/VariantDimension#testProguardFiles\(kotlin.Array\))` for test related variants.

### targetSdkVersion

Added in 7.0.0

Deprecated in 7.4.0
    
    
    val [targetSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#targetSdkVersion\(\)): [AndroidVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidVersion)

Gets the target SDK Version for this variant.

### unitTest
    
    
    val [unitTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#unitTest\(\)): [UnitTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/component/UnitTest)?

Variant's `[UnitTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/component/UnitTest)`, or null if the unit tests for this variant are disabled.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
