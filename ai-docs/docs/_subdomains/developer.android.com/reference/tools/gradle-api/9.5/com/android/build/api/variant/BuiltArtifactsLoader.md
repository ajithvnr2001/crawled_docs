---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifactsLoader/
title: BuiltArtifactsLoader \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:17:09.776598+00:00
---

# BuiltArtifactsLoader  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifactsLoader/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BuiltArtifactsLoader

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/BuiltArtifactsLoader.kt+class:com.android.build.api.variant.BuiltArtifactsLoader)

Added in 4.2.0
    
    
    interface [BuiltArtifactsLoader](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifactsLoader)

* * *

Facility to load `[BuiltArtifacts](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts)` instances from metadata files in the file system.

When an artifact can have more than one output file, its `[com.android.build.api.artifact.SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact)` is annotated with com.android.build.api.artifact.SingleArtifact.ContainsMany. com.android.build.api.artifact.ArtifactTypes.APK is an example of such an artifact: the folder produced can contain multiple APK files when multi-apk build is configured.

To be able to understand the content of such a folder, and in particular to know which file is associated with which `[VariantFilter](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantFilter)`, a metadata file is stored along side the artifact files.

`[BuiltArtifactsLoader](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifactsLoader)` will allow to load the content of the metadata file is obtained information about each file produced by AGP.

This interface should not be implemented by third party.

Implementation of this interface can be obtained from `[com.android.build.api.artifact.Artifacts.getBuiltArtifactsLoader](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifacts#getBuiltArtifactsLoader\(\))`

## Summary

### Public functions  
  
---  
`[BuiltArtifacts](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts)?` |  `[load](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifactsLoader#load\(org.gradle.api.file.FileCollection\))(fileCollection: [FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html))` Loads a metadata file from the provided `[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)` and returns a new `[BuiltArtifacts](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts)` containing the `[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)` of `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)` that are present in the `[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)`  
`[BuiltArtifacts](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts)?` |  `[load](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifactsLoader#load\(org.gradle.api.file.Directory\))(folder: [Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html))` Loads a metadata file from the provided `[folder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifactsLoader#load\(org.gradle.api.file.Directory\))` and returns a new `[BuiltArtifacts](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts)` containing the `[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)` of `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)` that are present in the `[folder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifactsLoader#load\(org.gradle.api.file.Directory\))`  
  
## Public functions

### load

Added in 4.2.0
    
    
    fun [load](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifactsLoader#load\(org.gradle.api.file.FileCollection\))(fileCollection: [FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)): [BuiltArtifacts](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts)?

Loads a metadata file from the provided `[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)` and returns a new `[BuiltArtifacts](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts)` containing the `[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)` of `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)` that are present in the `[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)`

Parameters  
---  
`fileCollection: [FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)` |  the file collection that should contain built artifacts and associated metadata file saved using the `[BuiltArtifacts.save](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts#save\(org.gradle.api.file.Directory\))` methods.  
  
### load

Added in 4.2.0
    
    
    fun [load](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifactsLoader#load\(org.gradle.api.file.Directory\))(folder: [Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)): [BuiltArtifacts](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts)?

Loads a metadata file from the provided `[folder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifactsLoader#load\(org.gradle.api.file.Directory\))` and returns a new `[BuiltArtifacts](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts)` containing the `[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)` of `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)` that are present in the `[folder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifactsLoader#load\(org.gradle.api.file.Directory\))`

Parameters  
---  
`folder: [Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` |  the directory abstraction that should contain built artifacts and associated metadata file saved using the `[BuiltArtifacts.save](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts#save\(org.gradle.api.file.Directory\))` methods.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
