---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension/
title: FusedLibraryExtension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:02:58.178203+00:00
---

# FusedLibraryExtension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# FusedLibraryExtension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/FusedLibraryExtension.kt+class:com.android.build.api.dsl.FusedLibraryExtension)

Added in 7.3.0
    
    
    interface [FusedLibraryExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension)

* * *

Public extension properties for Fused Library.

[Android Developers page for Fused Library](https://developer.android.com/build/publish-library/fused-library)

[API reference](https://developer.android.com/reference/tools/gradle-api/com/android/build/api/dsl/FusedLibraryExtension)

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[aarMetadata](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension#aarMetadata\(kotlin.Function1\))(action: [AarMetadata](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AarMetadata).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Options for configuring AAR metadata.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension#minSdk\(kotlin.Function1\))(action: [MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/MinSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures minSdk, see `[MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/MinSdkSpec)` for available options.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension#packaging\(kotlin.Function1\))(action: [Packaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Packaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options and rules that determine which files the Android plugin packages into your fused AAR.  
  
### Public properties  
  
---  
`[AarMetadata](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AarMetadata)` |  `[aarMetadata](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension#aarMetadata\(\))` Options for configuring AAR metadata.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[experimentalProperties](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension#experimentalProperties\(\))` Used to set module-specific experimental property values.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[manifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension#manifestPlaceholders\(\))` Map with Manifest placeholder key and placeholder resolved value.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[namespace](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension#namespace\(\))` Namespace of the Fused Library.  
`[Packaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Packaging)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension#packaging\(\))` Specifies options and rules that determine which files the Android plugin packages into your fused AAR.  
  
## Public functions

### aarMetadata

Added in 9.1.1
    
    
    fun [aarMetadata](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension#aarMetadata\(kotlin.Function1\))(action: [AarMetadata](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AarMetadata).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Options for configuring AAR metadata.

### minSdk

Added in 9.1.1
    
    
    fun [minSdk](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension#minSdk\(kotlin.Function1\))(action: [MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/MinSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures minSdk, see `[MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/MinSdkSpec)` for available options.

### packaging

Added in 9.1.1
    
    
    fun [packaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension#packaging\(kotlin.Function1\))(action: [Packaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Packaging).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options and rules that determine which files the Android plugin packages into your fused AAR.

For more information about the properties you can configure in this block, see `[Packaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Packaging)`.

## Public properties

### aarMetadata

Added in 9.1.1
    
    
    val [aarMetadata](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension#aarMetadata\(\)): [AarMetadata](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AarMetadata)

Options for configuring AAR metadata.

### experimentalProperties

Added in 9.1.1
    
    
    val [experimentalProperties](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension#experimentalProperties\(\)): [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>

Used to set module-specific experimental property values.

### manifestPlaceholders

Added in 9.1.1
    
    
    val [manifestPlaceholders](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension#manifestPlaceholders\(\)): [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Map with Manifest placeholder key and placeholder resolved value. See [Inject build variables into the manifest](https://developer.android.com/build/manage-manifests#inject_build_variables_into_the_manifest)

### namespace

Added in 7.3.0
    
    
    var [namespace](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension#namespace\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Namespace of the Fused Library.

### packaging

Added in 9.1.1
    
    
    val [packaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/FusedLibraryExtension#packaging\(\)): [Packaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Packaging)

Specifies options and rules that determine which files the Android plugin packages into your fused AAR.

For more information about the properties you can configure in this block, see `[Packaging](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Packaging)`.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-13 UTC."],[],[]] 
