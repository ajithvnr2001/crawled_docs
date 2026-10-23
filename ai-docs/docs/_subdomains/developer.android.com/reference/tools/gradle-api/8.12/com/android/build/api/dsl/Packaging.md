---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging/
title: Packaging \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:02:16.591264+00:00
---

# Packaging  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Packaging

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/Packaging.kt+class:com.android.build.api.dsl.Packaging)

Added in 8.0.2
    
    
    interface [Packaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging)

* * *

Packaging option entry point for the Android DSL.
    
    
    android {  
        packaging {  
        }  
    }

This interface provide controls over what file gets packaged in case of conflicts.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[dex](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#dex\(kotlin.Function1\))(action: [DexPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DexPackaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Method to configure the packaging options for dex files via a lambda  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[doNotStrip](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#doNotStrip\(kotlin.String\))~~(pattern: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** This method is deprecated.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[exclude](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#exclude\(kotlin.String\))~~(pattern: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** This method is deprecated.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[jniLibs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#jniLibs\(kotlin.Function1\))(action: [JniLibsPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/JniLibsPackaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Method to configure the packaging options for JNI library files via a lambda  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[merge](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#merge\(kotlin.String\))~~(pattern: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** This method is deprecated.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[pickFirst](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#pickFirst\(kotlin.String\))~~(pattern: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** This method is deprecated.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[resources](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#resources\(kotlin.Function1\))(action: [ResourcesPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ResourcesPackaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Method to configure the packaging options for Java resources via a lambda  
  
### Public properties  
  
---  
`[DexPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DexPackaging)` |  `[dex](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#dex\(\))` Packaging options for dex files  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[doNotStrip](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#doNotStrip\(\))` **This property is deprecated.** This property is deprecated.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[excludes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#excludes\(\))` **This property is deprecated.** This property is deprecated.  
`[JniLibsPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/JniLibsPackaging)` |  `[jniLibs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#jniLibs\(\))` Packaging options for JNI library files  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[merges](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#merges\(\))` **This property is deprecated.** This property is deprecated.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[pickFirsts](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#pickFirsts\(\))` **This property is deprecated.** This property is deprecated.  
`[ResourcesPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ResourcesPackaging)` |  `[resources](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#resources\(\))` Packaging options for java resources  
  
## Public functions

### dex

Added in 8.0.2
    
    
    fun [dex](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#dex\(kotlin.Function1\))(action: [DexPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DexPackaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Method to configure the packaging options for dex files via a lambda
    
    
    android {  
        packaging {  
            dex {  
                useLegacyPackaging = false  
            }  
        }  
    }

### doNotStrip

Added in 8.0.2

Deprecated in 8.0.2
    
    
    fun ~~[doNotStrip](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#doNotStrip\(kotlin.String\))~~(pattern: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
This method is deprecated. Use jniLibs.keepDebugSymbols.add() instead.

Adds a doNotStrip pattern.

Parameters  
---  
`pattern: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the pattern, as packaged in the APK  
  
### exclude

Added in 8.0.2

Deprecated in 8.0.2
    
    
    fun ~~[exclude](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#exclude\(kotlin.String\))~~(pattern: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
This method is deprecated. Use resources.excludes.add() or jniLibs.excludes.add() instead. Use jniLibs.excludes.add() for .so file patterns, and use resources.excludes.add() for all other file patterns.

Adds an excluded pattern.

Parameters  
---  
`pattern: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the pattern  
  
### jniLibs

Added in 8.0.2
    
    
    fun [jniLibs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#jniLibs\(kotlin.Function1\))(action: [JniLibsPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/JniLibsPackaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Method to configure the packaging options for JNI library files via a lambda
    
    
    android {  
        packaging {  
            jniLibs {  
                excludes += "/..."  
            }  
        }  
    }

### merge

Added in 8.0.2

Deprecated in 8.0.2
    
    
    fun ~~[merge](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#merge\(kotlin.String\))~~(pattern: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
This method is deprecated. Use resources.merges.add() instead.

Adds a merge pattern.

Parameters  
---  
`pattern: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the pattern, as packaged in the APK  
  
### pickFirst

Added in 8.0.2

Deprecated in 8.0.2
    
    
    fun ~~[pickFirst](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#pickFirst\(kotlin.String\))~~(pattern: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
This method is deprecated. Use resources.pickFirsts.add() or jniLibs.pickFirsts.add() instead. Use jniLibs.pickFirsts.add() for .so file patterns, and use resources.pickFirsts.add() for all other file patterns.

Adds a first-pick pattern.

Parameters  
---  
`pattern: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the path to add.  
  
### resources

Added in 8.0.2
    
    
    fun [resources](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#resources\(kotlin.Function1\))(action: [ResourcesPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ResourcesPackaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Method to configure the packaging options for Java resources via a lambda
    
    
    android {  
        packaging {  
            resources {  
                excludes += "/..."  
            }  
        }  
    }

## Public properties

### dex

Added in 8.0.2
    
    
    val [dex](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#dex\(\)): [DexPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/DexPackaging)

Packaging options for dex files

### doNotStrip

Added in 8.0.2

Deprecated in 8.0.2
    
    
    val [doNotStrip](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#doNotStrip\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

**This property is deprecated.**  
This property is deprecated. Use jniLibs.keepDebugSymbols instead.

The set of patterns for native library that should not be stripped of debug symbols.

### excludes

Added in 8.0.2

Deprecated in 8.0.2
    
    
    val [excludes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#excludes\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

**This property is deprecated.**  
This property is deprecated. Use resources.excludes or jniLibs.excludes instead. Use jniLibs.excludes for .so file patterns, and use resources.excludes for all other file patterns.

The set of excluded paths.

### jniLibs

Added in 8.0.2
    
    
    val [jniLibs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#jniLibs\(\)): [JniLibsPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/JniLibsPackaging)

Packaging options for JNI library files

### merges

Added in 8.0.2

Deprecated in 8.0.2
    
    
    val [merges](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#merges\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

**This property is deprecated.**  
This property is deprecated. Use resources.merges instead.

The set of patterns where all occurrences are concatenated and packaged in the APK.

### pickFirsts

Added in 8.0.2

Deprecated in 8.0.2
    
    
    val [pickFirsts](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#pickFirsts\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

**This property is deprecated.**  
This property is deprecated. Use resources.pickFirsts or jniLibs.pickFirsts instead. Use jniLibs.pickFirsts for .so file patterns, and use resources.pickFirsts for all other file patterns.

The set of patterns where the first occurrence is packaged in the APK. First pick patterns do get packaged in the APK, but only the first occurrence found gets packaged.

### resources

Added in 8.0.2
    
    
    val [resources](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Packaging#resources\(\)): [ResourcesPackaging](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ResourcesPackaging)

Packaging options for java resources

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
