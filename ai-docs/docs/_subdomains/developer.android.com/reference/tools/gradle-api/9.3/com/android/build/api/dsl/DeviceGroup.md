---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DeviceGroup/
title: DeviceGroup \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:28:37.171738+00:00
---

# DeviceGroup  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DeviceGroup/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DeviceGroup

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/DeviceGroup.kt+class:com.android.build.api.dsl.DeviceGroup)

Added in 4.2.0
    
    
    interface [DeviceGroup](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DeviceGroup) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html)

* * *

A group of devices to be run with tests using the Unified Test Platform.

## Summary

### Public properties  
  
---  
`[DomainObjectSet](https://docs.gradle.org/current/javadoc/org/gradle/api/DomainObjectSet.html)<[Device](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Device)>` |  `[targetDevices](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DeviceGroup#targetDevices\(\))`  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
## Public properties

### targetDevices

Added in 4.2.0
    
    
    val [targetDevices](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DeviceGroup#targetDevices\(\)): [DomainObjectSet](https://docs.gradle.org/current/javadoc/org/gradle/api/DomainObjectSet.html)<[Device](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Device)>

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
