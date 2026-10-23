---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCodeTransparency/
title: BundleCodeTransparency \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:27:28.546538+00:00
---

# BundleCodeTransparency  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCodeTransparency/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BundleCodeTransparency

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/BundleCodeTransparency.kt+class:com.android.build.api.dsl.BundleCodeTransparency)

Added in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [BundleCodeTransparency](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCodeTransparency)

* * *

DSL object for configuring the App Bundle Code Transparency options

This is accessed via `[Bundle.codeTransparency](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Bundle#codeTransparency\(kotlin.Function1\))`

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[signing](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCodeTransparency#signing\(kotlin.Function1\))(action: [SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies the signing configuration for the code transparency feature of `bundletool`.  
  
### Public properties  
  
---  
`[SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig)` |  `[signing](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCodeTransparency#signing\(\))` Specifies the signing configuration for the code transparency feature of `bundletool`.  
  
## Public functions

### signing

Added in 7.1.0
    
    
    fun [signing](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCodeTransparency#signing\(kotlin.Function1\))(action: [SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies the signing configuration for the code transparency feature of `bundletool`.

When the `[SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig)` has all necessary values set, it will be used for signing non-debuggable bundles using code transparency.

## Public properties

### signing

Added in 7.1.0
    
    
    val [signing](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BundleCodeTransparency#signing\(\)): [SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig)

Specifies the signing configuration for the code transparency feature of `bundletool`.

When the `[SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig)` has all necessary values set, it will be used for signing non-debuggable bundles using code transparency.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
