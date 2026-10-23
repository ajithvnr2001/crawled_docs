---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet.TestApk
title: TestSuiteSourceSet.TestApk \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:02:42.133336+00:00
---

# TestSuiteSourceSet.TestApk  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet.TestApk

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestSuiteSourceSet.TestApk

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/TestSuiteSourceSet.kt+class:com.android.build.api.variant.TestSuiteSourceSet.TestApk)

Added in 9.4.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [TestSuiteSourceSet.TestApk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet.TestApk) : [TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet)

* * *

Represents a `[TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet)` for test apks.

## Summary

### Public properties  
  
---  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)?` |  `[java](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet.TestApk#java\(\))`  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)?` |  `[kotlin](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet.TestApk#kotlin\(\))`  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)` |  `[manifestFile](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet.TestApk#manifestFile\(\))`  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)` |  `[resources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet.TestApk#resources\(\))`  
`open [TestSuiteSourceType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceType)` |  `[type](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet.TestApk#type\(\))` The source type.  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet) | `[AgpTestSuiteDependencies](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AgpTestSuiteDependencies)?` |  `[dependencies](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet#dependencies\(\))` The dependencies associated with this source or null if this `[type](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet#type\(\))` does not support source dependencies (like `[TestSuiteSourceType.ASSETS](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceType#ASSETS)`]).  
---|---  
  
## Public properties

### java

Added in 9.4.1
    
    
    val [java](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet.TestApk#java\(\)): [SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)?

### kotlin

Added in 9.4.1
    
    
    val [kotlin](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet.TestApk#kotlin\(\)): [SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)?

### manifestFile

Added in 9.4.1
    
    
    val [manifestFile](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet.TestApk#manifestFile\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)

### resources

Added in 9.4.1
    
    
    val [resources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet.TestApk#resources\(\)): [SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)

### type
    
    
    open val [type](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceSet.TestApk#type\(\)): [TestSuiteSourceType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteSourceType)

The source type.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
