---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Prefab/
title: Prefab \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:31:24.927618+00:00
---

# Prefab  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Prefab/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Prefab

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/Prefab.kt+class:com.android.build.api.dsl.Prefab)

Added in 8.0.2
    
    
    interface [Prefab](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Prefab)

* * *

Options for including [Prefab](https://google.github.io/prefab/) packages in AARs.

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[headerOnly](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Prefab#headerOnly\(\))` True if the library is header only and contains no library files.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[headers](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Prefab#headers\(\))` Path to a directory containing headers to export to dependents of this module.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[libraryName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Prefab#libraryName\(\))` The name of the library file, if it does not match the convention of lib.so or lib.a.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Prefab#name\(\))` The name of the library from the external native build to include in the AAR.  
  
## Public properties

### headerOnly

Added in 8.0.2
    
    
    var [headerOnly](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Prefab#headerOnly\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

True if the library is header only and contains no library files.

This value defaults to false.

### headers

Added in 8.0.2
    
    
    var [headers](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Prefab#headers\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Path to a directory containing headers to export to dependents of this module.

Note that any file in this directory will be included.

If not set, no headers will be exported for this library.

### libraryName

Added in 8.0.2
    
    
    var [libraryName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Prefab#libraryName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The name of the library file, if it does not match the convention of lib.so or lib.a.

This option can be used to specify the name of the library file if it does not match the name of the library in the build system. For example, if a CMake target is named "mylib" but the name of the library file was overridden to "mylib.so" rather than the default of "libmylib.so" using OUTPUT_NAME, libraryName should be set to "mylib".

If this option is null, the default convention of lib will be used.

### name

Added in 8.0.2
    
    
    var [name](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Prefab#name\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

The name of the library from the external native build to include in the AAR.

The name of the library must match the name of the library used by the external native build. For an ndk-build project, this is the LOCAL_MODULE option. For a CMake project, this is the name of the target.

This name will be the name of the module in the prefab package, and the package name will be the name of the gradle project.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
