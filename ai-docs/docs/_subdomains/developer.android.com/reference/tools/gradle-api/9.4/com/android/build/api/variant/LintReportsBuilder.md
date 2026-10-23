---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LintReportsBuilder/
title: LintReportsBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:01:44.564398+00:00
---

# LintReportsBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LintReportsBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# LintReportsBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/LintReportsBuilder.kt+class:com.android.build.api.variant.LintReportsBuilder)

Added in 9.4.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [LintReportsBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LintReportsBuilder)

* * *

Build-time configuration for lint reports.

This object is accessible on `[LintBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LintBuilder)` via `[LintBuilder.reports](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LintBuilder#reports\(\))`.

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableReportWithDependencies](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LintReportsBuilder#enableReportWithDependencies\(\))` Whether the lint report task that includes dependencies should be enabled for this variant.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableReportWithoutDependencies](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LintReportsBuilder#enableReportWithoutDependencies\(\))` Whether the local lint report task (which excludes dependencies) should be enabled for this variant.  
  
## Public properties

### enableReportWithDependencies

Added in 9.4.1
    
    
    var [enableReportWithDependencies](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LintReportsBuilder#enableReportWithDependencies\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether the lint report task that includes dependencies should be enabled for this variant.

Only has an effect if `[VariantBuilder.enableLint](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantBuilder#enableLint\(\))` is also true and the Gradle property android.experimental.lint.lintReportAggregation is enabled.

Defaults to `true`.

### enableReportWithoutDependencies

Added in 9.4.1
    
    
    var [enableReportWithoutDependencies](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LintReportsBuilder#enableReportWithoutDependencies\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether the local lint report task (which excludes dependencies) should be enabled for this variant.

Only has an effect if `[VariantBuilder.enableLint](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantBuilder#enableLint\(\))` is also true and the Gradle property android.experimental.lint.lintReportAggregation is enabled.

Defaults to `true`.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
