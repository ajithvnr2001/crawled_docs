---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/InAndOutDirectoryOperationRequest/
title: InAndOutDirectoryOperationRequest \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:28:42.984496+00:00
---

# InAndOutDirectoryOperationRequest  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/InAndOutDirectoryOperationRequest/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# InAndOutDirectoryOperationRequest

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/OperationRequests.kt+class:com.android.build.api.artifact.InAndOutDirectoryOperationRequest)

Added in 4.2.0
    
    
    interface [InAndOutDirectoryOperationRequest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/InAndOutDirectoryOperationRequest)<TaskT : [Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)>

* * *

Operations performed by a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` with a single `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` output.

`[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` is consuming existing version of the target `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact)` and producing a new version.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<ArtifactTypeT : [Artifact.Single](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Single)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)> & [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Transformable)> [toTransform](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/InAndOutDirectoryOperationRequest#toTransform\(com.android.build.api.artifact.Artifact.Single\))(  
type: ArtifactTypeT  
)` Initiates a transform request to a single `[Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Transformable)` artifact type.  
`[ArtifactTransformationRequest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/ArtifactTransformationRequest)<TaskT>` |  `<ArtifactTypeT : [Artifact.Single](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Single)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)> & [Artifact.ContainsMany](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.ContainsMany) & [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Transformable)> [toTransformMany](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/InAndOutDirectoryOperationRequest#toTransformMany\(com.android.build.api.artifact.Artifact.Single\))(  
type: ArtifactTypeT  
)` Initiates a transform request to a single `[Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Transformable)` artifact type that can contain more than one artifact.  
  
## Public functions

### toTransform

Added in 7.0.0
    
    
    fun <ArtifactTypeT : [Artifact.Single](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Single)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)> & [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Transformable)> [toTransform](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/InAndOutDirectoryOperationRequest#toTransform\(com.android.build.api.artifact.Artifact.Single\))(  
        type: ArtifactTypeT  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Initiates a transform request to a single `[Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Transformable)` artifact type.

Parameters  
---  
`type: ArtifactTypeT` |  The `[Artifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact)` identifying the artifact to transform. The `[Artifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact)`'s `[Artifact.kind](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact#kind\(\))` must be `[Artifact.DIRECTORY](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact#DIRECTORY\(\))` The artifact type must be `[Artifact.Single](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Single)` and `[Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Transformable)`. Let's take a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` transforming an input `[org.gradle.api.file.Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` into an output:
    
    
        abstract class MyTask: DefaultTask() {  
             @get:InputFiles abstract val inputDir: DirectoryProperty  
             @get:OutputDirectory abstract val outputDir: DirectoryProperty  
      
             @TaskAction fun taskAction() {  
                 ... read inputFile and write outputFile ...  
             }  
        }

An ArtifactType defined as follows:
    
    
        sealed class ArtifactType<T: FileSystemLocation>(val kind: ArtifactKind) {  
             object SINGLE_DIR_ARTIFACT:  
                     ArtifactType<Directory>(DIRECTORY), Single, Transformable  
        }

You can register a transform to the collection of `[org.gradle.api.file.RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)`.
    
    
        val taskProvider= projects.tasks.register(MyTask::class.java, "transformTask")  
        artifacts.use(taskProvider)  
         .wiredWithDirectories(  
             MyTask::inputDir,  
             MyTask::outputDir)  
         .toTransform(ArtifactType.SINGLE_DIR_ARTIFACT)  
  
### toTransformMany

Added in 8.4.0
    
    
    fun <ArtifactTypeT : [Artifact.Single](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Single)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)> & [Artifact.ContainsMany](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.ContainsMany) & [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Transformable)> [toTransformMany](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/InAndOutDirectoryOperationRequest#toTransformMany\(com.android.build.api.artifact.Artifact.Single\))(  
        type: ArtifactTypeT  
    ): [ArtifactTransformationRequest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/ArtifactTransformationRequest)<TaskT>

Initiates a transform request to a single `[Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Transformable)` artifact type that can contain more than one artifact.

Parameters  
---  
`type: ArtifactTypeT` |  The `[Artifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact)` of the `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` identifying the artifact to transform.  
  
Returns  
---  
`[ArtifactTransformationRequest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/ArtifactTransformationRequest)<TaskT>` |  `[ArtifactTransformationRequest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/ArtifactTransformationRequest)` that will allow processing of individual artifacts located in the input directory. The artifact type must be `[Artifact.Single](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Single)`, `[Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Transformable)`, and `[Artifact.ContainsMany](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.ContainsMany)`. For example, let's take a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` to transform a list of `[org.gradle.api.file.RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` as inputs into a single output:
    
    
        abstract class MyTask: DefaultTask() {  
             @get:InputFiles abstract val inputFolder: DirectoryProperty  
             @get:OutputFile abstract val outputFolder: DirectoryProperty  
             @Internal abstract Property<ArtifactTransformationRequest<MyTask>> getTransformationRequest()  
      
             @TaskAction fun taskAction() {  
                transformationRequest.get().submit(  
                     ... submit a work item for each input file ...  
                )  
             }  
        }

You then register the task as follows:
    
    
        val taskProvider= projects.tasks.register(MyTask::class.java, "combineTask")  
        val transformationRequest = artifacts.use(taskProvider)  
          .wiredWithDirectories(  
             MyTask::inputFolder,  
             MyTask::outputFolder)  
          .toTransformMany(SingleArtifact.APK)  
        taskProvider.configure { task ->  
             task.getTransformationRequest().set(transformationRequest)  
        }  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
