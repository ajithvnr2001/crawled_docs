---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteBuilder/
title: TestSuiteBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:20:42.290964+00:00
---

# TestSuiteBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestSuiteBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/TestSuiteBuilder.kt+class:com.android.build.api.variant.TestSuiteBuilder)

Added in 9.5.0-alpha10
    
    
    interface [TestSuiteBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteBuilder) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html)

* * *

Interface to configure `[TestSuite](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite)` during the `[AndroidComponentsExtension.beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` callbacks.

##  Usage example
    
    
    androidComponents.beforeVariants { variant ->  
        (variant as? HasTestSuites)?.suites.forEach { suiteBuilder ->  
             suiteBuilder.enable = false  
        }  
    }

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[setEnabledCodeCoverage](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteBuilder#setEnabledCodeCoverage\(kotlin.Boolean\))(value: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Specifies test suite code coverage data collection by configuring the JacocoPlugin.  
  
### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteBuilder#enable\(\))` Enables or disable the test suite for the current variant.  
`[JUnitEngineSpecBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/JUnitEngineSpecBuilder)` |  `[junitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteBuilder#junitEngineSpec\(\))` Configure the `[com.android.build.api.dsl.JUnitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/JUnitEngineSpec)` for this test suite in this variant.  
`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [TestSuiteTargetBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteTargetBuilder)>` |  `[targets](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteBuilder#targets\(\))` Configure the list of `[TestSuiteTargetBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteTargetBuilder)` for this test suite in this variant.  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
## Public functions

### setEnabledCodeCoverage

Added in 9.5.0-alpha10
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [setEnabledCodeCoverage](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteBuilder#setEnabledCodeCoverage\(kotlin.Boolean\))(value: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies test suite code coverage data collection by configuring the JacocoPlugin.

When enabled, the Jacoco plugin is applied and coverage data is collected by the Jacoco plugin.

If the value is initialized from the DSL `[com.android.build.api.dsl.AgpTestSuite.codeCoverage](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AgpTestSuite#codeCoverage\(\))`, it will be used.

## Public properties

### enable

Added in 9.5.0-alpha10
    
    
    var [enable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteBuilder#enable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Enables or disable the test suite for the current variant.

### junitEngineSpec

Added in 9.5.0-alpha10
    
    
    val [junitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteBuilder#junitEngineSpec\(\)): [JUnitEngineSpecBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/JUnitEngineSpecBuilder)

Configure the `[com.android.build.api.dsl.JUnitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/JUnitEngineSpec)` for this test suite in this variant.

### targets

Added in 9.5.0-alpha10
    
    
    val [targets](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteBuilder#targets\(\)): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [TestSuiteTargetBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteTargetBuilder)>

Configure the list of `[TestSuiteTargetBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteTargetBuilder)` for this test suite in this variant.

The `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)` keys are the test suite names.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
