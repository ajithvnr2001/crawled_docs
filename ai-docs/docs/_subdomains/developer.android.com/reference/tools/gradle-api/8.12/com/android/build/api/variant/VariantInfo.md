---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantInfo/
title: VariantInfo \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:10:02.397575+00:00
---

# VariantInfo  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantInfo/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# VariantInfo

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/VariantInfo.java+class:com.android.build.api.variant.VariantInfo)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    interface [VariantInfo](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantInfo)

* * *

**This interface is deprecated.**  


Information about the variant being built. 

Only the Android Gradle Plugin should create instances of this interface. 

Immutable, no access to tasks

## Summary

### Public functions  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  `[getBuildTypeName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantInfo#getBuildTypeName\(\))()` Returns the name of the build type.  
`[ImmutableList](https://guava.dev/releases/18.0/api/docs/com/google/common/collect/ImmutableList.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>!` |  `[getFlavorNames](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantInfo#getFlavorNames\(\))()` Returns a list of flavor names that make up this variant.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  `[getFullVariantName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantInfo#getFullVariantName\(\))()` Returns the name of the variant.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isDebuggable](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantInfo#isDebuggable\(\))()` Returns true if the variant is debuggable  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantInfo#isTest\(\))()` Returns true if this is a test variant  
  
## Public functions

### getBuildTypeName

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getBuildTypeName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantInfo#getBuildTypeName\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!

Returns the name of the build type. 

By convention, build-type settings should override flavor settings.

### getFlavorNames

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getFlavorNames](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantInfo#getFlavorNames\(\))(): [ImmutableList](https://guava.dev/releases/18.0/api/docs/com/google/common/collect/ImmutableList.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>!

Returns a list of flavor names that make up this variant. 

By convention settings from earlier flavors should override settings from later flavors.

Returns  
---  
`[ImmutableList](https://guava.dev/releases/18.0/api/docs/com/google/common/collect/ImmutableList.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>!` |  the ordered list of flavor names. May be empty.  
  
### getFullVariantName

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getFullVariantName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantInfo#getFullVariantName\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!

Returns the name of the variant. This is composed of the build types and flavors

### isDebuggable

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [isDebuggable](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantInfo#isDebuggable\(\))(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Returns true if the variant is debuggable

### isTest

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [isTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantInfo#isTest\(\))(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Returns true if this is a test variant

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
