---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories/
title: SourceDirectories \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:02:07.840583+00:00
---

# SourceDirectories  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# SourceDirectories

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/SourceDirectories.kt+class:com.android.build.api.variant.SourceDirectories)

Added in 7.2.0
    
    
    interface [SourceDirectories](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html)

Known direct subclasses 

[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat), [SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Layered)

`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)` |  Represents all the source folders for a source type.  
---|---  
`[SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Layered)` |  Represent a collection of directories that have overlay properties to each other.  
  
* * *

Defines all common behaviors to sources access in AGP.

`[SourceDirectories](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories)` and subtypes are available for the variant instances through the `[Sources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources)` interface. They are also used in `[TestSuite](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuite)` through the `[TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet)` interface.

Adding directories to instances returned by the `[Sources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources)` will alter the underlying component. Similarly, adding directories to instances returned by the `[TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet)` will change the underlying test suite. However, since a test suite can apply to multiple variants through the `[com.android.build.api.dsl.AgpTestSuite.targetVariants](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AgpTestSuite#targetVariants\(\))` dsl element, modifying the test suite affects all variants that the test suite targets.

Adding directories is always added to the "Variant" overlay and will therefore carry the highest possible priority among all directories for the source type.

## Summary

### Nested types  
  
---  
`interface [SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat) : [SourceDirectories](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories)` Represents all the source folders for a source type.  
`interface [SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Layered) : [SourceDirectories](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories)` Represent a collection of directories that have overlay properties to each other.  
  
### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<TASK : [Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)> [addGeneratedSourceDirectory](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories#addGeneratedSourceDirectory\(org.gradle.api.tasks.TaskProvider,kotlin.Function1\))(  
taskProvider: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<TASK>,  
wiredWith: (TASK) -> [DirectoryProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/DirectoryProperty.html)  
)` Add the output of a custom task to the list of source directories.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[addStaticSourceDirectory](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories#addStaticSourceDirectory\(kotlin.String\))(srcDir: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Add a source directory with sources already present to the variant.  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
## Public functions

### addGeneratedSourceDirectory
    
    
    fun <TASK : [Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)> [addGeneratedSourceDirectory](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories#addGeneratedSourceDirectory\(org.gradle.api.tasks.TaskProvider,kotlin.Function1\))(  
        taskProvider: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<TASK>,  
        wiredWith: (TASK) -> [DirectoryProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/DirectoryProperty.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Add the output of a custom task to the list of source directories.

The `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` is the output of a Task `[TASK](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories#addGeneratedSourceDirectory\(org.gradle.api.tasks.TaskProvider,kotlin.Function1\))` that has been registered using the Gradle's Task manager.

The `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` is added last to the receiver's list of source directories. In case there is merging for the source type, the `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` will have the highest priority.

Parameters  
---  
`taskProvider: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<TASK>` |  the `[TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)` returned by Gradle's Task manager when registering the Task of type `[TASK](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories#addGeneratedSourceDirectory\(org.gradle.api.tasks.TaskProvider,kotlin.Function1\))`.  
`wiredWith: (TASK) -> [DirectoryProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/DirectoryProperty.html)` |  the method reference returning the `[TASK](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories#addGeneratedSourceDirectory\(org.gradle.api.tasks.TaskProvider,kotlin.Function1\))` task's output to use as a source directory. The generated source directory location is automatically determined by the Android Gradle Plugin and will be set using the `[DirectoryProperty.convention](https://docs.gradle.org/current/javadoc/org/gradle/api/file/DirectoryProperty.html#convention-org.gradle.api.file.Directory-)` method. Therefore, if you need to set the directory to a different location, use `[DirectoryProperty.set](https://docs.gradle.org/current/javadoc/org/gradle/api/file/DirectoryProperty.html#set-java.io.File-)`.  
  
### addStaticSourceDirectory

Added in 7.3.0
    
    
    fun [addStaticSourceDirectory](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories#addStaticSourceDirectory\(kotlin.String\))(srcDir: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Add a source directory with sources already present to the variant.

The directory will be added last in the receiver's list of source folders. In case there is merging for the source type, `[srcDir](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories#addStaticSourceDirectory\(kotlin.String\))` will be the folder with the highest priority.

Do not use `[addStaticSourceDirectory](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories#addStaticSourceDirectory\(kotlin.String\))` to add sources that are generated by a task, instead use `[addGeneratedSourceDirectory](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories#addGeneratedSourceDirectory\(org.gradle.api.tasks.TaskProvider,kotlin.Function1\))`

Parameters  
---  
`srcDir: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the source directory path, that will be resolved using the `[Directory.dir](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html#dir-kotlin.String-)` API relative to the Gradle project directory.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
