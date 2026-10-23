---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format/
title: Format \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:05:32.005481+00:00
---

# Format  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Format

[View Source](https://cs.android.com/search?q=file:com/android/build/api/transform/Format.java+class:com.android.build.api.transform.Format)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    enum [Format](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format)

* * *

**This enum is deprecated.**  


The format in which content is stored.

## Summary

### Enum Values  
  
---  
`[DIRECTORY](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format#DIRECTORY)` |  The content is a directory.  
`[JAR](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format#JAR)` |  The content is a jar.  
  
### Public functions  
  
---  
`java-static [Format](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format)!` |  `[valueOf](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format#valueOf\(java.lang.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` Returns the enum constant of this type with the specified name.  
`java-static [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Format](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format)!>!` |  `[values](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format#values\(\))()` Returns an array containing the constants of this enum type, in the order they're declared.  
  
## Enum Values

### DIRECTORY
    
    
    val [Format.DIRECTORY](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format#DIRECTORY): [Format](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format)

The content is a directory. 

This means that in the case of java class files, the files should be in directories matching their package names, directly under the root directory.

### JAR
    
    
    val [Format.JAR](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format#JAR): [Format](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format)

The content is a jar.

## Public functions

### valueOf

Added in 4.2.0
    
    
    java-static fun [valueOf](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format#valueOf\(java.lang.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!): [Format](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format)!

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

Returns  
---  
`[Format](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format)!` |  the enum constant with the specified name  
  
Throws  
---  
`[java.lang.IllegalArgumentException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/IllegalArgumentException.html)` |  if this enum type has no constant with the specified name  
  
### values

Added in 4.2.0
    
    
    java-static fun [values](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format#values\(\))(): [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Format](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format)!>!

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

Returns  
---  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Format](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Format)!>!` |  an array containing the constants of this enum type, in the order they're declared  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
