---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DslExtension/
title: DslExtension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:27:14.740653+00:00
---

# DslExtension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DslExtension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DslExtension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/DslExtension.kt+class:com.android.build.api.variant.DslExtension)

Added in 7.0.0
    
    
    class [DslExtension](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DslExtension)

* * *

Third party DSL extension configuration.

When a third party plugins needs to extend the Android Gradle Plugin DSL, it needs to indicate the location of these extension elements.

Currently, we support extending :

  * [com.android.build.api.dsl.DefaultConfig]
  * [com.android.build.api.dsl.BuildType]
  * [com.android.build.api.dsl.ProductFlavor]



A plugin can choose to extend one or more of these elements by calling the appropriate methods on the `[Builder](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DslExtension.Builder)` like `[Builder.extendBuildTypeWith](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DslExtension.Builder#extendBuildTypeWith\(java.lang.Class\))` to extend `[com.android.build.api.dsl.BuildType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BuildType)`.

Because the number of instances of each extension point is determined during evaluation phase, Gradle will be creating those instances on demand. See full documentation at : https://docs.gradle.org/current/userguide/custom_plugins.html#sec:getting_input_from_the_build

## Summary

### Nested types  
  
---  
`class [DslExtension.Builder](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DslExtension.Builder)` Creates a `[Builder](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DslExtension.Builder)` to instance to create a `[DslExtension](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DslExtension)` containing all desired extension points to the Android Gradle Plugin DSL.  
  
### Public properties  
  
---  
`[Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>?` |  `[buildTypeExtensionType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DslExtension#buildTypeExtensionType\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[dslName](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DslExtension#dslName\(\))`  
`[Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>?` |  `[productFlavorExtensionType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DslExtension#productFlavorExtensionType\(\))`  
`[Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>?` |  `[projectExtensionType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DslExtension#projectExtensionType\(\))`  
  
## Public properties

### buildTypeExtensionType

Added in 7.0.0
    
    
    val [buildTypeExtensionType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DslExtension#buildTypeExtensionType\(\)): [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>?

### dslName

Added in 7.0.0
    
    
    val [dslName](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DslExtension#dslName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

### productFlavorExtensionType

Added in 7.0.0
    
    
    val [productFlavorExtensionType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DslExtension#productFlavorExtensionType\(\)): [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>?

### projectExtensionType

Added in 7.0.0
    
    
    val [projectExtensionType](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DslExtension#projectExtensionType\(\)): [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>?

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
