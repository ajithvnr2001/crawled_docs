---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope/
title: InstrumentationScope \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:51:02.907768+00:00
---

# InstrumentationScope  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# InstrumentationScope

[View Source](https://cs.android.com/search?q=file:com/android/build/api/instrumentation/InstrumentationScope.kt+class:com.android.build.api.instrumentation.InstrumentationScope)

Added in 4.2.0
    
    
    enum [InstrumentationScope](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)  
|  ↳ | [com.android.build.api.instrumentation.InstrumentationScope](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope)  
  
* * *

## Summary

### Enum Values  
  
---  
`[ALL](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope#ALL)` |  Instrument the classes of the current project and its library dependencies.  
`[PROJECT](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope#PROJECT)` |  Instrument the classes of the current project only.  
  
### Public functions  
  
---  
`[InstrumentationScope](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope)` |  `[valueOf](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Returns the enum constant of this type with the specified name.  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[InstrumentationScope](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope)>` |  `[values](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope#values\(\))()` Returns an array containing the constants of this enum type, in the order they're declared.  
  
## Enum Values

### ALL
    
    
    val [InstrumentationScope.ALL](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope#ALL): [InstrumentationScope](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope)

Instrument the classes of the current project and its library dependencies.

This can't be applied to library projects, as instrumenting library dependencies will have no effect on library consumers.

### PROJECT
    
    
    val [InstrumentationScope.PROJECT](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope#PROJECT): [InstrumentationScope](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope)

Instrument the classes of the current project only.

Libraries that this project depends on will not be instrumented.

## Public functions

### valueOf

Added in 4.2.0
    
    
    fun [valueOf](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [InstrumentationScope](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope)

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

Throws  
---  
`kotlin.IllegalArgumentException` |  if this enum type has no constant with the specified name  
  
### values

Added in 4.2.0
    
    
    fun [values](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope#values\(\))(): [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[InstrumentationScope](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/instrumentation/InstrumentationScope)>

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
