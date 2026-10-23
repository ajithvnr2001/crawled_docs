---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet/
title: TestSuiteSourceSet \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:38:20.380468+00:00
---

# TestSuiteSourceSet  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestSuiteSourceSet

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/TestSuiteSourceSet.kt+class:com.android.build.api.variant.TestSuiteSourceSet)

Added in 9.3.3
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html)

Known direct subclasses 

[TestSuiteSourceSet.Assets](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet.Assets), [TestSuiteSourceSet.HostJar](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet.HostJar), [TestSuiteSourceSet.TestApk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet.TestApk)

`[TestSuiteSourceSet.Assets](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet.Assets)` |  Represents a `[TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet)` for asset based tests.  
---|---  
`[TestSuiteSourceSet.HostJar](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet.HostJar)` |  Represents a `[TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet)` for host jars.  
`[TestSuiteSourceSet.TestApk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet.TestApk)` |  Represents a `[TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet)` for test apks.  
  
* * *

A test source abstraction which can be either an asset folder, a host jar source, or a test apk source.

Test suite sources attached to the `[TestSuite](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuite)`. These are not specific to a single variant but shared between all variants that the test suite targets through the `[com.android.build.api.dsl.AgpTestSuite.targetVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#targetVariants\(\))` API.

## Summary

### Nested types  
  
---  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
interface [TestSuiteSourceSet.Assets](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet.Assets) : [TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet)` Represents a `[TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet)` for asset based tests.  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
interface [TestSuiteSourceSet.HostJar](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet.HostJar) : [TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet)` Represents a `[TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet)` for host jars.  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
interface [TestSuiteSourceSet.TestApk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet.TestApk) : [TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet)` Represents a `[TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet)` for test apks.  
  
### Public properties  
  
---  
`[AgpTestSuiteDependencies](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteDependencies)?` |  `[dependencies](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet#dependencies\(\))` The dependencies associated with this source or null if this `[type](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet#type\(\))` does not support source dependencies (like `[TestSuiteSourceType.ASSETS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType#ASSETS)`]).  
`[TestSuiteSourceType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType)` |  `[type](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet#type\(\))` The source type.  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
## Public properties

### dependencies

Added in 9.3.3
    
    
    val [dependencies](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet#dependencies\(\)): [AgpTestSuiteDependencies](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteDependencies)?

The dependencies associated with this source or null if this `[type](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet#type\(\))` does not support source dependencies (like `[TestSuiteSourceType.ASSETS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType#ASSETS)`]).

The dependencies added through the DSL declarations will not be queryable through the returned instance. This `[dependencies](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet#dependencies\(\))` is only for adding new dependencies that were not added at the DSL declaration.

### type

Added in 9.3.3
    
    
    val [type](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceSet#type\(\)): [TestSuiteSourceType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType)

The source type.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
