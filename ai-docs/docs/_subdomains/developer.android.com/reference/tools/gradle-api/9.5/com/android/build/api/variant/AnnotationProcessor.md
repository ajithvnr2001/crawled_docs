---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AnnotationProcessor/
title: AnnotationProcessor \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:16:35.520612+00:00
---

# AnnotationProcessor  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AnnotationProcessor/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AnnotationProcessor

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/AnnotationProcessor.kt+class:com.android.build.api.variant.AnnotationProcessor)

Added in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [AnnotationProcessor](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AnnotationProcessor)

* * *

Build-time properties for Java annotation processors inside a `[Component](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/Component)`

This is accessed via `[JavaCompilation.annotationProcessor](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/JavaCompilation#annotationProcessor\(\))`

## Summary

### Public properties  
  
---  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[CommandLineArgumentProvider](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html)>` |  `[argumentProviders](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AnnotationProcessor#argumentProviders\(\))` Options for the annotation processors provided via `[CommandLineArgumentProvider](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html)`.  
`[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[arguments](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AnnotationProcessor#arguments\(\))` Options for the annotation processors provided via key-value pairs.  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[classNames](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AnnotationProcessor#classNames\(\))` Annotation processors to run.  
  
## Public properties

### argumentProviders

Added in 7.1.0
    
    
    val [argumentProviders](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AnnotationProcessor#argumentProviders\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[CommandLineArgumentProvider](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html)>

Options for the annotation processors provided via `[CommandLineArgumentProvider](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html)`.

See also  
---  
`[arguments](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AnnotationProcessor#arguments\(\))` |   
  
### arguments

Added in 7.1.0
    
    
    val [arguments](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AnnotationProcessor#arguments\(\)): [MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Options for the annotation processors provided via key-value pairs.

See also  
---  
`[argumentProviders](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AnnotationProcessor#argumentProviders\(\))` |   
  
### classNames

Added in 7.1.0
    
    
    val [classNames](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AnnotationProcessor#classNames\(\)): [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Annotation processors to run.

If empty, processors will be automatically discovered.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
