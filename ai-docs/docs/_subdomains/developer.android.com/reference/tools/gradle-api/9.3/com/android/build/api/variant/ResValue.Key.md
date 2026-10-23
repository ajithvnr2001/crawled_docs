---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ResValue.Key
title: ResValue.Key \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:37:44.538893+00:00
---

# ResValue.Key  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ResValue.Key

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ResValue.Key

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/ResValue.kt+class:com.android.build.api.variant.ResValue.Key)

Added in 7.0.0
    
    
    interface [ResValue.Key](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ResValue.Key) : [Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)

* * *

a generated resource is identified by its type+name as you can create @string/foo and @dimen/foo,

To create instances of `[Key](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ResValue.Key)`, use `[Variant.makeResValueKey](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Variant#makeResValueKey\(kotlin.String,kotlin.String\))` function. This interface should not be extended by third party plugin or build scripts.

## Summary

### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ResValue.Key#name\(\))` name of the resource.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[type](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ResValue.Key#type\(\))` type of the resource like 'string'  
  
## Public properties

### name

Added in 7.0.0
    
    
    val [name](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ResValue.Key#name\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

name of the resource.

### type

Added in 7.0.0
    
    
    val [type](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ResValue.Key#type\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

type of the resource like 'string'

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
