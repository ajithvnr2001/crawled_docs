---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackExtension/
title: AssetPackExtension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:27:08.286772+00:00
---

# AssetPackExtension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackExtension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AssetPackExtension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/AssetPackExtension.kt+class:com.android.build.api.dsl.AssetPackExtension)

Added in 4.2.0
    
    
    interface [AssetPackExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackExtension)

* * *

Extension properties for the Asset Pack plugin.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[dynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackExtension#dynamicDelivery\(kotlin.Function1\))(action: [DynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DynamicDelivery).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
  
### Public properties  
  
---  
`[DynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DynamicDelivery)` |  `[dynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackExtension#dynamicDelivery\(\))` Contains the dynamic delivery settings for the asset pack.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[packName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackExtension#packName\(\))` The split name to assign to the asset pack.  
  
## Public functions

### dynamicDelivery

Added in 4.2.0
    
    
    fun [dynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackExtension#dynamicDelivery\(kotlin.Function1\))(action: [DynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DynamicDelivery).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

See also  
---  
`[dynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackExtension#dynamicDelivery\(kotlin.Function1\))` |   
  
## Public properties

### dynamicDelivery

Added in 4.2.0
    
    
    val [dynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackExtension#dynamicDelivery\(\)): [DynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DynamicDelivery)

Contains the dynamic delivery settings for the asset pack.

### packName

Added in 4.2.0
    
    
    val [packName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AssetPackExtension#packName\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The split name to assign to the asset pack.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
