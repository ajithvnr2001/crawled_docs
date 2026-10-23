---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ExternalNativeBuild/
title: ExternalNativeBuild \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:11:27.004982+00:00
---

# ExternalNativeBuild  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ExternalNativeBuild/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ExternalNativeBuild

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ExternalNativeBuild.kt+class:com.android.build.api.dsl.ExternalNativeBuild)

Added in 4.2.0
    
    
    interface [ExternalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ExternalNativeBuild)

* * *

DSL object to configure external native builds using [CMake](https://cmake.org/) or [ndk-build](https://developer.android.com/ndk/guides/build.html)
    
    
    android {  
        externalNativeBuild {  
            // Encapsulates your CMake build configurations.  
            // For ndk-build, instead use the ndkBuild block.  
            cmake {  
                // Specifies a path to your CMake build script that's  
                // relative to the build.gradle file.  
                path "CMakeLists.txt"  
            }  
        }  
    }

To learn more about including external native builds to your Android Studio projects, read [Add C and C++ Code to Your Project](https://developer.android.com/studio/projects/add-native-code.html)

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[cmake](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ExternalNativeBuild#cmake\(kotlin.Function1\))(action: [Cmake](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Cmake).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Per module settings, such as the path to `CMakeLists.txt`, for an external CMake project.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[ndkBuild](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ExternalNativeBuild#ndkBuild\(kotlin.Function1\))(action: [NdkBuild](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/NdkBuild).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Per module settings, such as the path to `Android.mk`, for an external ndk-build project.  
  
### Public properties  
  
---  
`[Cmake](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Cmake)` |  `[cmake](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ExternalNativeBuild#cmake\(\))` Per module settings, such as the path to `CMakeLists.txt`, for an external CMake project.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[experimentalProperties](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ExternalNativeBuild#experimentalProperties\(\))` Additional per module experimental properties for C and C++.  
`[NdkBuild](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/NdkBuild)` |  `[ndkBuild](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ExternalNativeBuild#ndkBuild\(\))` Per module settings, such as the path to `Android.mk`, for an external ndk-build project.  
  
## Public functions

### cmake

Added in 4.2.0
    
    
    fun [cmake](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ExternalNativeBuild#cmake\(kotlin.Function1\))(action: [Cmake](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Cmake).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Per module settings, such as the path to `CMakeLists.txt`, for an external CMake project.

For more information about the properties you can configure in this block, see `[Cmake](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Cmake)`.

### ndkBuild

Added in 4.2.0
    
    
    fun [ndkBuild](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ExternalNativeBuild#ndkBuild\(kotlin.Function1\))(action: [NdkBuild](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/NdkBuild).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Per module settings, such as the path to `Android.mk`, for an external ndk-build project.

For more information about the properties you can configure in this block, see `[NdkBuild](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/NdkBuild)`.

## Public properties

### cmake

Added in 4.2.0
    
    
    val [cmake](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ExternalNativeBuild#cmake\(\)): [Cmake](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Cmake)

Per module settings, such as the path to `CMakeLists.txt`, for an external CMake project.

For more information about the properties you can configure in this block, see `[Cmake](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Cmake)`.

### experimentalProperties

Added in 7.3.0
    
    
    val [experimentalProperties](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ExternalNativeBuild#experimentalProperties\(\)): [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>

Additional per module experimental properties for C and C++.

### ndkBuild

Added in 4.2.0
    
    
    val [ndkBuild](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ExternalNativeBuild#ndkBuild\(\)): [NdkBuild](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/NdkBuild)

Per module settings, such as the path to `Android.mk`, for an external ndk-build project.

For more information about the properties you can configure in this block, see `[NdkBuild](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/NdkBuild)`.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
