---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder/
title: HostTestBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:39:49.686780+00:00
---

# HostTestBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# HostTestBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/HostTestBuilder.kt+class:com.android.build.api.variant.HostTestBuilder)

Added in 8.5.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [HostTestBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder)

* * *

Interface to turn on or off host tests. Host tests run on the development machine, `[UNIT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder.Companion#UNIT_TEST_TYPE\(\))` or `[SCREENSHOT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder.Companion#SCREENSHOT_TEST_TYPE\(\))` are examples of host tests.

## Summary

### Constants  
  
---  
`const [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[SCREENSHOT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder.Companion#SCREENSHOT_TEST_TYPE\(\))` Host test type for default screenshot tests.  
`const [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[UNIT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder.Companion#UNIT_TEST_TYPE\(\))` Host test type for default unit tests.  
  
### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder#enable\(\))` Set to `true` if the variant's has any host tests, false otherwise.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableCodeCoverage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder#enableCodeCoverage\(\))` Specifies host test code coverage data collection by configuring the JacocoPlugin.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[type](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder#type\(\))` Type of the `[HostTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTest)`, which can be '`[UNIT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder.Companion#UNIT_TEST_TYPE\(\))` or `[SCREENSHOT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder.Companion#SCREENSHOT_TEST_TYPE\(\))` for `[HostTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTest)`s created by AGP.  
  
## Constants

### SCREENSHOT_TEST_TYPE

Added in 8.5.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    const val [SCREENSHOT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder.Companion#SCREENSHOT_TEST_TYPE\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Host test type for default screenshot tests.

### UNIT_TEST_TYPE

Added in 8.5.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    const val [UNIT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder.Companion#UNIT_TEST_TYPE\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Host test type for default unit tests.

## Public properties

### enable

Added in 8.5.0
    
    
    var [enable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder#enable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Set to `true` if the variant's has any host tests, false otherwise.

Not setting this value relies on the AGP default behavior for this host test type.

### enableCodeCoverage

Added in 8.5.0

Deprecated in 8.5.0
    
    
    var [enableCodeCoverage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder#enableCodeCoverage\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Specifies host test code coverage data collection by configuring the JacocoPlugin.

When enabled, the Jacoco plugin is applied and coverage data is collected by the Jacoco plugin. This can avoid unwanted build time instrumentation required to collect coverage data from other test types such as connected tests.

If the value is initialized from the DSL `[com.android.build.api.dsl.BuildType.enableUnitTestCoverage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/BuildType#enableUnitTestCoverage\(\))`, it will be used for `[HostTestBuilder.UNIT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder.Companion#UNIT_TEST_TYPE\(\))`.

### type

Added in 8.5.0
    
    
    val [type](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder#type\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Type of the `[HostTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTest)`, which can be '`[UNIT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder.Companion#UNIT_TEST_TYPE\(\))` or `[SCREENSHOT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTestBuilder.Companion#SCREENSHOT_TEST_TYPE\(\))` for `[HostTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/HostTest)`s created by AGP.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
