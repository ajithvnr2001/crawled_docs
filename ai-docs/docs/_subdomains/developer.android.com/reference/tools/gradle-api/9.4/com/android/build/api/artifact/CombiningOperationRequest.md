---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/CombiningOperationRequest/
title: CombiningOperationRequest \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:47:08.285083+00:00
---

# CombiningOperationRequest  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/CombiningOperationRequest/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# CombiningOperationRequest

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/OperationRequests.kt+class:com.android.build.api.artifact.CombiningOperationRequest)

Added in 4.2.0
    
    
    interface [CombiningOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/CombiningOperationRequest)<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)>

* * *

Operations performed by a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` with a single `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` or `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` output.

`[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` is consuming existing version of the target `[MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact)` and producing a new version.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<ArtifactTypeT : [Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)<FileTypeT> & [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Transformable)> [toTransform](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/CombiningOperationRequest#toTransform\(com.android.build.api.artifact.Artifact.Multiple\))(  
type: ArtifactTypeT  
)` Initiates a transform request to a multiple `[Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Transformable)` artifact type.  
  
## Public functions

### toTransform

Added in 7.0.0
    
    
    fun <ArtifactTypeT : [Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)<FileTypeT> & [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Transformable)> [toTransform](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/CombiningOperationRequest#toTransform\(com.android.build.api.artifact.Artifact.Multiple\))(  
        type: ArtifactTypeT  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Initiates a transform request to a multiple `[Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Transformable)` artifact type.

Parameters  
---  
`type: ArtifactTypeT` |  The `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact)` of `[FileTypeT](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/CombiningOperationRequest)` identifying the artifact to transform. The artifact type must be `[Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)` and `[Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Transformable)`. The implementation of the task must combine all the inputs into a single output. Chained transforms will get a `[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)` containing the single output from the upstream transform. If some append calls are made on the same artifact type, the first transform will always get the complete list of artifacts irrespective of the timing of the calls. In the following example, let's take a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` to transform a list of `[org.gradle.api.file.RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` as inputs into a single output:
    
    
        abstract class MyTask: DefaultTask() {  
             @get:InputFiles abstract val inputFiles: ListProperty<RegularFile>  
             @get:OutputFile abstract val outputFile: RegularFileProperty  
      
             @TaskAction fun taskAction() {  
                 ... read all inputFiles and write outputFile ...  
             }  
        }

A `[MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/MultipleArtifact)` is defined as follows:
    
    
        sealed class ArtifactType<T: FileSystemLocation>(val kind: ArtifactKind) {  
             object MULTIPLE_FILE_ARTIFACT:  
                     ArtifactType<RegularFile>(FILE), Multiple, Transformable  
        }

You then register the task as follows:
    
    
        val taskProvider= projects.tasks.register(MyTask::class.java, "combineTask")  
        artifacts.use(taskProvider)  
         .wiredWith(  
             MyTask::inputFiles,  
             MyTask::outputFile)  
         .toTransform(ArtifactType.MULTIPLE_FILE_ARTIFACT)  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
