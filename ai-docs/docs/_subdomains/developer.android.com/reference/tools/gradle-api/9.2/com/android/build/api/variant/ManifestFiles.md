---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ManifestFiles/
title: ManifestFiles \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:54:54.575178+00:00
---

# ManifestFiles  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ManifestFiles/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ManifestFiles

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/ManifestFiles.kt+class:com.android.build.api.variant.ManifestFiles)

Added in 8.3.1
    
    
    interface [ManifestFiles](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ManifestFiles) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html)

* * *

Defines a set of manifests for particular variant. Adding manifest is always added static and generated manifests carry the highest possible priority across all manifests.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<TASK : [Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)> [addGeneratedManifestFile](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ManifestFiles#addGeneratedManifestFile\(org.gradle.api.tasks.TaskProvider,kotlin.Function1\))(  
taskProvider: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<TASK>,  
wiredWith: (TASK) -> [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)  
)` Add the output of a custom task to the list of manifests.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[addStaticManifestFile](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ManifestFiles#addStaticManifestFile\(kotlin.String\))(relativeFilePath: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Add existing manifest file to the variant.  
  
### Public properties  
  
---  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>>` |  `[all](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ManifestFiles#all\(\))` Get all registered manifests as a `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)` of `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)`.  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
## Public functions

### addGeneratedManifestFile
    
    
    fun <TASK : [Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)> [addGeneratedManifestFile](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ManifestFiles#addGeneratedManifestFile\(org.gradle.api.tasks.TaskProvider,kotlin.Function1\))(  
        taskProvider: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<TASK>,  
        wiredWith: (TASK) -> [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Add the output of a custom task to the list of manifests.

The `[RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)` is the output of a Task `[TASK](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ManifestFiles#addGeneratedManifestFile\(org.gradle.api.tasks.TaskProvider,kotlin.Function1\))` that has been registered using the Gradle's Task manager.

The manifest is added last to the variant's list and has the highest priority.

Parameters  
---  
`taskProvider: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<TASK>` |  the `[TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)` returned by Gradle's Task manager when registering the Task of type `[TASK](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ManifestFiles#addGeneratedManifestFile\(org.gradle.api.tasks.TaskProvider,kotlin.Function1\))`.  
`wiredWith: (TASK) -> [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)` |  the method reference returning the `[TASK](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ManifestFiles#addGeneratedManifestFile\(org.gradle.api.tasks.TaskProvider,kotlin.Function1\))` task's output to use as a source directory. The generated manifest location is automatically determined by the Android Gradle Plugin  
  
### addStaticManifestFile

Added in 8.3.1
    
    
    fun [addStaticManifestFile](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ManifestFiles#addStaticManifestFile\(kotlin.String\))(relativeFilePath: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Add existing manifest file to the variant.

The file will be added last in the list of manifest files for the variant. As long as there is a manifest merging process, added manifest will overlay others and become the one with the highest priority.

Do not use `[addStaticManifestFile](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ManifestFiles#addStaticManifestFile\(kotlin.String\))` to add sources that are generated by a task, instead use `[addGeneratedManifestFile](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ManifestFiles#addGeneratedManifestFile\(org.gradle.api.tasks.TaskProvider,kotlin.Function1\))`

Parameters  
---  
`relativeFilePath: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the manifest file path, that will be resolved using the `[Directory.file](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html#file-kotlin.String-)` API relative to the Gradle project directory.  
  
## Public properties

### all

Added in 8.3.1
    
    
    val [all](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ManifestFiles#all\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>>

Get all registered manifests as a `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)` of `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)`.

The outer `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)` represents the priority of manifests respective to each other, meaning that elements first in the list overrides elements last in the list.

The returned `[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)` can be used directly in a `[org.gradle.api.tasks.InputFiles](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/InputFiles.html)` annotated property of a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
