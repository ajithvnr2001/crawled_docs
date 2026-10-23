---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/gradle/api/AndroidBasePlugin/
title: AndroidBasePlugin \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:40:47.126194+00:00
---

# AndroidBasePlugin  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/gradle/api/AndroidBasePlugin/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AndroidBasePlugin

[View Source](https://cs.android.com/search?q=file:com/android/build/gradle/api/AndroidBasePlugin.kt+class:com.android.build.gradle.api.AndroidBasePlugin)

Added in 4.2.0
    
    
    class [AndroidBasePlugin](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/gradle/api/AndroidBasePlugin) : [Plugin](https://docs.gradle.org/current/javadoc/org/gradle/api/Plugin.html)

* * *

Common plugin applied by all plugins that have a `[CommonExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension)`

The purpose of this no-op plugin is to allow other plugin authors to determine if an Android plugin with a `[CommonExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CommonExtension)` was applied.

This is tied to the `com.android.base` plugin ID.

## Summary

### Public constructors  
  
---  
`[AndroidBasePlugin](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/gradle/api/AndroidBasePlugin#AndroidBasePlugin\(\))()`  
  
### Public functions  
  
---  
`open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[apply](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/gradle/api/AndroidBasePlugin#apply\(org.gradle.api.Project\))(project: [Project](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html))`  
  
## Public constructors

### AndroidBasePlugin

Added in 4.2.0
    
    
    [AndroidBasePlugin](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/gradle/api/AndroidBasePlugin#AndroidBasePlugin\(\))()

## Public functions

### apply

Added in 4.2.0
    
    
    open fun [apply](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/gradle/api/AndroidBasePlugin#apply\(org.gradle.api.Project\))(project: [Project](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
