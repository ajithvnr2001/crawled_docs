---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuildConfigField/
title: BuildConfigField \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:21:40.408028+00:00
---

# BuildConfigField  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuildConfigField/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BuildConfigField

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/BuildConfigField.kt+class:com.android.build.api.variant.BuildConfigField)

Added in 4.2.0
    
    
    class [BuildConfigField](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuildConfigField)<T : [Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)> : [Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)

* * *

Field definition for the generated BuildConfig class.

The field is generated as:  = ;

## Summary

### Public constructors  
  
---  
`<T : [Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)> [BuildConfigField](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuildConfigField#BuildConfigField\(kotlin.String,java.io.Serializable,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: T, comment: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)`  
  
### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[comment](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuildConfigField#comment\(\))` Optional field comment that will be added to the generated source file or null if no comment is necessary.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[type](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuildConfigField#type\(\))` Value to be written as BuildConfig field type.  
`T` |  `[value](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuildConfigField#value\(\))` Value of the generated field.  
  
## Public constructors

### BuildConfigField
    
    
    <T : [Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)> [BuildConfigField](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuildConfigField#BuildConfigField\(kotlin.String,java.io.Serializable,kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: T, comment: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)

## Public properties

### comment

Added in 4.2.0
    
    
    val [comment](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuildConfigField#comment\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Optional field comment that will be added to the generated source file or null if no comment is necessary.

### type

Added in 4.2.0
    
    
    val [type](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuildConfigField#type\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Value to be written as BuildConfig field type.

### value

Added in 4.2.0
    
    
    val [value](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuildConfigField#value\(\)): T

Value of the generated field. If `[type](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuildConfigField#type\(\))` is `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, then `[value](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuildConfigField#value\(\))` should include quotes.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
