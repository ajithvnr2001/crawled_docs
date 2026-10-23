---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicDelivery/
title: DynamicDelivery \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:17:39.625453+00:00
---

# DynamicDelivery  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicDelivery/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DynamicDelivery

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/DynamicDelivery.kt+class:com.android.build.api.dsl.DynamicDelivery)

Added in 4.2.0
    
    
    interface [DynamicDelivery](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicDelivery)

* * *

DSL object to configure dynamic delivery of an asset pack.

## Summary

### Public properties  
  
---  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[deliveryType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicDelivery#deliveryType\(\))` Identifies the delivery type {install-time, fast-follow, on-demand} when the asset pack is used with a persistent app.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[instantDeliveryType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicDelivery#instantDeliveryType\(\))` Identifies the delivery type {on-demand} when the asset pack is used with an instant app.  
  
## Public properties

### deliveryType

Added in 4.2.0
    
    
    val [deliveryType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicDelivery#deliveryType\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Identifies the delivery type {install-time, fast-follow, on-demand} when the asset pack is used with a persistent app.

### instantDeliveryType

Added in 4.2.0
    
    
    val [instantDeliveryType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/DynamicDelivery#instantDeliveryType\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Identifies the delivery type {on-demand} when the asset pack is used with an instant app.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
