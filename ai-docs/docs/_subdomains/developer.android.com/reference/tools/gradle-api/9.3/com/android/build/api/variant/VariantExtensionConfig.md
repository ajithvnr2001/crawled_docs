---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtensionConfig/
title: VariantExtensionConfig \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:39:02.613348+00:00
---

# VariantExtensionConfig  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtensionConfig/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# VariantExtensionConfig

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/VariantExtensionConfig.kt+class:com.android.build.api.variant.VariantExtensionConfig)

Added in 7.0.0
    
    
    interface [VariantExtensionConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtensionConfig)<VariantT : [Variant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Variant)>

* * *

Configuration object passed to the lambda responsible for creating a `[com.android.build.api.variant.VariantExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtension)` for each `[com.android.build.api.variant.Variant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Variant)` instance.

Parameters  
---  
`<VariantT : [Variant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Variant)>` |  the type of `[com.android.build.api.variant.Variant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Variant)` object.  
  
## Summary

### Public functions  
  
---  
`T` |  `<T : [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?> [buildTypeExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtensionConfig#buildTypeExtension\(java.lang.Class\))(extensionType: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<T>)` Returns the `[variant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtensionConfig#variant\(\))` specific extension registered through the `[com.android.build.api.variant.DslExtension.buildTypeExtensionType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DslExtension#buildTypeExtensionType\(\))` API.  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<T>` |  `<T : [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?> [productFlavorsExtensions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtensionConfig#productFlavorsExtensions\(java.lang.Class\))(extensionType: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<T>)` Returns the `[variant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtensionConfig#variant\(\))` specific extension registered through the `[com.android.build.api.variant.DslExtension.productFlavorExtensionType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DslExtension#productFlavorExtensionType\(\))` API.  
`T` |  `<T : [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?> [projectExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtensionConfig#projectExtension\(java.lang.Class\))(extensionType: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<T>)` Returns the project (across variants) extension registered through the `[com.android.build.api.variant.DslExtension.projectExtensionType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DslExtension#projectExtensionType\(\))` API.  
  
### Public properties  
  
---  
`VariantT` |  `[variant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtensionConfig#variant\(\))` Gets the variant object the `[com.android.build.api.variant.VariantExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtension)` should be associated with.  
  
## Public functions

### buildTypeExtension

Added in 7.0.0
    
    
    fun <T : [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?> [buildTypeExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtensionConfig#buildTypeExtension\(java.lang.Class\))(extensionType: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<T>): T

Returns the `[variant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtensionConfig#variant\(\))` specific extension registered through the `[com.android.build.api.variant.DslExtension.buildTypeExtensionType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DslExtension#buildTypeExtensionType\(\))` API.

Returns  
---  
`T` |  the custom extension for the `[variant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtensionConfig#variant\(\))`'s build type.  
  
### productFlavorsExtensions

Added in 7.0.0
    
    
    fun <T : [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?> [productFlavorsExtensions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtensionConfig#productFlavorsExtensions\(java.lang.Class\))(extensionType: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<T>): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<T>

Returns the `[variant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtensionConfig#variant\(\))` specific extension registered through the `[com.android.build.api.variant.DslExtension.productFlavorExtensionType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DslExtension#productFlavorExtensionType\(\))` API.

Returns  
---  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<T>` |  a `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)` of `[T](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtensionConfig#productFlavorsExtensions\(java.lang.Class\))` extension for all the defined product flavors in the project. The order of the elements is the same as the order of product flavors returned by the `[Variant.productFlavors](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Variant#productFlavors\(\))`  
  
### projectExtension

Added in 7.0.0
    
    
    fun <T : [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?> [projectExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtensionConfig#projectExtension\(java.lang.Class\))(extensionType: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<T>): T

Returns the project (across variants) extension registered through the `[com.android.build.api.variant.DslExtension.projectExtensionType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DslExtension#projectExtensionType\(\))` API.

## Public properties

### variant

Added in 7.0.0
    
    
    val [variant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtensionConfig#variant\(\)): VariantT

Gets the variant object the `[com.android.build.api.variant.VariantExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantExtension)` should be associated with.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
