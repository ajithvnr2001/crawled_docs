---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts/
title: Artifacts \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:41:25.108106+00:00
---

# Artifacts  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Artifacts

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/Artifacts.kt+class:com.android.build.api.artifact.Artifacts)

Added in 4.2.0
    
    
    interface [Artifacts](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts)

* * *

Access to the artifacts on a Variant object.

Artifacts are temporary or final files or directories that are produced by the Android Gradle plugin during the build. Depending on its configuration, each `[com.android.build.api.variant.VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder)` produces different versions of some of the output artifacts.

An example of temporary artifacts are .class files obtained from compiling source files that will eventually get transformed further into dex files. Final artifacts are APKs and bundle files that are not transformed further.

Artifacts are uniquely defined by their `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact)` type and public artifact types that can be accessed from third-party plugins or build script are defined in `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/SingleArtifact)`

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> ~~[add](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#add\(com.android.build.api.artifact.MultipleArtifact,org.gradle.api.file.FileSystemLocation\))~~(  
type: [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/MultipleArtifact)<FileTypeT>,  
artifact: FileTypeT  
)` **This function is deprecated.** Use addStaticDirectory instead  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<MultipleArtifactT : [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/MultipleArtifact)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)> & [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Appendable)> [addStaticDirectory](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#addStaticDirectory\(com.android.build.api.artifact.MultipleArtifact,org.gradle.api.file.Directory\))(  
type: MultipleArtifactT,  
inputLocation: [Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)  
)` Add existing directory of type `[MultipleArtifactT](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#addStaticDirectory\(com.android.build.api.artifact.MultipleArtifact,org.gradle.api.file.Directory\))` to be combined with project artifact.  
`[ScopedArtifacts](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ScopedArtifacts)` |  `[forScope](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#forScope\(com.android.build.api.variant.ScopedArtifacts.Scope\))(scope: [ScopedArtifacts.Scope](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ScopedArtifacts.Scope))` Some artifacts do not have a single origin (like compiled from source code).  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<FileTypeT>` |  `<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [get](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#get\(com.android.build.api.artifact.SingleArtifact\))(type: [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/SingleArtifact)<FileTypeT>)` Get the `[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)` of `[FileTypeT](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#get\(com.android.build.api.artifact.SingleArtifact\))` for the passed `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact)`.  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<FileTypeT>>` |  `<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [getAll](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#getAll\(com.android.build.api.artifact.MultipleArtifact\))(type: [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/MultipleArtifact)<FileTypeT>)` Get all the `[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)`s of `[FileTypeT](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#getAll\(com.android.build.api.artifact.MultipleArtifact\))` for the passed `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact)`.  
`[BuiltArtifactsLoader](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/BuiltArtifactsLoader)` |  `[getBuiltArtifactsLoader](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#getBuiltArtifactsLoader\(\))()` Provides an implementation of `[BuiltArtifactsLoader](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/BuiltArtifactsLoader)` that can be used to load built artifacts metadata.  
`[TaskBasedOperation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/TaskBasedOperation)<TaskT>` |  `<TaskT : [Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)> [use](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#use\(org.gradle.api.tasks.TaskProvider\))(taskProvider: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<TaskT>)` Access `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` based operations.  
  
## Public functions

### add

Added in 8.0.2

Deprecated in 8.4.0
    
    
    fun <FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> ~~[add](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#add\(com.android.build.api.artifact.MultipleArtifact,org.gradle.api.file.FileSystemLocation\))~~(  
        type: [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/MultipleArtifact)<FileTypeT>,  
        artifact: FileTypeT  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Use addStaticDirectory instead

Add an existing `[FileTypeT](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#add\(com.android.build.api.artifact.MultipleArtifact,org.gradle.api.file.FileSystemLocation\))` for the passed `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact)`. For task generated folder or file, do not use this API but instead use the `[use](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#use\(org.gradle.api.tasks.TaskProvider\))` API.

Parameters  
---  
`type: [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/MultipleArtifact)<FileTypeT>` |  Type of the multiple artifact.  
`artifact: FileTypeT` |  is an existing static `[FileTypeT](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#add\(com.android.build.api.artifact.MultipleArtifact,org.gradle.api.file.FileSystemLocation\))`  
  
### addStaticDirectory

Added in 8.4.0
    
    
    fun <MultipleArtifactT : [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/MultipleArtifact)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)> & [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Appendable)> [addStaticDirectory](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#addStaticDirectory\(com.android.build.api.artifact.MultipleArtifact,org.gradle.api.file.Directory\))(  
        type: MultipleArtifactT,  
        inputLocation: [Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Add existing directory of type `[MultipleArtifactT](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#addStaticDirectory\(com.android.build.api.artifact.MultipleArtifact,org.gradle.api.file.Directory\))` to be combined with project artifact. Do not use this for generated files, use the `[use](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#use\(org.gradle.api.tasks.TaskProvider\))` API instead.

Parameters  
---  
`type: MultipleArtifactT` |  type of the multiple artifact.  
`inputLocation: [Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` |  is an existing static file  
  
### forScope

Added in 7.4.0
    
    
    fun [forScope](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#forScope\(com.android.build.api.variant.ScopedArtifacts.Scope\))(scope: [ScopedArtifacts.Scope](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ScopedArtifacts.Scope)): [ScopedArtifacts](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ScopedArtifacts)

Some artifacts do not have a single origin (like compiled from source code). Some artifacts can be obtained from a combination of `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)`s running or incoming dependencies. For example, classes used for dexing can come from compilation related tasks as well as .aar or .jar files expressed as a project dependency.

Therefore, these artifacts values can have a scope like `[ScopedArtifacts.Scope.PROJECT](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ScopedArtifacts.Scope#PROJECT)` for values directly produced by this module (as a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` output most likely). Alternatively, the `[ScopedArtifacts.Scope.ALL](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ScopedArtifacts.Scope#ALL)` adds all incoming dependencies (including transitive ones) to the previous scope.

For such cases, the artifact is represented as `[ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact)` and can be manipulated by its own set of API that are scope aware.

Return `[ScopedArtifacts](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ScopedArtifacts)` for a `[ScopedArtifacts.Scope](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ScopedArtifacts.Scope)`

### get

Added in 7.0.0
    
    
    fun <FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [get](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#get\(com.android.build.api.artifact.SingleArtifact\))(type: [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/SingleArtifact)<FileTypeT>): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<FileTypeT>

Get the `[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)` of `[FileTypeT](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#get\(com.android.build.api.artifact.SingleArtifact\))` for the passed `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact)`.

Parameters  
---  
`type: [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/SingleArtifact)<FileTypeT>` |  Type of the single artifact.  
  
### getAll

Added in 7.0.0
    
    
    fun <FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [getAll](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#getAll\(com.android.build.api.artifact.MultipleArtifact\))(type: [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/MultipleArtifact)<FileTypeT>): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<FileTypeT>>

Get all the `[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)`s of `[FileTypeT](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#getAll\(com.android.build.api.artifact.MultipleArtifact\))` for the passed `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact)`.

Parameters  
---  
`type: [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/MultipleArtifact)<FileTypeT>` |  Type of the multiple artifact.  
  
### getBuiltArtifactsLoader

Added in 4.2.0
    
    
    fun [getBuiltArtifactsLoader](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#getBuiltArtifactsLoader\(\))(): [BuiltArtifactsLoader](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/BuiltArtifactsLoader)

Provides an implementation of `[BuiltArtifactsLoader](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/BuiltArtifactsLoader)` that can be used to load built artifacts metadata.

Returns  
---  
`[BuiltArtifactsLoader](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/BuiltArtifactsLoader)` |  A thread safe implementation of `[BuiltArtifactsLoader](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/BuiltArtifactsLoader)` that can be reused.  
  
### use

Added in 4.2.0
    
    
    fun <TaskT : [Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)> [use](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#use\(org.gradle.api.tasks.TaskProvider\))(taskProvider: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<TaskT>): [TaskBasedOperation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/TaskBasedOperation)<TaskT>

Access `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` based operations.

Parameters  
---  
`taskProvider: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<TaskT>` |  The `[TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)` for the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifacts#use\(org.gradle.api.tasks.TaskProvider\))` that will be producing and/or consuming artifact types.  
  
Returns  
---  
`[TaskBasedOperation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/TaskBasedOperation)<TaskT>` |  A `[TaskBasedOperation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/TaskBasedOperation)` object using the passed `[TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)` for all its operations.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
