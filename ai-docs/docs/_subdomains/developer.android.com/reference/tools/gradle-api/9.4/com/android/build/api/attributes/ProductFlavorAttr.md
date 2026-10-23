---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/attributes/ProductFlavorAttr/
title: ProductFlavorAttr \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:49:11.124586+00:00
---

# ProductFlavorAttr  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/attributes/ProductFlavorAttr/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ProductFlavorAttr

[View Source](https://cs.android.com/search?q=file:com/android/build/api/attributes/ProductFlavorAttr.kt+class:com.android.build.api.attributes.ProductFlavorAttr)

Added in 4.2.0
    
    
    interface [ProductFlavorAttr](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/attributes/ProductFlavorAttr) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html)

* * *

Type for the attribute holding ProductFlavor information.

There can be more than one attribute associated to each `[org.gradle.api.artifacts.Configuration](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)` object, where each represents a different flavor dimension.

The key should be created with `ProductFlavorAttr.of(flavorDimension)`.

## Summary

### Public companion functions  
  
---  
`[Attribute](https://docs.gradle.org/current/javadoc/org/gradle/api/attributes/Attribute.html)<[ProductFlavorAttr](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/attributes/ProductFlavorAttr)>` |  `[of](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/attributes/ProductFlavorAttr.Companion#of\(kotlin.String\))(flavorDimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Returns a product flavor attribute for the given flavor dimension  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
## Public companion functions

### of

Added in 7.1.0
    
    
    fun [of](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/attributes/ProductFlavorAttr.Companion#of\(kotlin.String\))(flavorDimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Attribute](https://docs.gradle.org/current/javadoc/org/gradle/api/attributes/Attribute.html)<[ProductFlavorAttr](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/attributes/ProductFlavorAttr)>

Returns a product flavor attribute for the given flavor dimension

Parameters  
---  
`flavorDimension: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  The name of the flavor dimension, as specified in the Android Gradle Plugin DSL.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
