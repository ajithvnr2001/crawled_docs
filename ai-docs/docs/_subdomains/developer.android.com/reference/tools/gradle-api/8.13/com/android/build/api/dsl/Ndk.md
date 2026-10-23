---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk/
title: Ndk \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:34:13.530293+00:00
---

# Ndk  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Ndk

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/Ndk.kt+class:com.android.build.api.dsl.Ndk)

Added in 4.2.0
    
    
    interface [Ndk](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk)

* * *

DSL object for per-variant NDK settings, such as the ABI filter.

## Summary

### Public properties  
  
---  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[abiFilters](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk#abiFilters\(\))` Specifies the Application Binary Interfaces (ABI) that Gradle should build outputs for and package with your APK.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[cFlags](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk#cFlags\(\))` **This property is deprecated.** Specify C/C++ flags in CMakeLists.txt or Application.mk  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[debugSymbolLevel](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk#debugSymbolLevel\(\))` The type of debug metadata which will be packaged in the app bundle.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[jobs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk#jobs\(\))` **This property is deprecated.** Use Cmake or NdkBuild DSL instead  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>?` |  `[ldLibs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk#ldLibs\(\))` **This property is deprecated.** Specify LD libs in CMakeLists.txt or Application.mk  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[moduleName](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk#moduleName\(\))` **This property is deprecated.** Specify module name in CMakeLists.txt or Application.mk  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[stl](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk#stl\(\))` **This property is deprecated.** Specify stl name in CMakeLists.txt or Application.mk  
  
## Public properties

### abiFilters

Added in 4.2.0
    
    
    val [abiFilters](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk#abiFilters\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies the Application Binary Interfaces (ABI) that Gradle should build outputs for and package with your APK.

You can list any subset of the [ABIs the NDK supports](https://developer.android.com/ndk/guides/abis.html#sa), as shown below:
    
    
    android {  
        // Similar to other properties in the defaultConfig block, you can override  
        // these properties for each product flavor in your build configuration.  
        defaultConfig {  
            ndk {  
                // Tells Gradle to build outputs for the following ABIs and package  
                // them into your APK.  
                abiFilters 'x86', 'x86_64', 'armeabi'  
            }  
        }  
    }

When this flag is not configured, Gradle builds and packages all available ABIs.

To reduce the size of your APK, consider [configuring multiple APKs based on ABI](https://developer.android.com/studio/build/configure-apk-splits.html#configure-abi-split)—instead of creating one large APK with all versions of your native libraries, Gradle creates a separate APK for each ABI you want to support and only packages the files each ABI needs.

### cFlags

Added in 4.2.0

Deprecated in 8.5.0
    
    
    var [cFlags](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk#cFlags\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

**This property is deprecated.**  
Specify C/C++ flags in CMakeLists.txt or Application.mk

The C Flags

### debugSymbolLevel

Added in 4.2.0
    
    
    var [debugSymbolLevel](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk#debugSymbolLevel\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The type of debug metadata which will be packaged in the app bundle.

Supported values are 'none' (default, no native debug metadata will be packaged), 'symbol_table' (only the symbol tables will be packaged), and 'full' (the debug info and symbol tables will be packaged).

Example usage:
    
    
    android {
        buildTypes {
            release {
                ndk {
                    debugSymbolLevel 'symbol_table'
                }
            }
        }
    }
    

### jobs

Added in 4.2.0

Deprecated in 8.5.0
    
    
    var [jobs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk#jobs\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

**This property is deprecated.**  
Use Cmake or NdkBuild DSL instead

Number of parallel threads to spawn.

### ldLibs

Added in 4.2.0

Deprecated in 8.5.0
    
    
    val [ldLibs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk#ldLibs\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>?

**This property is deprecated.**  
Specify LD libs in CMakeLists.txt or Application.mk

The LD Libs

### moduleName

Added in 4.2.0

Deprecated in 8.5.0
    
    
    var [moduleName](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk#moduleName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

**This property is deprecated.**  
Specify module name in CMakeLists.txt or Application.mk

The module name

### stl

Added in 4.2.0

Deprecated in 8.5.0
    
    
    var [stl](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Ndk#stl\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

**This property is deprecated.**  
Specify stl name in CMakeLists.txt or Application.mk

The APP_STL value

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
