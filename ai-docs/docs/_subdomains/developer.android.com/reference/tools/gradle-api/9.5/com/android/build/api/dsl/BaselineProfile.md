---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BaselineProfile/
title: BaselineProfile \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:09:21.461171+00:00
---

# BaselineProfile  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BaselineProfile/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BaselineProfile

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/BaselineProfile.kt+class:com.android.build.api.dsl.BaselineProfile)

Added in 8.2.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [BaselineProfile](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BaselineProfile)

* * *

DSL object in `[Optimization](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Optimization)` for configuring properties related to Baseline Profiles.

## Summary

### Public properties  
  
---  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[ignoreFrom](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BaselineProfile#ignoreFrom\(\))` Ignore baseline profiles from listed external dependencies.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[ignoreFromAllExternalDependencies](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BaselineProfile#ignoreFromAllExternalDependencies\(\))` Ignore baseline profiles from all the external dependencies.  
  
## Public properties

### ignoreFrom

Added in 8.2.0
    
    
    val [ignoreFrom](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BaselineProfile#ignoreFrom\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Ignore baseline profiles from listed external dependencies. External dependencies can be specified via GAV coordinates(e.g. "groupId:artifactId:version") or in the format of "groupId:artifactId" in which case dependencies are ignored as long as they match groupId & artifactId.

### ignoreFromAllExternalDependencies

Added in 8.2.0
    
    
    var [ignoreFromAllExternalDependencies](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BaselineProfile#ignoreFromAllExternalDependencies\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Ignore baseline profiles from all the external dependencies.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
