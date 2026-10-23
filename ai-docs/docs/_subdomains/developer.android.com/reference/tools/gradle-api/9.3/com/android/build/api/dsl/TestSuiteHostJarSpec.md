---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestSuiteHostJarSpec/
title: TestSuiteHostJarSpec \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:32:35.868658+00:00
---

# TestSuiteHostJarSpec  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestSuiteHostJarSpec/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestSuiteHostJarSpec

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/TestSuiteHostJarSpec.kt+class:com.android.build.api.dsl.TestSuiteHostJarSpec)

Added in 9.3.3
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [TestSuiteHostJarSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestSuiteHostJarSpec)

* * *

Definition of host test sources for a test suite. Host test source files are compiled and therefore dependencies can be attached to them.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[dependencies](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestSuiteHostJarSpec#dependencies\(kotlin.Function1\))(action: [AgpTestSuiteDependencies](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteDependencies).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies dependency information for this test suite.  
  
### Public properties  
  
---  
`[AgpTestSuiteDependencies](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteDependencies)` |  `[dependencies](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestSuiteHostJarSpec#dependencies\(\))` Dependency handler for this sources  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestSuiteHostJarSpec#enableAndroidResources\(\))` If this property is set to `true`, the plugin performs resource, asset, and manifest merging before running your host tests.  
  
## Public functions

### dependencies

Added in 9.3.3
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [dependencies](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestSuiteHostJarSpec#dependencies\(kotlin.Function1\))(action: [AgpTestSuiteDependencies](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteDependencies).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies dependency information for this test suite.

## Public properties

### dependencies

Added in 9.3.3
    
    
    val [dependencies](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestSuiteHostJarSpec#dependencies\(\)): [AgpTestSuiteDependencies](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteDependencies)

Dependency handler for this sources

### enableAndroidResources

Added in 9.3.3
    
    
    var [enableAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TestSuiteHostJarSpec#enableAndroidResources\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

If this property is set to `true`, the plugin performs resource, asset, and manifest merging before running your host tests. Your tests can then inspect a file called `com/android/tools/test_config.properties` on the classpath, which is a Java properties file with the following keys:

`android_resource_apk`: the path to the APK-like zip file containing merged resources, which includes all the resources from the current subproject and all its dependencies.

`android_merged_assets`: the path to the directory containing merged assets. The merged assets directory contains assets from the current subproject and it dependencies.

`android_merged_manifest`: the path to the merged manifest file. Only app subprojects have the manifest merged from their dependencies. Library subprojects do not include manifest components from their dependencies.

`android_custom_package`: the package name (namespace) of the final R class.

Note that the paths above are relative paths (relative to the current project directory, not the root project directory).

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
