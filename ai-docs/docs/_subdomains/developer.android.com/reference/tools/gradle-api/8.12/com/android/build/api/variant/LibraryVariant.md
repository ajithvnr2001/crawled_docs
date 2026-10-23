---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/LibraryVariant/
title: LibraryVariant \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:08:49.958863+00:00
---

# LibraryVariant  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/LibraryVariant/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# LibraryVariant

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/LibraryVariant.kt+class:com.android.build.api.variant.LibraryVariant)

Added in 4.2.0
    
    
    interface [LibraryVariant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/LibraryVariant) : [Variant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant), [GeneratesAar](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/GeneratesAar), [HasDeviceTests](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasDeviceTests), [HasAndroidTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasAndroidTest), [HasHostTests](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasHostTests), [HasUnitTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasUnitTest), [HasTestFixtures](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasTestFixtures), [CanMinifyCode](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/CanMinifyCode)

Known direct subclasses 

[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)

`[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)` |  Properties for the main Variant of a kotlin multiplatform android library  
---|---  
  
* * *

Model for library components that only contains build-time properties.

See `[Component](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component)` and `[Variant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant)` for more information.

## Summary

### Public properties  
  
---  
`[Renderscript](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Renderscript)?` |  `[renderscript](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/LibraryVariant#renderscript\(\))` Variant specific settings for the renderscript compiler.  
  
### Inherited functions  
  
---  
From [com.android.build.api.variant.Component](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[computeTaskName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component#computeTaskName\(kotlin.String,kotlin.String\))(action: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), subject: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Utility method to create unique task name for component.  
---|---  
`[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[getResolvableConfiguration](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component#getResolvableConfiguration\(kotlin.String\))(sourceSetConfigurationsAffix: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Access to the component's resolvable configuration corresponding to the source set configurations added via `[AndroidComponentsExtension.addSourceSetConfigurations](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AndroidComponentsExtension#addSourceSetConfigurations\(kotlin.String\))`.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[setAsmFramesComputationMode](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component#setAsmFramesComputationMode\(com.android.build.api.instrumentation.FramesComputationMode\))~~(mode: [FramesComputationMode](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/FramesComputationMode))` **This function is deprecated.** Will be removed in v9.0, use the instrumentation block.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<ParamT : [InstrumentationParameters](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/InstrumentationParameters)> ~~[transformClassesWith](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component#transformClassesWith\(java.lang.Class,com.android.build.api.instrumentation.InstrumentationScope,kotlin.Function1\))~~(  
classVisitorFactoryImplClass: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[AsmClassVisitorFactory](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/AsmClassVisitorFactory)<ParamT>>,  
scope: [InstrumentationScope](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/InstrumentationScope),  
instrumentationParamsConfig: (ParamT) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
)` **This function is deprecated.** Will be removed in v9.0, use the instrumentation block.  
  
From [com.android.build.api.variant.HasAndroidResources](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasAndroidResources) | `[ResValue.Key](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ResValue.Key)` |  `[makeResValueKey](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasAndroidResources#makeResValueKey\(kotlin.String,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Make a `[ResValue.Key](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ResValue.Key)` to interact with `[resValues](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasAndroidResources#resValues\(\))`'s `[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)`  
---|---  
  
From [com.android.build.api.variant.Variant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant) | `T?` |  `<T : [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?> [getExtension](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#getExtension\(java.lang.Class\))(type: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<T>)` Returns an extension object registered via the `[VariantBuilder.registerExtension](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantBuilder#registerExtension\(java.lang.Class,kotlin.Any\))` API or null if none were registered under the passed `[type](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#getExtension\(java.lang.Class\))`.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[missingDimensionStrategy](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#missingDimensionStrategy\(kotlin.String,kotlin.Array\))(  
dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),  
vararg requestedValues: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)  
)` Set up a new matching request for a given flavor dimension and value.  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.CanMinifyCode](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/CanMinifyCode) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isMinifyEnabled](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/CanMinifyCode#isMinifyEnabled\(\))` Specifies whether code will be minified.  
---|---  
  
From [com.android.build.api.variant.Component](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component) | `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` |  `[annotationProcessorConfiguration](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component#annotationProcessorConfiguration\(\))` Access to the variant's annotation processor `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)`; for example, the debugAnnotationProcessor `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` for the debug variant.  
---|---  
`[Artifacts](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/artifact/Artifacts)` |  `[artifacts](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component#artifacts\(\))` Access to the variant's buildable artifacts for build customization.  
`[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)` |  `[compileClasspath](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component#compileClasspath\(\))` Access to the variant's compile classpath.  
`[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` |  `[compileConfiguration](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component#compileConfiguration\(\))` Access to the variant's compile `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)`; for example, the debugCompileClasspath `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` for the debug variant.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[debuggable](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component#debuggable\(\))` Whether the produced artifacts will be debuggable  
`[Instrumentation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Instrumentation)` |  `[instrumentation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component#instrumentation\(\))` Access to the variant's instrumentation options.  
`[JavaCompilation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/JavaCompilation)` |  `[javaCompilation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component#javaCompilation\(\))` Access to the variant's java compilation options.  
`[LifecycleTasks](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/LifecycleTasks)` |  `[lifecycleTasks](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component#lifecycleTasks\(\))` Provides access to the `[LifecycleTasks](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/LifecycleTasks)` created for this component.  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[namespace](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component#namespace\(\))` The namespace of the generated R and BuildConfig classes.  
`[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` |  `[runtimeConfiguration](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component#runtimeConfiguration\(\))` Access to the variant's runtime `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)`; for example, the debugRuntimeClasspath `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` for the debug variant.  
`[Sources](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Sources)` |  `[sources](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component#sources\(\))` Access to variant's source files.  
  
From [com.android.build.api.variant.ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ComponentIdentity) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[buildType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ComponentIdentity#buildType\(\))` Build type name.  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[flavorName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ComponentIdentity#flavorName\(\))` The multi-flavor name of the variant.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ComponentIdentity#name\(\))` Component's name.  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>>` |  `[productFlavors](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ComponentIdentity#productFlavors\(\))` List of flavor names.  
  
From [com.android.build.api.variant.GeneratesAar](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/GeneratesAar) | `[AarMetadata](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AarMetadata)` |  `[aarMetadata](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/GeneratesAar#aarMetadata\(\))` Variant's aar metadata, initialized by merging the corresponding `[com.android.build.api.dsl.AarMetadata](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/AarMetadata)` DSL elements.  
---|---  
  
From [com.android.build.api.variant.HasAndroidResources](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasAndroidResources) | `[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[pseudoLocalesEnabled](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasAndroidResources#pseudoLocalesEnabled\(\))` Variant's is pseudo locales enabled, initialized by the corresponding DSL elements.  
---|---  
`[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[ResValue.Key](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ResValue.Key), [ResValue](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ResValue)>` |  `[resValues](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasAndroidResources#resValues\(\))` Variant's `[ResValue](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ResValue)` which will be generated.  
  
From [com.android.build.api.variant.HasAndroidTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasAndroidTest) | `[AndroidTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AndroidTest)?` |  `[androidTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasAndroidTest#androidTest\(\))` Variant's `[AndroidTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AndroidTest)` configuration, or null if android tests are disabled for this variant.  
---|---  
  
From [com.android.build.api.variant.HasDeviceTests](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasDeviceTests) | `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [DeviceTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTest)>` |  `[deviceTests](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasDeviceTests#deviceTests\(\))` Variant's `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)` of `[DeviceTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/DeviceTest)` configurations, or empty if all devices tests (like android tests) are disabled for this variant.  
---|---  
  
From [com.android.build.api.variant.HasHostTests](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasHostTests) | `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [HostTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HostTest)>` |  `[hostTests](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasHostTests#hostTests\(\))` `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)` of Variant's `[HostTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HostTest)`, or empty if all host tests (like unit test) for this variant are disabled.  
---|---  
  
From [com.android.build.api.variant.HasTestFixtures](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasTestFixtures) | `[TestFixtures](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/TestFixtures)?` |  `[testFixtures](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/HasTestFixtures#testFixtures\(\))` Variant's `[TestFixtures](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/TestFixtures)`, or null if the test fixtures for this variant are disabled.  
---|---  
  
From [com.android.build.api.variant.Variant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant) | `[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [BuildConfigField](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/BuildConfigField)<[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)>>?` |  `[buildConfigFields](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#buildConfigFields\(\))` Variant's `[BuildConfigField](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/BuildConfigField)` which will be generated in the BuildConfig class.  
---|---  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Component](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component)>` |  `[components](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#components\(\))` List containing this variant and all of its `[nestedComponents](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#nestedComponents\(\))`  
`[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[experimentalProperties](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#experimentalProperties\(\))` Additional per variant experimental properties.  
`[ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ExternalNativeBuild)?` |  `[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#externalNativeBuild\(\))` Variant's cmake `[ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ExternalNativeBuild)`, initialized by merging the product flavor values or null if no cmake external build is configured for this variant.  
`[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[manifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#manifestPlaceholders\(\))` `[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)` of the variant's manifest placeholders.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[maxSdk](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#maxSdk\(\))` Gets the maximum supported SDK Version for this variant.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[maxSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#maxSdkVersion\(\))`  
`[AndroidVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AndroidVersion)` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#minSdk\(\))` Gets the minimum supported SDK Version for this variant.  
`[AndroidVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AndroidVersion)` |  `[minSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#minSdkVersion\(\))`  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Component](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component)>` |  `[nestedComponents](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#nestedComponents\(\))` List of the components nested in this variant, the returned list will contain:  
`[Packaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Packaging)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#packaging\(\))` Variant's packagingOptions, initialized by the corresponding global DSL element.  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>` |  `[proguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#proguardFiles\(\))` List of proguard configuration files for this variant.  
`[AndroidVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AndroidVersion)` |  `[targetSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#targetSdkVersion\(\))` Gets the target SDK Version for this variant.  
`[UnitTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/component/UnitTest)?` |  `[unitTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Variant#unitTest\(\))` Variant's `[UnitTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/component/UnitTest)`, or null if the unit tests for this variant are disabled.  
  
## Public properties

### renderscript

Added in 7.0.0
    
    
    val [renderscript](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/LibraryVariant#renderscript\(\)): [Renderscript](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Renderscript)?

Variant specific settings for the renderscript compiler. This will return null when `[com.android.build.api.dsl.BuildFeatures.renderScript](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/BuildFeatures#renderScript\(\))` is false.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
