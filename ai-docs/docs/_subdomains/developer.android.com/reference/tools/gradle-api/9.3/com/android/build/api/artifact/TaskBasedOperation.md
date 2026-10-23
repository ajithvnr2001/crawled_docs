---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation/
title: TaskBasedOperation \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:23:47.302701+00:00
---

# TaskBasedOperation  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TaskBasedOperation

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/TaskBasedOperation.kt+class:com.android.build.api.artifact.TaskBasedOperation)

Added in 4.2.0
    
    
    interface [TaskBasedOperation](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)<TaskT : [Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)>

* * *

Interface with methods to wire input and output method references to `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)`-based operations.

A `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)`-based operation will create, transform, or append files or directories to public `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)` to customize or participate in the build flow.

Each operation should indicate through the methods of this interface which method can be used to set or retrieve the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` inputs and outputs.

## Summary

### Public functions  
  
---  
`[OutOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/OutOperationRequest)<FileTypeT>` |  `<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [wiredWith](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWith\(kotlin.Function1\))(  
taskOutput: (TaskT) -> [FileSystemLocationProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocationProperty.html)<FileTypeT>  
)` Sets the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` output method reference so the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` result can be retrieved after successful task execution.  
`[CombiningOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/CombiningOperationRequest)<FileTypeT>` |  `<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [wiredWith](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWith\(kotlin.Function1,kotlin.Function1\))(  
taskInput: (TaskT) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<FileTypeT>,  
taskOutput: (TaskT) -> [FileSystemLocationProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocationProperty.html)<FileTypeT>  
)` Sets the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` input and output methods references so the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` can retrieve the current versions of a `[Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)` when invoking `[taskInput](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWith\(kotlin.Function1,kotlin.Function1\))` while producing a new version of the same artifact type accessible through the `[taskOutput](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWith\(kotlin.Function1,kotlin.Function1\))` method after successful execution.  
`[InAndOutDirectoryOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/InAndOutDirectoryOperationRequest)<TaskT>` |  `[wiredWithDirectories](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWithDirectories\(kotlin.Function1,kotlin.Function1\))(  
taskInput: (TaskT) -> [DirectoryProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/DirectoryProperty.html),  
taskOutput: (TaskT) -> [DirectoryProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/DirectoryProperty.html)  
)` Sets the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` input and output methods references so the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` can retrieve the current version of the target `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)` when invoking `[taskInput](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWithDirectories\(kotlin.Function1,kotlin.Function1\))`.  
`[InAndOutFileOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/InAndOutFileOperationRequest)` |  `[wiredWithFiles](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWithFiles\(kotlin.Function1,kotlin.Function1\))(  
taskInput: (TaskT) -> [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html),  
taskOutput: (TaskT) -> [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)  
)` Sets the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` input and output methods references so the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` can retrieve the current version of the target `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)` when invoking `[taskInput](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWithFiles\(kotlin.Function1,kotlin.Function1\))`.  
`[MultipleArtifactTypeOutOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifactTypeOutOperationRequest)<FileTypeT>` |  `<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [wiredWithMultiple](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWithMultiple\(kotlin.Function1\))(  
taskInput: (TaskT) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<FileTypeT>  
)` Sets the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` input method reference so the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` can be retrieve the current version of the target `[MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact)` when invoking `[taskInput](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWithMultiple\(kotlin.Function1\))`.  
  
## Public functions

### wiredWith

Added in 4.2.0
    
    
    fun <FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [wiredWith](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWith\(kotlin.Function1\))(  
        taskOutput: (TaskT) -> [FileSystemLocationProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocationProperty.html)<FileTypeT>  
    ): [OutOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/OutOperationRequest)<FileTypeT>

Sets the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` output method reference so the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` result can be retrieved after successful task execution.

This method is useful when creating a new version, when appending to existing artifacts, or when access to the current version of an artifact isn't required.

Parameters  
---  
`taskOutput: (TaskT) -> [FileSystemLocationProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocationProperty.html)<FileTypeT>` |  The method reference to retrieve the task output after successful task execution.  
  
Returns  
---  
`[OutOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/OutOperationRequest)<FileTypeT>` |  The `[OutOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/OutOperationRequest)` to set the desired operation type and `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)` on which the operation applies.  
  
### wiredWith

Added in 4.2.0
    
    
    fun <FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [wiredWith](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWith\(kotlin.Function1,kotlin.Function1\))(  
        taskInput: (TaskT) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<FileTypeT>,  
        taskOutput: (TaskT) -> [FileSystemLocationProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocationProperty.html)<FileTypeT>  
    ): [CombiningOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/CombiningOperationRequest)<FileTypeT>

Sets the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` input and output methods references so the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` can retrieve the current versions of a `[Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)` when invoking `[taskInput](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWith\(kotlin.Function1,kotlin.Function1\))` while producing a new version of the same artifact type accessible through the `[taskOutput](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWith\(kotlin.Function1,kotlin.Function1\))` method after successful execution.

This method is useful when `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` is combining all elements of an `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)` into a single element.

Parameters  
---  
`taskInput: (TaskT) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<FileTypeT>` |  The method reference the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` will use to retrieve the current artifact versions during `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` execution (and only then).  
`taskOutput: (TaskT) -> [FileSystemLocationProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocationProperty.html)<FileTypeT>` |  The method reference to retrieve the task output after successful task execution.  
  
Returns  
---  
`[CombiningOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/CombiningOperationRequest)<FileTypeT>` |  The `[CombiningOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/CombiningOperationRequest)` to set the desired operation type and `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)` as well as the target `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)`.  
  
### wiredWithDirectories
    
    
    fun [wiredWithDirectories](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWithDirectories\(kotlin.Function1,kotlin.Function1\))(  
        taskInput: (TaskT) -> [DirectoryProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/DirectoryProperty.html),  
        taskOutput: (TaskT) -> [DirectoryProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/DirectoryProperty.html)  
    ): [InAndOutDirectoryOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/InAndOutDirectoryOperationRequest)<TaskT>

Sets the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` input and output methods references so the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` can retrieve the current version of the target `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)` when invoking `[taskInput](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWithDirectories\(kotlin.Function1,kotlin.Function1\))`. `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` will also produce a new version of the same artifact type accessible through the `[taskOutput](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWithDirectories\(kotlin.Function1,kotlin.Function1\))` method after successful execution.

This method is useful when `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` is transforming an `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)` from its current version to a new one and the `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)`'s `[Artifact.kind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#kind\(\))` is `[Artifact.DIRECTORY](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#DIRECTORY\(\))`

Parameters  
---  
`taskInput: (TaskT) -> [DirectoryProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/DirectoryProperty.html)` |  The method reference the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` will use to retrieve the current artifact version during `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` execution (and only then).  
`taskOutput: (TaskT) -> [DirectoryProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/DirectoryProperty.html)` |  The method reference to retrieve the task output after successful task execution.  
  
Returns  
---  
`[InAndOutDirectoryOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/InAndOutDirectoryOperationRequest)<TaskT>` |  The `[InAndOutDirectoryOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/InAndOutDirectoryOperationRequest)` to set the desired operation type as well as the target `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)`.  
  
### wiredWithFiles
    
    
    fun [wiredWithFiles](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWithFiles\(kotlin.Function1,kotlin.Function1\))(  
        taskInput: (TaskT) -> [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html),  
        taskOutput: (TaskT) -> [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)  
    ): [InAndOutFileOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/InAndOutFileOperationRequest)

Sets the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` input and output methods references so the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` can retrieve the current version of the target `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)` when invoking `[taskInput](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWithFiles\(kotlin.Function1,kotlin.Function1\))`. `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` will also produce a new version of the same artifact type accessible through the `[taskOutput](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWithFiles\(kotlin.Function1,kotlin.Function1\))` method after successful execution.

This method is useful when `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` is transforming an `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)` from its current version to a new one and the `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)`'s `[Artifact.kind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#kind\(\))` is `[Artifact.FILE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#FILE\(\))`

Parameters  
---  
`taskInput: (TaskT) -> [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)` |  The method reference the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` will use to retrieve the current artifact version during `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` execution (and only then).  
`taskOutput: (TaskT) -> [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)` |  The method reference to retrieve the task output after successful task execution.  
  
Returns  
---  
`[InAndOutFileOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/InAndOutFileOperationRequest)` |  The `[OutOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/OutOperationRequest)` to set the desired operation type and `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)` as well as the target `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)`.  
  
### wiredWithMultiple

Added in 8.3.1
    
    
    fun <FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [wiredWithMultiple](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWithMultiple\(kotlin.Function1\))(  
        taskInput: (TaskT) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<FileTypeT>  
    ): [MultipleArtifactTypeOutOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifactTypeOutOperationRequest)<FileTypeT>

Sets the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` input method reference so the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` can be retrieve the current version of the target `[MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact)` when invoking `[taskInput](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation#wiredWithMultiple\(kotlin.Function1\))`.

Parameters  
---  
`taskInput: (TaskT) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<FileTypeT>` |  The method reference the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` will use to retrieve the current artifact version during `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/TaskBasedOperation)` execution (and only then).  
  
Returns  
---  
`[MultipleArtifactTypeOutOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifactTypeOutOperationRequest)<FileTypeT>` |  the `[MultipleArtifactTypeOutOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifactTypeOutOperationRequest)` to set the desired operation type and the target `[MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact)`  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
