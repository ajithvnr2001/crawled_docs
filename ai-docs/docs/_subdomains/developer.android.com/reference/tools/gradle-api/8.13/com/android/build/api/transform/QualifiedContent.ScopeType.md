---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ScopeType
title: QualifiedContent.ScopeType \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:36:44.030962+00:00
---

# QualifiedContent.ScopeType  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ScopeType

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# QualifiedContent.ScopeType

[View Source](https://cs.android.com/search?q=file:com/android/build/api/transform/QualifiedContent.java+class:com.android.build.api.transform.QualifiedContent.ScopeType)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    interface [QualifiedContent.ScopeType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ScopeType)

Known direct subclasses 

[QualifiedContent.Scope](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope)

`[QualifiedContent.Scope](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope)` |  The scope of the content.  
---|---  
  
* * *

Definition of a scope.

## Summary

### Public functions  
  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[getValue](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ScopeType#getValue\(\))()` A scope binary flag that will be used to encode directory names.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  `[name](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ScopeType#name\(\))()` Scope name, readable by humans.  
  
## Public functions

### getValue

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getValue](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ScopeType#getValue\(\))(): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

A scope binary flag that will be used to encode directory names. Must be unique.

Returns  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  a scope binary flag.  
  
### name

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [name](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ScopeType#name\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!

Scope name, readable by humans.

Returns  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  a scope name.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
