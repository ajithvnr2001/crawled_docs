---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/FilterConfiguration/
title: FilterConfiguration \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:08:53.427721+00:00
---

# FilterConfiguration  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/FilterConfiguration/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# FilterConfiguration

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/FilterConfiguration.kt+class:com.android.build.api.variant.FilterConfiguration)

Added in 4.2.0
    
    
    interface [FilterConfiguration](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/FilterConfiguration)

* * *

Immutable filter configuration.

## Summary

### Nested types  
  
---  
`enum [FilterConfiguration.FilterType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/FilterConfiguration.FilterType) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)` Split dimension type  
  
### Public properties  
  
---  
`[FilterConfiguration.FilterType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/FilterConfiguration.FilterType)` |  `[filterType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/FilterConfiguration#filterType\(\))` Returns the `[FilterType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/FilterConfiguration.FilterType)` for this filter configuration.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[identifier](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/FilterConfiguration#identifier\(\))` Returns the identifier for this filter.  
  
## Public properties

### filterType

Added in 4.2.0
    
    
    val [filterType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/FilterConfiguration#filterType\(\)): [FilterConfiguration.FilterType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/FilterConfiguration.FilterType)

Returns the `[FilterType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/FilterConfiguration.FilterType)` for this filter configuration.

### identifier

Added in 4.2.0
    
    
    val [identifier](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/FilterConfiguration#identifier\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Returns the identifier for this filter. The filter identifier is dependent on the `[FilterConfiguration.filterType](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/FilterConfiguration#filterType\(\))`.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
