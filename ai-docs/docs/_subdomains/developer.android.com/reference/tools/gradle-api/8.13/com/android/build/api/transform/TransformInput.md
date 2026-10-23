---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInput/
title: TransformInput \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:36:48.429778+00:00
---

# TransformInput  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInput/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TransformInput

[View Source](https://cs.android.com/search?q=file:com/android/build/api/transform/TransformInput.java+class:com.android.build.api.transform.TransformInput)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    interface [TransformInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInput)

* * *

**This interface is deprecated.**  


The input to a Transform. 

It is mostly composed of a list of `[JarInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/JarInput)` and a list of `[DirectoryInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/DirectoryInput)`.

## Summary

### Public functions  
  
---  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[DirectoryInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/DirectoryInput)!>!` |  `[getDirectoryInputs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInput#getDirectoryInputs\(\))()` Returns a collection of `[DirectoryInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/DirectoryInput)`.  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[JarInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/JarInput)!>!` |  `[getJarInputs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInput#getJarInputs\(\))()` Returns a collection of `[JarInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/JarInput)`.  
  
## Public functions

### getDirectoryInputs

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getDirectoryInputs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInput#getDirectoryInputs\(\))(): ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[DirectoryInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/DirectoryInput)!>!

Returns a collection of `[DirectoryInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/DirectoryInput)`.

### getJarInputs

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getJarInputs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInput#getJarInputs\(\))(): ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[JarInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/JarInput)!>!

Returns a collection of `[JarInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/JarInput)`.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
