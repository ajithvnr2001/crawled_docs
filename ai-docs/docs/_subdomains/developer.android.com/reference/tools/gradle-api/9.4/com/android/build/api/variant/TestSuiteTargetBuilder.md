---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteTargetBuilder/
title: TestSuiteTargetBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:02:46.966852+00:00
---

# TestSuiteTargetBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteTargetBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestSuiteTargetBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/TestSuiteTargetBuilder.kt+class:com.android.build.api.variant.TestSuiteTargetBuilder)

Added in 9.4.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [TestSuiteTargetBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteTargetBuilder) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html)

* * *

Test suite target builder.

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteTargetBuilder#enable\(\))`  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[targetDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteTargetBuilder#targetDevices\(\))` Targeted devices for this test suite in this variant.  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
## Public properties

### enable

Added in 9.4.1
    
    
    var [enable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteTargetBuilder#enable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

### targetDevices

Added in 9.4.1
    
    
    val [targetDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteTargetBuilder#targetDevices\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Targeted devices for this test suite in this variant.

AGP may choose to allocate multiple Test tasks for running the test suites depending on the targeted devices, so the list of devices must be fixed before the `[AndroidComponentsExtension.onVariants](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` run.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
