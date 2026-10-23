---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifactTypeOutOperationRequest/
title: MultipleArtifactTypeOutOperationRequest \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:58:18.709426+00:00
---

# MultipleArtifactTypeOutOperationRequest  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifactTypeOutOperationRequest/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# MultipleArtifactTypeOutOperationRequest

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/OperationRequests.kt+class:com.android.build.api.artifact.MultipleArtifactTypeOutOperationRequest)

Added in 8.3.1
    
    
    interface [MultipleArtifactTypeOutOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifactTypeOutOperationRequest)<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)>

* * *

Read-only Operations performed by a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` with a multiple `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` or `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` output.

All APIs will use a `[Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Multiple)` as a target type and must use a `[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)` of `[FileTypeT](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifactTypeOutOperationRequest)` to retrieve the artifacts.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<ArtifactTypeT : [Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Multiple)<FileTypeT>> [toListenTo](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifactTypeOutOperationRequest#toListenTo\(com.android.build.api.artifact.Artifact.Multiple\))(  
type: ArtifactTypeT  
)` Initiates a reactive request where the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` used in the `[Artifacts.use](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifacts#use\(org.gradle.api.tasks.TaskProvider\))` method will be executed once the final version of the `[type](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifactTypeOutOperationRequest#toListenTo\(com.android.build.api.artifact.Artifact.Multiple\))` artifact has been produced.  
  
## Public functions

### toListenTo

Added in 8.3.1
    
    
    fun <ArtifactTypeT : [Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Multiple)<FileTypeT>> [toListenTo](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifactTypeOutOperationRequest#toListenTo\(com.android.build.api.artifact.Artifact.Multiple\))(  
        type: ArtifactTypeT  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Initiates a reactive request where the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` used in the `[Artifacts.use](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifacts#use\(org.gradle.api.tasks.TaskProvider\))` method will be executed once the final version of the `[type](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifactTypeOutOperationRequest#toListenTo\(com.android.build.api.artifact.Artifact.Multiple\))` artifact has been produced.

The final version artifact will be injected in the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)`.

Remember that an artifact is not always produced, for instance, an artifact related to minification will not be produced unless minification is turned on.

When an artifact is not produced in the current build flow, the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` will NOT be invoked.

For example, let's take a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` that wants to listen to the merged manifest file production :
    
    
            abstract class MyTask: DefaultTask() {  
                 @get:InputFiles abstract val proguardFiles: ListProperty<RegularFile>  
      
                 @TaskAction fun taskAction() {  
                     ... verify that those proguard files are correct ...  
                 }  
            }  
      
        You can register the Task that consumes the proguard files as a [ListProperty] of  
        [org.gradle.api.file.RegularFile]:  
      
        ```kotlin  
      
        val taskProvider= projects.tasks.register(MyTask::class.java, "verifyKeepProguardTask") artifacts.use(taskProvider)  
        .wiredWithMultiple(MyTask::proguardFiles) .toListenTo(MultipleArtifact.MULTIDEX_KEEP_PROGUARD)

`[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` will be registered as a finalizer task for the final producer of the `[type](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifactTypeOutOperationRequest#toListenTo\(com.android.build.api.artifact.Artifact.Multiple\))` artifact using Gradle's `[Task.finalizedBy](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html#finalizedBy-kotlin.Array\[kotlin.Any\]-)` API.

Parameters  
---  
`type: ArtifactTypeT` |  the `[Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Multiple)` artifact identifier.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-05 UTC."],[],[]] 
