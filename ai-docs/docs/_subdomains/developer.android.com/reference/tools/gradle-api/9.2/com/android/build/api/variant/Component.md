---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component/
title: Component \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:52:32.848474+00:00
---

# Component  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Component

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/Component.kt+class:com.android.build.api.variant.Component)

Added in 7.0.0
    
    
    interface [Component](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component) : [ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity)

Known direct subclasses 

[TestComponent](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestComponent), [TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestFixtures), [Variant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant)

`[TestComponent](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestComponent)` |  Model for test components that contains build-time properties.  
---|---  
`[TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestFixtures)` |  Model for Test Fixtures components that contains build-time properties  
`[Variant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant)` |  Model for variant components that only contains build-time properties  
  
Known indirect subclasses 

[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidTest), [ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApplicationVariant), [DeviceTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DeviceTest), [DynamicFeatureVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DynamicFeatureVariant), [HostTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HostTest), [KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/KotlinMultiplatformAndroidVariant), [LibraryVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/LibraryVariant), [TestVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestVariant), [UnitTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/component/UnitTest), [UnitTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/UnitTest)

`[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidTest)` |  Model for Android Test components that contains build-time properties  
---|---  
`[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApplicationVariant)` |  Model for application components that only contains build-time properties.  
`[DeviceTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DeviceTest)` |  Model for Device Test components that contains build-time properties  
`[DynamicFeatureVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DynamicFeatureVariant)` |  Model for dynamic feature components that only contains build-time properties.  
`[HostTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HostTest)` |  Model for Host Test components that contains build-time properties.  
`[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)` |  Properties for the main Variant of a kotlin multiplatform android library  
`[LibraryVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/LibraryVariant)` |  Model for library components that only contains build-time properties.  
`[TestVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestVariant)` |  Model for test components that only contains build-time properties.  
`[UnitTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/component/UnitTest)` |  **This interface is deprecated.** Use the com.android.build.api.variant package  
`[UnitTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/UnitTest)` |  `[Component](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component)` for unit tests  
  
* * *

Model for components that only contains build-time properties

Components can be APKs, AARs, test APKs, unit tests, test fixtures, ...

This is the parent interface for all components. From there, there is a first fork, via `[Variant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant)` which are production build output (APKs, AARs), and `[TestComponent](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestComponent)` that are test components. `[TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestFixtures)` is another separate component. See these types for more information.

See `[Variant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant)` for more information on accessing instances of this type.

The properties exposed by this object do not impact the build flow. They are directly set on tasks via `[org.gradle.api.provider.Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)` linking.

For example:
    
    
    tasks.register(...) {  
      input.set(myComponent.someProperty)  
    * }

Because links between `[org.gradle.api.provider.Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)` objects are lazy, they are ordering-safe and any plugins can set new values or link them into their own tasks in any order.

However, calling `[org.gradle.api.provider.Property.get](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html#get--)` during configuration on these properties is not safe as the values could be linked to task output (that requires the task to run).

The object also exposes read-only version of the properties exposed by `[ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentBuilder)`. These will contain the final values set after all `[AndroidComponentsExtension.beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` callbacks have been executed. It is safe to read these values during configuration time.

See [here](https://developer.android.com/build/extend-agp#variant-api-artifacts-tasks) for more information

## Summary

### Public functions  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[computeTaskName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#computeTaskName\(kotlin.String,kotlin.String\))(action: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), subject: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Utility method to create unique task name for component.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[configureJavaCompileTask](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#configureJavaCompileTask\(kotlin.Function1\))(action: ([JavaCompile](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/compile/JavaCompile.html)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Runs an action to configure Components's java compilation `[JavaCompile](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/compile/JavaCompile.html)` task.  
`[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[getResolvableConfiguration](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#getResolvableConfiguration\(kotlin.String\))(sourceSetConfigurationsAffix: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Access to the component's resolvable configuration corresponding to the source set configurations added via `[AndroidComponentsExtension.addSourceSetConfigurations](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#addSourceSetConfigurations\(kotlin.String\))`.  
  
### Public properties  
  
---  
`[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` |  `[annotationProcessorConfiguration](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#annotationProcessorConfiguration\(\))` Access to the variant's annotation processor `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)`; for example, the debugAnnotationProcessor `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` for the debug variant.  
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
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[buildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity#buildType\(\))` Build type name.  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[flavorName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity#flavorName\(\))` The multi-flavor name of the variant.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity#name\(\))` Component's name.  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>>` |  `[productFlavors](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity#productFlavors\(\))` List of flavor names.  
  
## Public functions

### computeTaskName

Added in 8.4.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [computeTaskName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#computeTaskName\(kotlin.String,kotlin.String\))(action: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), subject: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Utility method to create unique task name for component. You still need to assign task name during task registration. For  variant `getTaskName("produce", "manifestReport")` will return produceDebugManifestReport

### configureJavaCompileTask

Added in 9.2.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [configureJavaCompileTask](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#configureJavaCompileTask\(kotlin.Function1\))(action: ([JavaCompile](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/compile/JavaCompile.html)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Runs an action to configure Components's java compilation `[JavaCompile](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/compile/JavaCompile.html)` task.

The action will only run if the task is configured.

Where possible, use the AGP DSL and API

Note: This API is here to allow access to the java compiler elements that aren't exposed explicitly in the AGP DSL or API, such as `[com.android.build.api.dsl.CompileOptions.targetCompatibility](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileOptions#targetCompatibility\(kotlin.Any\))` for example. Properties set using this API don't propagate anywhere else. For example if you set `compileTask.targetCompatibility`, it will not update `[com.android.build.api.dsl.CompileOptions.targetCompatibility](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/CompileOptions#targetCompatibility\(kotlin.Any\))`

Example :
    
    
    androidComponents {  
        onVariants { variant ->  
            variant.configureJavaCompileTask { compileTask ->  
                compileTask.options.compilerArgs.add("-Werror")  
            }  
        }  
    }

Parameters  
---  
`action: ([JavaCompile](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/compile/JavaCompile.html)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  to configure the `[JavaCompile](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/compile/JavaCompile.html)` task.  
  
### getResolvableConfiguration

Added in 8.9.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [getResolvableConfiguration](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#getResolvableConfiguration\(kotlin.String\))(sourceSetConfigurationsAffix: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)

Access to the component's resolvable configuration corresponding to the source set configurations added via `[AndroidComponentsExtension.addSourceSetConfigurations](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#addSourceSetConfigurations\(kotlin.String\))`.

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

The returned `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` should not be resolved until execution time.

## Public properties

### annotationProcessorConfiguration

Added in 7.3.0
    
    
    val [annotationProcessorConfiguration](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#annotationProcessorConfiguration\(\)): [Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)

Access to the variant's annotation processor `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)`; for example, the debugAnnotationProcessor `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` for the debug variant.

The returned `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` should not be resolved until execution time.

### artifacts

Added in 7.0.0
    
    
    val [artifacts](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#artifacts\(\)): [Artifacts](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts)

Access to the variant's buildable artifacts for build customization.

### compileClasspath

Added in 7.3.0
    
    
    val [compileClasspath](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#compileClasspath\(\)): [FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)

Access to the variant's compile classpath.

The returned `[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)` should not be resolved until execution time.

### compileConfiguration

Added in 7.3.0
    
    
    val [compileConfiguration](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#compileConfiguration\(\)): [Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)

Access to the variant's compile `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)`; for example, the debugCompileClasspath `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` for the debug variant.

The returned `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` should not be resolved until execution time.

### debuggable

Added in 8.3.1
    
    
    val [debuggable](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#debuggable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether the produced artifacts will be debuggable

### instrumentation

Added in 7.2.0
    
    
    val [instrumentation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#instrumentation\(\)): [Instrumentation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Instrumentation)

Access to the variant's instrumentation options.

### javaCompilation

Added in 7.1.0
    
    
    val [javaCompilation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#javaCompilation\(\)): [JavaCompilation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/JavaCompilation)?

Access to the variant's java compilation options.

### lifecycleTasks

Added in 8.3.1
    
    
    val [lifecycleTasks](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#lifecycleTasks\(\)): [LifecycleTasks](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/LifecycleTasks)

Provides access to the `[LifecycleTasks](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/LifecycleTasks)` created for this component.

### namespace

Added in 8.1.0
    
    
    val [namespace](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#namespace\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The namespace of the generated R and BuildConfig classes. Also, the namespace used to resolve any relative class names that are declared in the AndroidManifest.xml.

### runtimeConfiguration

Added in 7.3.0
    
    
    val [runtimeConfiguration](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#runtimeConfiguration\(\)): [Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)

Access to the variant's runtime `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)`; for example, the debugRuntimeClasspath `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` for the debug variant.

The returned `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` should not be resolved until execution time.

### sources

Added in 7.2.0
    
    
    val [sources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Component#sources\(\)): [Sources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Sources)

Access to variant's source files.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
