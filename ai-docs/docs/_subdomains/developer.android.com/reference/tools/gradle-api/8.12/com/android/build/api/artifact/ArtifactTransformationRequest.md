---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/artifact/ArtifactTransformationRequest/
title: ArtifactTransformationRequest \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:47:31.369622+00:00
---

# ArtifactTransformationRequest  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/artifact/ArtifactTransformationRequest/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ArtifactTransformationRequest

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/ArtifactTransformationRequest.kt+class:com.android.build.api.artifact.ArtifactTransformationRequest)

Added in 4.2.0
    
    
    interface [ArtifactTransformationRequest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/artifact/ArtifactTransformationRequest)<TaskT : [Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)>

* * *

When a `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` contains more than one artifact (for example, consider `[SingleArtifact.APK](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/artifact/SingleArtifact.APK)` with multiple APKs for different screen densities), this object will abstract away having to deal with `[BuiltArtifacts](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/BuiltArtifacts)` and manually load and write the metadata files.

Instead, users can focus on writing transformation code that transform one file at at time into a newer version. It will also provide the ability to use Gradle's `[WorkQueue](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkQueue.html)` to multi-thread the transformations.

Here is an example of a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` copying (unchanged) the APK files from one location to another.
    
    
    // parameter interface to pass to work items.  
    interface WorkItemParameters: WorkParameters, Serializable {  
       val inputApkFile: RegularFileProperty  
       val outputApkFile: RegularFileProperty  
    }
    
    
    // work item that copies one file at a time.  
    abstract class WorkItem @Inject constructor(  
         private val workItemParameters: WorkItemParameters  
    ): WorkAction<WorkItemParameters> {  
      
       override fun execute() {  
         workItemParameters.inputApkFile.asFile.get().copyTo(  
         workItemParameters.outputApkFile.get().asFile)  
       }  
    }

And the task that wires things together:
    
    
    abstract class CopyApksTask @Inject constructor(private val workers: WorkerExecutor): DefaultTask() {  
      
    @get:InputFiles  
    abstract val apkFolder: DirectoryProperty  
      
    @get:OutputDirectory  
    abstract val outFolder: DirectoryProperty  
      
    @get:Internal  
    abstract val transformationRequest: Property<ArtifactTransformationRequest<CopyApksTask>>  
      
    @TaskAction  
    fun taskAction() {  
     transformationRequest.get().submit(  
        this,  
        workers.noIsolation(),  
        WorkItem::class.java) {  
        builtArtifact: BuiltArtifact,  
        outputLocation: Directory,  
        param: WorkItemParameters ->  
          val inputFile = File(builtArtifact.outputFile)  
          param.inputApkFile.set(inputFile)  
          param.outputApkFile.set(File(outputLocation.asFile, inputFile.name))  
          param.outputApkFile.get().asFile  
        }  
      }  
    }

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[submit](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/artifact/ArtifactTransformationRequest#submit\(org.gradle.api.Task,kotlin.Function1\))(task: TaskT, transformer: (input: [BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/BuiltArtifact)) -> [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html))` Submit a lambda to process each input `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/BuiltArtifact)` object synchronously.  
`[Supplier](https://developer.android.com/reference/tools/gradle-api/8.12/java/util/function/Supplier)<[BuiltArtifacts](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/BuiltArtifacts)>` |  `<ParamT : [WorkParameters](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkParameters.html)> [submit](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/artifact/ArtifactTransformationRequest#submit\(org.gradle.api.Task,org.gradle.workers.WorkQueue,java.lang.Class,kotlin.Function3\))(  
task: TaskT,  
workQueue: [WorkQueue](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkQueue.html),  
actionType: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[WorkAction](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkAction.html)<ParamT>>,  
parameterConfigurator: (builtArtifact: [BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/BuiltArtifact), outputLocation: [Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html), parameters) -> [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)  
)` Submit a `org.gradle.workers` style of `[WorkAction](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkAction.html)` to process each input `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/BuiltArtifact)`.  
  
## Public functions

### submit
    
    
    fun [submit](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/artifact/ArtifactTransformationRequest#submit\(org.gradle.api.Task,kotlin.Function1\))(task: TaskT, transformer: (input: [BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/BuiltArtifact)) -> [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Submit a lambda to process each input `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/BuiltArtifact)` object synchronously.

### submit
    
    
    fun <ParamT : [WorkParameters](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkParameters.html)> [submit](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/artifact/ArtifactTransformationRequest#submit\(org.gradle.api.Task,org.gradle.workers.WorkQueue,java.lang.Class,kotlin.Function3\))(  
        task: TaskT,  
        workQueue: [WorkQueue](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkQueue.html),  
        actionType: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[WorkAction](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkAction.html)<ParamT>>,  
        parameterConfigurator: (builtArtifact: [BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/BuiltArtifact), outputLocation: [Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html), parameters) -> [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)  
    ): [Supplier](https://developer.android.com/reference/tools/gradle-api/8.12/java/util/function/Supplier)<[BuiltArtifacts](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/BuiltArtifacts)>

Submit a `org.gradle.workers` style of `[WorkAction](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkAction.html)` to process each input `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/BuiltArtifact)`.

Parameters  
---  
`task: TaskT` |  The Task initiating the `[WorkQueue](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkQueue.html)` requests.  
`workQueue: [WorkQueue](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkQueue.html)` |  The Gradle `[WorkQueue](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkQueue.html)` instance to use to spawn worker items with.  
`actionType: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[WorkAction](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkAction.html)<ParamT>>` |  The type of the `[WorkAction](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkAction.html)` subclass that process that input `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/BuiltArtifact)`.  
`parameterConfigurator: (builtArtifact: [BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/BuiltArtifact), outputLocation: [Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html), parameters) -> [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)` |  The lambda to configure instances of parameterType for each `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/BuiltArtifact)`.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
