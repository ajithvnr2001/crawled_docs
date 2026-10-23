---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationAndroidResources/
title: ApplicationAndroidResources \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:50:07.974377+00:00
---

# ApplicationAndroidResources  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationAndroidResources/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ApplicationAndroidResources

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ApplicationAndroidResources.kt+class:com.android.build.api.dsl.ApplicationAndroidResources)

Added in 8.1.0
    
    
    interface [ApplicationAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationAndroidResources) : [AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources)

* * *

DSL object for configuring Android resource options for Application plugins.

This is accessed via `[ApplicationExtension.androidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationExtension#androidResources\(kotlin.Function1\))`

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[generateLocaleConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationAndroidResources#generateLocaleConfig\(\))` Property that automatically generates locale config when enabled.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[localeFilters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationAndroidResources#localeFilters\(\))` Specifies a list of locales that resources will be kept for.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#additionalParameters\(kotlin.String\))~~(params: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property additionalParameters  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#additionalParameters\(kotlin.Array\))~~(vararg params: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property additionalParameters  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[noCompress](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#noCompress\(kotlin.String\))~~(noCompress: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property noCompress  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[noCompress](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#noCompress\(kotlin.Array\))~~(vararg noCompress: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property noCompress  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources) | `[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#additionalParameters\(\))` List of additional parameters to pass to `aapt`.  
---|---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[failOnMissingConfigEntry](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#failOnMissingConfigEntry\(\))` Forces aapt to return an error if it fails to find an entry for a configuration.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[ignoreAssetsPattern](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#ignoreAssetsPattern\(\))` Pattern describing assets to be ignored.  
`[MutableCollection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[ignoreAssetsPatterns](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#ignoreAssetsPatterns\(\))` Patterns describing assets to be ignored.  
`[MutableCollection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[noCompress](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AndroidResources#noCompress\(\))` File extensions of Android resources, assets, and Java resources to be stored uncompressed in the APK.  
  
## Public properties

### generateLocaleConfig

Added in 8.1.0
    
    
    var [generateLocaleConfig](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationAndroidResources#generateLocaleConfig\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Property that automatically generates locale config when enabled.

### localeFilters

Added in 8.8.0
    
    
    val [localeFilters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationAndroidResources#localeFilters\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies a list of locales that resources will be kept for.

For example, if you are using a library that includes locale-specific resources (such as AppCompat or Google Play Services), then your APK includes all translated language strings for the messages in those libraries whether the rest of your app is translated to the same languages or not. If you'd like to keep only the languages that your app officially supports, you can specify those languages using the `localeFilters` property, as shown in the sample below. Any resources for locales not specified are not included in the build.
    
    
    android {  
        androidResources {  
            ...  
            // Keeps language resources for only the locales specified below.  
            localeFilters += listOf("en-rGB", "fr")  
        }  
    }

The locale must be specified either as (1) a two-letter ISO 639-1 language code, with the option to add a two-letter ISO 3166-1-alpha-2 region code preceded by "-r" (e.g. en-rUS), or (2) a BCP-47 language tag, which additionally allows you to specify a script subtag (e.g. b+sr+Latn+RS).

For more information on formulating locale qualifiers, see "Language, script (optional), and region (optional)" in the [alternative resources](https://d.android.com/r/tools/alternative-resources) table.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
