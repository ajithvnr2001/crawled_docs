---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifact.NATIVE_SYMBOL_TABLES
title: MultipleArtifact.NATIVE_SYMBOL_TABLES \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:58:54.465788+00:00
---

# MultipleArtifact.NATIVE_SYMBOL_TABLES  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifact.NATIVE_SYMBOL_TABLES

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# MultipleArtifact.NATIVE_SYMBOL_TABLES

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/MultipleArtifact.kt+class:com.android.build.api.artifact.MultipleArtifact.NATIVE_SYMBOL_TABLES)

Added in 8.0.2
    
    
    object [MultipleArtifact.NATIVE_SYMBOL_TABLES](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifact.NATIVE_SYMBOL_TABLES) : [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifact), [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Replaceable), [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Appendable), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Transformable)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact)  
|  ↳ | [com.android.build.api.artifact.Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Multiple)  
|  |  ↳ | [com.android.build.api.artifact.MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifact)  
|  |  |  ↳ | [com.android.build.api.artifact.MultipleArtifact.NATIVE_SYMBOL_TABLES](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifact.NATIVE_SYMBOL_TABLES)  
  
* * *

Directories with debug symbol table

If set, the debug symbol table files(with extension .sym) are combined with extracted debug symbol tables and packaged together.

## Summary

### Inherited functions  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact) | `open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFileSystemLocationName](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact#getFileSystemLocationName\(\))()`  
---|---  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFolderName](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact#getFolderName\(\))()`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact#name\(\))()` Provide a unique name for the artifact type.  
  
### Inherited properties  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact) | `[Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Category)` |  `[category](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact#category\(\))`  
---|---  
`[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ArtifactKind)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)>` |  `[kind](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact#kind\(\))`  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
