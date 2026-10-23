---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector/
title: VariantSelector \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:03:24.980829+00:00
---

# VariantSelector  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# VariantSelector

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/VariantSelector.kt+class:com.android.build.api.variant.VariantSelector)

Added in 7.0.0
    
    
    interface [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)

* * *

Selector to reduce the number of variants that are of interests when calling any of the variant API like `[AndroidComponentsExtension.beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))`.

## Summary

### Public functions  
  
---  
`[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)` |  `[all](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector#all\(\))()` Creates a `[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)` of `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)` that includes all the variants for the current module.  
`[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)` |  `[withBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector#withBuildType\(kotlin.String\))(buildType: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Returns a new selector for `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)` objects with a given build type.  
`[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)` |  `[withFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector#withFlavor\(kotlin.Pair\))(dimensionToFlavor: [Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>)` Returns a new selector for `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)` objects with a given (dimension, flavorName).  
`[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)` |  `[withFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector#withFlavor\(kotlin.String,kotlin.String\))(dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), flavorName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Returns a new selector for `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)` objects with a given (flavorName).  
`[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)` |  `[withName](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector#withName\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Returns a new selector for `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)` objects with a given name.  
`[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)` |  `[withName](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector#withName\(java.util.regex.Pattern\))(pattern: [Pattern](https://developer.android.com/reference/tools/gradle-api/9.4/java/util/regex/Pattern))` Returns a new selector for `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)` objects with a given name pattern.  
  
## Public functions

### all

Added in 7.0.0
    
    
    fun [all](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector#all\(\))(): [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)

Creates a `[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)` of `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)` that includes all the variants for the current module.

Returns  
---  
`[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)` |  a `[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)` for all variants.  
  
### withBuildType

Added in 7.0.0
    
    
    fun [withBuildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector#withBuildType\(kotlin.String\))(buildType: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)

Returns a new selector for `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)` objects with a given build type.

Parameters  
---  
`buildType: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  Build type to filter `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)` on.  
  
Returns  
---  
`[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)` |  An instance of `[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)` to further filter variants.  
  
### withFlavor

Added in 7.0.0
    
    
    fun [withFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector#withFlavor\(kotlin.Pair\))(dimensionToFlavor: [Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>): [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)

Returns a new selector for `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)` objects with a given (dimension, flavorName).

Parameters  
---  
`dimensionToFlavor: [Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  Dimension and flavor to filter `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)` on.  
  
Returns  
---  
`[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)` |  `[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)` instance to further filter instances of `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)`  
  
### withFlavor

Added in 8.1.0
    
    
    fun [withFlavor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector#withFlavor\(kotlin.String,kotlin.String\))(dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), flavorName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)

Returns a new selector for `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)` objects with a given (flavorName).

Parameters  
---  
`dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  dimension name  
`flavorName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  flavor name to filter `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)` on.  
  
Returns  
---  
`[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)` |  `[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)` instance to further filter instances of `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)`  
  
### withName

Added in 7.0.0
    
    
    fun [withName](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector#withName\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)

Returns a new selector for `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)` objects with a given name.

Parameters  
---  
`name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` to test against the `[org.gradle.api.Named.getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)` for equality.  
  
### withName

Added in 7.0.0
    
    
    fun [withName](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector#withName\(java.util.regex.Pattern\))(pattern: [Pattern](https://developer.android.com/reference/tools/gradle-api/9.4/java/util/regex/Pattern)): [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantSelector)

Returns a new selector for `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)` objects with a given name pattern.

Parameters  
---  
`pattern: [Pattern](https://developer.android.com/reference/tools/gradle-api/9.4/java/util/regex/Pattern)` |  `[Pattern](https://developer.android.com/reference/tools/gradle-api/9.4/java/util/regex/Pattern)` to apply on the `[org.gradle.api.Named.getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)` to filter `[ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity)` instances on  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
