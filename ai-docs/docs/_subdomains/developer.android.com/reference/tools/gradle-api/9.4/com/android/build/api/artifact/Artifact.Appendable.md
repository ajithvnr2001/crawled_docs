---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Appendable
title: Artifact.Appendable \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:54.038322+00:00
---

# Artifact.Appendable  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Appendable

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Artifact.Appendable

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/Artifact.kt+class:com.android.build.api.artifact.Artifact.Appendable)

Added in 4.2.0
    
    
    interface [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Appendable)

Known direct subclasses 

[MultipleArtifact.NATIVE_DEBUG_METADATA](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.NATIVE_DEBUG_METADATA), [MultipleArtifact.NATIVE_SYMBOL_TABLES](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.NATIVE_SYMBOL_TABLES), [MultipleArtifact.PRE_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.PRE_COMPILATION_CLASSES), [ScopedArtifact.CLASSES](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ScopedArtifact.CLASSES), [ScopedArtifact.JAVA_RES](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ScopedArtifact.JAVA_RES)

`[MultipleArtifact.NATIVE_DEBUG_METADATA](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.NATIVE_DEBUG_METADATA)` |  Directories with native debug metadata  
---|---  
`[MultipleArtifact.NATIVE_SYMBOL_TABLES](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.NATIVE_SYMBOL_TABLES)` |  Directories with debug symbol table  
`[MultipleArtifact.PRE_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.PRE_COMPILATION_CLASSES)` |  Directories containing generated code that will be added to compile classpath for the module.  
`[ScopedArtifact.CLASSES](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ScopedArtifact.CLASSES)` |  .class files, result of sources compilation and/or external dependencies depending on the scope; includes users' transformation, but does not include Jacoco instrumentation  
`[ScopedArtifact.JAVA_RES](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ScopedArtifact.JAVA_RES)` |   
  
* * *

Denotes an artifact type that can be appended to. Appending means that existing artifacts produced by other tasks are untouched and a new task producing the artifact type will have its output appended to the list of artifacts.

Due to the additive behavior of the append scenario, an `[Appendable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Appendable)` must be a `[Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)`.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
