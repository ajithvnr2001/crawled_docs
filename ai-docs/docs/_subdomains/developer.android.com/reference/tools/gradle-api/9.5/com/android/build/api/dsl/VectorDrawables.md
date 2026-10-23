---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/VectorDrawables/
title: VectorDrawables \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:15:23.985262+00:00
---

# VectorDrawables  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/VectorDrawables/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# VectorDrawables

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/VectorDrawables.kt+class:com.android.build.api.dsl.VectorDrawables)

Added in 4.2.0
    
    
    interface [VectorDrawables](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/VectorDrawables)

* * *

DSL object used to configure `vector` drawable options.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[generatedDensities](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/VectorDrawables#generatedDensities\(kotlin.Array\))(vararg densities: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Densities used when generating PNGs from vector drawables at build time.  
  
### Public properties  
  
---  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>?` |  `[generatedDensities](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/VectorDrawables#generatedDensities\(\))` Densities used when generating PNGs from vector drawables at build time.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[useSupportLibrary](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/VectorDrawables#useSupportLibrary\(\))` Whether to use runtime support for `vector` drawables, instead of build-time support.  
  
## Public functions

### generatedDensities

Added in 4.2.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [generatedDensities](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/VectorDrawables#generatedDensities\(kotlin.Array\))(vararg densities: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Densities used when generating PNGs from vector drawables at build time. For the PNGs to be generated, minimum SDK has to be below 21.

If set to an empty collection, all special handling of vector drawables will be disabled.

See [Supporting Multiple Screens](http://developer.android.com/guide/practices/screens_support.html).

## Public properties

### generatedDensities

Added in 4.2.0
    
    
    val [generatedDensities](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/VectorDrawables#generatedDensities\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>?

Densities used when generating PNGs from vector drawables at build time. For the PNGs to be generated, minimum SDK has to be below 21.

If set to an empty collection, all special handling of vector drawables will be disabled.

See [Supporting Multiple Screens](http://developer.android.com/guide/practices/screens_support.html).

### useSupportLibrary

Added in 4.2.0
    
    
    var [useSupportLibrary](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/VectorDrawables#useSupportLibrary\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Whether to use runtime support for `vector` drawables, instead of build-time support.

See [Vector Asset Studio](http://developer.android.com/tools/help/vector-asset-studio.html).

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
