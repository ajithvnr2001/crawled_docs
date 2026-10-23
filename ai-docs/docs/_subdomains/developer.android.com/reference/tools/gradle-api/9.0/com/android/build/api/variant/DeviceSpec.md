---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec/
title: DeviceSpec \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:27:09.492488+00:00
---

# DeviceSpec  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DeviceSpec

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/DeviceSpec.kt+class:com.android.build.api.variant.DeviceSpec)

Added in 8.8.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    class [DeviceSpec](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec)

* * *

A class representing device-specific attributes.

## Summary

### Nested types  
  
---  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
class [DeviceSpec.Builder](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec.Builder)`  
  
### Public functions  
  
---  
`open operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[equals](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#equals\(kotlin.Any\))(other: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?)`  
`open [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[hashCode](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#hashCode\(\))()`  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[toString](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#toString\(\))()`  
  
### Public properties  
  
---  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[abis](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#abis\(\))` The ABIs of the device.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[apiLevel](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#apiLevel\(\))` The API level of the device.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[codeName](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#codeName\(\))` The code name of the device.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#name\(\))` The name of the device which can be helpful in debugging.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[screenDensity](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#screenDensity\(\))` The screen density of the device.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[supportsPrivacySandbox](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#supportsPrivacySandbox\(\))` Whether the device supports Privacy Sandbox.  
  
## Public functions

### equals
    
    
    open operator fun [equals](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#equals\(kotlin.Any\))(other: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

### hashCode
    
    
    open fun [hashCode](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#hashCode\(\))(): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

### toString
    
    
    open fun [toString](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#toString\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

## Public properties

### abis

Added in 8.8.0
    
    
    val [abis](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#abis\(\)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The ABIs of the device.

### apiLevel

Added in 8.8.0
    
    
    val [apiLevel](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#apiLevel\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

The API level of the device.

### codeName

Added in 8.8.0
    
    
    val [codeName](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#codeName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The code name of the device.

### name

Added in 8.8.0
    
    
    val [name](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#name\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The name of the device which can be helpful in debugging.

### screenDensity

Added in 8.8.0
    
    
    val [screenDensity](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#screenDensity\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

The screen density of the device.

### supportsPrivacySandbox

Added in 8.8.0
    
    
    val [supportsPrivacySandbox](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec#supportsPrivacySandbox\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether the device supports Privacy Sandbox.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
