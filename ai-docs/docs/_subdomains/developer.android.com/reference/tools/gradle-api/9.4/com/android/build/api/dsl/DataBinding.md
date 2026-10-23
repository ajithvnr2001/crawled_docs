---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding/
title: DataBinding \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:51:51.981072+00:00
---

# DataBinding  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DataBinding

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/DataBinding.kt+class:com.android.build.api.dsl.DataBinding)

Added in 4.2.0
    
    
    interface [DataBinding](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding)

* * *

DSL object for configuring databinding options.

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[addDefaultAdapters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding#addDefaultAdapters\(\))` Whether to add the default data binding adapters.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[addKtx](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding#addKtx\(\))` Whether to add the data binding KTX features.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding#enable\(\))` Whether to enable data binding.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableForTests](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding#enableForTests\(\))` Whether to run data binding code generation for test projects.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isEnabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding#isEnabled\(\))` **This property is deprecated.** deprecated, use enable  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isEnabledForTests](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding#isEnabledForTests\(\))` **This property is deprecated.** deprecated, use enableForTests  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[version](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding#version\(\))` The version of data binding to use.  
  
## Public properties

### addDefaultAdapters

Added in 4.2.0
    
    
    var [addDefaultAdapters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding#addDefaultAdapters\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether to add the default data binding adapters.

### addKtx

Added in 7.0.0
    
    
    var [addKtx](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding#addKtx\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Whether to add the data binding KTX features. A null value means that the user hasn't specified any value in the DSL. The default value can be tweaked globally using the `android.defaults.databinding.addKtx` gradle property.

### enable

Added in 7.3.0
    
    
    var [enable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding#enable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether to enable data binding.

### enableForTests

Added in 7.3.0
    
    
    var [enableForTests](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding#enableForTests\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether to run data binding code generation for test projects.

### isEnabled

Added in 4.2.0

Deprecated in 7.3.0
    
    
    var [isEnabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding#isEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
deprecated, use enable

### isEnabledForTests

Added in 4.2.0

Deprecated in 7.3.0
    
    
    var [isEnabledForTests](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding#isEnabledForTests\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
deprecated, use enableForTests

### version

Added in 4.2.0
    
    
    var [version](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DataBinding#version\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The version of data binding to use.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
