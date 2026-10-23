---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LintBuilder/
title: LintBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:01:38.439818+00:00
---

# LintBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LintBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# LintBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/LintBuilder.kt+class:com.android.build.api.variant.LintBuilder)

Added in 9.4.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [LintBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LintBuilder)

* * *

Build-time configuration for lint.

This object is accessible on `[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantBuilder)` via `[VariantBuilder.lint](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantBuilder#lint\(\))`.

## Summary

### Public properties  
  
---  
`[LintReportsBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LintReportsBuilder)` |  `[reports](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LintBuilder#reports\(\))` Access to lint reports configuration.  
  
## Public properties

### reports

Added in 9.4.1
    
    
    val [reports](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LintBuilder#reports\(\)): [LintReportsBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LintReportsBuilder)

Access to lint reports configuration.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
