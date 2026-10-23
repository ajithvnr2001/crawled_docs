---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ScopedArtifacts/
title: ScopedArtifacts \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:55:06.494445+00:00
---

# ScopedArtifacts  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ScopedArtifacts/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ScopedArtifacts

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/ScopedArtifacts.kt+class:com.android.build.api.variant.ScopedArtifacts)

Added in 7.4.0
    
    
    interface [ScopedArtifacts](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ScopedArtifacts)

* * *

Scoped artifacts are artifacts that can be made available in the current variant scope, or may be optionally include the project's dependencies in the results.

This is only available for elements that are part of the `[com.android.build.api.artifact.ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact)` hierarchy.

## Summary

### Nested types  
  
---  
`enum [ScopedArtifacts.Scope](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ScopedArtifacts.Scope) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)` Defines possible scopes.  
  
### Public functions  
  
---  
`[ScopedArtifactsOperation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ScopedArtifactsOperation)<T>` |  `<T : [Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)> [use](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ScopedArtifacts#use\(org.gradle.api.tasks.TaskProvider\))(taskProvider: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<T>)` Access `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` based operations.  
  
## Public functions

### use

Added in 7.4.0
    
    
    fun <T : [Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)> [use](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ScopedArtifacts#use\(org.gradle.api.tasks.TaskProvider\))(taskProvider: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<T>): [ScopedArtifactsOperation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ScopedArtifactsOperation)<T>

Access `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` based operations.

So far, all operations are only accessible providing a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` instance.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
