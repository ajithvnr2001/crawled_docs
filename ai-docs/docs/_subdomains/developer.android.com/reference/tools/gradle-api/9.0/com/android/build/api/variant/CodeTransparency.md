---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/CodeTransparency/
title: CodeTransparency \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:23:39.386130+00:00
---

# CodeTransparency  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/CodeTransparency/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# CodeTransparency

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/CodeTransparency.kt+class:com.android.build.api.variant.CodeTransparency)

Added in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [CodeTransparency](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/CodeTransparency)

* * *

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[setSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/CodeTransparency#setSigningConfig\(com.android.build.api.dsl.SigningConfig\))(signingConfig: [SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/SigningConfig))` Sets the `[com.android.build.api.dsl.SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/SigningConfig)` with information on how to retrieve the signing configuration.  
  
## Public functions

### setSigningConfig

Added in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [setSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/CodeTransparency#setSigningConfig\(com.android.build.api.dsl.SigningConfig\))(signingConfig: [SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/SigningConfig)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Sets the `[com.android.build.api.dsl.SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/SigningConfig)` with information on how to retrieve the signing configuration.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
