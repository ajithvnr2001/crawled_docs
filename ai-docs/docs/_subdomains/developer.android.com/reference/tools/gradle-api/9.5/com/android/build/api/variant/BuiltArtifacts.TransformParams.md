---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts.TransformParams
title: BuiltArtifacts.TransformParams \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:17:05.809966+00:00
---

# BuiltArtifacts.TransformParams  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts.TransformParams

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BuiltArtifacts.TransformParams

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/BuiltArtifacts.kt+class:com.android.build.api.variant.BuiltArtifacts.TransformParams)

Added in 4.2.0
    
    
    interface [BuiltArtifacts.TransformParams](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts.TransformParams) : [WorkParameters](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkParameters.html), [Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)

* * *

Specialized version of Gradle's `[WorkParameters](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkParameters.html)` so we can retrieve the output file generated when transforming an instance of `[BuiltArtifacts](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts)` into a new one.

## Summary

### Public properties  
  
---  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)` |  `[output](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts.TransformParams#output\(\))` Result of the work item submission must be made available through this field.  
  
## Public properties

### output

Added in 4.2.0
    
    
    val [output](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts.TransformParams#output\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)

Result of the work item submission must be made available through this field.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
