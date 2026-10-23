---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MultipleVariants/
title: MultipleVariants \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:31:10.260953+00:00
---

# MultipleVariants  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MultipleVariants/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# MultipleVariants

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/MultipleVariants.kt+class:com.android.build.api.dsl.MultipleVariants)

Added in 7.1.0
    
    
    interface [MultipleVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MultipleVariants) : [PublishingOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/PublishingOptions)

* * *

Multi variant publishing options.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[allVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MultipleVariants#allVariants\(\))()` Publish all the variants to the component.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[includeBuildTypeValues](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MultipleVariants#includeBuildTypeValues\(kotlin.Array\))(vararg buildTypes: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Publish variants to the component based on the specified build types.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[includeFlavorDimensionAndValues](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MultipleVariants#includeFlavorDimensionAndValues\(kotlin.String,kotlin.Array\))(dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), vararg values: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Publish variants to the component based on the specified product flavor dimension and values.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.PublishingOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/PublishingOptions) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[withJavadocJar](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/PublishingOptions#withJavadocJar\(\))()` Publish javadoc jar generated from java & kotlin source as a secondary artifact to a Maven repository.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[withSourcesJar](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/PublishingOptions#withSourcesJar\(\))()` Publish java & kotlin sources jar as a secondary artifact to a Maven repository.  
  
## Public functions

### allVariants

Added in 7.1.0
    
    
    fun [allVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MultipleVariants#allVariants\(\))(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Publish all the variants to the component.

### includeBuildTypeValues

Added in 7.1.0
    
    
    fun [includeBuildTypeValues](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MultipleVariants#includeBuildTypeValues\(kotlin.Array\))(vararg buildTypes: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Publish variants to the component based on the specified build types.

### includeFlavorDimensionAndValues

Added in 7.1.0
    
    
    fun [includeFlavorDimensionAndValues](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MultipleVariants#includeFlavorDimensionAndValues\(kotlin.String,kotlin.Array\))(dimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), vararg values: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Publish variants to the component based on the specified product flavor dimension and values.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
