---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ConsumerKeepRules/
title: ConsumerKeepRules \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:57:37.135752+00:00
---

# ConsumerKeepRules  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ConsumerKeepRules/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ConsumerKeepRules

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/KmpOptimization.kt+class:com.android.build.api.dsl.ConsumerKeepRules)

Added in 8.2.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [ConsumerKeepRules](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ConsumerKeepRules) : [ConfigurableFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ConfigurableFiles)

* * *

## Summary

### Public properties  
  
---  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[ignoreFrom](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ConsumerKeepRules#ignoreFrom\(\))` Ignore keep rules from listed external dependencies.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[ignoreFromAllExternalDependencies](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ConsumerKeepRules#ignoreFromAllExternalDependencies\(\))` Ignore keep rules from all the external dependencies.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[publish](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ConsumerKeepRules#publish\(\))` Publishing consumer proguard rules as part of a kmp library is an opt-in feature.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.ConfigurableFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ConfigurableFiles) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[file](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ConfigurableFiles#file\(kotlin.Any\))(file: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))`  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[files](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ConfigurableFiles#files\(kotlin.Array\))(vararg files: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))`  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.ConfigurableFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ConfigurableFiles) | `[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)>` |  `[files](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ConfigurableFiles#files\(\))`  
---|---  
  
## Public properties

### ignoreFrom

Added in 8.2.0
    
    
    val [ignoreFrom](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ConsumerKeepRules#ignoreFrom\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Ignore keep rules from listed external dependencies. External dependencies can be specified via GAV coordinates(e.g. "groupId:artifactId:version") or in the format of "groupId:artifactId" in which case dependencies are ignored as long as they match groupId & artifactId.

### ignoreFromAllExternalDependencies

Added in 8.2.0
    
    
    var [ignoreFromAllExternalDependencies](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ConsumerKeepRules#ignoreFromAllExternalDependencies\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Ignore keep rules from all the external dependencies.

### publish

Added in 8.2.0
    
    
    var [publish](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ConsumerKeepRules#publish\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Publishing consumer proguard rules as part of a kmp library is an opt-in feature. By default, consumer proguard rules will not be published.

To enable it, set this property to `true`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
