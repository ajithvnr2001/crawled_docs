---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ContentType
title: QualifiedContent.ContentType \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:36:41.562104+00:00
---

# QualifiedContent.ContentType  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ContentType

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# QualifiedContent.ContentType

[View Source](https://cs.android.com/search?q=file:com/android/build/api/transform/QualifiedContent.java+class:com.android.build.api.transform.QualifiedContent.ContentType)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    interface [QualifiedContent.ContentType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ContentType)

Known direct subclasses 

[QualifiedContent.DefaultContentType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType)

`[QualifiedContent.DefaultContentType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType)` |  The type of of the content.  
---|---  
  
* * *

A content type that is requested through the transform API.

## Summary

### Public functions  
  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[getValue](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ContentType#getValue\(\))()` A unique value for a content type.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  `[name](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ContentType#name\(\))()` Content type name, readable by humans.  
  
## Public functions

### getValue

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getValue](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ContentType#getValue\(\))(): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

A unique value for a content type.

### name

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [name](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ContentType#name\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!

Content type name, readable by humans.

Returns  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  the string content type name  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
