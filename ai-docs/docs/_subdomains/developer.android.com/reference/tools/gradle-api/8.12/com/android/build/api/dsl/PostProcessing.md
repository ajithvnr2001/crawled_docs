---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing/
title: PostProcessing \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:02:21.103351+00:00
---

# PostProcessing  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# PostProcessing

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/PostProcessing.kt+class:com.android.build.api.dsl.PostProcessing)

Added in 7.0.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [PostProcessing](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing)

* * *

DSL object for configuring postProcessing: removing dead code, obfuscating etc.

This DSL is incubating and subject to change. To configure code and resource shrinkers, Instead use the properties already available in the [`buildType`](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/com.android.build.gradle.internal.dsl.BuildType) block.

To learn more, read [Shrink Your Code and Resources](https://developer.android.com/studio/build/shrink-code.html). 

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[consumerProguardFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#consumerProguardFile\(kotlin.Any\))(file: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[consumerProguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#consumerProguardFiles\(kotlin.Array\))(vararg files: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[initWith](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#initWith\(com.android.build.api.dsl.PostProcessing\))(that: [PostProcessing](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[proguardFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#proguardFile\(kotlin.Any\))(file: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[proguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#proguardFiles\(kotlin.Array\))(vararg files: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[setConsumerProguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#setConsumerProguardFiles\(kotlin.collections.List\))(consumerProguardFiles: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[setProguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#setProguardFiles\(kotlin.collections.List\))(proguardFiles: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[setTestProguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#setTestProguardFiles\(kotlin.collections.List\))(testProguardFiles: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[testProguardFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#testProguardFile\(kotlin.Any\))(file: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[testProguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#testProguardFiles\(kotlin.Array\))(vararg files: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))`  
  
### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[codeShrinker](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#codeShrinker\(\))` **This property is deprecated.** This property no longer has any effect.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isObfuscate](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#isObfuscate\(\))`  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isOptimizeCode](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#isOptimizeCode\(\))`  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isRemoveUnusedCode](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#isRemoveUnusedCode\(\))`  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isRemoveUnusedResources](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#isRemoveUnusedResources\(\))`  
  
## Public functions

### consumerProguardFile

Added in 7.0.0
    
    
    fun [consumerProguardFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#consumerProguardFile\(kotlin.Any\))(file: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### consumerProguardFiles

Added in 7.0.0
    
    
    fun [consumerProguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#consumerProguardFiles\(kotlin.Array\))(vararg files: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### initWith

Added in 7.0.0
    
    
    fun [initWith](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#initWith\(com.android.build.api.dsl.PostProcessing\))(that: [PostProcessing](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### proguardFile

Added in 7.0.0
    
    
    fun [proguardFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#proguardFile\(kotlin.Any\))(file: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### proguardFiles

Added in 7.0.0
    
    
    fun [proguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#proguardFiles\(kotlin.Array\))(vararg files: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### setConsumerProguardFiles
    
    
    fun [setConsumerProguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#setConsumerProguardFiles\(kotlin.collections.List\))(consumerProguardFiles: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### setProguardFiles
    
    
    fun [setProguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#setProguardFiles\(kotlin.collections.List\))(proguardFiles: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### setTestProguardFiles
    
    
    fun [setTestProguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#setTestProguardFiles\(kotlin.collections.List\))(testProguardFiles: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### testProguardFile

Added in 7.0.0
    
    
    fun [testProguardFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#testProguardFile\(kotlin.Any\))(file: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### testProguardFiles

Added in 7.0.0
    
    
    fun [testProguardFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#testProguardFiles\(kotlin.Array\))(vararg files: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

## Public properties

### codeShrinker

Added in 7.0.0

Deprecated in 7.0.0
    
    
    var [codeShrinker](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#codeShrinker\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

**This property is deprecated.**  
This property no longer has any effect. R8 is always used.

### isObfuscate

Added in 7.0.0
    
    
    var [isObfuscate](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#isObfuscate\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

### isOptimizeCode

Added in 7.0.0
    
    
    var [isOptimizeCode](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#isOptimizeCode\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

### isRemoveUnusedCode

Added in 7.0.0
    
    
    var [isRemoveUnusedCode](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#isRemoveUnusedCode\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

### isRemoveUnusedResources

Added in 7.0.0
    
    
    var [isRemoveUnusedResources](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PostProcessing#isRemoveUnusedResources\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
