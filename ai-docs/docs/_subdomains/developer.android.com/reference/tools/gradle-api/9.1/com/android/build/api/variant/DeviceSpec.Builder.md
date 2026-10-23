---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder
title: DeviceSpec.Builder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:11:57.944260+00:00
---

# DeviceSpec.Builder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DeviceSpec.Builder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/DeviceSpec.kt+class:com.android.build.api.variant.DeviceSpec.Builder)

Added in 8.8.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    class [DeviceSpec.Builder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder)

* * *

## Summary

### Public constructors  
  
---  
`[Builder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#Builder\(\))()`  
  
### Public functions  
  
---  
`[DeviceSpec](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec)` |  `[build](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#build\(\))()`  
`[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/9.1/\[JVM%20root\]/<Error%20class:%20unknown%20class>)` |  `[setAbis](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#setAbis\(kotlin.collections.List\))(abis: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>)`  
`[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/9.1/\[JVM%20root\]/<Error%20class:%20unknown%20class>)` |  `[setApiLevel](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#setApiLevel\(kotlin.Int\))(apiLevel: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))`  
`[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/9.1/\[JVM%20root\]/<Error%20class:%20unknown%20class>)` |  `[setCodeName](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#setCodeName\(kotlin.String\))(codeName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)`  
`[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/9.1/\[JVM%20root\]/<Error%20class:%20unknown%20class>)` |  `[setName](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#setName\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)`  
`[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/9.1/\[JVM%20root\]/<Error%20class:%20unknown%20class>)` |  `[setScreenDensity](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#setScreenDensity\(kotlin.Int\))(screenDensity: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))`  
`[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/9.1/\[JVM%20root\]/<Error%20class:%20unknown%20class>)` |  `[setSupportsPrivacySandbox](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#setSupportsPrivacySandbox\(kotlin.Boolean\))(supportsPrivacySandbox: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))`  
  
### Public properties  
  
---  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[abis](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#abis\(\))`  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[apiLevel](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#apiLevel\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[codeName](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#codeName\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#name\(\))`  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[screenDensity](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#screenDensity\(\))`  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[supportsPrivacySandbox](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#supportsPrivacySandbox\(\))`  
  
## Public constructors

### Builder

Added in 8.8.0
    
    
    [Builder](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#Builder\(\))()

## Public functions

### build

Added in 8.8.0
    
    
    fun [build](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#build\(\))(): [DeviceSpec](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec)

### setAbis

Added in 8.8.0
    
    
    fun [setAbis](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#setAbis\(kotlin.collections.List\))(abis: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>): [<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/9.1/\[JVM%20root\]/<Error%20class:%20unknown%20class>)

### setApiLevel

Added in 8.8.0
    
    
    fun [setApiLevel](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#setApiLevel\(kotlin.Int\))(apiLevel: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/9.1/\[JVM%20root\]/<Error%20class:%20unknown%20class>)

### setCodeName

Added in 8.8.0
    
    
    fun [setCodeName](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#setCodeName\(kotlin.String\))(codeName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?): [<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/9.1/\[JVM%20root\]/<Error%20class:%20unknown%20class>)

### setName

Added in 8.8.0
    
    
    fun [setName](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#setName\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?): [<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/9.1/\[JVM%20root\]/<Error%20class:%20unknown%20class>)

### setScreenDensity

Added in 8.8.0
    
    
    fun [setScreenDensity](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#setScreenDensity\(kotlin.Int\))(screenDensity: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/9.1/\[JVM%20root\]/<Error%20class:%20unknown%20class>)

### setSupportsPrivacySandbox

Added in 8.8.0
    
    
    fun [setSupportsPrivacySandbox](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#setSupportsPrivacySandbox\(kotlin.Boolean\))(supportsPrivacySandbox: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/9.1/\[JVM%20root\]/<Error%20class:%20unknown%20class>)

## Public properties

### abis

Added in 8.8.0
    
    
    var [abis](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#abis\(\)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

### apiLevel

Added in 8.8.0
    
    
    var [apiLevel](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#apiLevel\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

### codeName

Added in 8.8.0
    
    
    var [codeName](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#codeName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

### name

Added in 8.8.0
    
    
    var [name](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#name\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

### screenDensity

Added in 8.8.0
    
    
    var [screenDensity](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#screenDensity\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

### supportsPrivacySandbox

Added in 8.8.0
    
    
    var [supportsPrivacySandbox](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/DeviceSpec.Builder#supportsPrivacySandbox\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
