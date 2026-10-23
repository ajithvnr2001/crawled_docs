---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AiPackExtension/
title: AiPackExtension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:26:07.085829+00:00
---

# AiPackExtension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AiPackExtension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AiPackExtension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/AiPackExtension.kt+class:com.android.build.api.dsl.AiPackExtension)

Added in 8.7.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [AiPackExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AiPackExtension)

* * *

Extension properties for the Asset Pack plugin that are specific to AI packs.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[dynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AiPackExtension#dynamicDelivery\(kotlin.Function1\))(action: [DynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DynamicDelivery).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[modelDependency](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AiPackExtension#modelDependency\(kotlin.Function1\))(action: [ModelDependency](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ModelDependency).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
  
### Public properties  
  
---  
`[DynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DynamicDelivery)` |  `[dynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AiPackExtension#dynamicDelivery\(\))` Contains the dynamic delivery settings for the AI pack.  
`[ModelDependency](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ModelDependency)` |  `[modelDependency](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AiPackExtension#modelDependency\(\))` The AI model which this AI pack depends upon.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[packName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AiPackExtension#packName\(\))` The split name to assign to the AI pack.  
  
## Public functions

### dynamicDelivery

Added in 8.7.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [dynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AiPackExtension#dynamicDelivery\(kotlin.Function1\))(action: [DynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DynamicDelivery).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

See also  
---  
`[dynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AiPackExtension#dynamicDelivery\(kotlin.Function1\))` |   
  
### modelDependency

Added in 8.7.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [modelDependency](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AiPackExtension#modelDependency\(kotlin.Function1\))(action: [ModelDependency](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ModelDependency).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

See also  
---  
`[modelDependency](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AiPackExtension#modelDependency\(kotlin.Function1\))` |   
  
## Public properties

### dynamicDelivery

Added in 8.7.0
    
    
    val [dynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AiPackExtension#dynamicDelivery\(\)): [DynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DynamicDelivery)

Contains the dynamic delivery settings for the AI pack.

### modelDependency

Added in 8.7.0
    
    
    val [modelDependency](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AiPackExtension#modelDependency\(\)): [ModelDependency](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ModelDependency)

The AI model which this AI pack depends upon.

### packName

Added in 8.7.0
    
    
    val [packName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AiPackExtension#packName\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The split name to assign to the AI pack.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
