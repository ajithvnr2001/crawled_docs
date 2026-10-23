---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind/
title: ArtifactKind \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:47:35.756668+00:00
---

# ArtifactKind  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ArtifactKind

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/ArtifactKind.kt+class:com.android.build.api.artifact.ArtifactKind)

Added in 4.2.0
    
    
    sealed class [ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind)<T : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> : [Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)

Known direct subclasses 

[ArtifactKind.DIRECTORY](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind.DIRECTORY), [ArtifactKind.FILE](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind.FILE)

`[ArtifactKind.DIRECTORY](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind.DIRECTORY)` |  A type of artifact file that is a `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)`  
---|---  
`[ArtifactKind.FILE](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind.FILE)` |  A Type of artifact that is a `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)`  
  
* * *

Exhaustive list of artifact file representations supported by the Android Gradle plugin.

As of now, only `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` represented by `[FILE](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind.FILE)` and `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` represented by `[DIRECTORY](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind.DIRECTORY)` are supported.

## Summary

### Nested types  
  
---  
`object [ArtifactKind.DIRECTORY](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind.DIRECTORY) : [ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind)` A type of artifact file that is a `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)`  
`object [ArtifactKind.FILE](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind.FILE) : [ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind)` A Type of artifact that is a `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)`  
  
### Protected constructors  
  
---  
`<T : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind#ArtifactKind\(\))()`  
  
### Public functions  
  
---  
`abstract [KClass](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/index.html)<T>` |  `[dataType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind#dataType\(\))()`  
  
## Protected constructors

### ArtifactKind
    
    
    protected <T : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind#ArtifactKind\(\))()

## Public functions

### dataType

Added in 4.2.0
    
    
    abstract fun [dataType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind#dataType\(\))(): [KClass](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/index.html)<T>

Returns  
---  
`[KClass](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/index.html)<T>` |  The data type used by Gradle to represent the file abstraction for this artifact kind.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
