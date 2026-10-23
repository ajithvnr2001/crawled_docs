---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BundleTexture/
title: BundleTexture \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:45:34.383015+00:00
---

# BundleTexture  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BundleTexture/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BundleTexture

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/BundleTexture.kt+class:com.android.build.api.dsl.BundleTexture)

Added in 4.2.0
    
    
    interface [BundleTexture](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BundleTexture)

* * *

DSL object for configuring the App Bundle Texture options

This is accessed via `[Bundle.texture](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/Bundle#texture\(kotlin.Function1\))`

## Summary

### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[defaultFormat](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BundleTexture#defaultFormat\(\))` Specifies the default texture format to be used when it's not possible to deliver a format targeted to the device.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[enableSplit](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BundleTexture#enableSplit\(\))`  
  
## Public properties

### defaultFormat

Added in 4.2.0
    
    
    var [defaultFormat](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BundleTexture#defaultFormat\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Specifies the default texture format to be used when it's not possible to deliver a format targeted to the device. This is for example the case for standalone APKs, generated for pre-Lollipop devices.

If left empty or unspecified, the fallback folders (folders not containing a #tcf suffix) will be delivered to pre-Lollipop devices.

If the default format is set and not empty (for example, it's set to "etc2"), and a pre-Lollipop device does not support this format, then the app will be considered as not compatible and won't be installable.

since 4.1.0

### enableSplit

Added in 4.2.0
    
    
    var [enableSplit](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/BundleTexture#enableSplit\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
