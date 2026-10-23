---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestSuiteTestApkSpec/
title: TestSuiteTestApkSpec \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:50:11.655272+00:00
---

# TestSuiteTestApkSpec  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestSuiteTestApkSpec/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestSuiteTestApkSpec

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/TestSuiteTestApkSpec.kt+class:com.android.build.api.dsl.TestSuiteTestApkSpec)

Added in 9.2.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [TestSuiteTestApkSpec](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestSuiteTestApkSpec)

* * *

Definition of device test sources for a test suite. Device test source files are compiled and therefore dependencies can be attached to them.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[dependencies](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestSuiteTestApkSpec#dependencies\(kotlin.Function1\))(action: [AgpTestSuiteDependencies](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AgpTestSuiteDependencies).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies dependency information for this test suite.  
  
### Public properties  
  
---  
`[AgpTestSuiteDependencies](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AgpTestSuiteDependencies)` |  `[dependencies](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestSuiteTestApkSpec#dependencies\(\))` Dependency handler for this sources  
  
## Public functions

### dependencies

Added in 9.2.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [dependencies](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestSuiteTestApkSpec#dependencies\(kotlin.Function1\))(action: [AgpTestSuiteDependencies](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AgpTestSuiteDependencies).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies dependency information for this test suite.

## Public properties

### dependencies

Added in 9.2.1
    
    
    val [dependencies](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestSuiteTestApkSpec#dependencies\(\)): [AgpTestSuiteDependencies](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/AgpTestSuiteDependencies)

Dependency handler for this sources

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
