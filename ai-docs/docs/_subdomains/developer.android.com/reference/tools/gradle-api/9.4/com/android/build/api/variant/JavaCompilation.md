---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JavaCompilation/
title: JavaCompilation \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:01:03.683246+00:00
---

# JavaCompilation  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JavaCompilation/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# JavaCompilation

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/JavaCompilation.kt+class:com.android.build.api.variant.JavaCompilation)

Added in 7.1.0
    
    
    interface [JavaCompilation](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JavaCompilation)

* * *

Build-time properties for Java compile inside a `[Component](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Component)`

This is accessed via `[Component.javaCompilation](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Component#javaCompilation\(\))`

## Summary

### Public properties  
  
---  
`[AnnotationProcessor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AnnotationProcessor)` |  `[annotationProcessor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JavaCompilation#annotationProcessor\(\))` Returns the `[AnnotationProcessor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AnnotationProcessor)` for configuring Java annotation processor.  
`[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` |  `[annotationProcessorConfiguration](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JavaCompilation#annotationProcessorConfiguration\(\))` Access to the variant's annotation processor `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)`; for example, the debugAnnotationProcessor `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` for the debug variant.  
  
## Public properties

### annotationProcessor

Added in 7.1.0
    
    
    val [annotationProcessor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JavaCompilation#annotationProcessor\(\)): [AnnotationProcessor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AnnotationProcessor)

Returns the `[AnnotationProcessor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AnnotationProcessor)` for configuring Java annotation processor.

### annotationProcessorConfiguration

Added in 8.10.1
    
    
    val [annotationProcessorConfiguration](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/JavaCompilation#annotationProcessorConfiguration\(\)): [Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)

Access to the variant's annotation processor `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)`; for example, the debugAnnotationProcessor `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` for the debug variant.

The returned `[Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` should not be resolved until execution time.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
