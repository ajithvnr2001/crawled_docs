---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension/
title: AssetPackBundleExtension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:27:05.383965+00:00
---

# AssetPackBundleExtension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AssetPackBundleExtension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/AssetPackBundleExtension.kt+class:com.android.build.api.dsl.AssetPackBundleExtension)

Added in 7.0.0
    
    
    interface [AssetPackBundleExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension)

* * *

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[aiModelVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#aiModelVersion\(kotlin.Function1\))(action: [BundleAiModelVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleAiModelVersion).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[countrySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#countrySet\(kotlin.Function1\))(action: [BundleCountrySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCountrySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[deviceTier](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#deviceTier\(kotlin.Function1\))(action: [BundleDeviceTier](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleDeviceTier).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[signingConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#signingConfig\(kotlin.Function1\))(action: [SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[texture](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#texture\(kotlin.Function1\))(action: [BundleTexture](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleTexture).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
  
### Public properties  
  
---  
`[BundleAiModelVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleAiModelVersion)` |  `[aiModelVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#aiModelVersion\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[applicationId](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#applicationId\(\))`  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[assetPacks](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#assetPacks\(\))`  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#compileSdk\(\))`  
`[BundleCountrySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCountrySet)` |  `[countrySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#countrySet\(\))`  
`[BundleDeviceTier](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleDeviceTier)` |  `[deviceTier](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#deviceTier\(\))`  
`[SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig)` |  `[signingConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#signingConfig\(\))`  
`[BundleTexture](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleTexture)` |  `[texture](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#texture\(\))`  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)>` |  `[versionCodes](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#versionCodes\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[versionTag](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#versionTag\(\))`  
  
## Public functions

### aiModelVersion

Added in 8.7.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [aiModelVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#aiModelVersion\(kotlin.Function1\))(action: [BundleAiModelVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleAiModelVersion).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### countrySet

Added in 8.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [countrySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#countrySet\(kotlin.Function1\))(action: [BundleCountrySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCountrySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### deviceTier

Added in 7.0.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [deviceTier](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#deviceTier\(kotlin.Function1\))(action: [BundleDeviceTier](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleDeviceTier).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### signingConfig

Added in 7.0.0
    
    
    fun [signingConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#signingConfig\(kotlin.Function1\))(action: [SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### texture

Added in 7.0.0
    
    
    fun [texture](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#texture\(kotlin.Function1\))(action: [BundleTexture](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleTexture).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

## Public properties

### aiModelVersion

Added in 8.7.0
    
    
    val [aiModelVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#aiModelVersion\(\)): [BundleAiModelVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleAiModelVersion)

### applicationId

Added in 7.0.0
    
    
    var [applicationId](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#applicationId\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

### assetPacks

Added in 7.0.0
    
    
    val [assetPacks](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#assetPacks\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

### compileSdk

Added in 7.0.0
    
    
    var [compileSdk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#compileSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

### countrySet

Added in 8.1.0
    
    
    val [countrySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#countrySet\(\)): [BundleCountrySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCountrySet)

### deviceTier

Added in 7.0.0
    
    
    val [deviceTier](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#deviceTier\(\)): [BundleDeviceTier](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleDeviceTier)

### signingConfig

Added in 7.0.0
    
    
    val [signingConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#signingConfig\(\)): [SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig)

### texture

Added in 7.0.0
    
    
    val [texture](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#texture\(\)): [BundleTexture](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleTexture)

### versionCodes

Added in 7.0.0
    
    
    val [versionCodes](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#versionCodes\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)>

### versionTag

Added in 7.0.0
    
    
    var [versionTag](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackBundleExtension#versionTag\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
