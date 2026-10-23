---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryKeepRules/
title: LibraryKeepRules \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:48:03.318285+00:00
---

# LibraryKeepRules  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryKeepRules/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# LibraryKeepRules

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/KmpOptimization.kt+class:com.android.build.api.dsl.LibraryKeepRules)

Added in 8.2.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [LibraryKeepRules](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryKeepRules) : [ConfigurableFiles](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ConfigurableFiles)

* * *

## Summary

### Public properties  
  
---  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[ignoreFrom](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryKeepRules#ignoreFrom\(\))` Ignore keep rules from listed external dependencies.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[ignoreFromAllExternalDependencies](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryKeepRules#ignoreFromAllExternalDependencies\(\))` Ignore keep rules from all the external dependencies.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.ConfigurableFiles](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ConfigurableFiles) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[file](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ConfigurableFiles#file\(kotlin.Any\))(file: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))`  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[files](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ConfigurableFiles#files\(kotlin.Array\))(vararg files: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))`  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.ConfigurableFiles](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ConfigurableFiles) | `[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>` |  `[files](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ConfigurableFiles#files\(\))`  
---|---  
  
## Public properties

### ignoreFrom

Added in 8.2.0
    
    
    val [ignoreFrom](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryKeepRules#ignoreFrom\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Ignore keep rules from listed external dependencies. External dependencies can be specified via GAV coordinates(e.g. "groupId:artifactId:version") or in the format of "groupId:artifactId" in which case dependencies are ignored as long as they match groupId & artifactId.

### ignoreFromAllExternalDependencies

Added in 8.2.0
    
    
    var [ignoreFromAllExternalDependencies](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryKeepRules#ignoreFromAllExternalDependencies\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Ignore keep rules from all the external dependencies.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
