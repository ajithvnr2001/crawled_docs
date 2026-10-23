---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteDependencies/
title: AgpTestSuiteDependencies \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:26:03.362885+00:00
---

# AgpTestSuiteDependencies  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteDependencies/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AgpTestSuiteDependencies

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/AgpTestSuiteDependencies.kt+class:com.android.build.api.dsl.AgpTestSuiteDependencies)

Added in 9.3.3
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [AgpTestSuiteDependencies](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteDependencies)

* * *

DSL element to add dependencies to an `[AgpTestSuite](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite)`

## Summary

### Public properties  
  
---  
`[DependencyCollector](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyCollector.html)` |  `[compileOnly](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteDependencies#compileOnly\(\))` Returns a `[DependencyCollector](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyCollector.html)` that collects the set of compile-only dependencies.  
`[DependencyCollector](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyCollector.html)` |  `[implementation](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteDependencies#implementation\(\))` Returns a []DependencyCollector] that collects the set of implementation dependencies.  
`[DependencyCollector](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyCollector.html)` |  `[runtimeOnly](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteDependencies#runtimeOnly\(\))` Returns a `[DependencyCollector](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyCollector.html)` that collects the set of runtime-only dependencies.  
  
## Public properties

### compileOnly

Added in 9.3.3
    
    
    val [compileOnly](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteDependencies#compileOnly\(\)): [DependencyCollector](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyCollector.html)

Returns a `[DependencyCollector](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyCollector.html)` that collects the set of compile-only dependencies.

### implementation

Added in 9.3.3
    
    
    val [implementation](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteDependencies#implementation\(\)): [DependencyCollector](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyCollector.html)

Returns a []DependencyCollector] that collects the set of implementation dependencies.

### runtimeOnly

Added in 9.3.3
    
    
    val [runtimeOnly](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteDependencies#runtimeOnly\(\)): [DependencyCollector](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyCollector.html)

Returns a `[DependencyCollector](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyCollector.html)` that collects the set of runtime-only dependencies.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
