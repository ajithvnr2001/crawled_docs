---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions/
title: AnnotationProcessorOptions \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:49:59.715908+00:00
---

# AnnotationProcessorOptions  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AnnotationProcessorOptions

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/AnnotationProcessorOptions.kt+class:com.android.build.api.dsl.AnnotationProcessorOptions)

Added in 4.2.0
    
    
    interface [AnnotationProcessorOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions)

* * *

Options for configuring Java annotation processor.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[argument](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#argument\(kotlin.String,kotlin.String\))(key: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds an argument that represent primitive types for annotation processors.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[arguments](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#arguments\(kotlin.collections.Map\))(arguments: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>)` Adds arguments that represent primitive types for annotation processors.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[className](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#className\(kotlin.String\))(className: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds an annotation processor class to run.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[classNames](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#classNames\(kotlin.Array\))(vararg classNames: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds annotation processor classes to run.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compilerArgumentProvider](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#compilerArgumentProvider\(org.gradle.process.CommandLineArgumentProvider\))(  
compilerArgumentProvider: [CommandLineArgumentProvider](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html)  
)` Adds an argument for annotation processors that you want to pass to the Android plugin using the `[CommandLineArgumentProvider](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html)` class.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compilerArgumentProviders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#compilerArgumentProviders\(kotlin.Array\))(  
vararg compilerArgumentProviders: [CommandLineArgumentProvider](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html)  
)` Adds arguments for annotation processors that you want to pass to the Android plugin using the `[CommandLineArgumentProvider](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html)` class.  
  
### Public properties  
  
---  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[arguments](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#arguments\(\))` Specifies arguments that represent primitive types for annotation processors.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[classNames](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#classNames\(\))` Specifies the annotation processor classes to run.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[CommandLineArgumentProvider](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html)>` |  `[compilerArgumentProviders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#compilerArgumentProviders\(\))` Specifies arguments for annotation processors that you want to pass to the Android plugin using the `[CommandLineArgumentProvider](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html)` class.  
  
## Public functions

### argument

Added in 4.2.0
    
    
    fun [argument](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#argument\(kotlin.String,kotlin.String\))(key: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds an argument that represent primitive types for annotation processors.

If one or more arguments represent files or directories, you must instead use `[compilerArgumentProviders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#compilerArgumentProviders\(kotlin.Array\))`.

See also  
---  
`[compilerArgumentProviders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#compilerArgumentProviders\(kotlin.Array\))` |   
  
### arguments

Added in 4.2.0
    
    
    fun [arguments](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#arguments\(kotlin.collections.Map\))(arguments: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds arguments that represent primitive types for annotation processors.

If one or more arguments represent files or directories, you must instead use `[compilerArgumentProviders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#compilerArgumentProviders\(kotlin.Array\))`.

See also  
---  
`[compilerArgumentProviders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#compilerArgumentProviders\(kotlin.Array\))` |   
  
### className

Added in 4.2.0
    
    
    fun [className](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#className\(kotlin.String\))(className: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds an annotation processor class to run.

By default, this property is empty and the plugin automatically discovers and runs annotation processors that you add to the annotation processor classpath. To learn more about adding annotation processor dependencies to your project, read [Add annotation processors](https://d.android.com/studio/build/dependencies#annotation_processor).

### classNames

Added in 4.2.0
    
    
    fun [classNames](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#classNames\(kotlin.Array\))(vararg classNames: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds annotation processor classes to run.

By default, this property is empty and the plugin automatically discovers and runs annotation processors that you add to the annotation processor classpath. To learn more about adding annotation processor dependencies to your project, read [Add annotation processors](https://d.android.com/studio/build/dependencies#annotation_processor).

### compilerArgumentProvider

Added in 4.2.0
    
    
    fun [compilerArgumentProvider](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#compilerArgumentProvider\(org.gradle.process.CommandLineArgumentProvider\))(  
        compilerArgumentProvider: [CommandLineArgumentProvider](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds an argument for annotation processors that you want to pass to the Android plugin using the `[CommandLineArgumentProvider](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html)` class.

The benefit of using this class is that it allows you or the annotation processor author to improve the correctness and performance of incremental and cached clean builds by applying [incremental build property type annotations](https://docs.gradle.org/current/userguide/more_about_tasks.html#sec:up_to_date_checks).

To learn more about how to use this class to annotate arguments for annotation processors and pass them to the Android plugin, read [Pass arguments to annotation processors](https://developer.android.com/studio/build/dependencies#processor-arguments).

### compilerArgumentProviders

Added in 4.2.0
    
    
    fun [compilerArgumentProviders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#compilerArgumentProviders\(kotlin.Array\))(  
        vararg compilerArgumentProviders: [CommandLineArgumentProvider](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds arguments for annotation processors that you want to pass to the Android plugin using the `[CommandLineArgumentProvider](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html)` class.

The benefit of using this class is that it allows you or the annotation processor author to improve the correctness and performance of incremental and cached clean builds by applying [incremental build property type annotations](https://docs.gradle.org/current/userguide/more_about_tasks.html#sec:up_to_date_checks).

To learn more about how to use this class to annotate arguments for annotation processors and pass them to the Android plugin, read [Pass arguments to annotation processors](https://developer.android.com/studio/build/dependencies#processor-arguments).

## Public properties

### arguments

Added in 4.2.0
    
    
    val [arguments](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#arguments\(\)): [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies arguments that represent primitive types for annotation processors.

If one or more arguments represent files or directories, you must instead use `[compilerArgumentProviders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#compilerArgumentProviders\(kotlin.Array\))`.

See also  
---  
`[compilerArgumentProviders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#compilerArgumentProviders\(kotlin.Array\))` |   
  
### classNames

Added in 4.2.0
    
    
    val [classNames](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#classNames\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies the annotation processor classes to run.

By default, this property is empty and the plugin automatically discovers and runs annotation processors that you add to the annotation processor classpath. To learn more about adding annotation processor dependencies to your project, read [Add annotation processors](https://d.android.com/studio/build/dependencies#annotation_processor).

### compilerArgumentProviders

Added in 4.2.0
    
    
    val [compilerArgumentProviders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AnnotationProcessorOptions#compilerArgumentProviders\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[CommandLineArgumentProvider](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html)>

Specifies arguments for annotation processors that you want to pass to the Android plugin using the `[CommandLineArgumentProvider](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html)` class.

The benefit of using this class is that it allows you or the annotation processor author to improve the correctness and performance of incremental and cached clean builds by applying [incremental build property type annotations](https://docs.gradle.org/current/userguide/more_about_tasks.html#sec:up_to_date_checks).

To learn more about how to use this class to annotate arguments for annotation processors and pass them to the Android plugin, read [Pass arguments to annotation processors](https://developer.android.com/studio/build/dependencies#processor-arguments).

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
