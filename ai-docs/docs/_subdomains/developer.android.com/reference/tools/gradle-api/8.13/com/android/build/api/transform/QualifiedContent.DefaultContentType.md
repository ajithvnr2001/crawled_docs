---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType
title: QualifiedContent.DefaultContentType \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:37:02.435693+00:00
---

# QualifiedContent.DefaultContentType  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# QualifiedContent.DefaultContentType

[View Source](https://cs.android.com/search?q=file:com/android/build/api/transform/QualifiedContent.java+class:com.android.build.api.transform.QualifiedContent.DefaultContentType)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    enum [QualifiedContent.DefaultContentType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType) : [QualifiedContent.ContentType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ContentType)

* * *

The type of of the content.

## Summary

### Enum Values  
  
---  
`[CLASSES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType#CLASSES)` |  The content is compiled Java code.  
`[RESOURCES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType#RESOURCES)` |  The content is standard Java resources.  
  
### Public functions  
  
---  
`java-static [QualifiedContent.DefaultContentType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType)!` |  `[valueOf](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType#valueOf\(java.lang.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` Returns the enum constant of this type with the specified name.  
`java-static [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[QualifiedContent.DefaultContentType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType)!>!` |  `[values](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType#values\(\))()` Returns an array containing the constants of this enum type, in the order they're declared.  
  
### Public properties  
  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[value](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType#value\(\))`  
  
### Inherited functions  
  
---  
From [com.android.build.api.transform.QualifiedContent.ContentType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ContentType) | `abstract [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  `[name](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ContentType#name\(\))()` Content type name, readable by humans.  
---|---  
  
## Enum Values

### CLASSES
    
    
    val [QualifiedContent.DefaultContentType.CLASSES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType#CLASSES): [QualifiedContent.DefaultContentType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType)

The content is compiled Java code. This can be in a Jar file or in a folder. If in a folder, it is expected to in sub-folders matching package names.

### RESOURCES
    
    
    val [QualifiedContent.DefaultContentType.RESOURCES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType#RESOURCES): [QualifiedContent.DefaultContentType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType)

The content is standard Java resources.

## Public functions

### valueOf

Added in 4.2.0
    
    
    java-static fun [valueOf](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType#valueOf\(java.lang.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!): [QualifiedContent.DefaultContentType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType)!

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

Returns  
---  
`[QualifiedContent.DefaultContentType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType)!` |  the enum constant with the specified name  
  
Throws  
---  
`[java.lang.IllegalArgumentException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/IllegalArgumentException.html)` |  if this enum type has no constant with the specified name  
  
### values

Added in 4.2.0
    
    
    java-static fun [values](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType#values\(\))(): [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[QualifiedContent.DefaultContentType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType)!>!

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

Returns  
---  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[QualifiedContent.DefaultContentType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType)!>!` |  an array containing the constants of this enum type, in the order they're declared  
  
## Public properties

### value
    
    
    val [value](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.DefaultContentType#value\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
