---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension/
title: AndroidComponentsExtension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:07:11.145420+00:00
---

# AndroidComponentsExtension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AndroidComponentsExtension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/AndroidComponentsExtension.kt+class:com.android.build.api.variant.AndroidComponentsExtension)

Added in 7.0.0
    
    
    interface [AndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension)<DslExtensionT : [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html), VariantBuilderT : [VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantBuilder), VariantT : [Variant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/Variant)> : [DslLifecycle](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DslLifecycle), [AndroidComponents](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponents)

Known direct subclasses 

[ApplicationAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/ApplicationAndroidComponentsExtension), [DynamicFeatureAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DynamicFeatureAndroidComponentsExtension), [KotlinMultiplatformAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/KotlinMultiplatformAndroidComponentsExtension), [LibraryAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/LibraryAndroidComponentsExtension), [TestAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/TestAndroidComponentsExtension)

`[ApplicationAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/ApplicationAndroidComponentsExtension)` |  Extension for the Android Application Gradle Plugin components.  
---|---  
`[DynamicFeatureAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DynamicFeatureAndroidComponentsExtension)` |  Extension for the Android Dynamic Feature Gradle Plugin components.  
`[KotlinMultiplatformAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/KotlinMultiplatformAndroidComponentsExtension)` |  Components extension for KMP Android Gradle Plugin related components.  
`[LibraryAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/LibraryAndroidComponentsExtension)` |  Extension for the Android Library Gradle Plugin components.  
`[TestAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/TestAndroidComponentsExtension)` |  Extension for the Android Test Gradle Plugin components.  
  
* * *

Generic extension for Android Gradle Plugin related components.

Each component has a type, like application or library and will have a dedicated extension with methods that are related to the particular component type.

This can be used via
    
    
    androidComponents {  
    }

In a plugin this can be queried via
    
    
    project.plugins.withType(AppPlugin::class.java) {  
      val androidComponents = project.extensions.getByType(ApplicationAndroidComponentsExtension::class.java)  
    }

@param DslExtensionT the type of the DSL to be used in `[DslLifecycle.finalizeDsl](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DslLifecycle#finalizeDsl\(kotlin.Function1\))` @param VariantBuilderT the `[ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/ComponentBuilder)` type produced by this variant. @param VariantT the `[Variant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/Variant)` type produced by this variant.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[addSourceSetConfigurations](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#addSourceSetConfigurations\(kotlin.String\))(suffix: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds a custom configuration for each source set.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,org.gradle.api.Action\))(  
selector: [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector),  
callback: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<VariantBuilderT>  
)` `[Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)` based version of `[beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` above.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))(  
selector: [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector),  
callback: (VariantBuilderT) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
)` Method to register a `[callback](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` to be called with `[VariantBuilderT](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension)` instances that satisfies the `[selector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))`.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[onVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,org.gradle.api.Action\))(selector: [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector), callback: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<VariantT>)` `[Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)` based version of `[onVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` above.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[onVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))(selector: [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector), callback: (VariantT) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Allow for registration of a `[callback](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` to be called with variant instances of type `[VariantT](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension)` once the list of `[com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact)` has been determined.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[registerExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#registerExtension\(com.android.build.api.variant.DslExtension,kotlin.Function1\))(  
dslExtension: [DslExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DslExtension),  
configurator: (variantExtensionConfig: [VariantExtensionConfig](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantExtensionConfig)<VariantT>) -> [VariantExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantExtension)  
)` Register an Android Gradle Plugin DSL extension.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[registerSourceType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#registerSourceType\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Register a new source type to all source sets.  
`[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector)` |  `[selector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#selector\(\))()` Creates a `[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector)` instance that can be configured to reduce the set of `[ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/ComponentBuilder)` instances participating in the `[beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` and `[onVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` callback invocation.  
  
### Inherited functions  
  
---  
From [com.android.build.api.variant.DslLifecycle](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DslLifecycle) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[finalizeDsl](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DslLifecycle#finalizeDsl\(org.gradle.api.Action\))(callback: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<DslExtensionT>)` `[Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)` based version of `[finalizeDsl](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DslLifecycle#finalizeDsl\(kotlin.Function1\))` above.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[finalizeDsl](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DslLifecycle#finalizeDsl\(kotlin.Function1\))(callback: (DslExtensionT) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` API to customize the DSL Objects programmatically after they have been evaluated from the build files and before used in the build process next steps like variant or tasks creation.  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.AndroidComponents](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponents) | `[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/AndroidPluginVersion)` |  `[pluginVersion](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponents#pluginVersion\(\))` The version of the Android Gradle Plugin currently in use.  
---|---  
`[SdkComponents](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/SdkComponents)` |  `[sdkComponents](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponents#sdkComponents\(\))` Provides access to underlying Android SDK and build-tools components like adb.  
  
## Public functions

### addSourceSetConfigurations

Added in 8.9.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [addSourceSetConfigurations](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#addSourceSetConfigurations\(kotlin.String\))(suffix: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds a custom configuration for each source set.

The `[suffix](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#addSourceSetConfigurations\(kotlin.String\))` parameter determines the naming convention for the generated configurations. For example, if `[suffix](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#addSourceSetConfigurations\(kotlin.String\))` is "custom", the generated configurations would be "custom", "debugCustom", "releaseCustom", "testCustom", etc.

Under the hood, this API:

  1. Creates a configuration for each source set.

  2. Creates resolvable configurations for each component.

  3. Ensures that each resolvable configuration extends the corresponding source set configurations.




Each component's corresponding resolvable configuration can be accessed via `[Component.getResolvableConfiguration](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/Component#getResolvableConfiguration\(kotlin.String\))`.

Example usage:
    
    
    androidComponents {  
        addSourceSetConfigurations("foo")  
        onVariants { variant ->  
            val resolvableConfiguration = variant.getResolvableConfiguration("foo")  
            variant.nestedComponents.forEach { component ->  
                val nestedResolvableConfiguration =  
                    component.getResolvableConfiguration("foo")  
            }  
        }  
    }

Parameters  
---  
`suffix: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the suffix to append to the generated configuration names.  
  
### beforeVariants

Added in 7.0.0
    
    
    fun [beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,org.gradle.api.Action\))(  
        selector: [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector) = selector().all(),  
        callback: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<VariantBuilderT>  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

`[Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)` based version of `[beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` above.

### beforeVariants

Added in 7.0.0
    
    
    fun [beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))(  
        selector: [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector) = selector().all(),  
        callback: (VariantBuilderT) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Method to register a `[callback](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` to be called with `[VariantBuilderT](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension)` instances that satisfies the `[selector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))`. The `[callback](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` will be called as soon as the `[VariantBuilderT](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension)` instance has been created but before any `[com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact)` has been determined, therefore the build flow can still be changed when the `[callback](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` is invoked.

At this stage, access to the DSL objects is disallowed, use `[finalizeDsl](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#finalizeDsl\(kotlin.Function1\))` method to programmatically access the DSL objects before the `[VariantBuilderT](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension)` object is built.

The goal of this callback is to make changes before the variants and components are created. This includes enabling/disabling components and making decisions on properties that can impact task creation and build flow. This guarantees that the matching `[onVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` callback does not have to deal with changing configuration and can focus on updating task inputs. See `[ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/ComponentBuilder)` for more information.

Example without selection:
    
    
    androidComponents {  
        beforeVariants {  
        }  
    }

Example with selection:
    
    
    androidComponents {  
        val debug = selector().withBuildType("debug")  
        beforeVariants(debug) {  
        }  
    }

See [here](https://developer.android.com/build/extend-agp#variant-api-artifacts-tasks) for more information

Parameters  
---  
`selector: [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector) = selector().all()` |  `[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector)` to select which instance of `[VariantBuilderT](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension)` are of interest. By default, all instances are of interest.  
`callback: (VariantBuilderT) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  lambda to be called with each instance of `[VariantBuilderT](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension)` of interest.  
  
### onVariants

Added in 7.0.0
    
    
    fun [onVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,org.gradle.api.Action\))(  
        selector: [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector) = selector().all(),  
        callback: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<VariantT>  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

`[Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)` based version of `[onVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` above.

### onVariants

Added in 7.0.0
    
    
    fun [onVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))(  
        selector: [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector) = selector().all(),  
        callback: (VariantT) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Allow for registration of a `[callback](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` to be called with variant instances of type `[VariantT](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension)` once the list of `[com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact)` has been determined.

At this stage, access to the DSL objects is disallowed and access to the `[VariantBuilderT](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension)` instance is limited to read-only access.

At this stage, the build flow is final, with the callback for `[beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` having modified properties that can impact which tasks are created and how they are configured. The ability to query or modify the build intermediate files between tasks, including adding additional new steps between existing tasks must be done via the `[Component.artifacts](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/Component#artifacts\(\))` API. See `[com.android.build.api.artifact.Artifacts](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifacts)` for details.

The `[VariantT](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension)` object exposes many `[org.gradle.api.provider.Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)` that are then used as task inputs. It is safe to set new values on the properties, including using `[org.gradle.api.provider.Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)` with or without task dependencies. When reading values, these `[org.gradle.api.provider.Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)` must be lazily linked to properties used as task inputs. It is not safe to call `[org.gradle.api.provider.Property.get](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html#get--)` during build configuration.

Example without selection:
    
    
    androidComponents {  
        onVariants {  
        }  
    }

Example with selection:
    
    
    androidComponents {  
        val debug = selector().withBuildType("debug")  
        onVariants(debug) {  
        }  
    }

See [here](https://developer.android.com/build/extend-agp#variant-api-artifacts-tasks) for more information

Parameters  
---  
`selector: [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector) = selector().all()` |  `[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector)` to select which instance of `[VariantBuilderT](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension)` are of interest. By default, all instances are of interest.  
`callback: (VariantT) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  lambda to be called with each instance of `[VariantT](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension)` of interest.  
  
### registerExtension
    
    
    fun [registerExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#registerExtension\(com.android.build.api.variant.DslExtension,kotlin.Function1\))(  
        dslExtension: [DslExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DslExtension),  
        configurator: (variantExtensionConfig: [VariantExtensionConfig](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantExtensionConfig)<VariantT>) -> [VariantExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantExtension)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Register an Android Gradle Plugin DSL extension.

Please see Gradle documentation first at : https://docs.gradle.org/current/userguide/custom_plugins.html#sec:getting_input_from_the_build

A lambda must be provided to create and configure the variant scoped object that will be stored alongside the Android Gradle Plugin's `[com.android.build.api.variant.Variant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/Variant)` instance.

Variant Scoped objects should use `[org.gradle.api.provider.Property](https://developer.android.com/reference/tools/gradle-api/9.1/\[JVM%20root\]/package-summary)` for its mutable state to allow for late binding. (see `[com.android.build.api.variant.Variant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/Variant)` for examples).

The `[DslExtension.Builder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DslExtension.Builder)` allow you to choose if you want to extend Project, BuiltType or ProductFlavor. You can extend just one or up to all of them.

A BuildType extension of type BuildTypeDslExtension will allow users to have the following declarations in their build files:
    
    
    android {  
        buildTypes {  
            debug {  
                extensions.configure<BuildTypeDslExtension> {  
                    buildTypeSettingOne = "build_type_debug"  
                }  
            }  
        }  
    }

A Product flavor extension of type ProductFlavorDslExtension will allow users to specify the following declarations in their build files:
    
    
    android {  
        flavorDimensions += "version"  
        productFlavors {  
            create("demo")  {  
                dimension = "version"  
                extensions.configure<ProductFlavorDslExtension> {  
                    productFlavorSettingOne = "product_flavor_demo"  
                    productFlavorSettingTwo = 99  
                }  
            }  
        }  
    }

Parameters  
---  
`dslExtension: [DslExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DslExtension)` |  the DSL extension configuration.  
`configurator: (variantExtensionConfig: [VariantExtensionConfig](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantExtensionConfig)<VariantT>) -> [VariantExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantExtension)` |  a lambda to create a variant scoped object. The lambda is provided with the `[VariantExtensionConfig](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantExtensionConfig)` that can be used to retrieve the `[VariantT](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension)` instance as well as DSL extensions registered with `[DslExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DslExtension)`  
  
Returns  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  an instance of a sub type of `[VariantExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantExtension)` that will be stored with the `[VariantT](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension)` instance and can be retrieved by `[Variant.getExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/Variant#getExtension\(java.lang.Class\))` API.  
  
### registerSourceType

Added in 7.2.0
    
    
    fun [registerSourceType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#registerSourceType\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Register a new source type to all source sets.

The name of the source type will be used to create expected directories names in the various source sets. For instance, src/main/ or src/debug/.

There is no notion of priorities between the build-type, flavor specific directories, all the expected directories will be interpreted as a flat namespace.

Therefore, any `[org.gradle.api.Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` that needs access to the entire list of source folders can just use the Sources.extras's Flat.all method for that source type.

However, If you need to have overriding priorities between the expected directories and therefore require a merging activity, you can still use this API but you will need to create a merging task that will have all sources in input and produce a single output folder for the merged sources.

Parameters  
---  
`name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the name of the source type.  
  
### selector

Added in 7.0.0
    
    
    fun [selector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#selector\(\))(): [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector)

Creates a `[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector)` instance that can be configured to reduce the set of `[ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/ComponentBuilder)` instances participating in the `[beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` and `[onVariants](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` callback invocation.

Returns  
---  
`[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector)` |  `[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantSelector)` to select the variants of interest.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-05 UTC."],[],[]] 
