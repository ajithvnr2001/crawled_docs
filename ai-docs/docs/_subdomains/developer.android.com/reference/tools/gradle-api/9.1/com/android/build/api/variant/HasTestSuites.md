---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasTestSuites/
title: HasTestSuites \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:09:31.443633+00:00
---

# HasTestSuites  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasTestSuites/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# HasTestSuites

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/HasTestSuites.kt+class:com.android.build.api.variant.HasTestSuites)

Added in 9.1.1
    
    
    interface [HasTestSuites](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasTestSuites)

Known direct subclasses 

[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/ApplicationVariant)

`[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/ApplicationVariant)` |  Model for application components that only contains build-time properties.  
---|---  
  
* * *

`[Variant](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/Variant)` that optionally have `[TestSuite](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/TestSuite)`s.

## Summary

### Public properties  
  
---  
`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [TestSuite](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/TestSuite)>` |  `[suites](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasTestSuites#suites\(\))` Variant's com.android.build.gradle.internal.testsuites.TestSuite configuration to configure test suites associated with this variant.  
  
## Public properties

### suites

Added in 9.1.1
    
    
    val [suites](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/HasTestSuites#suites\(\)): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [TestSuite](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/TestSuite)>

Variant's com.android.build.gradle.internal.testsuites.TestSuite configuration to configure test suites associated with this variant.

Returns  
---  
`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [TestSuite](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/TestSuite)>` |  a `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)` which keys are unique names within the test suites  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-13 UTC."],[],[]] 
