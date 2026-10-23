---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope
title: ScopedArtifacts.Scope \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:22:03.335395+00:00
---

# ScopedArtifacts.Scope  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ScopedArtifacts.Scope

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/ScopedArtifacts.kt+class:com.android.build.api.variant.ScopedArtifacts.Scope)

Added in 7.4.0
    
    
    enum [ScopedArtifacts.Scope](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)  
|  ↳ | [com.android.build.api.variant.ScopedArtifacts.Scope](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope)  
  
* * *

Defines possible scopes.

## Summary

### Enum Values  
  
---  
`[ALL](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope#ALL)` |  Full scope, including project scope, imported projects and all external dependencies.  
`[PROJECT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope#PROJECT)` |  Project scope, not including imported projects nor external dependencies.  
  
### Public functions  
  
---  
`[ScopedArtifacts.Scope](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope)` |  `[valueOf](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Returns the enum constant of this type with the specified name.  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[ScopedArtifacts.Scope](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope)>` |  `[values](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope#values\(\))()` Returns an array containing the constants of this enum type, in the order they're declared.  
  
## Enum Values

### ALL
    
    
    val [ScopedArtifacts.Scope.ALL](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope#ALL): [ScopedArtifacts.Scope](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope)

Full scope, including project scope, imported projects and all external dependencies.

### PROJECT
    
    
    val [ScopedArtifacts.Scope.PROJECT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope#PROJECT): [ScopedArtifacts.Scope](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope)

Project scope, not including imported projects nor external dependencies.

## Public functions

### valueOf

Added in 7.4.0
    
    
    fun [valueOf](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [ScopedArtifacts.Scope](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope)

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

Throws  
---  
`kotlin.IllegalArgumentException` |  if this enum type has no constant with the specified name  
  
### values

Added in 7.4.0
    
    
    fun [values](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope#values\(\))(): [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[ScopedArtifacts.Scope](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScopedArtifacts.Scope)>

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
