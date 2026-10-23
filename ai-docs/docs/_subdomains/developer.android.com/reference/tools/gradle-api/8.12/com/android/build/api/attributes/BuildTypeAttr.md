---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/attributes/BuildTypeAttr/
title: BuildTypeAttr \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:52:46.472245+00:00
---

# BuildTypeAttr  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/attributes/BuildTypeAttr/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BuildTypeAttr

[View Source](https://cs.android.com/search?q=file:com/android/build/api/attributes/BuildTypeAttr.kt+class:com.android.build.api.attributes.BuildTypeAttr)

Added in 4.2.0
    
    
    interface [BuildTypeAttr](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/attributes/BuildTypeAttr) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html)

* * *

Type for the attribute holding BuildType information.

There should only be one build type attribute associated to each `[org.gradle.api.artifacts.Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` object. The key should be `[ATTRIBUTE](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/attributes/BuildTypeAttr.Companion#ATTRIBUTE\(\))`.

## Summary

### Public companion properties  
  
---  
`[Attribute](https://docs.gradle.org/current/javadoc/org/gradle/api/attributes/Attribute.html)<[BuildTypeAttr](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/attributes/BuildTypeAttr)>` |  `[ATTRIBUTE](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/attributes/BuildTypeAttr.Companion#ATTRIBUTE\(\))`  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
## Public companion properties

### ATTRIBUTE
    
    
    val [ATTRIBUTE](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/attributes/BuildTypeAttr.Companion#ATTRIBUTE\(\)): [Attribute](https://docs.gradle.org/current/javadoc/org/gradle/api/attributes/Attribute.html)<[BuildTypeAttr](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/attributes/BuildTypeAttr)>

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
