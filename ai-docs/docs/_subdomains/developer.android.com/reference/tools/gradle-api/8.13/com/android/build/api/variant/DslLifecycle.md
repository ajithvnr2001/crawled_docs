---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslLifecycle/
title: DslLifecycle \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:38:51.119206+00:00
---

# DslLifecycle  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslLifecycle/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DslLifecycle

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/DslLifecycle.kt+class:com.android.build.api.variant.DslLifecycle)

Added in 7.1.0
    
    
    interface [DslLifecycle](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslLifecycle)<T : [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?>

Known direct subclasses 

[AndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidComponentsExtension), [LintLifecycleExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/LintLifecycleExtension)

`[AndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidComponentsExtension)` |  Generic extension for Android Gradle Plugin related components.  
---|---  
`[LintLifecycleExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/LintLifecycleExtension)` |   
  
Known indirect subclasses 

[ApplicationAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ApplicationAndroidComponentsExtension), [DynamicFeatureAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DynamicFeatureAndroidComponentsExtension), [KotlinMultiplatformAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/KotlinMultiplatformAndroidComponentsExtension), [LibraryAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/LibraryAndroidComponentsExtension), [TestAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/TestAndroidComponentsExtension)

`[ApplicationAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ApplicationAndroidComponentsExtension)` |  Extension for the Android Application Gradle Plugin components.  
---|---  
`[DynamicFeatureAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DynamicFeatureAndroidComponentsExtension)` |  Extension for the Android Dynamic Feature Gradle Plugin components.  
`[KotlinMultiplatformAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/KotlinMultiplatformAndroidComponentsExtension)` |  Components extension for KMP Android Gradle Plugin related components.  
`[LibraryAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/LibraryAndroidComponentsExtension)` |  Extension for the Android Library Gradle Plugin components.  
`[TestAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/TestAndroidComponentsExtension)` |  Extension for the Android Test Gradle Plugin components.  
  
* * *

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[finalizeDsl](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslLifecycle#finalizeDsl\(org.gradle.api.Action\))(callback: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<T>)` `[Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)` based version of `[finalizeDsl](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslLifecycle#finalizeDsl\(kotlin.Function1\))` above.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[finalizeDsl](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslLifecycle#finalizeDsl\(kotlin.Function1\))(callback: (T) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` API to customize the DSL Objects programmatically after they have been evaluated from the build files and before used in the build process next steps like variant or tasks creation.  
  
## Public functions

### finalizeDsl

Added in 7.1.0
    
    
    fun [finalizeDsl](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslLifecycle#finalizeDsl\(org.gradle.api.Action\))(callback: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<T>): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

`[Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)` based version of `[finalizeDsl](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslLifecycle#finalizeDsl\(kotlin.Function1\))` above.

### finalizeDsl

Added in 7.1.0
    
    
    fun [finalizeDsl](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslLifecycle#finalizeDsl\(kotlin.Function1\))(callback: (T) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

API to customize the DSL Objects programmatically after they have been evaluated from the build files and before used in the build process next steps like variant or tasks creation.

Example of a build type creation:
    
    
    androidComponents.finalizeDsl { extension ->  
        extension.buildTypes.create("extra")  
    }

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
