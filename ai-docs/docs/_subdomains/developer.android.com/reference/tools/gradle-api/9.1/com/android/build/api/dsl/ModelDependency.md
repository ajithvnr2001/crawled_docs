---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ModelDependency/
title: ModelDependency \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:04:34.887205+00:00
---

# ModelDependency  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ModelDependency/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ModelDependency

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ModelDependency.kt+class:com.android.build.api.dsl.ModelDependency)

Added in 8.7.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [ModelDependency](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ModelDependency)

* * *

DSL object to configure a model dependency for an AI pack.

## Summary

### Public properties  
  
---  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[aiModelName](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ModelDependency#aiModelName\(\))` The name of the AI model dependency.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[aiModelPackageName](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ModelDependency#aiModelPackageName\(\))` The package name of the app that contains this model dependency.  
  
## Public properties

### aiModelName

Added in 8.7.0
    
    
    val [aiModelName](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ModelDependency#aiModelName\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The name of the AI model dependency.

### aiModelPackageName

Added in 8.7.0
    
    
    val [aiModelPackageName](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/ModelDependency#aiModelPackageName\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The package name of the app that contains this model dependency.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
