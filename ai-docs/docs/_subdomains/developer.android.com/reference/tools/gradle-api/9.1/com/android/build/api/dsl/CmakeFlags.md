---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags/
title: CmakeFlags \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:01:42.623674+00:00
---

# CmakeFlags  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# CmakeFlags

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/CmakeFlags.kt+class:com.android.build.api.dsl.CmakeFlags)

Added in 8.0.2
    
    
    interface [CmakeFlags](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags)

* * *

DSL object for per-variant CMake options, such as CMake arguments and compiler flags.

To learn more about including CMake builds to your Android Studio projects, read [Add C and C++ Code to Your Project](https://developer.android.com/studio/projects/add-native-code.html). You can also read more documentation about [the Android CMake toolchain](https://developer.android.com/ndk/guides/cmake.html).

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[abiFilters](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#abiFilters\(kotlin.Array\))(vararg abiFilters: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Specifies the Application Binary Interfaces (ABI) that Gradle should build outputs for.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[arguments](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#arguments\(kotlin.Array\))(vararg arguments: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Specifies arguments for CMake.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[cFlags](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#cFlags\(kotlin.Array\))(vararg cFlags: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Specifies flags for the C compiler.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[cppFlags](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#cppFlags\(kotlin.Array\))(vararg cppFlags: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Specifies flags for the C++ compiler.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[targets](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#targets\(kotlin.Array\))(vararg targets: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Specifies the library and executable targets from your CMake project that Gradle should build.  
  
### Public properties  
  
---  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[abiFilters](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#abiFilters\(\))` Specifies the Application Binary Interfaces (ABI) that Gradle should build outputs for.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[arguments](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#arguments\(\))` Specifies arguments for CMake.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[cFlags](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#cFlags\(\))` Specifies flags for the C compiler.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[cppFlags](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#cppFlags\(\))` Specifies flags for the C++ compiler.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[targets](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#targets\(\))` Specifies the library and executable targets from your CMake project that Gradle should build.  
  
## Public functions

### abiFilters

Added in 8.0.2
    
    
    fun [abiFilters](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#abiFilters\(kotlin.Array\))(vararg abiFilters: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies the Application Binary Interfaces (ABI) that Gradle should build outputs for. The ABIs that Gradle packages into your APK are determined by `[android.defaultConfig.ndk.abiFilter](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Ndk#abiFilters\(\))`

In most cases, you need to specify ABIs using only `[android.defaultConfig.ndk.abiFilter](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Ndk#abiFilters\(\))`, because it tells Gradle which ABIs to both build and package into your APK. However, if you want to control what Gradle should build, independently of what you want it to package into your APK, configure this property with the ABIs you want Gradle to build.

To further reduce the size of your APK, consider [configuring multiple APKs based on ABI](https://developer.android.com/studio/build/configure-apk-splits.html#configure-abi-split)—instead of creating one large APK with all versions of your native libraries, Gradle creates a separate APK for each ABI you want to support and only packages the files each ABI needs.

By default, this property is `null`.

since 2.2.0

### arguments

Added in 8.0.2
    
    
    fun [arguments](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#arguments\(kotlin.Array\))(vararg arguments: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies arguments for CMake.

The following sample enables NEON support and tells CMake to use the Clang compiler toolchain:
    
    
    android {  
        // Similar to other properties in the defaultConfig block, you can override  
        // these properties for each product flavor you configure.  
        defaultConfig {  
            externalNativeBuild {  
                cmake {  
                    // Passes optional arguments to CMake.  
                    arguments "-DANDROID_ARM_NEON=TRUE", "-DANDROID_TOOLCHAIN=clang"  
                }  
            }  
        }  
    }

By default, this property is `null`. For a list of properties you can configure, see [CMake Variables List](https://developer.android.com/ndk/guides/cmake.html#variables).

since 2.2.0

### cFlags

Added in 8.0.2
    
    
    fun [cFlags](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#cFlags\(kotlin.Array\))(vararg cFlags: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies flags for the C compiler.

The following sample enables format macro constants:
    
    
    android {  
        // Similar to other properties in the defaultConfig block, you can override  
        // these properties for each product flavor in your build configuration.  
        defaultConfig {  
            externalNativeBuild {  
                cmake {  
                    // Sets an optional flag for the C compiler.  
                    cFlags "-D__STDC_FORMAT_MACROS"  
                }  
            }  
        }  
    }

By default, this property is `null`.

since 2.2.0

### cppFlags

Added in 8.0.2
    
    
    fun [cppFlags](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#cppFlags\(kotlin.Array\))(vararg cppFlags: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies flags for the C++ compiler.

The following sample enables RTTI (RunTime Type Information) support and C++ exceptions:
    
    
    android {  
        // Similar to other properties in the defaultConfig block, you can override  
        // these properties for each product flavor in your build configuration.  
        defaultConfig {  
            externalNativeBuild {  
                cmake {  
                    // Sets optional flags for the C++ compiler.  
                    cppFlags "-fexceptions", "-frtti"  
                }  
            }  
        }  
    }

By default, this property is `null`.

since 2.2.0

### targets

Added in 8.0.2
    
    
    fun [targets](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#targets\(kotlin.Array\))(vararg targets: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies the library and executable targets from your CMake project that Gradle should build.

For example, if your CMake project defines multiple libraries and executables, you can tell Gradle to build only a subset of those outputs as follows:
    
    
    android {  
        // Similar to other properties in the defaultConfig block, you can override  
        // these properties for each product flavor in your build configuration.  
        defaultConfig {  
            externalNativeBuild {  
                cmake {  
                    // The following tells Gradle to build only the "libexample-one.so" and  
                    // "my-executible-two" targets from the linked CMake project. If you don't  
                    // configure this property, Gradle builds all executables and shared object  
                    // libraries that you define in your CMake project. However, Gradle packages  
                    // only shared libraries into your APK.  
                    targets "libexample-one",  
                            // You need to specify this executable and its sources in your  
                            // CMakeLists.txt using the add_executable() CMake command. However,  
                            // building executables from your native sources is optional, and  
                            // building native libraries to package into your APK satisfies most  
                            // project requirements.  
                            "my-executible-demo"  
                }  
            }  
        }  
    }

If you don't configure this property, Gradle builds all executables and shared object libraries that you define in your CMake project. However, by default, Gradle packages only the shared libraries in your APK.

since 2.2.0

## Public properties

### abiFilters

Added in 8.0.2
    
    
    val [abiFilters](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#abiFilters\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies the Application Binary Interfaces (ABI) that Gradle should build outputs for. The ABIs that Gradle packages into your APK are determined by `[android.defaultConfig.ndk.abiFilter](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Ndk#abiFilters\(\))`

In most cases, you need to specify ABIs using only `[android.defaultConfig.ndk.abiFilter](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Ndk#abiFilters\(\))`, because it tells Gradle which ABIs to both build and package into your APK. However, if you want to control what Gradle should build, independently of what you want it to package into your APK, configure this property with the ABIs you want Gradle to build.

To further reduce the size of your APK, consider [configuring multiple APKs based on ABI](https://developer.android.com/studio/build/configure-apk-splits.html#configure-abi-split)—instead of creating one large APK with all versions of your native libraries, Gradle creates a separate APK for each ABI you want to support and only packages the files each ABI needs.

By default, this property is `null`.

since 2.2.0

### arguments

Added in 8.0.2
    
    
    val [arguments](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#arguments\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies arguments for CMake.

The following sample enables NEON support and tells CMake to use the Clang compiler toolchain:
    
    
    android {  
        // Similar to other properties in the defaultConfig block, you can override  
        // these properties for each product flavor you configure.  
        defaultConfig {  
            externalNativeBuild {  
                cmake {  
                    // Passes optional arguments to CMake.  
                    arguments "-DANDROID_ARM_NEON=TRUE", "-DANDROID_TOOLCHAIN=clang"  
                }  
            }  
        }  
    }

By default, this property is `null`. For a list of properties you can configure, see [CMake Variables List](https://developer.android.com/ndk/guides/cmake.html#variables).

since 2.2.0

### cFlags

Added in 8.0.2
    
    
    val [cFlags](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#cFlags\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies flags for the C compiler.

The following sample enables format macro constants:
    
    
    android {  
        // Similar to other properties in the defaultConfig block, you can override  
        // these properties for each product flavor in your build configuration.  
        defaultConfig {  
            externalNativeBuild {  
                cmake {  
                    // Sets an optional flag for the C compiler.  
                    cFlags "-D__STDC_FORMAT_MACROS"  
                }  
            }  
        }  
    }

By default, this property is `null`.

since 2.2.0

### cppFlags

Added in 8.0.2
    
    
    val [cppFlags](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#cppFlags\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies flags for the C++ compiler.

The following sample enables RTTI (RunTime Type Information) support and C++ exceptions:
    
    
    android {  
        // Similar to other properties in the defaultConfig block, you can override  
        // these properties for each product flavor in your build configuration.  
        defaultConfig {  
            externalNativeBuild {  
                cmake {  
                    // Sets optional flags for the C++ compiler.  
                    cppFlags "-fexceptions", "-frtti"  
                }  
            }  
        }  
    }

By default, this property is `null`.

since 2.2.0

### targets

Added in 8.0.2
    
    
    val [targets](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/CmakeFlags#targets\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies the library and executable targets from your CMake project that Gradle should build.

For example, if your CMake project defines multiple libraries and executables, you can tell Gradle to build only a subset of those outputs as follows:
    
    
    android {  
        // Similar to other properties in the defaultConfig block, you can override  
        // these properties for each product flavor in your build configuration.  
        defaultConfig {  
            externalNativeBuild {  
                cmake {  
                    // The following tells Gradle to build only the "libexample-one.so" and  
                    // "my-executible-two" targets from the linked CMake project. If you don't  
                    // configure this property, Gradle builds all executables and shared object  
                    // libraries that you define in your CMake project. However, Gradle packages  
                    // only shared libraries into your APK.  
                    targets "libexample-one",  
                            // You need to specify this executable and its sources in your  
                            // CMakeLists.txt using the add_executable() CMake command. However,  
                            // building executables from your native sources is optional, and  
                            // building native libraries to package into your APK satisfies most  
                            // project requirements.  
                            "my-executible-demo"  
                }  
            }  
        }  
    }

If you don't configure this property, Gradle builds all executables and shared object libraries that you define in your CMake project. However, by default, Gradle packages only the shared libraries in your APK.

since 2.2.0

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
