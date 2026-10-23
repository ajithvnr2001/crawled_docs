---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet.Assets
title: TestSuiteSourceSet.Assets \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:20:47.536790+00:00
---

# TestSuiteSourceSet.Assets  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet.Assets

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestSuiteSourceSet.Assets

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/TestSuiteSourceSet.kt+class:com.android.build.api.variant.TestSuiteSourceSet.Assets)

Added in 9.5.0-alpha10
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [TestSuiteSourceSet.Assets](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet.Assets) : [TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet)

* * *

Represents a `[TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet)` for asset based tests.

## Summary

### Public functions  
  
---  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/SourceDirectories.Flat)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[get](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet.Assets#get\(\))()`  
  
### Public properties  
  
---  
`open [TestSuiteSourceType](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceType)` |  `[type](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet.Assets#type\(\))` The source type.  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet) | `[AgpTestSuiteDependencies](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AgpTestSuiteDependencies)?` |  `[dependencies](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet#dependencies\(\))` The dependencies associated with this source or null if this `[type](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet#type\(\))` does not support source dependencies (like `[TestSuiteSourceType.ASSETS](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceType#ASSETS)`]).  
---|---  
  
## Public functions

### get

Added in 9.5.0-alpha10
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [get](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet.Assets#get\(\))(): [SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/SourceDirectories.Flat)

## Public properties

### type
    
    
    open val [type](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet.Assets#type\(\)): [TestSuiteSourceType](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceType)

The source type.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
