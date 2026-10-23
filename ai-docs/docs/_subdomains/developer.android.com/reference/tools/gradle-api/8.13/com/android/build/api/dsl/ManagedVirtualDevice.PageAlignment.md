---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment
title: ManagedVirtualDevice.PageAlignment \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:36:01.442804+00:00
---

# ManagedVirtualDevice.PageAlignment  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ManagedVirtualDevice.PageAlignment

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ManagedVirtualDevice.kt+class:com.android.build.api.dsl.ManagedVirtualDevice.PageAlignment)

Added in 8.13.2
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    enum [ManagedVirtualDevice.PageAlignment](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)  
|  ↳ | [com.android.build.api.dsl.ManagedVirtualDevice.PageAlignment](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment)  
  
* * *

Defines possible system image selection strategies based on the requested Page Alignment

This allows for testing on devices for both 4KB and 16KB page sizes. See [Android Page Sizes](https://developer.android.com/guide/practices/page-sizes) for more information.

## Summary

### Enum Values  
  
---  
`[DEFAULT_FOR_SDK_VERSION](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment#DEFAULT_FOR_SDK_VERSION)` |  Selects the page alignment that would result in the certified system image for the given `[sdkVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice#sdkVersion\(\))`.  
`[FORCE_16KB_PAGES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment#FORCE_16KB_PAGES)` |  Selects the system image with 16KB aligned pages.  
`[FORCE_4KB_PAGES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment#FORCE_4KB_PAGES)` |  Selects the system image with 4KB aligned pages.  
  
### Public functions  
  
---  
`[ManagedVirtualDevice.PageAlignment](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment)` |  `[valueOf](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Returns the enum constant of this type with the specified name.  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[ManagedVirtualDevice.PageAlignment](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment)>` |  `[values](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment#values\(\))()` Returns an array containing the constants of this enum type, in the order they're declared.  
  
## Enum Values

### DEFAULT_FOR_SDK_VERSION
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    val [ManagedVirtualDevice.PageAlignment.DEFAULT_FOR_SDK_VERSION](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment#DEFAULT_FOR_SDK_VERSION): [ManagedVirtualDevice.PageAlignment](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment)

Selects the page alignment that would result in the certified system image for the given `[sdkVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice#sdkVersion\(\))`. At present (API 35 and below), the certified image is always 4KB aligned.

### FORCE_16KB_PAGES
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    val [ManagedVirtualDevice.PageAlignment.FORCE_16KB_PAGES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment#FORCE_16KB_PAGES): [ManagedVirtualDevice.PageAlignment](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment)

Selects the system image with 16KB aligned pages. If no such image exists, the setup for the managed device will fail.

### FORCE_4KB_PAGES
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    val [ManagedVirtualDevice.PageAlignment.FORCE_4KB_PAGES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment#FORCE_4KB_PAGES): [ManagedVirtualDevice.PageAlignment](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment)

Selects the system image with 4KB aligned pages. If no such image exists, the setup for the managed device will fail.

## Public functions

### valueOf

Added in 8.13.2
    
    
    fun [valueOf](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [ManagedVirtualDevice.PageAlignment](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment)

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

Throws  
---  
`[kotlin.IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html)` |  if this enum type has no constant with the specified name  
  
### values

Added in 8.13.2
    
    
    fun [values](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment#values\(\))(): [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[ManagedVirtualDevice.PageAlignment](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment)>

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-11 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-11 UTC."],[],[]] 
