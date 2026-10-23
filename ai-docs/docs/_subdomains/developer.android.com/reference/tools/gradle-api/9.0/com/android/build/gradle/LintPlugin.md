---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/gradle/LintPlugin/
title: LintPlugin \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:27:51.451337+00:00
---

# LintPlugin  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/gradle/LintPlugin/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# LintPlugin

[View Source](https://cs.android.com/search?q=file:com/android/build/gradle/LintPlugin.kt+class:com.android.build.gradle.LintPlugin)

Added in 8.0.2
    
    
    abstract class [LintPlugin](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/gradle/LintPlugin) : [BasePlugin](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/gradle/BasePlugin)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [com.android.build.gradle.BasePlugin](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/gradle/BasePlugin)  
|  ↳ | [com.android.build.gradle.LintPlugin](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/gradle/LintPlugin)  
  
* * *

Plugin for running lint **without** the Android Gradle plugin, such as in a pure Kotlin project.

## Summary

### Public constructors  
  
---  
`[LintPlugin](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/gradle/LintPlugin#LintPlugin\(\))()`  
  
### Public functions  
  
---  
`open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[apply](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/gradle/LintPlugin#apply\(org.gradle.api.Project\))(project: [Project](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html))`  
  
## Public constructors

### LintPlugin

Added in 8.0.2
    
    
    [LintPlugin](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/gradle/LintPlugin#LintPlugin\(\))()

## Public functions

### apply
    
    
    open fun [apply](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/gradle/LintPlugin#apply\(org.gradle.api.Project\))(project: [Project](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
