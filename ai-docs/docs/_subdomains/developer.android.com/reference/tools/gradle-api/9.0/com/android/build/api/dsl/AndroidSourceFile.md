---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidSourceFile/
title: AndroidSourceFile \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:15:37.222309+00:00
---

# AndroidSourceFile  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidSourceFile/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AndroidSourceFile

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/AndroidSourceFile.kt+class:com.android.build.api.dsl.AndroidSourceFile)

Added in 4.2.0
    
    
    interface [AndroidSourceFile](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidSourceFile) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html)

* * *

An AndroidSourceFile represents a single file input for an Android project.

## Summary

### Public functions  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidSourceFile#getName\(\))()` A concise name for the source directory (typically used to identify it in a collection).  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[srcFile](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidSourceFile#srcFile\(kotlin.Any\))(srcPath: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Sets the location of the file.  
  
## Public functions

### getName
    
    
    fun [getName](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidSourceFile#getName\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

A concise name for the source directory (typically used to identify it in a collection).

### srcFile

Added in 4.2.0
    
    
    fun [srcFile](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidSourceFile#srcFile\(kotlin.Any\))(srcPath: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)

Sets the location of the file.

Parameters  
---  
`srcPath: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  The source directory. This is evaluated as `[org.gradle.api.Project.file](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html#file-kotlin.Any-)` This method has a return value for legacy reasons.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
