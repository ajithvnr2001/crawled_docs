---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts/
title: BuiltArtifacts \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:17:02.706852+00:00
---

# BuiltArtifacts  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BuiltArtifacts

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/BuiltArtifacts.kt+class:com.android.build.api.variant.BuiltArtifacts)

Added in 4.2.0
    
    
    interface [BuiltArtifacts](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts)

* * *

Represents a `[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)` of `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)` produced by a `[org.gradle.api.Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)`.

Tasks in Android Gradle Plugin can produce more than one file in the output folder so any `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact)` with a `[Artifact.kind](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact#kind\(\))` of type `[com.android.build.api.artifact.ArtifactKind.DIRECTORY](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/ArtifactKind.DIRECTORY)` can actually contain several produced `[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)`. For instance, when dealing with multi-apk, there will be several manifest files or APKs produced by the Android Gradle Plugin.

Each produced file can be identified with unique metadata like the list of filters and/or version code or version name. This instance will allow producer and consumer `[org.gradle.api.Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)`s to easily match produced files with this metadata without relying on name mangling or other custom solutions.

Simple use of this facility can look like :
    
    
    abstract class MyTask @inject constructor(val objectFactory: ObjectFactory): DefaultTask() {
        @get:InputDirectory
        abstract val input: DirectoryProperty
        @get:OutputDirectory
        abstract val output: DirectoryProperty
        @get:Internal
        abstract val artifactsLoader: Property
    
        @TaskAction
        fun taskAction() {
             val builtArtifacts= artifactsLoader.get().load(
                  objectFactory, input.get())
    
             TODO : TBD what will be surfaced here
    
             newBuiltArtifacts.save(output.get()))
        }
    }
    

This `[BuiltArtifacts](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts)` will abstract access to these produced files and provided some metadata associated with each file to be able to identify filters, version code or version name.

## Summary

### Nested types  
  
---  
`interface [BuiltArtifacts.TransformParams](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts.TransformParams) : [WorkParameters](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkParameters.html), [Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)` Specialized version of Gradle's `[WorkParameters](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkParameters.html)` so we can retrieve the output file generated when transforming an instance of `[BuiltArtifacts](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts)` into a new one.  
  
### Constants  
  
---  
`const [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[METADATA_FILE_VERSION](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts.Companion#METADATA_FILE_VERSION\(\)) = 3` Current version of the metadata file.  
  
### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[save](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts#save\(org.gradle.api.file.Directory\))(out: [Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html))` Saves the metadata associated with this instance into a folder.  
  
### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[applicationId](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts#applicationId\(\))` Returns the application ID for these `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)` instances.  
`[Artifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact)<*>` |  `[artifactType](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts#artifactType\(\))` Identifies the `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact)` for this `[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)` of `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)`, all `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)` are the same type of artifact.  
`[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)>` |  `[elements](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts#elements\(\))` Returns the `[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)` of `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[variantName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts#variantName\(\))` Identifies the variant name for these `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)`  
  
## Constants

### METADATA_FILE_VERSION

Added in 4.2.0
    
    
    const val [METADATA_FILE_VERSION](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts.Companion#METADATA_FILE_VERSION\(\)) = 3: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Current version of the metadata file.

## Public functions

### save

Added in 4.2.0
    
    
    fun [save](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts#save\(org.gradle.api.file.Directory\))(out: [Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Saves the metadata associated with this instance into a folder.

Parameters  
---  
`out: [Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` |  the `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` that can be used to save the metadata using a standard file name.  
  
## Public properties

### applicationId

Added in 4.2.0
    
    
    val [applicationId](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts#applicationId\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Returns the application ID for these `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)` instances.

Returns  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the application ID.  
  
### artifactType

Added in 4.2.0
    
    
    val [artifactType](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts#artifactType\(\)): [Artifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact)<*>

Identifies the `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact)` for this `[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)` of `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)`, all `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)` are the same type of artifact.

Returns  
---  
`[Artifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact)<*>` |  the `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact)` for all the `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)` instances.  
  
### elements

Added in 4.2.0
    
    
    val [elements](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts#elements\(\)): [Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)>

Returns the `[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)` of `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)`.

### variantName

Added in 4.2.0
    
    
    val [variantName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts#variantName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Identifies the variant name for these `[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
