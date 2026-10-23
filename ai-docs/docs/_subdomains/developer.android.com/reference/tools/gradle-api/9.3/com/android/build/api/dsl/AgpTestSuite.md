---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite/
title: AgpTestSuite \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:26:01.017370+00:00
---

# AgpTestSuite  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AgpTestSuite

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/AgpTestSuite.kt+class:com.android.build.api.dsl.AgpTestSuite)

Added in 9.3.3
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [AgpTestSuite](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite) : [TestSuite](https://docs.gradle.org/current/javadoc/org/gradle/testing/base/TestSuite.html)

* * *

A test suite that runs with the Android Gradle Plugin.

An `[AgpTestSuite](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite)` can run against a single or multiple variants. Users should use `[com.android.build.api.dsl.AgpTestSuite.targetVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#targetVariants\(\))` to identify the final list of variants that will be tested.

Although this is not strictly necessary, if the test suite has source code, it will be recompiled for each variant it targets. This is to ensure the compatibility of the test suite with each variant individually.

Defines how different types of source files are organized and declared for a test suite within the Android Gradle Plugin. Test suites can incorporate various kinds of sources, each serving a distinct purpose and following specific conventions.

All sources for a given test suite (e.g., one named `myTestSuite`) are typically organized under the `src/myTestSuite/` directory, relative to the module's root. Within this directory, specific source types will reside in conventional subdirectories.

Three primary types of sources can be associated with a test suite using the methods on this interface:

  1. **Asset Test Sources (configured via`assets`)**:

     * **Content** : A single folder containing static files like XML, JSON, or other declarative resources that describe or support tests. These files are not compiled.

     * **Purpose** : Typically interpreted directly by test execution engines (e.g., JUnit).

     * **Default Location** : `src/<testSuiteName>/assets/`

  2. **Host Test Sources (configured via`hostJar`)**:

     * **Content** : A single folder containing compilable source code (e.g., Kotlin or Java) intended for tests that run on the host machine (JVM).

     * **Purpose** : Compiled before test execution. The compiled classes are then used by test engines.

     * **Default Location** : `src/<testSuiteName>/` (which would then contain standard source layouts like `java/`, `kotlin/`, `resources/`)

  3. **Device Test Sources (configured via`testApk`)**:

     * **Content** : A standard Android source set structure, including compilable source code (Kotlin/Java), Android resources (`res/`), Android assets (`assets/`), and an AndroidManifest.xml file.

     * **Purpose** : Compiled into a test APK that runs on an Android device or emulator.

     * **Default Location** : `src/<testSuiteName>/androidTest/` (which would then contain standard Android source layouts like `java/`, `res/`, `assets/`, etc.)




**Configuration Notes:**

  * A test suite can include one or more of these source types. For example, a suite might define both `hostTest` sources and `assetTest` sources.

  * Currently, it is not possible to declare the same type of source (e.g., two `hostTest` blocks) for a single test suite.

  * Future versions of this API may introduce more flexibility, such as allowing multiple instances of the same source type or providing ways to customize the default directory names.




Test execution engines can retrieve the locations or outputs of these configured sources through properties defined in `com.android.build.api.variant.AgpTestSuiteInputParameters` (e.g., `STATIC_FILES`, `TEST_CLASSES`, `TESTED_APKS`). *

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[assets](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#assets\(kotlin.Function1\))(action: [TestSuiteAssetsSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestSuiteAssetsSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Adds an asset folder to this test suite sources, containing static sources like xml, or json files.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[configureTestTasks](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#configureTestTasks\(kotlin.Function2\))(action: [Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html).(context: [TestTaskContext](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestTaskContext)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configure the test tasks for this test target.  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[AgpTestSuiteTarget](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteTarget)>` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[getTargets](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#getTargets\(\))()` Targets for this test suite, must be manually created in order to provide the variants this test suite applies to.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[hostJar](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#hostJar\(kotlin.Function1\))(action: [TestSuiteHostJarSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestSuiteHostJarSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Adds a host test folder to this test suite sources, containing kotlin sources that will be compiled.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[testApk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#testApk\(kotlin.Function1\))(action: [TestSuiteTestApkSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestSuiteTestApkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Adds a device test source folder to this test suite, containing all necessary sources to create an APK.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[useJunitEngine](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#useJunitEngine\(kotlin.Function1\))(action: [JUnitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JUnitEngineSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies properties for the JUnit test engines to run in this test suite  
  
### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[codeCoverage](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#codeCoverage\(\))` Turns on or off the code coverage support.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[targetVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#targetVariants\(\))` Defines which variant this tests suite targets.  
`[JUnitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JUnitEngineSpec)` |  `[useJunitEngine](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#useJunitEngine\(\))` Spec to identify the test engine that will be used to run this test suite.  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
## Public functions

### assets

Added in 9.3.3
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [assets](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#assets\(kotlin.Function1\))(action: [TestSuiteAssetsSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestSuiteAssetsSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds an asset folder to this test suite sources, containing static sources like xml, or json files.

The folder will be named 'assets' by default and will be therefore located at `src/<testSuiteName>/assets/`

No compilation of the sources will be performed and the sources files will be provided to the configured junit engines using the `[AgpTestSuiteInputParameters.STATIC_FILES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#STATIC_FILES)`

### configureTestTasks

Added in 9.3.3
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [configureTestTasks](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#configureTestTasks\(kotlin.Function2\))(action: [Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html).(context: [TestTaskContext](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestTaskContext)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configure the test tasks for this test target.

There can be one to many instances of `[Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` tasks for a particular test suite target. For instance, if the test suite targets more than one device, AGP may decide to create one `[Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` instance per device.

The configuration block can use the `[action](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#configureTestTasks\(kotlin.Function2\))`'s context parameter to disambiguate between each `[Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` task instance.

Do not make assumption about how AGP decides to allocate `[Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` task instances per device, as each AGP version can potentially change it in future release, always use the context object to determine what the `[Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` task applies to.

Parameters  
---  
`action: [Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html).(context: [TestTaskContext](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestTaskContext)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  a block to configure the `[Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` tasks associated with this test suite target.  
  
### getTargets

Added in 9.3.3
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [getTargets](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#getTargets\(\))(): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[AgpTestSuiteTarget](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteTarget)>

Targets for this test suite, must be manually created in order to provide the variants this test suite applies to.

### hostJar

Added in 9.3.3
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [hostJar](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#hostJar\(kotlin.Function1\))(action: [TestSuiteHostJarSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestSuiteHostJarSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds a host test folder to this test suite sources, containing kotlin sources that will be compiled.

The folder will be named 'test' by default. It's the root path of the sources and may contain subfolders like 'java', 'kotlin' and 'resources'. The full path will be by default `src//test/

questionable : Configured test engines can retrieve the compiled classes using the `[AgpTestSuiteInputParameters.TEST_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#TEST_CLASSES)` property.

### testApk

Added in 9.3.3
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [testApk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#testApk\(kotlin.Function1\))(action: [TestSuiteTestApkSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestSuiteTestApkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds a device test source folder to this test suite, containing all necessary sources to create an APK.

The parent folder will be 'androidTest' by default.

The sources will be compiled to produce a test APK that can be retrieved by the test engine using the `[AgpTestSuiteInputParameters.TESTED_APKS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#TESTED_APKS)` property.

### useJunitEngine

Added in 9.3.3
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [useJunitEngine](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#useJunitEngine\(kotlin.Function1\))(action: [JUnitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JUnitEngineSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies properties for the JUnit test engines to run in this test suite

## Public properties

### codeCoverage

Added in 9.3.3
    
    
    var [codeCoverage](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#codeCoverage\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Turns on or off the code coverage support.

By default, the code coverage is disabled.

### targetVariants

Added in 9.3.3
    
    
    val [targetVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#targetVariants\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Defines which variant this tests suite targets.

### useJunitEngine

Added in 9.3.3
    
    
    val [useJunitEngine](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#useJunitEngine\(\)): [JUnitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JUnitEngineSpec)

Spec to identify the test engine that will be used to run this test suite. Do not call this method if the test suite should use a dedicated test task. Calling this method will direct AGP to create a `[org.gradle.api.tasks.testing.Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` task and configure it using the returned `[JUnitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JUnitEngineSpec)`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
