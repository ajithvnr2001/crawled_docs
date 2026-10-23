---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteTarget/
title: TestSuiteTarget \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:20:55.092509+00:00
---

# TestSuiteTarget  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteTarget/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestSuiteTarget

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/TestSuiteTarget.kt+class:com.android.build.api.variant.TestSuiteTarget)

Added in 9.5.0-alpha10
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [TestSuiteTarget](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteTarget) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html)

* * *

Model for running a `[TestSuite](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite)` in a context (local attached devices, gmd, etc...)

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enabled](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteTarget#enabled\(\))`  
`[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[targetDevices](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteTarget#targetDevices\(\))` GMD identifier to deploy APKs to.  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
## Public properties

### enabled

Added in 9.5.0-alpha10
    
    
    val [enabled](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteTarget#enabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

### targetDevices

Added in 9.5.0-alpha10
    
    
    val [targetDevices](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteTarget#targetDevices\(\)): [Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

GMD identifier to deploy APKs to. The identifier must be defined in the `[com.android.build.api.dsl.ManagedDevices](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ManagedDevices)` for this module.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
