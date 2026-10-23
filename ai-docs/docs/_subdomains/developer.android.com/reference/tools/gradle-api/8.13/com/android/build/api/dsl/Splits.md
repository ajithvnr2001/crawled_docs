---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits/
title: Splits \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:35:10.509247+00:00
---

# Splits  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Splits

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/Splits.kt+class:com.android.build.api.dsl.Splits)

Added in 4.2.0
    
    
    interface [Splits](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits)

* * *

Options to configure Multiple APKs.

`[`android`](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#splits\(kotlin.Function1\))``.``[`splits`](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits)`

If you publish your app to Google Play, you should build and upload an [Android App Bundle](https://developer.android.com/guide/app-bundle). When you do so, Google Play automatically generates and serves optimized APKs for each user’s device configuration, so they download only the code and resources they need to run your app. This is much simpler than managing multiple APKs manually.

If you publish your app to a store that doesn't support the Android App Bundle format, you can publish [multiple APKs](https://developer.android.com/studio/build/configure-apk-splits.html) manually.

The Android Gradle plugin supports generating multiple APKs based on screen density and [Application Binary Interface (ABI)](https://developer.android.com/ndk/guides/abis.html), where each APK contains the code and resources required for a given device configuration.

You will also need to [assign version codes to each APK](https://developer.android.com/studio/build/configure-apk-splits.html#configure-APK-versions) so that you are able to manage updates later.

Previously the Android Gradle plugin also supported building 'Configuration APKs' for Instant Apps using this `splits` block, but that has been superseded by the Android App Bundle format.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[abi](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits#abi\(kotlin.Function1\))(action: [AbiSplit](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AbiSplit).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates settings for [building per-ABI APKs](https://developer.android.com/studio/build/configure-apk-splits.html#configure-abi-split).  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[density](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits#density\(kotlin.Function1\))(action: [DensitySplit](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DensitySplit).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Encapsulates settings for [building per-density APKs](https://developer.android.com/studio/build/configure-apk-splits.html#configure-density-split).  
  
### Public properties  
  
---  
`[AbiSplit](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AbiSplit)` |  `[abi](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits#abi\(\))` Encapsulates settings for [building per-ABI APKs](https://developer.android.com/studio/build/configure-apk-splits.html#configure-abi-split).  
`[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[abiFilters](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits#abiFilters\(\))` Returns the list of ABIs that the plugin will generate separate APKs for.  
`[DensitySplit](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DensitySplit)` |  `[density](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits#density\(\))` Encapsulates settings for [building per-density APKs](https://developer.android.com/studio/build/configure-apk-splits.html#configure-density-split).  
`[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[densityFilters](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits#densityFilters\(\))` Returns the list of screen density configurations that the plugin will generate separate APKs for.  
  
## Public functions

### abi

Added in 4.2.0
    
    
    fun [abi](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits#abi\(kotlin.Function1\))(action: [AbiSplit](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AbiSplit).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Encapsulates settings for [building per-ABI APKs](https://developer.android.com/studio/build/configure-apk-splits.html#configure-abi-split).

For more information about the properties you can configure in this block, see `[AbiSplit](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AbiSplit)`.

### density

Added in 4.2.0
    
    
    fun [density](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits#density\(kotlin.Function1\))(action: [DensitySplit](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DensitySplit).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Encapsulates settings for [building per-density APKs](https://developer.android.com/studio/build/configure-apk-splits.html#configure-density-split).

For more information about the properties you can configure in this block, see `[DensitySplit](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DensitySplit)`.

## Public properties

### abi

Added in 4.2.0
    
    
    val [abi](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits#abi\(\)): [AbiSplit](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/AbiSplit)

Encapsulates settings for [building per-ABI APKs](https://developer.android.com/studio/build/configure-apk-splits.html#configure-abi-split).

### abiFilters

Added in 4.2.0
    
    
    val [abiFilters](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits#abiFilters\(\)): [Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Returns the list of ABIs that the plugin will generate separate APKs for.

If this property returns `null`, it means the plugin will not generate separate per-ABI APKs. That is, each APK will include binaries for all ABIs your project supports.

Returns  
---  
`[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  a set of ABIs.  
  
### density

Added in 4.2.0
    
    
    val [density](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits#density\(\)): [DensitySplit](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/DensitySplit)

Encapsulates settings for [building per-density APKs](https://developer.android.com/studio/build/configure-apk-splits.html#configure-density-split).

### densityFilters

Added in 4.2.0
    
    
    val [densityFilters](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Splits#densityFilters\(\)): [Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Returns the list of screen density configurations that the plugin will generate separate APKs for.

If this property returns `null`, it means the plugin will not generate separate per-density APKs. That is, each APK will include resources for all screen density configurations your project supports.

Returns  
---  
`[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  a set of screen density configurations.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
