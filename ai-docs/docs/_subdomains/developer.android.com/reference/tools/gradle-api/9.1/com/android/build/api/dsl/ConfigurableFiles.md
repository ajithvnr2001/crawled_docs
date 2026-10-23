---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ConfigurableFiles/
title: ConfigurableFiles \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:02:00.465538+00:00
---

# ConfigurableFiles  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ConfigurableFiles/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ConfigurableFiles

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ConfigurableFiles.kt+class:com.android.build.api.dsl.ConfigurableFiles)

Added in 8.2.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [ConfigurableFiles](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ConfigurableFiles)

Known direct subclasses 

[ConsumerKeepRules](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ConsumerKeepRules), [LibraryKeepRules](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/LibraryKeepRules)

`[ConsumerKeepRules](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ConsumerKeepRules)` |   
---|---  
`[LibraryKeepRules](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/LibraryKeepRules)` |   
  
* * *

A container for a collection of files that has the capability to add a single existing file or a group of existing files to the collection

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[file](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ConfigurableFiles#file\(kotlin.Any\))(file: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[files](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ConfigurableFiles#files\(kotlin.Array\))(vararg files: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))`  
  
### Public properties  
  
---  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>` |  `[files](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ConfigurableFiles#files\(\))`  
  
## Public functions

### file

Added in 8.2.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [file](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ConfigurableFiles#file\(kotlin.Any\))(file: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### files

Added in 8.2.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [files](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ConfigurableFiles#files\(kotlin.Array\))(vararg files: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

## Public properties

### files

Added in 8.2.0
    
    
    val [files](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ConfigurableFiles#files\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-01-15 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-15 UTC."],[],[]] 
