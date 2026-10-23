---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantFilter/
title: VariantFilter \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:11:44.696204+00:00
---

# VariantFilter  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantFilter/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# VariantFilter

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/VariantFilter.kt+class:com.android.build.api.variant.VariantFilter)

Added in 4.2.0

Deprecated in 7.2.0
    
    
    interface [VariantFilter](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantFilter)

* * *

**This interface is deprecated.**  
Use AndroidComponentsExtension.beforeVariants API to disable specific variants

Interface for variant control, allowing to query a variant for some base data and allowing to disable some variants.

## Summary

### Public properties  
  
---  
`[BuildType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/builder/model/BuildType)` |  `[buildType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantFilter#buildType\(\))` Returns the Build Type.  
`[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/builder/model/ProductFlavor)` |  `[defaultConfig](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantFilter#defaultConfig\(\))` Returns the ProductFlavor that represents the default config.  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/builder/model/ProductFlavor)>` |  `[flavors](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantFilter#flavors\(\))` Returns the list of flavors, or an empty list.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[ignore](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantFilter#ignore\(\))` Whether or not to ignore this particular variant.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantFilter#name\(\))` Returns the unique variant name.  
  
## Public properties

### buildType

Added in 4.2.0

Deprecated in 7.2.0
    
    
    val [buildType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantFilter#buildType\(\)): [BuildType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/builder/model/BuildType)

Returns the Build Type.

### defaultConfig

Added in 4.2.0

Deprecated in 7.2.0
    
    
    val [defaultConfig](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantFilter#defaultConfig\(\)): [ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/builder/model/ProductFlavor)

Returns the ProductFlavor that represents the default config.

### flavors

Added in 4.2.0

Deprecated in 7.2.0
    
    
    val [flavors](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantFilter#flavors\(\)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[ProductFlavor](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/builder/model/ProductFlavor)>

Returns the list of flavors, or an empty list.

### ignore

Added in 4.2.0

Deprecated in 7.2.0
    
    
    var [ignore](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantFilter#ignore\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether or not to ignore this particular variant. Default is false.

### name

Added in 4.2.0

Deprecated in 7.2.0
    
    
    val [name](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantFilter#name\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Returns the unique variant name.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
