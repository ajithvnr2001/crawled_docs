---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/BasePlugin/
title: BasePlugin \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:10:48.622644+00:00
---

# BasePlugin  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/BasePlugin/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BasePlugin

[View Source](https://cs.android.com/search?q=file:com/android/build/gradle/BasePlugin.kt+class:com.android.build.gradle.BasePlugin)

Added in 8.0.2
    
    
    open class [BasePlugin](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/BasePlugin) : [Plugin](https://docs.gradle.org/current/javadoc/org/gradle/api/Plugin.html)

Known direct subclasses 

[AppPlugin](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/AppPlugin), [DynamicFeaturePlugin](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/DynamicFeaturePlugin), [KotlinMultiplatformAndroidPlugin](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/api/KotlinMultiplatformAndroidPlugin), [LibraryPlugin](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/LibraryPlugin), [LintPlugin](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/LintPlugin), [TestPlugin](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/TestPlugin)

`[AppPlugin](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/AppPlugin)` |  The plugin applied with `com.android.application`  
---|---  
`[DynamicFeaturePlugin](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/DynamicFeaturePlugin)` |  The plugin applied with `com.android.dynamic-feature`  
`[KotlinMultiplatformAndroidPlugin](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/api/KotlinMultiplatformAndroidPlugin)` |  The plugin applied with 'com.android.kotlin.multiplatform.library'  
`[LibraryPlugin](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/LibraryPlugin)` |  The plugin applied with `com.android.library`  
`[LintPlugin](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/LintPlugin)` |  Plugin for running lint **without** the Android Gradle plugin, such as in a pure Kotlin project.  
`[TestPlugin](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/TestPlugin)` |  The plugin applied with `com.android.test`  
  
* * *

Base class for the plugin.

Use the plugin classes directly

## Summary

### Public constructors  
  
---  
`[BasePlugin](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/BasePlugin#BasePlugin\(\))()`  
  
### Public functions  
  
---  
`open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[apply](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/BasePlugin#apply\(org.gradle.api.Project\))(project: [Project](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html))`  
  
## Public constructors

### BasePlugin

Added in 8.0.2
    
    
    [BasePlugin](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/BasePlugin#BasePlugin\(\))()

## Public functions

### apply

Added in 8.0.2
    
    
    open fun [apply](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/BasePlugin#apply\(org.gradle.api.Project\))(project: [Project](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
