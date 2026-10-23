---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestFixtures/
title: TestFixtures \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:35:28.058714+00:00
---

# TestFixtures  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestFixtures/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestFixtures

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/TestFixtures.kt+class:com.android.build.api.dsl.TestFixtures)

Added in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [TestFixtures](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestFixtures)

* * *

DSL object for configuring test fixtures.

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[androidResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestFixtures#androidResources\(\))` Flag to enable Android resource processing in test fixtures.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestFixtures#enable\(\))` Flag to enable test fixtures.  
  
## Public properties

### androidResources

Added in 7.1.0
    
    
    var [androidResources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestFixtures#androidResources\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Flag to enable Android resource processing in test fixtures.

Default value is 'false'.

### enable

Added in 7.1.0
    
    
    var [enable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TestFixtures#enable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Flag to enable test fixtures.

Default value is derived from `android.experimental.enableTestFixtures` which is 'false' by default.

You can override the default for this for all projects in your build by adding the line `android.experimental.enableTestFixtures=true` in the gradle.properties file at the root project of your build.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
