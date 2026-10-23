---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder/
title: HostTestBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:19:05.271790+00:00
---

# HostTestBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# HostTestBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/HostTestBuilder.kt+class:com.android.build.api.variant.HostTestBuilder)

Added in 8.5.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [HostTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder)

* * *

Interface to turn on or off host tests. Host tests run on the development machine, `[UNIT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder.Companion#UNIT_TEST_TYPE\(\))` or `[SCREENSHOT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder.Companion#SCREENSHOT_TEST_TYPE\(\))` are examples of host tests.

## Summary

### Constants  
  
---  
`const [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[SCREENSHOT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder.Companion#SCREENSHOT_TEST_TYPE\(\))` Host test type for default screenshot tests.  
`const [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[UNIT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder.Companion#UNIT_TEST_TYPE\(\))` Host test type for default unit tests.  
  
### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder#enable\(\))` Set to `true` if the variant's has any host tests, false otherwise.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableCodeCoverage](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder#enableCodeCoverage\(\))` Specifies host test code coverage data collection by configuring the JacocoPlugin.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[includeAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder#includeAndroidResources\(\))` Enables host tests to use Android resources, assets, and manifests.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[type](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder#type\(\))` Type of the `[HostTest](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTest)`, which can be '`[UNIT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder.Companion#UNIT_TEST_TYPE\(\))` or `[SCREENSHOT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder.Companion#SCREENSHOT_TEST_TYPE\(\))` for `[HostTest](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTest)`s created by AGP.  
  
## Constants

### SCREENSHOT_TEST_TYPE

Added in 8.5.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    const val [SCREENSHOT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder.Companion#SCREENSHOT_TEST_TYPE\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Host test type for default screenshot tests.

### UNIT_TEST_TYPE

Added in 8.5.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    const val [UNIT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder.Companion#UNIT_TEST_TYPE\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Host test type for default unit tests.

## Public properties

### enable

Added in 8.5.0
    
    
    var [enable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder#enable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Set to `true` if the variant's has any host tests, false otherwise.

Not setting this value relies on the AGP default behavior for this host test type.

### enableCodeCoverage

Added in 8.5.0

Deprecated in 8.5.0
    
    
    var [enableCodeCoverage](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder#enableCodeCoverage\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Specifies host test code coverage data collection by configuring the JacocoPlugin.

When enabled, the Jacoco plugin is applied and coverage data is collected by the Jacoco plugin. This can avoid unwanted build time instrumentation required to collect coverage data from other test types such as connected tests.

If the value is initialized from the DSL `[com.android.build.api.dsl.BuildType.enableUnitTestCoverage](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BuildType#enableUnitTestCoverage\(\))`, it will be used for `[HostTestBuilder.UNIT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder.Companion#UNIT_TEST_TYPE\(\))`.

### includeAndroidResources

Added in 9.5.0-alpha10

Deprecated in 9.5.0-alpha10
    
    
    var [includeAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder#includeAndroidResources\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Enables host tests to use Android resources, assets, and manifests.

If you set this property to `true`, the plugin performs resource, asset, and manifest merging before running your host tests. Your tests can then inspect a file called `com/android/tools/test_config.properties` on the classpath, which is a Java properties file with the following keys:

`android_resource_apk`: the path to the APK-like zip file containing merged resources, which includes all the resources from the current subproject and all its dependencies.

`android_merged_assets`: the path to the directory containing merged assets. The merged assets directory contains assets from the current subproject and it dependencies.

`android_merged_manifest`: the path to the merged manifest file. Only app subprojects have the manifest merged from their dependencies. Library subprojects do not include manifest components from their dependencies.

`android_custom_package`: the package name (namespace) of the final R class.

Note that the paths above are relative paths (relative to the current project directory, not the root project directory).

This field is initialized from the DSL `[com.android.build.api.dsl.UnitTestOptions.isIncludeAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/UnitTestOptions#isIncludeAndroidResources\(\))`.

### type

Added in 8.5.0
    
    
    val [type](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder#type\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Type of the `[HostTest](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTest)`, which can be '`[UNIT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder.Companion#UNIT_TEST_TYPE\(\))` or `[SCREENSHOT_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTestBuilder.Companion#SCREENSHOT_TEST_TYPE\(\))` for `[HostTest](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/HostTest)`s created by AGP.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
