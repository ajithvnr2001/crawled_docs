---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassContext/
title: ClassContext \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:04:42.346051+00:00
---

# ClassContext  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassContext/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ClassContext

[View Source](https://cs.android.com/search?q=file:com/android/build/api/instrumentation/ClassContext.kt+class:com.android.build.api.instrumentation.ClassContext)

Added in 4.2.0
    
    
    interface [ClassContext](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassContext)

* * *

## Summary

### Public functions  
  
---  
`[ClassData](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassData)?` |  `[loadClassData](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassContext#loadClassData\(kotlin.String\))(className: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Loads the class data for the class with given `[className](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassContext#loadClassData\(kotlin.String\))`.  
  
### Public properties  
  
---  
`[ClassData](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassData)` |  `[currentClassData](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassContext#currentClassData\(\))` Contains information about the class that will be instrumented.  
  
## Public functions

### loadClassData

Added in 4.2.0
    
    
    fun [loadClassData](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassContext#loadClassData\(kotlin.String\))(className: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [ClassData](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassData)?

Loads the class data for the class with given `[className](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassContext#loadClassData\(kotlin.String\))`.

Returns null if a class named `[className](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassContext#loadClassData\(kotlin.String\))` couldn't be found in the runtime classpath of the class defined by the `[currentClassData](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassContext#currentClassData\(\))`.

Parameters  
---  
`className: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the fully qualified name of the class, (e.g. "com.android.build.api.instrumentation.ClassContext")  
  
## Public properties

### currentClassData

Added in 4.2.0
    
    
    val [currentClassData](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassContext#currentClassData\(\)): [ClassData](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassData)

Contains information about the class that will be instrumented.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
