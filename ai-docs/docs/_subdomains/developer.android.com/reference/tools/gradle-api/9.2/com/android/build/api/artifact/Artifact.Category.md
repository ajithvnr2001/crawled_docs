---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category
title: Artifact.Category \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:41:59.482612+00:00
---

# Artifact.Category  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Artifact.Category

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/Artifact.kt+class:com.android.build.api.artifact.Artifact.Category)

Added in 4.2.0
    
    
    enum [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)  
|  ↳ | [com.android.build.api.artifact.Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category)  
  
* * *

Defines the kind of artifact type. this will be used to determine the output file location for instance.

## Summary

### Enum Values  
  
---  
`[GENERATED](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category#GENERATED)` |   
`[INTERMEDIATES](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category#INTERMEDIATES)` |   
`[OUTPUTS](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category#OUTPUTS)` |   
`[REPORTS](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category#REPORTS)` |   
`[SOURCES](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category#SOURCES)` |   
  
### Public functions  
  
---  
`[Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category)` |  `[valueOf](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Returns the enum constant of this type with the specified name.  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category)>` |  `[values](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category#values\(\))()` Returns an array containing the constants of this enum type, in the order they're declared.  
  
## Enum Values

### GENERATED
    
    
    val [Artifact.Category.GENERATED](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category#GENERATED): [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category)

### INTERMEDIATES
    
    
    val [Artifact.Category.INTERMEDIATES](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category#INTERMEDIATES): [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category)

### OUTPUTS
    
    
    val [Artifact.Category.OUTPUTS](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category#OUTPUTS): [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category)

### REPORTS
    
    
    val [Artifact.Category.REPORTS](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category#REPORTS): [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category)

### SOURCES
    
    
    val [Artifact.Category.SOURCES](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category#SOURCES): [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category)

## Public functions

### valueOf

Added in 4.2.0
    
    
    fun [valueOf](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category)

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

Throws  
---  
`kotlin.IllegalArgumentException` |  if this enum type has no constant with the specified name  
  
### values

Added in 4.2.0
    
    
    fun [values](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category#values\(\))(): [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category)>

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
