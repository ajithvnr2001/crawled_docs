---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder/
title: KotlinMultiplatformAndroidCompilationBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:24.792438+00:00
---

# KotlinMultiplatformAndroidCompilationBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# KotlinMultiplatformAndroidCompilationBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder.kt+class:com.android.build.api.dsl.KotlinMultiplatformAndroidCompilationBuilder)

Added in 8.2.0
    
    
    interface [KotlinMultiplatformAndroidCompilationBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder)

* * *

Options to build a `[KotlinMultiplatformAndroidCompilation](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation)` object.

## Summary

### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[sourceSetTreeName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder#sourceSetTreeName\(\))` The name of the sourceSet tree that would be used to infer the dependencies between sourceSets.  
  
## Public properties

### sourceSetTreeName

Added in 8.2.0
    
    
    var [sourceSetTreeName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder#sourceSetTreeName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The name of the sourceSet tree that would be used to infer the dependencies between sourceSets. For example, setting the sourceSetTreeName to `test` means that compilation will include the `commonTest` sourceSet, and setting it to `integrationTest` means that the compilation will include the `commonIntegrationTest` sourceSet if exists.

Setting this value to `null` means that this compilation is not part of any sourceSet trees and the kotlin plugin will not include any common test sourceSets in this compilation.

See also  
---  
`org.jetbrains.kotlin.gradle.dsl.KotlinMultiplatformExtension.targetHierarchy` |   
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
