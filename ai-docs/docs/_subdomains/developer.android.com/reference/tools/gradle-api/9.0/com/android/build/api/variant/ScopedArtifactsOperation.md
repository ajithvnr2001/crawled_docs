---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation/
title: ScopedArtifactsOperation \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:26:03.015563+00:00
---

# ScopedArtifactsOperation  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ScopedArtifactsOperation

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/ScopedArtifactsOperation.kt+class:com.android.build.api.variant.ScopedArtifactsOperation)

Added in 7.4.0
    
    
    interface [ScopedArtifactsOperation](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation)<T : [Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)>

* * *

Defines all possible operations on a `[ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact)` artifact type.

Depending on the scope, inputs may contain a mix of `[org.gradle.api.file.FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)`, `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` or `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` so all `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` consuming the current value of the artifact must provide two input fields that will contain the list of `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` and `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)`.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<ArtifactT : [ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact) & [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact.Appendable)> [toAppend](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toAppend\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1\))(  
to: ArtifactT,  
with: (T) -> [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)>  
)` Append a new `[FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)` (basically, either a `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` or a `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)`) to the artifact type referenced by `[to](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toAppend\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1\))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[toGet](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toGet\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1,kotlin.Function1\))(  
type: [ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact),  
inputJars: (T) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>,  
inputDirectories: (T) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)>  
)` Set the final version of the `[type](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toGet\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1,kotlin.Function1\))` artifact to the input fields of the `[Task](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation)`.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<ArtifactT : [ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact) & [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact.Replaceable)> [toReplace](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toReplace\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1\))(  
type: ArtifactT,  
into: (T) -> [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)  
)` Replace the current version of the `[type](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toReplace\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1\))` artifact with a new version.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<ArtifactT : [ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact) & [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact.Transformable)> [toTransform](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toTransform\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1,kotlin.Function1,kotlin.Function1\))(  
type: ArtifactT,  
inputJars: (T) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>,  
inputDirectories: (T) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)>,  
into: (T) -> [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)  
)` Transform the current version of the `[type](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toTransform\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1,kotlin.Function1,kotlin.Function1\))` artifact into a new version.  
  
## Public functions

### toAppend

Added in 8.7.0
    
    
    fun <ArtifactT : [ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact) & [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact.Appendable)> [toAppend](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toAppend\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1\))(  
        to: ArtifactT,  
        with: (T) -> [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)>  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Append a new `[FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)` (basically, either a `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` or a `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)`) to the artifact type referenced by `[to](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toAppend\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1\))`

Parameters  
---  
`to: ArtifactT` |  the `[ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact)` to add the `[with](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toAppend\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1\))` to.  
`with: (T) -> [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)>` |  lambda that returns the `[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)` used by the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` to save the appended element. The `[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)` value will be automatically set by the Android Gradle Plugin and its location should not be considered part of the API and can change in the future.  
  
### toGet

Added in 7.4.0
    
    
    fun [toGet](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toGet\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1,kotlin.Function1\))(  
        type: [ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact),  
        inputJars: (T) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>,  
        inputDirectories: (T) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)>  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Set the final version of the `[type](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toGet\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1,kotlin.Function1\))` artifact to the input fields of the `[Task](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation)`. Those input fields should be annotated with `[org.gradle.api.tasks.InputFiles](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/InputFiles.html)` for Gradle to property set the task dependency.

Parameters  
---  
`type: [ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact)` |  the `[ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact)` to obtain the final value of.  
`inputJars: (T) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>` |  lambda that returns a `[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)` or `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` that will be used to set all incoming files for this artifact type.  
`inputDirectories: (T) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)>` |  lambda that returns a `[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)` or `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` that will be used to set all incoming directories for this artifact type.  
  
### toReplace
    
    
    fun <ArtifactT : [ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact) & [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact.Replaceable)> [toReplace](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toReplace\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1\))(  
        type: ArtifactT,  
        into: (T) -> [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Replace the current version of the `[type](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toReplace\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1\))` artifact with a new version.

The main difference with the `[toTransform](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toTransform\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1,kotlin.Function1,kotlin.Function1\))` method is that the previously set of producers of this `[ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact)` will not be invoked.

The order in which the replace `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)`s are applied is directly set by the order of this method call. Last one wins and none of the previously set append/transform/replace registered `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)`s will be invoked since this `[Task](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation)` replace the final version.

Parameters  
---  
`type: ArtifactT` |  the `[ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact)` to replace.  
`into: (T) -> [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)` |  lambda that returns the `[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)` used by the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` to save the replaced element. The `[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)` value will be automatically set by the Android Gradle Plugin and its location should not be considered part of the API and can change in the future.  
  
### toTransform
    
    
    fun <ArtifactT : [ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact) & [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact.Transformable)> [toTransform](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toTransform\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1,kotlin.Function1,kotlin.Function1\))(  
        type: ArtifactT,  
        inputJars: (T) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>,  
        inputDirectories: (T) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)>,  
        into: (T) -> [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Transform the current version of the `[type](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ScopedArtifactsOperation#toTransform\(com.android.build.api.artifact.ScopedArtifact,kotlin.Function1,kotlin.Function1,kotlin.Function1\))` artifact into a new version. The order in which the transforms are applied is directly set by the order of this method call. First come, first served, last one provides the final version of the artifacts.

IMPORTANT: `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` will transform many inputs into a single output. That means task must have merging logic as jars contain similar files and folders (like META-INF). Merging logic depends on transformation nature.

Parameters  
---  
`type: ArtifactT` |  the `[ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact)` to transform.  
`inputJars: (T) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>` |  lambda that returns a `[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)` or `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` that will be used to set all incoming files for this artifact type.  
`inputDirectories: (T) -> [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)>` |  lambda that returns a `[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)` or `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` that will be used to set all incoming directories for this artifact type.  
`into: (T) -> [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)` |  lambda that returns the `[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)` used by the `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` to save the transformed element. The `[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)` value will be automatically set by the Android Gradle Plugin and its location should not be considered part of the API and can change in the future.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
