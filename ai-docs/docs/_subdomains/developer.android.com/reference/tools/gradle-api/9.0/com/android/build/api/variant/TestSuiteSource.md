---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestSuiteSource/
title: TestSuiteSource \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:26:29.039739+00:00
---

# TestSuiteSource  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestSuiteSource/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestSuiteSource

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/TestSuiteSource.kt+class:com.android.build.api.variant.TestSuiteSource)

Added in 9.0.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [TestSuiteSource](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestSuiteSource) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html)

* * *

A test source abstraction which can be either an asset folder, a host jar source, or a test apk source.

## Summary

### Public properties  
  
---  
`[AgpTestSuiteDependencies](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AgpTestSuiteDependencies)?` |  `[dependencies](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestSuiteSource#dependencies\(\))` The dependencies associated with this source or null if this `[type](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestSuiteSource#type\(\))` does not support source dependencies (like `[TestSuiteSourceType.ASSETS](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestSuiteSourceType#ASSETS)`]).  
`[TestSuiteSourceType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestSuiteSourceType)` |  `[type](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestSuiteSource#type\(\))` The source type.  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
## Public properties

### dependencies

Added in 9.0.1
    
    
    val [dependencies](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestSuiteSource#dependencies\(\)): [AgpTestSuiteDependencies](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AgpTestSuiteDependencies)?

The dependencies associated with this source or null if this `[type](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestSuiteSource#type\(\))` does not support source dependencies (like `[TestSuiteSourceType.ASSETS](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestSuiteSourceType#ASSETS)`]).

The dependencies added through the DSL declarations will not be queryable through the returned instance. This `[dependencies](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestSuiteSource#dependencies\(\))` is only for adding new dependencies that were not added at the DSL declaration.

### type

Added in 9.0.1
    
    
    val [type](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestSuiteSource#type\(\)): [TestSuiteSourceType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestSuiteSourceType)

The source type.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-13 UTC."],[],[]] 
