---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest/
title: OutOperationRequest \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:47:20.079725+00:00
---

# OutOperationRequest  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# OutOperationRequest

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/OperationRequests.kt+class:com.android.build.api.artifact.OutOperationRequest)

Added in 4.2.0
    
    
    interface [OutOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest)<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)>

* * *

Operations performed by a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` with a single `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` or `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` output.

`[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` is not consuming existing version of the target `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/SingleArtifact)`.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<ArtifactTypeT : [Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)<FileTypeT> & [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Appendable)> [toAppendTo](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#toAppendTo\(com.android.build.api.artifact.Artifact.Multiple\))(  
type: ArtifactTypeT  
)` Initiates an append request to a `[Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)` artifact type.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
<ArtifactTypeT : [Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)<FileTypeT> & [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Appendable) & [Artifact.WithQualifiers](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.WithQualifiers)> [toAppendTo](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#toAppendTo\(com.android.build.api.artifact.Artifact.Multiple,kotlin.collections.Map\))(  
type: ArtifactTypeT,  
qualifiers: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>  
)` Initiates an append request to a `[Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)` artifact type that is also a `[Artifact.WithQualifiers](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.WithQualifiers)`.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<ArtifactTypeT : [Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Single)<FileTypeT> & [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Replaceable)> [toCreate](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#toCreate\(com.android.build.api.artifact.Artifact.Single\))(  
type: ArtifactTypeT  
)` Initiates a creation request for a single `[Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Replaceable)` artifact type.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<ArtifactTypeT : [Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Single)<FileTypeT>> [toListenTo](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#toListenTo\(com.android.build.api.artifact.Artifact.Single\))(  
type: ArtifactTypeT  
)` Initiates a reactive request where the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` used in the `[Artifacts.use](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifacts#use\(org.gradle.api.tasks.TaskProvider\))` method will be executed once the final version of the `[type](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#toListenTo\(com.android.build.api.artifact.Artifact.Single\))` artifact has been produced.  
`[OutOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest)<FileTypeT>` |  `[withName](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#withName\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Sets the output file or directory name for the new artifact.  
  
## Public functions

### toAppendTo

Added in 7.0.0
    
    
    fun <ArtifactTypeT : [Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)<FileTypeT> & [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Appendable)> [toAppendTo](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#toAppendTo\(com.android.build.api.artifact.Artifact.Multiple\))(  
        type: ArtifactTypeT  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Initiates an append request to a `[Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)` artifact type.

Parameters  
---  
`type: ArtifactTypeT` |  The `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact)` of `[FileTypeT](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest)` identifying the artifact to append to. The artifact type must be `[Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)` and `[Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Appendable)`. As an example, let's take a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` that outputs a `[org.gradle.api.file.RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)`:
    
    
        abstract class MyTask: DefaultTask() {  
             @get:OutputFile abstract val outputFile: RegularFileProperty  
      
             @TaskAction fun taskAction() {  
                 ... outputFile.get().asFile.write( ... ) ...  
             }  
        }

and an ArtifactType defined as follows:
    
    
        sealed class ArtifactType<T: FileSystemLocation>(val kind: ArtifactKind) {  
             object MULTIPLE_FILE_ARTIFACT:  
                     ArtifactType<RegularFile>(FILE), Multiple, Appendable  
        }

You can then register the above task as a Provider of `[org.gradle.api.file.RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` for that artifact type:
    
    
        val taskProvider= projects.tasks.register(MyTask::class.java, "appendTask")  
        artifacts.use(taskProvider)  
         .wiredWith(MyTask::outputFile)  
         .toAppendTo(ArtifactType.MULTIPLE_FILE_ARTIFACT)  
  
### toAppendTo

Added in 9.4.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun <ArtifactTypeT : [Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)<FileTypeT> & [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Appendable) & [Artifact.WithQualifiers](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.WithQualifiers)> [toAppendTo](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#toAppendTo\(com.android.build.api.artifact.Artifact.Multiple,kotlin.collections.Map\))(  
        type: ArtifactTypeT,  
        qualifiers: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Initiates an append request to a `[Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)` artifact type that is also a `[Artifact.WithQualifiers](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.WithQualifiers)`.

Parameters  
---  
`type: ArtifactTypeT` |  The `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact)` of `[FileTypeT](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest)` identifying the artifact to append to.  
`qualifiers: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  the `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact)` attributes as a Map that uniquely identifies the instance in the set of artifacts for this `[type](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#toAppendTo\(com.android.build.api.artifact.Artifact.Multiple,kotlin.collections.Map\))`. The artifact type must be `[Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)`, `[Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Appendable)` and `[Artifact.WithQualifiers](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.WithQualifiers)` As an example, let's take a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` that outputs a `[org.gradle.api.file.RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)`:
    
    
        abstract class MyTask: DefaultTask() {  
             @get:OutputFile abstract val outputFile: RegularFileProperty  
      
             @TaskAction fun taskAction() {  
                 ... outputFile.get().asFile.write( ... ) ...  
             }  
        }

and an ArtifactType defined as follows :
    
    
        sealed class ArtifactType<T: FileSystemLocation>(  
             val kind: ArtifactKind  
             val qualifiers: List<String>  
        ): MultipleArtifactType {  
             object MULTIPLE_FILE_ARTIFACT:  
                     ArtifactType<RegularFile>(  
                         FILE,  
                         listOf("ATTR_KEY_ONE", ATTR_KEY_TWO"),  
                         ), Appendable, WithQualifiers  
        }

You can then register the above task as a Provider of `[org.gradle.api.file.RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` for that artifact type:
    
    
        val taskProvider= projects.tasks.register(MyTask::class.java, "appendTask")  
        artifacts.use(taskProvider)  
         .wiredWith(MyTask::outputFile)  
         .toAppendTo(ArtifactType.MULTIPLE_FILE_ARTIFACT,  
             mapOf("ATTR_KEY_ONE" to "valueOne, "ATTR_KEY_TWO" to "valueTwo")  
  
### toCreate

Added in 7.0.0
    
    
    fun <ArtifactTypeT : [Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Single)<FileTypeT> & [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Replaceable)> [toCreate](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#toCreate\(com.android.build.api.artifact.Artifact.Single\))(  
        type: ArtifactTypeT  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Initiates a creation request for a single `[Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Replaceable)` artifact type.

Parameters  
---  
`type: ArtifactTypeT` |  The `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact)` of `[FileTypeT](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest)` identifying the artifact to replace. The artifact type must be `[Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Replaceable)` A creation request does not care about the existing producer, since it replaces the existing producer. Therefore, the existing producer task will not execute (unless it produces other outputs). Please note that when such replace requests are made, the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` will replace initial AGP providers. You cannot replace the `[Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)` artifact type; therefore, you must instead combine it using the `[TaskBasedOperation.wiredWith](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/TaskBasedOperation#wiredWith\(kotlin.Function1\))` API. For example, let's take a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` that outputs a `[org.gradle.api.file.RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)`:
    
    
        abstract class MyTask: DefaultTask() {  
             @get:OutputFile abstract val outputFile: RegularFileProperty  
      
             @TaskAction fun taskAction() {  
                 ... write outputFile ...  
             }  
        }

A `[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/SingleArtifact)` is defined as follows:
    
    
        sealed class ArtifactType<T: FileSystemLocation>(val kind: ArtifactKind) {  
             object SINGLE_FILE_ARTIFACT:  
                     ArtifactType<RegularFile>(FILE), Replaceable  
        }

You can register a transform to the collection of `[org.gradle.api.file.RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)`:
    
    
        val taskProvider= projects.tasks.register(MyTask::class.java, "replaceTask")  
        artifacts.use(taskProvider)  
         .wiredWith(MyTask::outputFile)  
         .toCreate(ArtifactType.SINGLE_FILE_ARTIFACT)  
  
### toListenTo

Added in 8.3.1
    
    
    fun <ArtifactTypeT : [Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Single)<FileTypeT>> [toListenTo](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#toListenTo\(com.android.build.api.artifact.Artifact.Single\))(  
        type: ArtifactTypeT  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Initiates a reactive request where the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` used in the `[Artifacts.use](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifacts#use\(org.gradle.api.tasks.TaskProvider\))` method will be executed once the final version of the `[type](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#toListenTo\(com.android.build.api.artifact.Artifact.Single\))` artifact has been produced.

The final version artifact will be injected in the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)`.

Remember that an artifact is not always produced, for instance, an artifact related to minification will not be produced unless minification is turned on.

When an artifact is not produced in the current build flow, the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` will NOT be invoked.

For example, let's take a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` that wants to listen to the merged manifest file production :
    
    
            abstract class MyTask: DefaultTask() {  
                 @get:InputFile abstract val mergedManifestFile: RegularFileProperty  
      
                 @TaskAction fun taskAction() {  
                     ... verify that manifest is correct ...  
                 }  
            }  
      
        You can register the Task that consumes the manifest file as a [org.gradle.api.file.RegularFile]:  
      
        ```kotlin  
      
        val taskProvider= projects.tasks.register(MyTask::class.java, "verifyManifestTask") artifacts.use(taskProvider)  
        .wiredWith(MyTask::mergedManifestFile) .toListenTo(SingleArtifact.MERGED_MANIFEST)

`[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` will be registered as a finalizer task for the final producer of the `[type](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#toListenTo\(com.android.build.api.artifact.Artifact.Single\))` artifact using Gradle's `[Task.finalizedBy](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html#finalizedBy-kotlin.Array\[kotlin.Any\]-)` API.

Parameters  
---  
`type: ArtifactTypeT` |  the `[Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Single)` artifact identifier.  
  
### withName

Added in 8.4.0
    
    
    fun [withName](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#withName\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [OutOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest)<FileTypeT>

Sets the output file or directory name for the new artifact.

This name will only be used when `[toAppendTo](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#toAppendTo\(com.android.build.api.artifact.Artifact.Multiple\))` or `[toCreate](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#toCreate\(com.android.build.api.artifact.Artifact.Single\))` is invoked. Although you can use this method on `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)`, it will most likely not influence how the files contained in the resulting `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` are packaged in the APK or Bundle. This method is usually only useful for `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)`

Some `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact)` have a `[Artifact.name](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact#name\(\))` which cannot be changed. When invoking `[toAppendTo](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#toAppendTo\(com.android.build.api.artifact.Artifact.Multiple\))` or `[toCreate](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest#toCreate\(com.android.build.api.artifact.Artifact.Single\))` after this method will throw an exception if trying to set such a file or directory name when the target's `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact#name\(\))` is not null.

Parameters  
---  
`name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  file or directory name  
  
Returns  
---  
`[OutOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/OutOperationRequest)<FileTypeT>` |  itself  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
