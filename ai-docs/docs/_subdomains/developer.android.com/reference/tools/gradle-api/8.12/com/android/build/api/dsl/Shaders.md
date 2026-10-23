---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Shaders/
title: Shaders \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:03:09.442179+00:00
---

# Shaders  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Shaders/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Shaders

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/Shaders.kt+class:com.android.build.api.dsl.Shaders)

Added in 4.2.0
    
    
    interface [Shaders](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Shaders)

* * *

Options for configuring scoped shader options.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[glslcArgs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Shaders#glslcArgs\(kotlin.Array\))(vararg options: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds options to the list of glslc args.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[glslcScopedArgs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Shaders#glslcScopedArgs\(kotlin.String,kotlin.Array\))(key: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), vararg options: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds options to the list of scoped glsl args.  
  
### Public properties  
  
---  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[glslcArgs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Shaders#glslcArgs\(\))` The list of glslc args.  
`[ListMultimap](https://guava.dev/releases/18.0/api/docs/com/google/common/collect/ListMultimap.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[scopedGlslcArgs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Shaders#scopedGlslcArgs\(\))` The list of scoped glsl args.  
  
## Public functions

### glslcArgs

Added in 4.2.0
    
    
    fun [glslcArgs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Shaders#glslcArgs\(kotlin.Array\))(vararg options: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds options to the list of glslc args.

### glslcScopedArgs

Added in 4.2.0
    
    
    fun [glslcScopedArgs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Shaders#glslcScopedArgs\(kotlin.String,kotlin.Array\))(key: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), vararg options: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds options to the list of scoped glsl args.

## Public properties

### glslcArgs

Added in 4.2.0
    
    
    val [glslcArgs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Shaders#glslcArgs\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The list of glslc args.

### scopedGlslcArgs

Added in 4.2.0
    
    
    val [scopedGlslcArgs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Shaders#scopedGlslcArgs\(\)): [ListMultimap](https://guava.dev/releases/18.0/api/docs/com/google/common/collect/ListMultimap.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The list of scoped glsl args.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
