---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Multiple
title: Artifact.Multiple \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:23:51.725876+00:00
---

# Artifact.Multiple  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Multiple

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Artifact.Multiple

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/Artifact.kt+class:com.android.build.api.artifact.Artifact.Multiple)

Added in 7.0.0
    
    
    abstract class [Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Multiple)<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> : [Artifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact)  
|  ↳ | [com.android.build.api.artifact.Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Multiple)  
  
Known direct subclasses 

[MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact)

`[MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact)` |  Public `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact)` for Android Gradle plugin.  
---|---  
  
Known indirect subclasses 

[MultipleArtifact.MULTIDEX_KEEP_PROGUARD](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact.MULTIDEX_KEEP_PROGUARD), [MultipleArtifact.NATIVE_DEBUG_METADATA](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact.NATIVE_DEBUG_METADATA), [MultipleArtifact.NATIVE_SYMBOL_TABLES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact.NATIVE_SYMBOL_TABLES), [MultipleArtifact.PRE_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact.PRE_COMPILATION_CLASSES)

`[MultipleArtifact.MULTIDEX_KEEP_PROGUARD](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact.MULTIDEX_KEEP_PROGUARD)` |  Text files with additional ProGuard rules to be used to determine which classes are compiled into the main dex file.  
---|---  
`[MultipleArtifact.NATIVE_DEBUG_METADATA](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact.NATIVE_DEBUG_METADATA)` |  Directories with native debug metadata  
`[MultipleArtifact.NATIVE_SYMBOL_TABLES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact.NATIVE_SYMBOL_TABLES)` |  Directories with debug symbol table  
`[MultipleArtifact.PRE_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact.PRE_COMPILATION_CLASSES)` |  Directories containing generated code that will be added to compile classpath for the module.  
  
* * *

Denotes possible multiple `[FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)` instances for this artifact type. Consumers of artifact types with multiple instances must consume a collection of `[FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)`.

## Summary

### Public constructors  
  
---  
`<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [Multiple](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Multiple#Multiple\(com.android.build.api.artifact.ArtifactKind,com.android.build.api.artifact.Artifact.Category\))(  
kind: [ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ArtifactKind)<FileTypeT>,  
category: [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Category)  
)`  
  
### Inherited functions  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact) | `open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFileSystemLocationName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#getFileSystemLocationName\(\))()`  
---|---  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFolderName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#getFolderName\(\))()`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#name\(\))()` Provide a unique name for the artifact type.  
  
### Inherited properties  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact) | `[Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Category)` |  `[category](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#category\(\))`  
---|---  
`[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ArtifactKind)<FileTypeT>` |  `[kind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#kind\(\))`  
  
## Public constructors

### Multiple
    
    
    <FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [Multiple](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Multiple#Multiple\(com.android.build.api.artifact.ArtifactKind,com.android.build.api.artifact.Artifact.Category\))(  
        kind: [ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ArtifactKind)<FileTypeT>,  
        category: [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Category)  
    )

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
