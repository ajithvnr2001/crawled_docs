---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkInstallGroup/
title: ApkInstallGroup \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:58:16.776636+00:00
---

# ApkInstallGroup  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkInstallGroup/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ApkInstallGroup

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/ApkInstallGroup.kt+class:com.android.build.api.variant.ApkInstallGroup)

Added in 8.8.0
    
    
    interface [ApkInstallGroup](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkInstallGroup)

* * *

An interface representing a set of APKs files and that are installed as a unit on a device. These Apks are installed together with one install-multiple adb command if there are more than one Apks in the group.

## Summary

### Public properties  
  
---  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>` |  `[apks](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkInstallGroup#apks\(\))` A group of APK files installed as a unit on a device (e.g., via the install-multiple adb command).  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[description](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkInstallGroup#description\(\))` A brief description of this install group.  
  
## Public properties

### apks

Added in 8.8.0
    
    
    val [apks](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkInstallGroup#apks\(\)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>

A group of APK files installed as a unit on a device (e.g., via the install-multiple adb command).

### description

Added in 8.8.0
    
    
    val [description](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkInstallGroup#description\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

A brief description of this install group.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
