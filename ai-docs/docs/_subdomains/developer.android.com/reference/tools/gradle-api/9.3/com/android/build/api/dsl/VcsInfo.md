---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/VcsInfo/
title: VcsInfo \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:32:56.528436+00:00
---

# VcsInfo  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/VcsInfo/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# VcsInfo

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/VcsInfo.kt+class:com.android.build.api.dsl.VcsInfo)

Added in 8.3.1
    
    
    interface [VcsInfo](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/VcsInfo)

* * *

DSL object for configuring Version Control information

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[include](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/VcsInfo#include\(\))` Determines whether to include VCS info in the build.  
  
## Public properties

### include

Added in 8.3.1
    
    
    var [include](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/VcsInfo#include\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Determines whether to include VCS info in the build.

When the value is not set/null, the feature will be enabled by default in release builds. However, in the case that it is not successful, the build will not fail but will log the error message.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
