---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/DirectoryInput/
title: DirectoryInput \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:36:34.367327+00:00
---

# DirectoryInput  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/DirectoryInput/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DirectoryInput

[View Source](https://cs.android.com/search?q=file:com/android/build/api/transform/DirectoryInput.java+class:com.android.build.api.transform.DirectoryInput)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    interface [DirectoryInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/DirectoryInput) : [QualifiedContent](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent)

* * *

**This interface is deprecated.**  


A `[QualifiedContent](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent)` of type directory. 

This means the `[getFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent#getFile\(\))` is the root directory containing the content. 

This also contains incremental data if the transform is in incremental mode through `[getChangedFiles](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/DirectoryInput#getChangedFiles\(\))`. 

For a transform to run in incremental mode: 

  * `[isIncremental](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Transform#isIncremental\(\))` must return `true`
  * The parameter isIncremental of `[transform](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Transform#transform\(com.android.build.api.transform.Context,java.util.Collection<com.android.build.api.transform.TransformInput>,java.util.Collection<com.android.build.api.transform.TransformInput>,com.android.build.api.transform.TransformOutputProvider,boolean\))` must be `true`.

If the transform is not in incremental mode, `[getChangedFiles](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/DirectoryInput#getChangedFiles\(\))` will not contain any information (it will **not** contain the list of all the files with state `[NOTCHANGED](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status#NOTCHANGED)`.) 

When a root level directory is removed, and incremental mode is on, the instance will receive a `[DirectoryInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/DirectoryInput)` instance for the removed folder, but `[getFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent#getFile\(\))` will return a directory that does not exist. In this case, the transform should prcess this as a removed input.

## Summary

### Public functions  
  
---  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html))[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!, [Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)!>!` |  `[getChangedFiles](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/DirectoryInput#getChangedFiles\(\))()` Returns the changed files.  
  
### Inherited functions  
  
---  
From [com.android.build.api.transform.QualifiedContent](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent) | `([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[QualifiedContent.ContentType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ContentType)!>!` |  `[getContentTypes](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent#getContentTypes\(\))()` Returns the type of content that the stream represents.  
---|---  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!` |  `[getFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent#getFile\(\))()` Returns he location of the content.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  `[getName](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent#getName\(\))()` Returns the name of the content.  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!>!` |  `[getScopes](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent#getScopes\(\))()` Returns the scope of the content.  
  
## Public functions

### getChangedFiles

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getChangedFiles](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/DirectoryInput#getChangedFiles\(\))(): ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html))[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!, [Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)!>!

Returns the changed files. This is only valid if the transform is in incremental mode.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
