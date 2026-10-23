---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNativeBuild/
title: ExternalNativeBuild \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:53:07.285373+00:00
---

# ExternalNativeBuild  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNativeBuild/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ExternalNativeBuild

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/ExternalNativeBuild.kt+class:com.android.build.api.variant.ExternalNativeBuild)

Added in 7.0.0
    
    
    interface [ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNativeBuild)

Known direct subclasses 

[ExternalNdkBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNdkBuild)

`[ExternalNdkBuild](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNdkBuild)` |  Interface for ndk-build per-variant info.  
---|---  
  
* * *

Parameters to use when building native components.

Warning: Due to current limitations in how Android Gradle Plugin and native build interacts, it is not possible to wire a `[org.gradle.api.Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` mapped `[org.gradle.api.provider.Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)` to any of the collection `[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)` or `[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)` below. These properties must be resolved at configuration time and therefore cannot have results based on Task execution. This limitation might be lifted in the future.

## Summary

### Public properties  
  
---  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[abiFilters](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNativeBuild#abiFilters\(\))` Specifies the Application Binary Interfaces (ABI) that Gradle should build outputs for.  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[arguments](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNativeBuild#arguments\(\))` Specifies arguments for CMake.  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[cFlags](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNativeBuild#cFlags\(\))` Specifies flags for the C compiler.  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[cppFlags](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNativeBuild#cppFlags\(\))` Specifies flags for the CPP compiler.  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[targets](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNativeBuild#targets\(\))` Specifies the library and executable targets from your CMake project that Gradle should build.  
  
## Public properties

### abiFilters

Added in 7.0.0
    
    
    val [abiFilters](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNativeBuild#abiFilters\(\)): [SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies the Application Binary Interfaces (ABI) that Gradle should build outputs for. The ABIs that Gradle packages into your APK are determined by {@link com.android.build.gradle.internal.dsl.NdkOptions#abiFilter android.defaultConfig.ndk.abiFilter}

### arguments

Added in 7.0.0
    
    
    val [arguments](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNativeBuild#arguments\(\)): [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies arguments for CMake.

### cFlags

Added in 7.0.0
    
    
    val [cFlags](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNativeBuild#cFlags\(\)): [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies flags for the C compiler.

### cppFlags

Added in 7.0.0
    
    
    val [cppFlags](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNativeBuild#cppFlags\(\)): [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies flags for the CPP compiler.

### targets

Added in 7.0.0
    
    
    val [targets](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ExternalNativeBuild#targets\(\)): [SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies the library and executable targets from your CMake project that Gradle should build.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
