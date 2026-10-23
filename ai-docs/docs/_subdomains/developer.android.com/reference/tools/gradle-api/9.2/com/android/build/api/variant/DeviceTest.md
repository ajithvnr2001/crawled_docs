---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DeviceTest/
title: DeviceTest \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:52:44.908427+00:00
---

# DeviceTest  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DeviceTest/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DeviceTest

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/DeviceTest.kt+class:com.android.build.api.variant.DeviceTest)

Added in 8.4.0
    
    
    interface [DeviceTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DeviceTest) : [GeneratesTestApk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesTestApk), [HasAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasAndroidResources), [TestComponent](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestComponent)

Known direct subclasses 

[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidTest)

`[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidTest)` |  Model for Android Test components that contains build-time properties  
---|---  
  
* * *

Model for Device Test components that contains build-time properties

This object is accessible on subtypes of `[Variant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant)` that implement `[HasDeviceTests](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasDeviceTests)`, via `[HasDeviceTests.deviceTests](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasDeviceTests#deviceTests\(\))`. It is also part of `[Variant.nestedComponents](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#nestedComponents\(\))`.

The presence of this component in a variant is controlled by `[HasDeviceTestsBuilder.deviceTests](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasDeviceTestsBuilder#deviceTests\(\))` and `[DeviceTestBuilder.enable](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DeviceTestBuilder#enable\(\))` which is accessible on subtypes of `[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder)` that implement `[HasDeviceTestsBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasDeviceTestsBuilder)`

## Summary

### Public properties  
  
---  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[applicationId](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DeviceTest#applicationId\(\))` Variant's application ID as present in the final manifest file of the APK.  
`[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [BuildConfigField](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/BuildConfigField)<[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)>>?` |  `[buildConfigFields](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DeviceTest#buildConfigFields\(\))` Variant's `[BuildConfigField](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/BuildConfigField)` which will be generated in the BuildConfig class.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[codeCoverageEnabled](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DeviceTest#codeCoverageEnabled\(\))` Whether test coverage is enabled for this device test.  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>` |  `[proguardFiles](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DeviceTest#proguardFiles\(\))` List of proguard configuration files for this variant.  
`[SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/SigningConfig)?` |  `[signingConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DeviceTest#signingConfig\(\))` Variant's signingConfig, initialized by the corresponding DSL element.  
  
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
  
From [com.android.build.api.variant.GeneratesApk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesApk) | `[AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidResources)` |  `[androidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesApk#androidResources\(\))` Variant's android resources processing configuration, initialized by the corresponding global DSL element.  
---|---  
`[Dexing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Dexing)` |  `[dexing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesApk#dexing\(\))` Variant's specific dexing options  
`[AndroidVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidVersion)` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesApk#minSdk\(\))` Min SDK version for this variant  
`[ApkOutputProviders](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApkOutputProviders)` |  `[outputProviders](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesApk#outputProviders\(\))` Provides access to built artifacts output(e.g. APK) produced by this Variant.  
`[ApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApkPackaging)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesApk#packaging\(\))` Variant's packagingOptions, initialized by the corresponding global DSL element.  
`[Renderscript](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Renderscript)?` |  `[renderscript](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesApk#renderscript\(\))` Variant specific settings for the renderscript compiler.  
`[AndroidVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidVersion)` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesApk#targetSdk\(\))` Target SDK version for this variant.  
  
From [com.android.build.api.variant.GeneratesTestApk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesTestApk) | `[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[functionalTest](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesTestApk#functionalTest\(\))` The functionalTest value to use to run the tests.  
---|---  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[handleProfiling](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesTestApk#handleProfiling\(\))` The handleProfiling value to use to run the tests.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[instrumentationRunner](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesTestApk#instrumentationRunner\(\))` The instrumentationRunner to use to run the tests.  
`[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[instrumentationRunnerArguments](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesTestApk#instrumentationRunnerArguments\(\))` The instrumentationRunnerArguments to use to run the tests.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[testLabel](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesTestApk#testLabel\(\))` The test label, or "" if none defined.  
  
From [com.android.build.api.variant.HasAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasAndroidResources) | `[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[pseudoLocalesEnabled](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasAndroidResources#pseudoLocalesEnabled\(\))` Variant's is pseudo locales enabled, initialized by the corresponding DSL elements.  
---|---  
`[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[ResValue.Key](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ResValue.Key), [ResValue](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ResValue)>` |  `[resValues](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/HasAndroidResources#resValues\(\))` Variant's `[ResValue](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ResValue)` which will be generated.  
  
From [com.android.build.api.variant.TestComponent](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestComponent) | `[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[manifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestComponent#manifestPlaceholders\(\))` `[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)` of the test component's manifest placeholders.  
---|---  
  
## Public properties

### applicationId
    
    
    val [applicationId](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DeviceTest#applicationId\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Variant's application ID as present in the final manifest file of the APK.

### buildConfigFields

Added in 8.4.0
    
    
    val [buildConfigFields](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DeviceTest#buildConfigFields\(\)): [MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [BuildConfigField](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/BuildConfigField)<[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)>>?

Variant's `[BuildConfigField](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/BuildConfigField)` which will be generated in the BuildConfig class.

### codeCoverageEnabled

Added in 8.5.0
    
    
    val [codeCoverageEnabled](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DeviceTest#codeCoverageEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether test coverage is enabled for this device test.

If enabled, this uses Jacoco to capture coverage and creates a report in the build directory.

You cannot change the value any longer, to change it, please use `[DeviceTestBuilder.enableCodeCoverage](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DeviceTestBuilder#enableCodeCoverage\(\))` in the `[AndroidComponentsExtension.beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` callback.

### proguardFiles

Added in 8.4.0
    
    
    val [proguardFiles](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DeviceTest#proguardFiles\(\)): [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>

List of proguard configuration files for this variant. The list is initialized from the corresponding DSL element, and cannot be queried at configuration time. At configuration time, you can only add new elements to the list.

### signingConfig

Added in 8.4.0
    
    
    val [signingConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DeviceTest#signingConfig\(\)): [SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/SigningConfig)?

Variant's signingConfig, initialized by the corresponding DSL element.

Returns  
---  
`[SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/SigningConfig)?` |  Variant's config or null if the variant is not configured for signing.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
