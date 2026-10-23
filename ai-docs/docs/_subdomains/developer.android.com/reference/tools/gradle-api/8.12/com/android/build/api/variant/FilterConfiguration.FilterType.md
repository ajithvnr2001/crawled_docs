---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType
title: FilterConfiguration.FilterType \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:10:27.083531+00:00
---

# FilterConfiguration.FilterType  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# FilterConfiguration.FilterType

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/FilterConfiguration.kt+class:com.android.build.api.variant.FilterConfiguration.FilterType)

Added in 4.2.0
    
    
    enum [FilterConfiguration.FilterType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)  
|  ↳ | [com.android.build.api.variant.FilterConfiguration.FilterType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType)  
  
* * *

Split dimension type

## Summary

### Enum Values  
  
---  
`[ABI](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType#ABI)` |   
`[DENSITY](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType#DENSITY)` |   
`[LANGUAGE](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType#LANGUAGE)` |   
  
### Public functions  
  
---  
`[FilterConfiguration.FilterType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType)` |  `[valueOf](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Returns the enum constant of this type with the specified name.  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[FilterConfiguration.FilterType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType)>` |  `[values](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType#values\(\))()` Returns an array containing the constants of this enum type, in the order they're declared.  
  
## Enum Values

### ABI
    
    
    val [FilterConfiguration.FilterType.ABI](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType#ABI): [FilterConfiguration.FilterType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType)

### DENSITY
    
    
    val [FilterConfiguration.FilterType.DENSITY](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType#DENSITY): [FilterConfiguration.FilterType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType)

### LANGUAGE
    
    
    val [FilterConfiguration.FilterType.LANGUAGE](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType#LANGUAGE): [FilterConfiguration.FilterType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType)

## Public functions

### valueOf

Added in 4.2.0
    
    
    fun [valueOf](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [FilterConfiguration.FilterType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType)

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

Throws  
---  
`[kotlin.IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html)` |  if this enum type has no constant with the specified name  
  
### values

Added in 4.2.0
    
    
    fun [values](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType#values\(\))(): [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[FilterConfiguration.FilterType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/FilterConfiguration.FilterType)>

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
