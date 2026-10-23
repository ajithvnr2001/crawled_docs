---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScreenshotTestSuite/
title: ScreenshotTestSuite \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:20:16.307702+00:00
---

# ScreenshotTestSuite  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScreenshotTestSuite/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ScreenshotTestSuite

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/ScreenshotTestSuite.kt+class:com.android.build.api.variant.ScreenshotTestSuite)

Added in 9.5.0-alpha10
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [ScreenshotTestSuite](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScreenshotTestSuite) : [TestSuite](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite)

* * *

Model for screenshot test suites in the Variant API.

This object is accessible on subtypes of `[Variant](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/Variant)` that implement `[HasTestSuites](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HasTestSuites)`, via `[HasTestSuites.suites](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HasTestSuites#suites\(\))`.

## Summary

### Public properties  
  
---  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[engineVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScreenshotTestSuite#engineVersion\(\))` The version of the `com.android.tools.screenshot:screenshot-validation-junit-engine` artifact to use for layout rendering and screenshot validation.  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)>` |  `[imageDifferenceThreshold](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScreenshotTestSuite#imageDifferenceThreshold\(\))` The maximum allowed percentage difference between the reference image and the rendered image for a screenshot test to pass.  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
From [com.android.build.api.variant.TestSuite](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[configureTestTasks](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#configureTestTasks\(kotlin.Function2\))(action: [Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html).(context: [TestTaskContext](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TestTaskContext)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures the test tasks for this test target.  
---|---  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[instrumentationRunner](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#instrumentationRunner\(com.android.build.api.variant.TestSuiteSourceSet.TestApk\))(source: [TestSuiteSourceSet.TestApk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet.TestApk))` The instrumentationRunner to use to run the tests.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[withTestTaskProviders](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#withTestTaskProviders\(kotlin.Function2\))(action: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<[Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)>.(context: [TestTaskContext](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TestTaskContext)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Runs some action on the `[TestSuite](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite)` test task's `[TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)`.  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.TestSuite](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[codeCoverageEnabled](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#codeCoverageEnabled\(\))` Whether test coverage is enabled for this test suite.  
---|---  
`[JUnitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/JUnitEngineSpec)` |  `[junitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#junitEngineSpec\(\))` Return the `[JUnitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/JUnitEngineSpec)` for this test suite.  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[requiresUpdateTask](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#requiresUpdateTask\(\))` Whether this test suite requires an extra update task.  
`[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet)>` |  `[sources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#sources\(\))` Return the list of sourcesets associated with this test suite.  
`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [TestSuiteTarget](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteTarget)>` |  `[targets](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#targets\(\))` Return the list of `[TestSuiteTarget](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteTarget)` for this test suite in this variant.  
  
## Public properties

### engineVersion

Added in 9.5.0-alpha10
    
    
    val [engineVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScreenshotTestSuite#engineVersion\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The version of the `com.android.tools.screenshot:screenshot-validation-junit-engine` artifact to use for layout rendering and screenshot validation.

### imageDifferenceThreshold

Added in 9.5.0-alpha10
    
    
    val [imageDifferenceThreshold](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScreenshotTestSuite#imageDifferenceThreshold\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)>

The maximum allowed percentage difference between the reference image and the rendered image for a screenshot test to pass.

Specified as a floating-point value between `0.0f` (exact match required) and `1.0f` (100% difference allowed). For example, a value of `0.0001f` represents a 0.01% difference threshold.

Default value is `0.0f` (exact match required).

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
