---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ComposeOptions/
title: ComposeOptions \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:57:31.267938+00:00
---

# ComposeOptions  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ComposeOptions/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ComposeOptions

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ComposeOptions.kt+class:com.android.build.api.dsl.ComposeOptions)

Added in 4.2.0
    
    
    interface [ComposeOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ComposeOptions)

* * *

Optional settings for the Compose feature.

## Summary

### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[kotlinCompilerExtensionVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ComposeOptions#kotlinCompilerExtensionVersion\(\))` Sets the version of the Kotlin Compiler extension for the project or null if using the default one.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[kotlinCompilerVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ComposeOptions#kotlinCompilerVersion\(\))` **This property is deprecated.** Android Gradle Plugin will ignore this option and use the kotlin compiler version that is set in the build script.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[useLiveLiterals](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ComposeOptions#useLiveLiterals\(\))` **This property is deprecated.** ComposeOptions.useLiveLiterals is deprecated and will be removed in AGP 9.0.  
  
## Public properties

### kotlinCompilerExtensionVersion

Added in 4.2.0
    
    
    var [kotlinCompilerExtensionVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ComposeOptions#kotlinCompilerExtensionVersion\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Sets the version of the Kotlin Compiler extension for the project or null if using the default one.

### kotlinCompilerVersion

Added in 4.2.0

Deprecated in 7.0.0
    
    
    var [kotlinCompilerVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ComposeOptions#kotlinCompilerVersion\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

**This property is deprecated.**  
Android Gradle Plugin will ignore this option and use the kotlin compiler version that is set in the build script.

Sets the version of the Kotlin Compiler used to compile the project or null if using the default one.

### useLiveLiterals

Added in 7.0.0

Deprecated in 8.7.0
    
    
    var [useLiveLiterals](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ComposeOptions#useLiveLiterals\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
ComposeOptions.useLiveLiterals is deprecated and will be removed in AGP 9.0.

Enables live literals in Compose

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
