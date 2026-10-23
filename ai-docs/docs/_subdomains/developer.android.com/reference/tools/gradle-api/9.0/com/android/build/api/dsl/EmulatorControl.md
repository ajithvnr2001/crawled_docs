---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/EmulatorControl/
title: EmulatorControl \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:18:03.806543+00:00
---

# EmulatorControl  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/EmulatorControl/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# EmulatorControl

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/EmulatorControl.kt+class:com.android.build.api.dsl.EmulatorControl)

Added in 8.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [EmulatorControl](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/EmulatorControl)

* * *

Options for configuring Android Emulator Access

When enabled, it will be possible to control the emulator through gRPC.

## Summary

### Public properties  
  
---  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[allowedEndpoints](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/EmulatorControl#allowedEndpoints\(\))` Set of endpoints to which access is granted, this is only required if the method you wish to access is in the set of methods that require authorization as defined in emulator_access.json used by the emulator this test is running on.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enable](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/EmulatorControl#enable\(\))` True if emulator control should be enabled.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[secondsValid](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/EmulatorControl#secondsValid\(\))` The duration in seconds the test can access the gRPC endpoint.  
  
## Public properties

### allowedEndpoints

Added in 8.1.0
    
    
    val [allowedEndpoints](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/EmulatorControl#allowedEndpoints\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Set of endpoints to which access is granted, this is only required if the method you wish to access is in the set of methods that require authorization as defined in emulator_access.json used by the emulator this test is running on.

Details on which endpoints and what considerations are taken to make an endpoint accessible is described in go/emu-grpc-integration.

### enable

Added in 8.1.0
    
    
    var [enable](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/EmulatorControl#enable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

True if emulator control should be enabled.

### secondsValid

Added in 8.1.0
    
    
    var [secondsValid](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/EmulatorControl#secondsValid\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

The duration in seconds the test can access the gRPC endpoint. The default value is 3600 (one hour).

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
