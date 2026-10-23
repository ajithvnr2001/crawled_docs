---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidTest/
title: AndroidTest \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:15:41.412097+00:00
---

# AndroidTest  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidTest/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AndroidTest

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/AndroidTest.kt+class:com.android.build.api.dsl.AndroidTest)

Added in 8.3.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidTest)

* * *

DSL object on library build type for configurations of the android test component.

android { buildTypes { debug { androidTest { enableMinification = ... } } } }

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableMinification](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidTest#enableMinification\(\))` Enable minification for the android test component  
  
## Public properties

### enableMinification

Added in 8.3.1
    
    
    var [enableMinification](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AndroidTest#enableMinification\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Enable minification for the android test component

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
