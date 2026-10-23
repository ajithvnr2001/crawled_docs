---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/InAndOutFileOperationRequest/
title: InAndOutFileOperationRequest \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:23:37.853781+00:00
---

# InAndOutFileOperationRequest  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/InAndOutFileOperationRequest/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# InAndOutFileOperationRequest

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/OperationRequests.kt+class:com.android.build.api.artifact.InAndOutFileOperationRequest)

Added in 4.2.0
    
    
    interface [InAndOutFileOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/InAndOutFileOperationRequest)

* * *

Operations performed by a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` with a single `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` output.

`[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` is consuming existing version of the target `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)` and producing a new version.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<ArtifactTypeT : [Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Single)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)> & [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Transformable)> [toTransform](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/InAndOutFileOperationRequest#toTransform\(com.android.build.api.artifact.Artifact.Single\))(  
type: ArtifactTypeT  
)` Initiates a transform request to a single `[Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Transformable)` artifact type.  
`[InAndOutFileOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/InAndOutFileOperationRequest)` |  `[withName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/InAndOutFileOperationRequest#withName\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Sets the output file name for the transformed artifact.  
  
## Public functions

### toTransform

Added in 7.0.0
    
    
    fun <ArtifactTypeT : [Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Single)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)> & [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Transformable)> [toTransform](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/InAndOutFileOperationRequest#toTransform\(com.android.build.api.artifact.Artifact.Single\))(  
        type: ArtifactTypeT  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Initiates a transform request to a single `[Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Transformable)` artifact type.

Parameters  
---  
`type: ArtifactTypeT` |  The `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact)` identifying the artifact to transform. The `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact)`'s `[Artifact.kind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#kind\(\))` must be `[Artifact.FILE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#FILE\(\))`. The artifact type must be `[Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Single)` and `[Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Transformable)`. As an example, let's take a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` transforming an input `[org.gradle.api.file.RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` into an output:
    
    
        abstract class MyTask: DefaultTask() {  
             @get:InputFile abstract val inputFile: RegularFileProperty  
             @get:OutputFile abstract val outputFile: RegularFileProperty  
      
             @TaskAction fun taskAction() {  
                 ... read inputFile and write outputFile ...  
             }  
        }

An ArtifactType defined as follows:
    
    
        sealed class ArtifactType<T: FileSystemLocation>(val kind: ArtifactKind) {  
             object SINGLE_FILE_ARTIFACT:  
                     ArtifactType<RegularFile>(FILE), Single, Transformable  
        }

You can register a transform to the collection of `[org.gradle.api.file.RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)`.
    
    
        val taskProvider= projects.tasks.register(MyTask::class.java, "transformTask")  
        artifacts.use(taskProvider)  
         .wiredWithFiles(  
             MyTask::inputFile,  
             MyTask::outputFile)  
         .toTransform(ArtifactType.SINGLE_FILE_ARTIFACT)  
  
### withName

Added in 8.4.0
    
    
    fun [withName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/InAndOutFileOperationRequest#withName\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [InAndOutFileOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/InAndOutFileOperationRequest)

Sets the output file name for the transformed artifact.

Parameters  
---  
`name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  file name in the output folder.  
  
Returns  
---  
`[InAndOutFileOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/InAndOutFileOperationRequest)` |  itself  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
