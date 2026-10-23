---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SdkComponents/
title: SdkComponents \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:03:02.291733+00:00
---

# SdkComponents  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SdkComponents/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# SdkComponents

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/SdkComponents.kt+class:com.android.build.api.dsl.SdkComponents)

Added in 4.2.0
    
    
    interface [SdkComponents](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SdkComponents)

* * *

## Summary

### Public properties  
  
---  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[Aapt2](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Aapt2)>` |  `[aapt2](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SdkComponents#aapt2\(\))` Provides access to AAPT2  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>` |  `[adb](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SdkComponents#adb\(\))` The path to the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html) executable from the Android SDK.  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[Aidl](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Aidl)>` |  `[aidl](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SdkComponents#aidl\(\))` Provides access to aidl tools  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>>` |  `[bootClasspath](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SdkComponents#bootClasspath\(\))` The bootclasspath that will be used to compile classes in this project.  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)>` |  `[ndkDirectory](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SdkComponents#ndkDirectory\(\))` The path to the [Android NDK](https://developer.android.com/ndk/index.html) that Gradle uses for this project.  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)>` |  `[sdkDirectory](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SdkComponents#sdkDirectory\(\))` The path to the Android SDK that Gradle uses for this project.  
  
## Public properties

### aapt2

Added in 8.12.3
    
    
    val [aapt2](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SdkComponents#aapt2\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[Aapt2](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Aapt2)>

Provides access to AAPT2

The returned `[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)` can be used by tasks requiring AAPT2 as input with `[org.gradle.api.tasks.Nested](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/Nested.html)`. See `[Aapt2](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Aapt2)` for more details.

### adb

Added in 4.2.0
    
    
    val [adb](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SdkComponents#adb\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>

The path to the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html) executable from the Android SDK.

### aidl

Added in 8.1.0
    
    
    val [aidl](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SdkComponents#aidl\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[Aidl](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Aidl)>

Provides access to aidl tools

The returned `[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)` can be used by tasks requiring aidl tools as input with `[org.gradle.api.tasks.Nested](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/Nested.html)`. See `[Aidl](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Aidl)` for more details.

### bootClasspath

Added in 7.1.0
    
    
    val [bootClasspath](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SdkComponents#bootClasspath\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>>

The bootclasspath that will be used to compile classes in this project.

The returned `[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)` can only be used at execution time and therefore must be used as a `[org.gradle.api.Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` input to do so.

### ndkDirectory

Added in 4.2.0
    
    
    val [ndkDirectory](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SdkComponents#ndkDirectory\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)>

The path to the [Android NDK](https://developer.android.com/ndk/index.html) that Gradle uses for this project.

You can install the Android NDK by either [using the SDK manager](https://developer.android.com/studio/intro/update.html#sdk-manager) or downloading [the standalone NDK package](https://developer.android.com/ndk/downloads/index.html).

### sdkDirectory

Added in 4.2.0
    
    
    val [sdkDirectory](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SdkComponents#sdkDirectory\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)>

The path to the Android SDK that Gradle uses for this project.

To learn more about downloading and installing the Android SDK, read [Update Your Tools with the SDK Manager](https://developer.android.com/studio/intro/update.html#sdk-manager)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-09-11 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-11 UTC."],[],[]] 
