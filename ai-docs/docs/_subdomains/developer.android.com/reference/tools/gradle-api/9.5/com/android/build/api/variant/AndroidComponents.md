---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidComponents/
title: AndroidComponents \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:16:16.520954+00:00
---

# AndroidComponents  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidComponents/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AndroidComponents

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/AndroidComponents.kt+class:com.android.build.api.variant.AndroidComponents)

Added in 8.2.0
    
    
    interface [AndroidComponents](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidComponents)

Known direct subclasses 

[AndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidComponentsExtension)

`[AndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidComponentsExtension)` |  Generic extension for Android Gradle Plugin related components.  
---|---  
  
Known indirect subclasses 

[ApplicationAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ApplicationAndroidComponentsExtension), [DynamicFeatureAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/DynamicFeatureAndroidComponentsExtension), [KotlinMultiplatformAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/KotlinMultiplatformAndroidComponentsExtension), [LibraryAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/LibraryAndroidComponentsExtension), [TestAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestAndroidComponentsExtension)

`[ApplicationAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ApplicationAndroidComponentsExtension)` |  Extension for the Android Application Gradle Plugin components.  
---|---  
`[DynamicFeatureAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/DynamicFeatureAndroidComponentsExtension)` |  Extension for the Android Dynamic Feature Gradle Plugin components.  
`[KotlinMultiplatformAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/KotlinMultiplatformAndroidComponentsExtension)` |  Components extension for KMP Android Gradle Plugin related components.  
`[LibraryAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/LibraryAndroidComponentsExtension)` |  Extension for the Android Library Gradle Plugin components.  
`[TestAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestAndroidComponentsExtension)` |  Extension for the Android Test Gradle Plugin components.  
  
* * *

## Summary

### Public properties  
  
---  
`[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/AndroidPluginVersion)` |  `[pluginVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidComponents#pluginVersion\(\))` The version of the Android Gradle Plugin currently in use.  
`[SdkComponents](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SdkComponents)` |  `[sdkComponents](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidComponents#sdkComponents\(\))` Provides access to underlying Android SDK and build-tools components like adb.  
  
## Public properties

### pluginVersion

Added in 8.2.0
    
    
    val [pluginVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidComponents#pluginVersion\(\)): [AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/AndroidPluginVersion)

The version of the Android Gradle Plugin currently in use.

### sdkComponents

Added in 8.2.0
    
    
    val [sdkComponents](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidComponents#sdkComponents\(\)): [SdkComponents](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SdkComponents)

Provides access to underlying Android SDK and build-tools components like adb.

Returns  
---  
`[SdkComponents](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SdkComponents)` |  `[SdkComponents](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SdkComponents)` to access Android SDK used by Gradle.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
