---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedDevices/
title: ManagedDevices \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:54:28.193616+00:00
---

# ManagedDevices  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedDevices/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ManagedDevices

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ManagedDevices.kt+class:com.android.build.api.dsl.ManagedDevices)

Added in 7.2.0
    
    
    interface [ManagedDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedDevices)

* * *

Options for Managed Devices

## Summary

### Public properties  
  
---  
`[ExtensiblePolymorphicDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/ExtensiblePolymorphicDomainObjectContainer.html)<[Device](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Device)>` |  `[allDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedDevices#allDevices\(\))` List of test devices for this project for use with the Unified Test Platform  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DeviceGroup](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DeviceGroup)>` |  `[groups](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedDevices#groups\(\))` List of DeviceGroups to create tasks for.  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ManagedVirtualDevice](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice)>` |  `[localDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedDevices#localDevices\(\))` Convenience container for specifying managed devices of type `[ManagedVirtualDevice](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice)`.  
  
## Public properties

### allDevices

Added in 8.1.0
    
    
    val [allDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedDevices#allDevices\(\)): [ExtensiblePolymorphicDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/ExtensiblePolymorphicDomainObjectContainer.html)<[Device](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Device)>

List of test devices for this project for use with the Unified Test Platform

These APIs are experimental and may change without notice.

### groups

Added in 7.2.0
    
    
    val [groups](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedDevices#groups\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[DeviceGroup](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DeviceGroup)>

List of DeviceGroups to create tasks for.

These APIs are experimental and may change without notice.

### localDevices

Added in 8.1.0
    
    
    val [localDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedDevices#localDevices\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ManagedVirtualDevice](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice)>

Convenience container for specifying managed devices of type `[ManagedVirtualDevice](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice)`.

This list is managed in sync with `[allDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedDevices#allDevices\(\))`. `[ManagedVirtualDevice](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice)` definitions added or removed in this container are correspondingly handled in `[allDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedDevices#allDevices\(\))`, and vice versa.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
