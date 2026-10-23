---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder/
title: KotlinMultiplatformAndroidCompilationBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:59:47.649563+00:00
---

# KotlinMultiplatformAndroidCompilationBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# KotlinMultiplatformAndroidCompilationBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder.kt+class:com.android.build.api.dsl.KotlinMultiplatformAndroidCompilationBuilder)

Added in 8.2.0
    
    
    interface [KotlinMultiplatformAndroidCompilationBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder)

* * *

Options to build a `[KotlinMultiplatformAndroidCompilation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation)` object.

## Summary

### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[compilationName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder#compilationName\(\))` **This property is deprecated.** Changing the compilation name is discouraged.This API will be removed in AGP 9.0  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[defaultSourceSetName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder#defaultSourceSetName\(\))` **This property is deprecated.** Changing the name of the source set used as a default in a compilation is discouraged.This API will be removed in AGP 9.0  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[sourceSetTreeName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder#sourceSetTreeName\(\))` The name of the sourceSet tree that would be used to infer the dependencies between sourceSets.  
  
## Public properties

### compilationName

Added in 8.2.0

Deprecated in 8.8.0
    
    
    var [compilationName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder#compilationName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

**This property is deprecated.**  
Changing the compilation name is discouraged.This API will be removed in AGP 9.0

The name of the compilation object. The name can be used later to access the compilation object using
    
    
    kotlin {  
      android {  
        compilations.getByName("main") {  
          // configure compilation  
        }  
      }  
    }

See also  
---  
`[KotlinCompilation](https://developer.android.com/reference/tools/gradle-api/8.12/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation)` |   
  
### defaultSourceSetName

Added in 8.2.0

Deprecated in 8.8.0
    
    
    var [defaultSourceSetName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder#defaultSourceSetName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

**This property is deprecated.**  
Changing the name of the source set used as a default in a compilation is discouraged.This API will be removed in AGP 9.0

The name of the sourceSet that is used in the compilation as the default sourceSet to compile. The sourceSet created will be located at `$projectDir/src/$sourceSetName`.

The sourceSet name can be used later to access the sourceSet object using
    
    
    kotlin {  
      sourceSets.getByName("androidMain") {  
        // configure sourceSet  
      }  
    }

See also  
---  
`[KotlinSourceSet](https://developer.android.com/reference/tools/gradle-api/8.12/org/jetbrains/kotlin/gradle/plugin/KotlinSourceSet)` |   
  
### sourceSetTreeName

Added in 8.2.0
    
    
    var [sourceSetTreeName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilationBuilder#sourceSetTreeName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The name of the sourceSet tree that would be used to infer the dependencies between sourceSets. For example, setting the sourceSetTreeName to `test` means that compilation will include the `commonTest` sourceSet, and setting it to `integrationTest` means that the compilation will include the `commonIntegrationTest` sourceSet if exists.

Setting this value to `null` means that this compilation is not part of any sourceSet trees and the kotlin plugin will not include any common test sourceSets in this compilation.

See also  
---  
`org.jetbrains.kotlin.gradle.dsl.KotlinMultiplatformExtension.targetHierarchy` |   
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-06-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-06 UTC."],[],[]] 
