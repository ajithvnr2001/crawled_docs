---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ExternalNdkBuild/
title: ExternalNdkBuild \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:07:35.444588+00:00
---

# ExternalNdkBuild  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ExternalNdkBuild/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ExternalNdkBuild

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/ExternalNdkBuild.kt+class:com.android.build.api.variant.ExternalNdkBuild)

Added in 7.0.0
    
    
    interface [ExternalNdkBuild](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ExternalNdkBuild) : [ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ExternalNativeBuild)

* * *

Interface for ndk-build per-variant info.

see `[com.android.build.api.dsl.NdkBuildFlags](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/NdkBuildFlags)` for expanded documentation on each of these fields.

## Summary

### Inherited properties  
  
---  
From [com.android.build.api.variant.ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ExternalNativeBuild) | `[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[abiFilters](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ExternalNativeBuild#abiFilters\(\))` Specifies the Application Binary Interfaces (ABI) that Gradle should build outputs for.  
---|---  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[arguments](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ExternalNativeBuild#arguments\(\))` Specifies arguments for CMake.  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[cFlags](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ExternalNativeBuild#cFlags\(\))` Specifies flags for the C compiler.  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[cppFlags](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ExternalNativeBuild#cppFlags\(\))` Specifies flags for the CPP compiler.  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[targets](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ExternalNativeBuild#targets\(\))` Specifies the library and executable targets from your CMake project that Gradle should build.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
