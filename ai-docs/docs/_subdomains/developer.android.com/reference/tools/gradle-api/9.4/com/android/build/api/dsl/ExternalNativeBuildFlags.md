---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuildFlags/
title: ExternalNativeBuildFlags \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:52:55.916487+00:00
---

# ExternalNativeBuildFlags  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuildFlags/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ExternalNativeBuildFlags

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ExternalNativeBuildFlags.kt+class:com.android.build.api.dsl.ExternalNativeBuildFlags)

Added in 8.0.2
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [ExternalNativeBuildFlags](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuildFlags)

* * *

DSL object for per-variant CMake and ndk-build configurations, such as toolchain arguments and compiler flags.
    
    
    android {  
        // Similar to other properties in the defaultConfig block, you can override  
        // these properties for each product flavor you configure.  
        defaultConfig {  
            // This block is different from the one you use to link Gradle  
            // to your CMake or ndk-build script.  
            externalNativeBuild {  
                // For ndk-build, instead use the ndkBuild block.  
                cmake {  
                    // Passes optional arguments to CMake.  
                    arguments "-DANDROID_ARM_NEON=TRUE", "-DANDROID_TOOLCHAIN=clang"  
      
                    // Sets a flag to enable format macro constants for the C compiler.  
                    cFlags "-D__STDC_FORMAT_MACROS"  
      
                    // Sets optional flags for the C++ compiler.  
                    cppFlags "-fexceptions", "-frtti"  
      
                    // Specifies the library and executable targets from your CMake project  
                    // that Gradle should build.  
                    targets "libexample-one", "my-executible-demo"  
                }  
            }  
        }  
    }

To enable external native builds and set the path to your CMake or ndk-build script, use `[android.externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuild)`.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[cmake](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuildFlags#cmake\(kotlin.Function1\))(action: [CmakeFlags](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CmakeFlags).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates per-variant CMake configurations, such as compiler flags and toolchain arguments.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[ndkBuild](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuildFlags#ndkBuild\(kotlin.Function1\))(action: [NdkBuildFlags](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/NdkBuildFlags).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates per-variant ndk-build configurations, such as compiler flags and toolchain arguments.  
  
### Public properties  
  
---  
`[CmakeFlags](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CmakeFlags)` |  `[cmake](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuildFlags#cmake\(\))` Encapsulates per-variant CMake configurations, such as compiler flags and toolchain arguments.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[experimentalProperties](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuildFlags#experimentalProperties\(\))` Additional per-variant experimental properties for C and C++.  
`[NdkBuildFlags](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/NdkBuildFlags)` |  `[ndkBuild](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuildFlags#ndkBuild\(\))` Encapsulates per-variant ndk-build configurations, such as compiler flags and toolchain arguments.  
  
## Public functions

### cmake

Added in 8.0.2
    
    
    fun [cmake](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuildFlags#cmake\(kotlin.Function1\))(action: [CmakeFlags](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CmakeFlags).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Encapsulates per-variant CMake configurations, such as compiler flags and toolchain arguments.

To enable external native builds and set the path to your `CMakeLists.txt` script, use `[android.externalNativeBuild.cmake.path](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Cmake#path\(kotlin.Any\))`.

### ndkBuild

Added in 8.0.2
    
    
    fun [ndkBuild](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuildFlags#ndkBuild\(kotlin.Function1\))(action: [NdkBuildFlags](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/NdkBuildFlags).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Encapsulates per-variant ndk-build configurations, such as compiler flags and toolchain arguments.

To enable external native builds and set the path to your `Android.mk` script, use `[android.externalNativeBuild.ndkBuild.path](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/NdkBuild#path\(kotlin.Any\))`.

## Public properties

### cmake

Added in 8.0.2
    
    
    val [cmake](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuildFlags#cmake\(\)): [CmakeFlags](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/CmakeFlags)

Encapsulates per-variant CMake configurations, such as compiler flags and toolchain arguments.

To enable external native builds and set the path to your `CMakeLists.txt` script, use `[android.externalNativeBuild.cmake.path](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Cmake#path\(kotlin.Any\))`.

### experimentalProperties

Added in 8.0.2
    
    
    val [experimentalProperties](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuildFlags#experimentalProperties\(\)): [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>

Additional per-variant experimental properties for C and C++.

### ndkBuild

Added in 8.0.2
    
    
    val [ndkBuild](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ExternalNativeBuildFlags#ndkBuild\(\)): [NdkBuildFlags](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/NdkBuildFlags)

Encapsulates per-variant ndk-build configurations, such as compiler flags and toolchain arguments.

To enable external native builds and set the path to your `Android.mk` script, use `[android.externalNativeBuild.ndkBuild.path](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/NdkBuild#path\(kotlin.Any\))`.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
