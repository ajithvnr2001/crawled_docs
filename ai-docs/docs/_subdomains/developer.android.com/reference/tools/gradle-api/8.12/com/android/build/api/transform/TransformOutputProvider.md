---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformOutputProvider/
title: TransformOutputProvider \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:05:24.608696+00:00
---

# TransformOutputProvider  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformOutputProvider/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TransformOutputProvider

[View Source](https://cs.android.com/search?q=file:com/android/build/api/transform/TransformOutputProvider.java+class:com.android.build.api.transform.TransformOutputProvider)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    interface [TransformOutputProvider](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformOutputProvider)

* * *

**This interface is deprecated.**  


The output of a transform. 

There is no direct access to a location to write. Instead, Transforms can ask to get the location for given scopes, content-types and a format.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[deleteAll](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformOutputProvider#deleteAll\(\))()` Delete all content.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!` |  `[getContentLocation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformOutputProvider#getContentLocation\(java.lang.String,java.util.Set<com.android.build.api.transform.QualifiedContent.ContentType>,java.util.Set<?%20super%20com.android.build.api.transform.QualifiedContent.Scope>,com.android.build.api.transform.Format\))(  
name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!,  
types: ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[QualifiedContent.ContentType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.ContentType)!>!,  
scopes: ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!>!,  
format: [Format](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format)!  
)` **This function is deprecated.**  
  
## Public functions

### deleteAll

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [deleteAll](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformOutputProvider#deleteAll\(\))(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Delete all content. This is useful when running in non-incremental mode

Throws  
---  
`[java.io.IOException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/IOException.html)` |  if deleting the output failed.  
  
### getContentLocation
    
    
    fun [getContentLocation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformOutputProvider#getContentLocation\(java.lang.String,java.util.Set<com.android.build.api.transform.QualifiedContent.ContentType>,java.util.Set<?%20super%20com.android.build.api.transform.QualifiedContent.Scope>,com.android.build.api.transform.Format\))(  
        name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!,  
        types: ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[QualifiedContent.ContentType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.ContentType)!>!,  
        scopes: ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!>!,  
        format: [Format](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format)!  
    ): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!

**This function is deprecated.**  


Returns the location of content for a given set of Scopes, Content Types, and Format. 

If the format is `[DIRECTORY](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format#DIRECTORY)` then the result is the file location of the directory. If the format is `[JAR](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format#JAR)` then the result is a file representing the jar to create. 

Non of the directories or files are created by querying this method, and there is no checks regarding the existence of content in this location. 

In case of incremental processing of removed files, it is safe to query the method to get the location of the files to removed.

Parameters  
---  
`name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  a unique name for the content. For a given set of scopes/types/format it must be unique.  
`types: ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[QualifiedContent.ContentType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.ContentType)!>!` |  the content types associated with this content.  
`scopes: ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!>!` |  the scopes associated with this content.  
`format: [Format](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format)!` |  the format of the content.  
  
Returns  
---  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!` |  the location of the content.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
