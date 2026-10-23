---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Optimization/
title: Optimization \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:04:48.916079+00:00
---

# Optimization  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Optimization/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Optimization

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/Optimization.kt+class:com.android.build.api.dsl.Optimization)

Added in 7.3.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [Optimization](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Optimization)

* * *

DSL object for configurations aimed for optimizing build process(e.g. speed, correctness). This DSL object is applicable to buildTypes and productFlavors.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[baselineProfile](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Optimization#baselineProfile\(kotlin.Function1\))(action: [BaselineProfile](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/BaselineProfile).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configure baseline profile properties  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[keepRules](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Optimization#keepRules\(kotlin.Function1\))(action: [KeepRules](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/KeepRules).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configure keep rules inherited from external library dependencies  
  
### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Optimization#enable\(\))` Specifies whether to enable code shrinking and resource optimization.  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[packageScope](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Optimization#packageScope\(\))` Specifies what packages are included for optimization.  
  
## Public functions

### baselineProfile

Added in 8.2.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [baselineProfile](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Optimization#baselineProfile\(kotlin.Function1\))(action: [BaselineProfile](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/BaselineProfile).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configure baseline profile properties

### keepRules

Added in 7.3.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [keepRules](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Optimization#keepRules\(kotlin.Function1\))(action: [KeepRules](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/KeepRules).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configure keep rules inherited from external library dependencies

## Public properties

### enable

Added in 8.13.0
    
    
    var [enable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Optimization#enable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Specifies whether to enable code shrinking and resource optimization. Property works for applications only. For other types it will be ignored

By default, value is false to avoid runtime issue. When enabled the Android plugin uses R8 for optimization.

Flavours merge this property with "or" rule. That means having this enable=true sticks.

### packageScope

Added in 8.13.0
    
    
    val [packageScope](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Optimization#packageScope\(\)): [SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies what packages are included for optimization. Those may be local code packages and external libraries packages. You can include

  * classes for a single package, like "com.example.app.*"

  * classes from package and all subpackages, like "androidx.**"

  * everything "**"




Default (convention) value is "**"

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
