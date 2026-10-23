---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle/
title: Bundle \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:30:58.016970+00:00
---

# Bundle  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Bundle

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/Bundle.kt+class:com.android.build.api.dsl.Bundle)

Added in 4.2.0
    
    
    interface [Bundle](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle)

* * *

DSL object for configuring the Android Application Bundle

This is accessed via `[ApplicationExtension.bundle](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationExtension#bundle\(kotlin.Function1\))`

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[abi](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#abi\(kotlin.Function1\))(action: [BundleAbi](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleAbi).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[aiModelVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#aiModelVersion\(kotlin.Function1\))(action: [BundleAiModelVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleAiModelVersion).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[codeTransparency](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#codeTransparency\(kotlin.Function1\))(action: [BundleCodeTransparency](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleCodeTransparency).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[countrySet](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#countrySet\(kotlin.Function1\))(action: [BundleCountrySet](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleCountrySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[density](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#density\(kotlin.Function1\))(action: [BundleDensity](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleDensity).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[deviceGroup](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#deviceGroup\(kotlin.Function1\))(action: [BundleDeviceGroup](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleDeviceGroup).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[deviceTier](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#deviceTier\(kotlin.Function1\))~~(action: [BundleDeviceTier](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleDeviceTier).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Use deviceGroup instead  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[language](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#language\(kotlin.Function1\))(action: [BundleLanguage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleLanguage).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[storeArchive](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#storeArchive\(kotlin.Function1\))(action: [BundleStoreArchive](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleStoreArchive).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[texture](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#texture\(kotlin.Function1\))(action: [BundleTexture](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleTexture).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
  
### Public properties  
  
---  
`[BundleAbi](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleAbi)` |  `[abi](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#abi\(\))`  
`[BundleAiModelVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleAiModelVersion)` |  `[aiModelVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#aiModelVersion\(\))`  
`[BundleCodeTransparency](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleCodeTransparency)` |  `[codeTransparency](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#codeTransparency\(\))`  
`[BundleCountrySet](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleCountrySet)` |  `[countrySet](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#countrySet\(\))`  
`[BundleDensity](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleDensity)` |  `[density](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#density\(\))`  
`[BundleDeviceGroup](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleDeviceGroup)` |  `[deviceGroup](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#deviceGroup\(\))`  
`[RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)` |  `[deviceTargetingConfig](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#deviceTargetingConfig\(\))`  
`[BundleDeviceTier](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleDeviceTier)` |  `[deviceTier](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#deviceTier\(\))` **This property is deprecated.** Use deviceGroup instead  
`[DirectoryProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/DirectoryProperty.html)` |  `[integrityConfigDir](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#integrityConfigDir\(\))`  
`[BundleLanguage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleLanguage)` |  `[language](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#language\(\))`  
`[BundleStoreArchive](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleStoreArchive)` |  `[storeArchive](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#storeArchive\(\))`  
`[BundleTexture](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleTexture)` |  `[texture](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#texture\(\))`  
  
## Public functions

### abi

Added in 4.2.0
    
    
    fun [abi](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#abi\(kotlin.Function1\))(action: [BundleAbi](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleAbi).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### aiModelVersion

Added in 8.7.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [aiModelVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#aiModelVersion\(kotlin.Function1\))(action: [BundleAiModelVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleAiModelVersion).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### codeTransparency

Added in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [codeTransparency](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#codeTransparency\(kotlin.Function1\))(action: [BundleCodeTransparency](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleCodeTransparency).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### countrySet

Added in 8.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [countrySet](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#countrySet\(kotlin.Function1\))(action: [BundleCountrySet](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleCountrySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### density

Added in 4.2.0
    
    
    fun [density](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#density\(kotlin.Function1\))(action: [BundleDensity](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleDensity).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### deviceGroup

Added in 8.13.2
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [deviceGroup](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#deviceGroup\(kotlin.Function1\))(action: [BundleDeviceGroup](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleDeviceGroup).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### deviceTier

Added in 4.2.0

Deprecated in 8.13.2
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[deviceTier](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#deviceTier\(kotlin.Function1\))~~(action: [BundleDeviceTier](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleDeviceTier).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Use deviceGroup instead

### language

Added in 4.2.0
    
    
    fun [language](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#language\(kotlin.Function1\))(action: [BundleLanguage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleLanguage).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### storeArchive

Added in 7.3.0
    
    
    fun [storeArchive](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#storeArchive\(kotlin.Function1\))(action: [BundleStoreArchive](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleStoreArchive).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### texture

Added in 4.2.0
    
    
    fun [texture](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#texture\(kotlin.Function1\))(action: [BundleTexture](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleTexture).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

## Public properties

### abi

Added in 4.2.0
    
    
    val [abi](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#abi\(\)): [BundleAbi](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleAbi)

### aiModelVersion

Added in 8.7.0
    
    
    val [aiModelVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#aiModelVersion\(\)): [BundleAiModelVersion](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleAiModelVersion)

### codeTransparency

Added in 7.1.0
    
    
    val [codeTransparency](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#codeTransparency\(\)): [BundleCodeTransparency](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleCodeTransparency)

### countrySet

Added in 8.1.0
    
    
    val [countrySet](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#countrySet\(\)): [BundleCountrySet](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleCountrySet)

### density

Added in 4.2.0
    
    
    val [density](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#density\(\)): [BundleDensity](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleDensity)

### deviceGroup

Added in 8.13.2
    
    
    val [deviceGroup](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#deviceGroup\(\)): [BundleDeviceGroup](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleDeviceGroup)

### deviceTargetingConfig

Added in 8.13.2
    
    
    val [deviceTargetingConfig](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#deviceTargetingConfig\(\)): [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)

### deviceTier

Added in 4.2.0

Deprecated in 8.13.2
    
    
    val [deviceTier](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#deviceTier\(\)): [BundleDeviceTier](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleDeviceTier)

**This property is deprecated.**  
Use deviceGroup instead

### integrityConfigDir

Added in 7.2.0
    
    
    val [integrityConfigDir](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#integrityConfigDir\(\)): [DirectoryProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/DirectoryProperty.html)

### language

Added in 4.2.0
    
    
    val [language](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#language\(\)): [BundleLanguage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleLanguage)

### storeArchive

Added in 7.2.0
    
    
    val [storeArchive](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#storeArchive\(\)): [BundleStoreArchive](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleStoreArchive)

### texture

Added in 4.2.0
    
    
    val [texture](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Bundle#texture\(\)): [BundleTexture](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BundleTexture)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-11 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-11 UTC."],[],[]] 
