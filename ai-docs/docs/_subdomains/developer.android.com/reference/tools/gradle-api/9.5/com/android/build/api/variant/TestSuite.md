---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite/
title: TestSuite \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:20:40.392214+00:00
---

# TestSuite  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestSuite

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/TestSuite.kt+class:com.android.build.api.variant.TestSuite)

Added in 9.5.0-alpha10
    
    
    interface [TestSuite](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html)

Known direct subclasses 

[ScreenshotTestSuite](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScreenshotTestSuite)

`[ScreenshotTestSuite](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/ScreenshotTestSuite)` |  Model for screenshot test suites in the Variant API.  
---|---  
  
* * *

Model for test suites.

This object is accessible on subtypes of `[Variant](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/Variant)` that implement `[HasTestSuites](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HasTestSuites)`, via `[HasTestSuites.suites](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HasTestSuites#suites\(\))`.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[configureTestTasks](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#configureTestTasks\(kotlin.Function2\))(action: [Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html).(context: [TestTaskContext](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TestTaskContext)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures the test tasks for this test target.  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[instrumentationRunner](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#instrumentationRunner\(com.android.build.api.variant.TestSuiteSourceSet.TestApk\))(source: [TestSuiteSourceSet.TestApk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet.TestApk))` The instrumentationRunner to use to run the tests.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[withTestTaskProviders](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#withTestTaskProviders\(kotlin.Function2\))(action: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<[Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)>.(context: [TestTaskContext](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TestTaskContext)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Runs some action on the `[TestSuite](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite)` test task's `[TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)`.  
  
### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[codeCoverageEnabled](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#codeCoverageEnabled\(\))` Whether test coverage is enabled for this test suite.  
`[JUnitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/JUnitEngineSpec)` |  `[junitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#junitEngineSpec\(\))` Return the `[JUnitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/JUnitEngineSpec)` for this test suite.  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[requiresUpdateTask](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#requiresUpdateTask\(\))` Whether this test suite requires an extra update task.  
`[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet)>` |  `[sources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#sources\(\))` Return the list of sourcesets associated with this test suite.  
`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [TestSuiteTarget](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteTarget)>` |  `[targets](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#targets\(\))` Return the list of `[TestSuiteTarget](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteTarget)` for this test suite in this variant.  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
## Public functions

### configureTestTasks

Added in 9.5.0-alpha10
    
    
    fun [configureTestTasks](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#configureTestTasks\(kotlin.Function2\))(action: [Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html).(context: [TestTaskContext](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TestTaskContext)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures the test tasks for this test target.

There can be one to many instances of `[org.gradle.api.tasks.testing.Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` tasks for a particular test suite target. For instance, if the test suite targets more than one device, AGP may decide to create one `[org.gradle.api.tasks.testing.Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` instance per device.

The configuration block can use the `[action](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#configureTestTasks\(kotlin.Function2\))`'s context parameter to disambiguate between each `[org.gradle.api.tasks.testing.Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` task instance.

Do not make assumption about how AGP decides to allocate `[org.gradle.api.tasks.testing.Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` task instances per device, as each AGP version can potentially change it in future release, always use the context object to determine what the `[org.gradle.api.tasks.testing.Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` task applies to.

Parameters  
---  
`action: [Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html).(context: [TestTaskContext](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TestTaskContext)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  a block to configure the `[org.gradle.api.tasks.testing.Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` tasks associated with this test suite target. Example :
    
    
    androidComponents {  
        onVariants { variant ->  
            variant.testSuites.forEach { testSuite ->  
                testSuite.configureTestTask { testTask ->  
                    testTask.beforeTest { descriptor ->  
                        println("Running test: " + descriptor)  
                    }  
                }  
            }  
        }  
    }  
  
`action: [Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html).(context: [TestTaskContext](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TestTaskContext)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  to configure the `[org.gradle.api.tasks.testing.Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` task.  
  
### instrumentationRunner

Added in 9.5.0-alpha10
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [instrumentationRunner](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#instrumentationRunner\(com.android.build.api.variant.TestSuiteSourceSet.TestApk\))(source: [TestSuiteSourceSet.TestApk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet.TestApk)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The instrumentationRunner to use to run the tests.

Returns  
---  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  the instrumentation test runner name  
  
### withTestTaskProviders

Added in 9.5.0-alpha10
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [withTestTaskProviders](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#withTestTaskProviders\(kotlin.Function2\))(action: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<[Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)>.(context: [TestTaskContext](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TestTaskContext)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Runs some action on the `[TestSuite](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite)` test task's `[TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)`.

The action will only run if the `[TestSuite](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite)` is enabled. In particular the corresponding `[TestSuiteBuilder.enable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteBuilder#enable\(\))` must be set to true (it is true by default).

This is particularly useful to set manual tasks dependencies. However, you should avoid calling `[TaskProvider.get](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html#get--)` as it will automatically configure the task even if it is not scheduled to run, instead use the configureTestTask method.

Example :
    
    
    androidComponents {  
        onVariants { variant ->  
            variant.suites.forEach { suite ->  
              suite.withTestTaskProvider { testTaskProvider ->  
                someAnchorTask.dependsOn(testTaskProvider)  
            }  
          }  
        }  
    }

Parameters  
---  
`action: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<[Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)>.(context: [TestTaskContext](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TestTaskContext)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  on the test task `[TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)`.  
  
## Public properties

### codeCoverageEnabled

Added in 9.5.0-alpha10
    
    
    val [codeCoverageEnabled](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#codeCoverageEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether test coverage is enabled for this test suite.

If enabled, this uses Jacoco to capture coverage and creates a report in the build directory.

You cannot change the value any longer, to change it, please use `[TestSuiteBuilder.setEnabledCodeCoverage](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteBuilder#setEnabledCodeCoverage\(kotlin.Boolean\))` in the `[AndroidComponentsExtension.beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` callback.

### junitEngineSpec

Added in 9.5.0-alpha10
    
    
    val [junitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#junitEngineSpec\(\)): [JUnitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/JUnitEngineSpec)

Return the `[JUnitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/JUnitEngineSpec)` for this test suite.

### requiresUpdateTask

Added in 9.5.0-alpha10
    
    
    val [requiresUpdateTask](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#requiresUpdateTask\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>

Whether this test suite requires an extra update task.

Initialized from the corresponding `[com.android.build.api.dsl.AgpTestSuite.requiresUpdateTask](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AgpTestSuite#requiresUpdateTask\(\))`

### sources

Added in 9.5.0-alpha10
    
    
    val [sources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#sources\(\)): [Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet)>

Return the list of sourcesets associated with this test suite. Sourcesets are added through the DSL using one of the following methods:

  * `[com.android.build.api.dsl.AgpTestSuite.assets](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AgpTestSuite#assets\(kotlin.Function1\))`

  * `[com.android.build.api.dsl.AgpTestSuite.hostJar](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AgpTestSuite#hostJar\(kotlin.Function1\))`

  * `[com.android.build.api.dsl.AgpTestSuite.testApk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AgpTestSuite#testApk\(kotlin.Function1\))`




The returned `[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)` of `[TestSuiteSourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteSourceSet)` is not specific to this variant but to the related `[TestSuite](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite)` instance, which may apply to multiple variants as specified through the `[com.android.build.api.dsl.AgpTestSuite.targetVariants](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AgpTestSuite#targetVariants\(\))` API.

### targets

Added in 9.5.0-alpha10
    
    
    val [targets](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuite#targets\(\)): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [TestSuiteTarget](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteTarget)>

Return the list of `[TestSuiteTarget](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/TestSuiteTarget)` for this test suite in this variant.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
