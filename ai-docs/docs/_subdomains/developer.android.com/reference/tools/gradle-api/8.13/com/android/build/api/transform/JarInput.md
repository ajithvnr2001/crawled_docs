---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/JarInput/
title: JarInput \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:36:36.676566+00:00
---

# JarInput  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/JarInput/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# JarInput

[View Source](https://cs.android.com/search?q=file:com/android/build/api/transform/JarInput.java+class:com.android.build.api.transform.JarInput)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    interface [JarInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/JarInput) : [QualifiedContent](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent)

* * *

**This interface is deprecated.**  


A `[QualifiedContent](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent)` of type jar. 

This means the `[getFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent#getFile\(\))` is the jar file containing the content. 

This also contains the incremental state of the jar file, if the transform is in incremental mode through `[getStatus](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/JarInput#getStatus\(\))`. 

For a transform to run in incremental mode: 

  * `[isIncremental](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Transform#isIncremental\(\))` must return `true`
  * The parameter isIncremental of `[transform](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Transform#transform\(com.android.build.api.transform.Context,java.util.Collection<com.android.build.api.transform.TransformInput>,java.util.Collection<com.android.build.api.transform.TransformInput>,com.android.build.api.transform.TransformOutputProvider,boolean\))` must be `true`.

If the transform is not in incremental mode, `[getStatus](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/JarInput#getStatus\(\))` always returns `[NOTCHANGED](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status#NOTCHANGED)`. 

## Summary

### Public functions  
  
---  
`[Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)!` |  `[getStatus](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/JarInput#getStatus\(\))()`  
  
### Inherited functions  
  
---  
From [com.android.build.api.transform.QualifiedContent](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent) | `([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[QualifiedContent.ContentType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ContentType)!>!` |  `[getContentTypes](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent#getContentTypes\(\))()` Returns the type of content that the stream represents.  
---|---  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!` |  `[getFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent#getFile\(\))()` Returns he location of the content.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  `[getName](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent#getName\(\))()` Returns the name of the content.  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!>!` |  `[getScopes](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent#getScopes\(\))()` Returns the scope of the content.  
  
## Public functions

### getStatus

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getStatus](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/JarInput#getStatus\(\))(): [Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)!

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
