---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent/
title: QualifiedContent \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:05:10.246393+00:00
---

# QualifiedContent  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# QualifiedContent

[View Source](https://cs.android.com/search?q=file:com/android/build/api/transform/QualifiedContent.java+class:com.android.build.api.transform.QualifiedContent)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    interface [QualifiedContent](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent)

Known direct subclasses 

[DirectoryInput](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/DirectoryInput), [JarInput](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/JarInput)

`[DirectoryInput](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/DirectoryInput)` |  **This interface is deprecated.**  
---|---  
`[JarInput](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/JarInput)` |  **This interface is deprecated.**  
  
* * *

**This interface is deprecated.**  


Represent content qualified with one or more `[ContentType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.ContentType)` and one or more `[Scope](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.Scope)`.

## Summary

### Nested types  
  
---  
`interface [QualifiedContent.ContentType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.ContentType)` A content type that is requested through the transform API.  
`enum [QualifiedContent.DefaultContentType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.DefaultContentType) : [QualifiedContent.ContentType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.ContentType)` The type of of the content.  
`enum [QualifiedContent.Scope](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.Scope) : [QualifiedContent.ScopeType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.ScopeType)` The scope of the content.  
`interface [QualifiedContent.ScopeType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.ScopeType)` Definition of a scope.  
  
### Public functions  
  
---  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[QualifiedContent.ContentType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.ContentType)!>!` |  `[getContentTypes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent#getContentTypes\(\))()` Returns the type of content that the stream represents.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!` |  `[getFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent#getFile\(\))()` Returns he location of the content.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  `[getName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent#getName\(\))()` Returns the name of the content.  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!>!` |  `[getScopes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent#getScopes\(\))()` Returns the scope of the content.  
  
## Public functions

### getContentTypes

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getContentTypes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent#getContentTypes\(\))(): ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[QualifiedContent.ContentType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.ContentType)!>!

Returns the type of content that the stream represents. 

Even though this may return only `[RESOURCES](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.DefaultContentType#RESOURCES)` or `[CLASSES](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.DefaultContentType#CLASSES)`, the actual content (the folder or the jar) may contain files representing other content types. This is because the transform mechanism avoids duplicating files around to remove unwanted types for performance. 

For each input, transforms should always take care to read and process only the files associated with the types returned by this method.

Returns  
---  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[QualifiedContent.ContentType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.ContentType)!>!` |  a set of one or more types, never null nor empty.  
  
### getFile

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent#getFile\(\))(): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!

Returns he location of the content.

Returns  
---  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!` |  the content location.  
  
### getName

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent#getName\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!

Returns the name of the content. Can be used to differentiate different content using the same scope. This is not reliably usable at every stage of the transformations, but can be used for logging for instance.

Returns  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  the name  
  
### getScopes

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getScopes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent#getScopes\(\))(): ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!>!

Returns the scope of the content.

Returns  
---  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!>!` |  a set of one or more scopes, never null nor empty.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
