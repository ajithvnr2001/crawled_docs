---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status/
title: Status \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:37:07.580329+00:00
---

# Status  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Status

[View Source](https://cs.android.com/search?q=file:com/android/build/api/transform/Status.java+class:com.android.build.api.transform.Status)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    enum [Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)

* * *

**This enum is deprecated.**  


The file changed status for incremental execution.

## Summary

### Enum Values  
  
---  
`[ADDED](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status#ADDED)` |  The file was added since the last build.  
`[CHANGED](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status#CHANGED)` |  The file was modified since the last build.  
`[NOTCHANGED](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status#NOTCHANGED)` |  The file was not changed since the last build.  
`[REMOVED](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status#REMOVED)` |  The file was removed since the last build.  
  
### Public functions  
  
---  
`java-static [Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)!` |  `[valueOf](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status#valueOf\(java.lang.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` Returns the enum constant of this type with the specified name.  
`java-static [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)!>!` |  `[values](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status#values\(\))()` Returns an array containing the constants of this enum type, in the order they're declared.  
  
## Enum Values

### ADDED
    
    
    val [Status.ADDED](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status#ADDED): [Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)

The file was added since the last build.

### CHANGED
    
    
    val [Status.CHANGED](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status#CHANGED): [Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)

The file was modified since the last build.

### NOTCHANGED
    
    
    val [Status.NOTCHANGED](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status#NOTCHANGED): [Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)

The file was not changed since the last build.

### REMOVED
    
    
    val [Status.REMOVED](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status#REMOVED): [Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)

The file was removed since the last build.

## Public functions

### valueOf

Added in 4.2.0
    
    
    java-static fun [valueOf](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status#valueOf\(java.lang.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!): [Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)!

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

Returns  
---  
`[Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)!` |  the enum constant with the specified name  
  
Throws  
---  
`[java.lang.IllegalArgumentException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/IllegalArgumentException.html)` |  if this enum type has no constant with the specified name  
  
### values

Added in 4.2.0
    
    
    java-static fun [values](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status#values\(\))(): [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)!>!

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

Returns  
---  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)!>!` |  an array containing the constants of this enum type, in the order they're declared  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
