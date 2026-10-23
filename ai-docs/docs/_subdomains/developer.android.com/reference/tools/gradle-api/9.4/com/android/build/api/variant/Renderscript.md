---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Renderscript/
title: Renderscript \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:01:53.689227+00:00
---

# Renderscript  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Renderscript/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Renderscript

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/Renderscript.kt+class:com.android.build.api.variant.Renderscript)

Added in 7.0.0
    
    
    interface [Renderscript](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Renderscript)

* * *

Build-time properties for renderscript inside a `[Component](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Component)`.

This is accessed via `[GeneratesApk.renderscript](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApk#renderscript\(\))` or `[LibraryVariant.renderscript](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LibraryVariant#renderscript\(\))`

## Summary

### Public properties  
  
---  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[ndkModeEnabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Renderscript#ndkModeEnabled\(\))` Returns the renderscript NDK mode.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)>` |  `[optimLevel](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Renderscript#optimLevel\(\))`  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[supportModeBlasEnabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Renderscript#supportModeBlasEnabled\(\))` Returns the renderscript BLAS support mode.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[supportModeEnabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Renderscript#supportModeEnabled\(\))` Returns the renderscript support mode.  
  
## Public properties

### ndkModeEnabled

Added in 7.0.0
    
    
    val [ndkModeEnabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Renderscript#ndkModeEnabled\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>

Returns the renderscript NDK mode.

### optimLevel

Added in 7.0.0
    
    
    val [optimLevel](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Renderscript#optimLevel\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)>

### supportModeBlasEnabled

Added in 7.0.0
    
    
    val [supportModeBlasEnabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Renderscript#supportModeBlasEnabled\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>

Returns the renderscript BLAS support mode.

### supportModeEnabled

Added in 7.0.0
    
    
    val [supportModeEnabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Renderscript#supportModeEnabled\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>

Returns the renderscript support mode.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
