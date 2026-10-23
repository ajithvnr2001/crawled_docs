---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType
title: VariantOutputConfiguration.OutputType \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:12:15.891709+00:00
---

# VariantOutputConfiguration.OutputType  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# VariantOutputConfiguration.OutputType

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/VariantOutputConfiguration.kt+class:com.android.build.api.variant.VariantOutputConfiguration.OutputType)

Added in 4.2.0
    
    
    enum [VariantOutputConfiguration.OutputType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)  
|  ↳ | [com.android.build.api.variant.VariantOutputConfiguration.OutputType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType)  
  
* * *

The type of an output.

When support for Splits/Multi-APKs is turned on, the output will change from one `[SINGLE](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType#SINGLE)` output to multiple `[ONE_OF_MANY](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType#ONE_OF_MANY)` outputs, each with different `[filters](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration#filters\(\))` values.

In addition, if universal mode is on, then an additional `[OutputType.UNIVERSAL](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType#UNIVERSAL)` output can be found in the list.

## Summary

### Enum Values  
  
---  
`[ONE_OF_MANY](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType#ONE_OF_MANY)` |  Type of multiple output.  
`[SINGLE](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType#SINGLE)` |  Type for single output.  
`[UNIVERSAL](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType#UNIVERSAL)` |  Output for Universal APK.  
  
### Public functions  
  
---  
`[VariantOutputConfiguration.OutputType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType)` |  `[valueOf](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Returns the enum constant of this type with the specified name.  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[VariantOutputConfiguration.OutputType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType)>` |  `[values](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType#values\(\))()` Returns an array containing the constants of this enum type, in the order they're declared.  
  
## Enum Values

### ONE_OF_MANY
    
    
    val [VariantOutputConfiguration.OutputType.ONE_OF_MANY](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType#ONE_OF_MANY): [VariantOutputConfiguration.OutputType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType)

Type of multiple output. This type will be used by multiple outputs and each can be differentiated with `[VariantOutputConfiguration.filters](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration#filters\(\))`

### SINGLE
    
    
    val [VariantOutputConfiguration.OutputType.SINGLE](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType#SINGLE): [VariantOutputConfiguration.OutputType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType)

Type for single output. This is used when splits/multi-APK support is not turned on

### UNIVERSAL
    
    
    val [VariantOutputConfiguration.OutputType.UNIVERSAL](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType#UNIVERSAL): [VariantOutputConfiguration.OutputType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType)

Output for Universal APK. This is only valid if Splits/Multi-APK is on and universal mode was turned on (see `[com.android.build.api.dsl.AbiSplit.isUniversalApk](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AbiSplit#isUniversalApk\(\))`)

## Public functions

### valueOf

Added in 4.2.0
    
    
    fun [valueOf](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [VariantOutputConfiguration.OutputType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType)

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

Throws  
---  
`kotlin.IllegalArgumentException` |  if this enum type has no constant with the specified name  
  
### values

Added in 4.2.0
    
    
    fun [values](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType#values\(\))(): [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[VariantOutputConfiguration.OutputType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/VariantOutputConfiguration.OutputType)>

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
