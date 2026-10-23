---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ScreenshotTestSuite/
title: ScreenshotTestSuite \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:55:31.777604+00:00
---

# ScreenshotTestSuite  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ScreenshotTestSuite/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ScreenshotTestSuite

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ScreenshotTestSuite.kt+class:com.android.build.api.dsl.ScreenshotTestSuite)

Added in 9.4.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [ScreenshotTestSuite](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ScreenshotTestSuite)

* * *

A test suite to run Compose screenshot tests.

A `[ScreenshotTestSuite](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ScreenshotTestSuite)` configures the execution environment and inputs required to render Compose previews and execute screenshot tests.

Example usage:
    
    
    android {  
        testOptions {  
            screenshotTests {  
                create("myScreenshotTest") {  
                    engineVersion = "1.0.0"  
                    targetVariants.add("debug")  
                    dependencies {  
                        implementation(project(":my-test-helpers"))  
                    }  
                }  
            }  
        }  
    }

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[dependencies](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ScreenshotTestSuite#dependencies\(kotlin.Function1\))(action: [AgpTestSuiteDependencies](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AgpTestSuiteDependencies).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures the dependencies for this test suite.  
  
### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[engineVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ScreenshotTestSuite#engineVersion\(\))` The version of the screenshot validation engine.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[targetVariants](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ScreenshotTestSuite#targetVariants\(\))` Defines which variants this test suite targets.  
  
## Public functions

### dependencies

Added in 9.4.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [dependencies](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ScreenshotTestSuite#dependencies\(kotlin.Function1\))(action: [AgpTestSuiteDependencies](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AgpTestSuiteDependencies).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures the dependencies for this test suite.

Dependencies are added to the test suite's host (JVM) execution classpath. This enables the screenshot tests to access custom test helpers and preview providers during rendering.

## Public properties

### engineVersion

Added in 9.4.1
    
    
    var [engineVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ScreenshotTestSuite#engineVersion\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The version of the screenshot validation engine.

Specifies the version of the `com.android.tools.screenshot:screenshot-validation-junit-engine` artifact (published on the Google Maven repository) to use for layout rendering and screenshot validation.

This property is mandatory. A valid version must be provided; otherwise, a Gradle sync error will be reported.

### targetVariants

Added in 9.4.1
    
    
    val [targetVariants](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ScreenshotTestSuite#targetVariants\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Defines which variants this test suite targets.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
