---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/KeepRules/
title: KeepRules \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:18:34.422178+00:00
---

# KeepRules  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/KeepRules/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# KeepRules

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/KeepRules.kt+class:com.android.build.api.dsl.KeepRules)

Added in 7.3.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [KeepRules](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/KeepRules)

* * *

DSL object for external library dependencies keep rules configurations.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[ignoreAllExternalDependencies](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/KeepRules#ignoreAllExternalDependencies\(kotlin.Boolean\))~~(ignore: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` **This function is deprecated.** Renamed to ignoreFromAllExternalDependencies  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[ignoreExternalDependencies](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/KeepRules#ignoreExternalDependencies\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Renamed to ignoreFrom  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[ignoreFrom](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/KeepRules#ignoreFrom\(kotlin.Array\))(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Ignore keep rules from listed external dependencies.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[ignoreFromAllExternalDependencies](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/KeepRules#ignoreFromAllExternalDependencies\(kotlin.Boolean\))(ignore: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Ignore keep rules from all the external dependencies.  
  
### Public properties  
  
---  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>` |  `[files](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/KeepRules#files\(\))` Keep rules files set  
  
## Public functions

### ignoreAllExternalDependencies

Added in 7.3.0

Deprecated in 8.4.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[ignoreAllExternalDependencies](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/KeepRules#ignoreAllExternalDependencies\(kotlin.Boolean\))~~(ignore: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Renamed to ignoreFromAllExternalDependencies

### ignoreExternalDependencies

Added in 7.3.0

Deprecated in 8.4.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[ignoreExternalDependencies](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/KeepRules#ignoreExternalDependencies\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Renamed to ignoreFrom

### ignoreFrom

Added in 8.4.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [ignoreFrom](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/KeepRules#ignoreFrom\(kotlin.Array\))(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Ignore keep rules from listed external dependencies. External dependencies can be specified via GAV coordinates(e.g. "groupId:artifactId:version") or in the format of "groupId:artifactId" in which case dependencies are ignored as long as they match groupId & artifactId.

### ignoreFromAllExternalDependencies

Added in 8.4.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [ignoreFromAllExternalDependencies](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/KeepRules#ignoreFromAllExternalDependencies\(kotlin.Boolean\))(ignore: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Ignore keep rules from all the external dependencies.

## Public properties

### files

Added in 8.13.0
    
    
    val [files](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/KeepRules#files\(\)): [SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>

Keep rules files set

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-10-09 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-09 UTC."],[],[]] 
