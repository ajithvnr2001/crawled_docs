---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Device/
title: Device \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:28:34.551748+00:00
---

# Device  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Device/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Device

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/Device.kt+class:com.android.build.api.dsl.Device)

Added in 4.2.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [Device](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Device) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html), [Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)

Known direct subclasses 

[ManagedVirtualDevice](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ManagedVirtualDevice)

`[ManagedVirtualDevice](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ManagedVirtualDevice)` |  Device type for emulators to be managed by the Android Gradle Plugin.  
---|---  
  
* * *

Top-level interface for all devices to run applications by tasks in the Android Gradle Plugin.

## Summary

### Public functions  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
@[Internal](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/Internal.html)  
[getName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Device#getName\(\))()`  
  
## Public functions

### getName
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    @[Internal](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/Internal.html)  
    fun [getName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Device#getName\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
