---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/gradle/SettingsPlugin/
title: SettingsPlugin \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:44:37.202822+00:00
---

# SettingsPlugin  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/gradle/SettingsPlugin/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# SettingsPlugin

[View Source](https://cs.android.com/search?q=file:com/android/build/gradle/SettingsPlugin.kt+class:com.android.build.gradle.SettingsPlugin)

Added in 7.4.0
    
    
    class [SettingsPlugin](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/gradle/SettingsPlugin) : [Plugin](https://docs.gradle.org/current/javadoc/org/gradle/api/Plugin.html)

* * *

The plugin applied with `com.android.settings'

This plugin is meant to be applied in `settings.gradle[.kts]`, not in subprojects.

## Summary

### Public constructors  
  
---  
`[SettingsPlugin](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/gradle/SettingsPlugin#SettingsPlugin\(\))()`  
  
### Public functions  
  
---  
`open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[apply](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/gradle/SettingsPlugin#apply\(org.gradle.api.initialization.Settings\))(settings: [Settings](https://docs.gradle.org/current/javadoc/org/gradle/api/initialization/Settings.html))`  
  
### Public properties  
  
---  
`[SettingsExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/SettingsExtension)` |  `[android](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/gradle/SettingsPlugin#android\(\))`  
  
## Public constructors

### SettingsPlugin

Added in 7.4.0
    
    
    [SettingsPlugin](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/gradle/SettingsPlugin#SettingsPlugin\(\))()

## Public functions

### apply

Added in 7.4.0
    
    
    open fun [apply](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/gradle/SettingsPlugin#apply\(org.gradle.api.initialization.Settings\))(settings: [Settings](https://docs.gradle.org/current/javadoc/org/gradle/api/initialization/Settings.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

## Public properties

### android

Added in 7.4.0
    
    
    val [android](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/gradle/SettingsPlugin#android\(\)): [SettingsExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/SettingsExtension)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
