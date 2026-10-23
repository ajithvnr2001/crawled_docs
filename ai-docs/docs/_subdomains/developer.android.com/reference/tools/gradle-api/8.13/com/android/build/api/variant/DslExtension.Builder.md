---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder
title: DslExtension.Builder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:42:37.941676+00:00
---

# DslExtension.Builder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DslExtension.Builder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/DslExtension.kt+class:com.android.build.api.variant.DslExtension.Builder)

Added in 7.0.0
    
    
    class [DslExtension.Builder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder)

* * *

Creates a `[Builder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder)` to instance to create a `[DslExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension)` containing all desired extension points to the Android Gradle Plugin DSL.

## Summary

### Public constructors  
  
---  
`[Builder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder#Builder\(kotlin.String\))(dslName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))`  
  
### Public functions  
  
---  
`[DslExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension)` |  `[build](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder#build\(\))()` Builds the final `[DslExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension)` instance that can be used with the `[AndroidComponentsExtension.registerExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidComponentsExtension#registerExtension\(com.android.build.api.variant.DslExtension,kotlin.Function1\))` API  
`[DslExtension.Builder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder)` |  `[extendBuildTypeWith](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder#extendBuildTypeWith\(java.lang.Class\))(typeExtension: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>)` Registers an extension point for the `[com.android.build.api.dsl.BuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType)`  
`[DslExtension.Builder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder)` |  `[extendProductFlavorWith](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder#extendProductFlavorWith\(java.lang.Class\))(typeExtension: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>)` Registers an extension point for the `[com.android.build.api.dsl.ProductFlavor](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ProductFlavor)`  
`[DslExtension.Builder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder)` |  `[extendProjectWith](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder#extendProjectWith\(java.lang.Class\))(typeExtension: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>)` Registers an extension point for the module's DSL, it will be available under the android block.  
  
## Public constructors

### Builder

Added in 7.0.0
    
    
    [Builder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder#Builder\(kotlin.String\))(dslName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))

Parameters  
---  
`dslName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the extension point name as it appears in build files.  
  
## Public functions

### build

Added in 7.0.0
    
    
    fun [build](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder#build\(\))(): [DslExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension)

Builds the final `[DslExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension)` instance that can be used with the `[AndroidComponentsExtension.registerExtension](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidComponentsExtension#registerExtension\(com.android.build.api.variant.DslExtension,kotlin.Function1\))` API

### extendBuildTypeWith
    
    
    fun [extendBuildTypeWith](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder#extendBuildTypeWith\(java.lang.Class\))(typeExtension: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>): [DslExtension.Builder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder)

Registers an extension point for the `[com.android.build.api.dsl.BuildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType)`

### extendProductFlavorWith
    
    
    fun [extendProductFlavorWith](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder#extendProductFlavorWith\(java.lang.Class\))(typeExtension: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>): [DslExtension.Builder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder)

Registers an extension point for the `[com.android.build.api.dsl.ProductFlavor](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ProductFlavor)`

### extendProjectWith
    
    
    fun [extendProjectWith](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder#extendProjectWith\(java.lang.Class\))(typeExtension: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>): [DslExtension.Builder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DslExtension.Builder)

Registers an extension point for the module's DSL, it will be available under the android block.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
