---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/AndroidSourceDirectorySet/
title: AndroidSourceDirectorySet \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:53:44.756828+00:00
---

# AndroidSourceDirectorySet  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/AndroidSourceDirectorySet/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AndroidSourceDirectorySet

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/AndroidSourceDirectorySet.kt+class:com.android.build.api.dsl.AndroidSourceDirectorySet)

Added in 4.2.0
    
    
    interface [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/AndroidSourceDirectorySet) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html)

* * *

An AndroidSourceDirectorySet represents a set of directory inputs for an Android project.

## Summary

### Public functions  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/AndroidSourceDirectorySet#getName\(\))()` A concise name for the source directory (typically used to identify it in a collection).  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[setSrcDirs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/AndroidSourceDirectorySet#setSrcDirs\(kotlin.collections.Iterable\))(srcDirs: [Iterable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html)<*>)` Sets the source directories for this set.  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[srcDir](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/AndroidSourceDirectorySet#srcDir\(kotlin.Any\))(srcDir: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds the given source directory to this set.  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[srcDirs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/AndroidSourceDirectorySet#srcDirs\(kotlin.Array\))(vararg srcDirs: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Adds the given source directories to this set.  
  
### Public properties  
  
---  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[directories](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/AndroidSourceDirectorySet#directories\(\))` Allows to add source directories as path strings to this set.  
  
## Public functions

### getName
    
    
    fun [getName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/AndroidSourceDirectorySet#getName\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

A concise name for the source directory (typically used to identify it in a collection).

### setSrcDirs

Added in 4.2.0
    
    
    fun [setSrcDirs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/AndroidSourceDirectorySet#setSrcDirs\(kotlin.collections.Iterable\))(srcDirs: [Iterable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html)<*>): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)

Sets the source directories for this set.

Parameters  
---  
`srcDirs: [Iterable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html)<*>` |  The source directories. These are evaluated as for `[org.gradle.api.Project.files](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html#files-kotlin.Array\[kotlin.Any\]-)` This method has a return value for legacy reasons.  
  
### srcDir

Added in 4.2.0
    
    
    fun [srcDir](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/AndroidSourceDirectorySet#srcDir\(kotlin.Any\))(srcDir: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)

Adds the given source directory to this set.

Parameters  
---  
`srcDir: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  The source directory. This is evaluated as `[org.gradle.api.Project.file](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html#file-kotlin.Any-)` This method has a return value for legacy reasons.  
  
### srcDirs

Added in 4.2.0
    
    
    fun [srcDirs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/AndroidSourceDirectorySet#srcDirs\(kotlin.Array\))(vararg srcDirs: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)

Adds the given source directories to this set.

Parameters  
---  
`vararg srcDirs: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  The source directories. These are evaluated as `[org.gradle.api.Project.files](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html#files-kotlin.Array\[kotlin.Any\]-)` This method has a return value for legacy reasons.  
  
## Public properties

### directories

Added in 8.5.0
    
    
    val [directories](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/AndroidSourceDirectorySet#directories\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Allows to add source directories as path strings to this set. `Directories` provides `MutableSet` style access to all source directories that are added via set itself or variety of `srcDirs` methods.

Note that tasks or buildscript may add more directories, so you should not read this property and use Variant API instead.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
