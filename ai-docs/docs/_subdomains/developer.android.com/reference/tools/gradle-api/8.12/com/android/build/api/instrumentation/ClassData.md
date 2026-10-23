---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassData/
title: ClassData \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:04:45.587208+00:00
---

# ClassData  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassData/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ClassData

[View Source](https://cs.android.com/search?q=file:com/android/build/api/instrumentation/ClassData.kt+class:com.android.build.api.instrumentation.ClassData)

Added in 4.2.0
    
    
    interface [ClassData](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassData)

* * *

Data about the class to be instrumented.

## Summary

### Public properties  
  
---  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[classAnnotations](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassData#classAnnotations\(\))` List of the annotations the class has.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[className](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassData#className\(\))` Fully qualified name of the class.  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[interfaces](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassData#interfaces\(\))` List of all the interfaces that this class or a superclass of this class implements.  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[superClasses](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassData#superClasses\(\))` List of all the super classes that this class or a super class of this class extends.  
  
## Public properties

### classAnnotations

Added in 4.2.0
    
    
    val [classAnnotations](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassData#classAnnotations\(\)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

List of the annotations the class has.

### className

Added in 4.2.0
    
    
    val [className](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassData#className\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Fully qualified name of the class.

### interfaces

Added in 4.2.0
    
    
    val [interfaces](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassData#interfaces\(\)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

List of all the interfaces that this class or a superclass of this class implements.

### superClasses

Added in 4.2.0
    
    
    val [superClasses](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/ClassData#superClasses\(\)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

List of all the super classes that this class or a super class of this class extends.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
