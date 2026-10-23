---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ApplicationAndroidResources/
title: ApplicationAndroidResources \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:34:27.301331+00:00
---

# ApplicationAndroidResources  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ApplicationAndroidResources/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ApplicationAndroidResources

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/ApplicationAndroidResources.kt+class:com.android.build.api.variant.ApplicationAndroidResources)

Added in 8.4.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [ApplicationAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ApplicationAndroidResources) : [AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidResources)

* * *

Build-time properties for Android Resources inside a `[Component](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component)`. Specialization of `[AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidResources)` for modules that applied the `com.android.application` plugin.

This is accessed via `[GeneratesApk.androidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/GeneratesApk#androidResources\(\))`

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[generateLocaleConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ApplicationAndroidResources#generateLocaleConfig\(\))` Read-only property that automatically generates locale config when enabled.  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[localeFilters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ApplicationAndroidResources#localeFilters\(\))` Specifies a list of locales that resources will be kept for.  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidResources) | `[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[aaptAdditionalParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidResources#aaptAdditionalParameters\(\))` The list of additional parameters to pass to aapt.  
---|---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[dataBinding](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidResources#dataBinding\(\))` Flag indicating whether databinding feature is on  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[ignoreAssetsPatterns](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidResources#ignoreAssetsPatterns\(\))` The list of patterns describing assets to be ignored.  
`[ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[noCompress](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidResources#noCompress\(\))` File extensions of Android resources, assets, and Java resources to be stored uncompressed in the APK.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[viewBinding](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidResources#viewBinding\(\))` Flag indicating whether viewbinding feature is on  
  
## Public properties

### generateLocaleConfig

Added in 8.4.0
    
    
    val [generateLocaleConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ApplicationAndroidResources#generateLocaleConfig\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Read-only property that automatically generates locale config when enabled.

To set it, use `[ApplicationAndroidResourcesBuilder.generateLocaleConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ApplicationAndroidResourcesBuilder#generateLocaleConfig\(\))` in a `[AndroidComponentsExtension.beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` callback.

### localeFilters

Added in 8.8.0
    
    
    val [localeFilters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ApplicationAndroidResources#localeFilters\(\)): [SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Specifies a list of locales that resources will be kept for.

For example, if you are using a library that includes locale-specific resources (such as AppCompat or Google Play Services), then your APK includes all translated language strings for the messages in those libraries whether the rest of your app is translated to the same languages or not. If you'd like to keep only the languages that your app officially supports, you can specify those languages using the `localeFilters` property, as shown in the sample below. Any resources for locales not specified are not included in the build.
    
    
    androidComponents {  
        onVariants(selector().withName("release")) { variant ->  
            // Keeps language resources for the locales specified below.  
            variant.androidResources.localeFilters.addAll("en-rGB", "fr")  
        }  
    }

The locale must be specified either as (1) a two-letter ISO 639-1 language code, with the option to add a two-letter ISO 3166-1-alpha-2 region code preceded by "-r" (e.g. en-rUS), or (2) a BCP-47 language tag, which additionally allows you to specify a script subtag (e.g. b+sr+Latn+RS).

For more information on formulating locale qualifiers, see "Language, script (optional), and region (optional)" in the [alternative resources](https://d.android.com/r/tools/alternative-resources) table.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
