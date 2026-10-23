---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestFixtures/
title: TestFixtures \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:38:11.781854+00:00
---

# TestFixtures  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestFixtures/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestFixtures

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/TestFixtures.kt+class:com.android.build.api.variant.TestFixtures)

Added in 7.0.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestFixtures) : [GeneratesAar](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/GeneratesAar), [HasAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/HasAndroidResources), [Component](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component)

* * *

Model for Test Fixtures components that contains build-time properties

This object is accessible on subtypes of `[Variant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Variant)` that implement `[HasTestFixtures](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/HasTestFixtures)`, via `[HasTestFixtures.testFixtures](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/HasTestFixtures#testFixtures\(\))`. It is also part of `[Variant.nestedComponents](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Variant#nestedComponents\(\))`.

The presence of this component in a variant is controlled by `[HasTestFixturesBuilder.enableTestFixtures](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/HasTestFixturesBuilder#enableTestFixtures\(\))` which is accessible on subtypes of `[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantBuilder)` that implement `[HasTestFixturesBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/HasTestFixturesBuilder)`

## Summary

### Inherited functions  
  
---  
From [com.android.build.api.variant.Component](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[computeTaskName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component#computeTaskName\(kotlin.String,kotlin.String\))(action: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), subject: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Utility method to create unique task name for component.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[configureJavaCompileTask](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component#configureJavaCompileTask\(kotlin.Function1\))(action: ([JavaCompile](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/compile/JavaCompile.html)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Runs an action to configure Components's java compilation `[JavaCompile](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/compile/JavaCompile.html)` task.  
`[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[getResolvableConfiguration](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component#getResolvableConfiguration\(kotlin.String\))(sourceSetConfigurationsAffix: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Access to the component's resolvable configuration corresponding to the source set configurations added via `[AndroidComponentsExtension.addSourceSetConfigurations](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidComponentsExtension#addSourceSetConfigurations\(kotlin.String\))`.  
  
From [com.android.build.api.variant.HasAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/HasAndroidResources) | `[ResValue.Key](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ResValue.Key)` |  `[makeResValueKey](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/HasAndroidResources#makeResValueKey\(kotlin.String,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Make a `[ResValue.Key](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ResValue.Key)` to interact with `[resValues](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/HasAndroidResources#resValues\(\))`'s `[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)`  
---|---  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.Component](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component) | `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` |  `[annotationProcessorConfiguration](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component#annotationProcessorConfiguration\(\))` Access to the variant's annotation processor `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)`; for example, the debugAnnotationProcessor `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` for the debug variant.  
---|---  
`[Artifacts](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifacts)` |  `[artifacts](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component#artifacts\(\))` Access to the variant's buildable artifacts for build customization.  
`[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)` |  `[compileClasspath](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component#compileClasspath\(\))` Access to the variant's compile classpath.  
`[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` |  `[compileConfiguration](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component#compileConfiguration\(\))` Access to the variant's compile `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)`; for example, the debugCompileClasspath `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` for the debug variant.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[debuggable](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component#debuggable\(\))` Whether the produced artifacts will be debuggable  
`[Instrumentation](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Instrumentation)` |  `[instrumentation](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component#instrumentation\(\))` Access to the variant's instrumentation options.  
`[JavaCompilation](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/JavaCompilation)?` |  `[javaCompilation](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component#javaCompilation\(\))` Access to the variant's java compilation options.  
`[LifecycleTasks](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/LifecycleTasks)` |  `[lifecycleTasks](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component#lifecycleTasks\(\))` Provides access to the `[LifecycleTasks](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/LifecycleTasks)` created for this component.  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[namespace](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component#namespace\(\))` The namespace of the generated R and BuildConfig classes.  
`[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` |  `[runtimeConfiguration](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component#runtimeConfiguration\(\))` Access to the variant's runtime `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)`; for example, the debugRuntimeClasspath `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` for the debug variant.  
`[Sources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources)` |  `[sources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component#sources\(\))` Access to variant's source files.  
  
From [com.android.build.api.variant.ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentIdentity) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[buildType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentIdentity#buildType\(\))` Build type name.  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[flavorName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentIdentity#flavorName\(\))` The multi-flavor name of the variant.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentIdentity#name\(\))` Component's name.  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>>` |  `[productFlavors](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentIdentity#productFlavors\(\))` List of flavor names.  
  
From [com.android.build.api.variant.GeneratesAar](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/GeneratesAar) | `[AarMetadata](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AarMetadata)` |  `[aarMetadata](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/GeneratesAar#aarMetadata\(\))` Variant's aar metadata, initialized by merging the corresponding `[com.android.build.api.dsl.AarMetadata](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AarMetadata)` DSL elements.  
---|---  
  
From [com.android.build.api.variant.HasAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/HasAndroidResources) | `[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[pseudoLocalesEnabled](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/HasAndroidResources#pseudoLocalesEnabled\(\))` Variant's is pseudo locales enabled, initialized by the corresponding DSL elements.  
---|---  
`[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[ResValue.Key](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ResValue.Key), [ResValue](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ResValue)>` |  `[resValues](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/HasAndroidResources#resValues\(\))` Variant's `[ResValue](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ResValue)` which will be generated.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
