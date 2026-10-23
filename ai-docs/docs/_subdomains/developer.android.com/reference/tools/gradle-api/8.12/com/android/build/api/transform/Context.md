---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Context/
title: Context \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:05:02.854874+00:00
---

# Context  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Context/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Context

[View Source](https://cs.android.com/search?q=file:com/android/build/api/transform/Context.java+class:com.android.build.api.transform.Context)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    interface [Context](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Context)

* * *

**This interface is deprecated.**  


Context for the transform. 

This gives access to a limited amount of context when the transform is run.

## Summary

### Public functions  
  
---  
`[LoggingManager](https://docs.gradle.org/current/javadoc/org/gradle/api/logging/LoggingManager.html)!` |  `[getLogging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Context#getLogging\(\))()` Returns the LoggingManager which can be used to control the logging level and standard output/error capture for this task.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  `[getPath](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Context#getPath\(\))()` Returns the path of the task, which is a fully qualified name for the task.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  `[getProjectName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Context#getProjectName\(\))()` Returns the project name containing the task.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!` |  `[getTemporaryDir](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Context#getTemporaryDir\(\))()` Returns a directory which this task can use to write temporary files to.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  `[getVariantName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Context#getVariantName\(\))()` Returns the name of the variant.  
`[WorkerExecutor](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkerExecutor.html)!` |  `[getWorkerExecutor](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Context#getWorkerExecutor\(\))()` Returns the `[org.gradle.workers.WorkerExecutor](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkerExecutor.html)` to enlist runnable pieces of work.  
  
## Public functions

### getLogging

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getLogging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Context#getLogging\(\))(): [LoggingManager](https://docs.gradle.org/current/javadoc/org/gradle/api/logging/LoggingManager.html)!

Returns the LoggingManager which can be used to control the logging level and standard output/error capture for this task. By default, System.out is redirected to the Gradle logging system at the QUIET log level, and System.err is redirected at the ERROR log level.

Returns  
---  
`[LoggingManager](https://docs.gradle.org/current/javadoc/org/gradle/api/logging/LoggingManager.html)!` |  the LoggingManager. Never returns null.  
  
### getPath

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getPath](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Context#getPath\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!

Returns the path of the task, which is a fully qualified name for the task. The path of a task is the path of its `Project` plus the name of the task, separated by `:`.

Returns  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  the path of the task, which is equal to the path of the project plus the name of the task.  
  
### getProjectName

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getProjectName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Context#getProjectName\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!

Returns the project name containing the task.

Returns  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  the `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html#getName--)`  
  
### getTemporaryDir

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getTemporaryDir](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Context#getTemporaryDir\(\))(): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!

Returns a directory which this task can use to write temporary files to. Each task instance is provided with a separate temporary directory. There are no guarantees that the contents of this directory will be kept beyond the execution of the task.

Returns  
---  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!` |  The directory. Never returns null. The directory will already exist.  
  
### getVariantName

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getVariantName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Context#getVariantName\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!

Returns the name of the variant.

Returns  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  the name of the variant.  
  
### getWorkerExecutor

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getWorkerExecutor](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Context#getWorkerExecutor\(\))(): [WorkerExecutor](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkerExecutor.html)!

Returns the `[org.gradle.workers.WorkerExecutor](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkerExecutor.html)` to enlist runnable pieces of work.

Returns  
---  
`[WorkerExecutor](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkerExecutor.html)!` |  a task level shared instance.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
