---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ApplicationAndroidResourcesBuilder/
title: ApplicationAndroidResourcesBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:06:28.590787+00:00
---

# ApplicationAndroidResourcesBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ApplicationAndroidResourcesBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ApplicationAndroidResourcesBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/ApplicationAndroidResourcesBuilder.kt+class:com.android.build.api.variant.ApplicationAndroidResourcesBuilder)

Added in 8.4.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [ApplicationAndroidResourcesBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ApplicationAndroidResourcesBuilder) : [AndroidResourcesBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AndroidResourcesBuilder)

* * *

Build-time properties for Android Resources inside a `[Component](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/Component)`. Specialization of `[AndroidResourcesBuilder](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/AndroidResourcesBuilder)` for modules that applied the `com.android.application` plugin.

This is accessed via `[ApplicationVariantBuilder.androidResources](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ApplicationVariantBuilder#androidResources\(\))`

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[generateLocaleConfig](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ApplicationAndroidResourcesBuilder#generateLocaleConfig\(\))` Property that automatically generates locale config when enabled.  
  
## Public properties

### generateLocaleConfig

Added in 8.4.0
    
    
    var [generateLocaleConfig](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/ApplicationAndroidResourcesBuilder#generateLocaleConfig\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Property that automatically generates locale config when enabled.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
