---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact/
title: MultipleArtifact \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:47:37.771139+00:00
---

# MultipleArtifact  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# MultipleArtifact

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/MultipleArtifact.kt+class:com.android.build.api.artifact.MultipleArtifact)

Added in 7.0.0
    
    
    sealed class [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact)<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> : [Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact)  
|  ↳ | [com.android.build.api.artifact.Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)  
|  |  ↳ | [com.android.build.api.artifact.MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact)  
  
Known direct subclasses 

[MultipleArtifact.MULTIDEX_KEEP_PROGUARD](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.MULTIDEX_KEEP_PROGUARD), [MultipleArtifact.NATIVE_DEBUG_METADATA](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.NATIVE_DEBUG_METADATA), [MultipleArtifact.NATIVE_SYMBOL_TABLES](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.NATIVE_SYMBOL_TABLES), [MultipleArtifact.PRE_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.PRE_COMPILATION_CLASSES)

`[MultipleArtifact.MULTIDEX_KEEP_PROGUARD](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.MULTIDEX_KEEP_PROGUARD)` |  Text files with additional ProGuard rules to be used to determine which classes are compiled into the main dex file.  
---|---  
`[MultipleArtifact.NATIVE_DEBUG_METADATA](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.NATIVE_DEBUG_METADATA)` |  Directories with native debug metadata  
`[MultipleArtifact.NATIVE_SYMBOL_TABLES](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.NATIVE_SYMBOL_TABLES)` |  Directories with debug symbol table  
`[MultipleArtifact.PRE_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.PRE_COMPILATION_CLASSES)` |  Directories containing generated code that will be added to compile classpath for the module.  
  
* * *

Public `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact)` for Android Gradle plugin.

This type inherits `[Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)`. For single artifacts, see `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/SingleArtifact)`.

All methods in `[Artifacts](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifacts)` should be supported with any subclass of this class.

## Summary

### Nested types  
  
---  
`object [MultipleArtifact.MULTIDEX_KEEP_PROGUARD](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.MULTIDEX_KEEP_PROGUARD) : [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact), [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Replaceable), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Transformable)` Text files with additional ProGuard rules to be used to determine which classes are compiled into the main dex file.  
`object [MultipleArtifact.NATIVE_DEBUG_METADATA](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.NATIVE_DEBUG_METADATA) : [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact), [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Replaceable), [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Appendable), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Transformable)` Directories with native debug metadata  
`object [MultipleArtifact.NATIVE_SYMBOL_TABLES](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.NATIVE_SYMBOL_TABLES) : [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact), [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Replaceable), [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Appendable), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Transformable)` Directories with debug symbol table  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
object [MultipleArtifact.PRE_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact.PRE_COMPILATION_CLASSES) : [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact), [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Replaceable), [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Appendable), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Transformable)` Directories containing generated code that will be added to compile classpath for the module.  
  
### Protected constructors  
  
---  
`<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact#MultipleArtifact\(com.android.build.api.artifact.ArtifactKind,com.android.build.api.artifact.Artifact.Category,kotlin.collections.List\))(  
kind: [ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind)<FileTypeT>,  
category: [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Category),  
attributeKeys: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>?  
)`  
  
### Public properties  
  
---  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>?` |  `[attributeKeys](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact#attributeKeys\(\))`  
  
### Inherited functions  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact) | `open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFileSystemLocationName](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact#getFileSystemLocationName\(\))()`  
---|---  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFolderName](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact#getFolderName\(\))()`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact#name\(\))()` Provide a unique name for the artifact type.  
  
### Inherited properties  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact) | `[Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Category)` |  `[category](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact#category\(\))`  
---|---  
`[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind)<FileTypeT>` |  `[kind](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact#kind\(\))`  
  
## Protected constructors

### MultipleArtifact
    
    
    protected <FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact#MultipleArtifact\(com.android.build.api.artifact.ArtifactKind,com.android.build.api.artifact.Artifact.Category,kotlin.collections.List\))(  
        kind: [ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind)<FileTypeT>,  
        category: [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Category) = Category.INTERMEDIATES,  
        attributeKeys: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>? = null  
    )

## Public properties

### attributeKeys

Added in 9.4.1
    
    
    val [attributeKeys](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact#attributeKeys\(\)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>?

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
