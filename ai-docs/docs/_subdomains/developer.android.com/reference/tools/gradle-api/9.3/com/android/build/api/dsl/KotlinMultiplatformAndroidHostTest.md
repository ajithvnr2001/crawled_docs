---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest/
title: KotlinMultiplatformAndroidHostTest \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:29:59.570771+00:00
---

# KotlinMultiplatformAndroidHostTest  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# KotlinMultiplatformAndroidHostTest

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest.kt+class:com.android.build.api.dsl.KotlinMultiplatformAndroidHostTest)

Added in 8.8.0
    
    
    interface [KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest)

Known direct subclasses 

[KotlinMultiplatformAndroidHostTestCompilation](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTestCompilation)

`[KotlinMultiplatformAndroidHostTestCompilation](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTestCompilation)` |   
---|---  
  
* * *

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest#targetSdk\(kotlin.Function1\))(action: [TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TargetSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding target sdk for host tests, see `[TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TargetSdkSpec)` for available options.  
  
### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableCoverage](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest#enableCoverage\(\))` Specifies unit test code coverage data collection by configuring the JacocoPlugin.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isIncludeAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest#isIncludeAndroidResources\(\))` Enables unit tests to use Android resources, assets, and manifests.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isReturnDefaultValues](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest#isReturnDefaultValues\(\))` Whether unmocked methods from android.jar should throw exceptions or return default values (i.e. zero or null).  
  
## Public functions

### targetSdk

Added in 8.12.0
    
    
    fun [targetSdk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest#targetSdk\(kotlin.Function1\))(action: [TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TargetSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures all aspects regarding target sdk for host tests, see `[TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/TargetSdkSpec)` for available options.

## Public properties

### enableCoverage

Added in 8.8.0
    
    
    var [enableCoverage](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest#enableCoverage\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Specifies unit test code coverage data collection by configuring the JacocoPlugin.

When enabled, the Jacoco plugin is applied and coverage data is collected by the Jacoco plugin. This can avoid unwanted build time instrumentation required to collect coverage data from other test types such as connected tests.

### isIncludeAndroidResources

Added in 8.8.0
    
    
    var [isIncludeAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest#isIncludeAndroidResources\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Enables unit tests to use Android resources, assets, and manifests.

If you set this property to `true`, the plugin performs resource, asset, and manifest merging before running your unit tests. Your tests can then inspect a file called `com/android/tools/test_config.properties` on the classpath, which is a Java properties file with the following keys:

`android_resource_apk`: the path to the APK-like zip file containing merged resources, which includes all the resources from the current subproject and all its dependencies. This property is available by default, or if the Gradle property `android.enableUnitTestBinaryResources` is set to `true`.

`android_merged_resources`: the path to the directory containing merged resources, which includes all the resources from the current subproject and all its dependencies. This property is available only if the Gradle property `android.enableUnitTestBinaryResources` is set to `false`.

`android_merged_assets`: the path to the directory containing merged assets. For app subprojects, the merged assets directory contains assets from the current subproject and its dependencies. For library subprojects, the merged assets directory contains only assets from the current subproject.

`android_merged_manifest`: the path to the merged manifest file. Only app subprojects have the manifest merged from their dependencies. Library subprojects do not include manifest components from their dependencies.

`android_custom_package`: the package name of the final R class. If you modify the application ID in your build scripts, this package name may not match the `package` attribute in the final app manifest.

Note that starting with version 3.5.0, if the Gradle property `android.testConfig.useRelativePath` is set to `true`, the paths above will be relative paths (relative to the current project directory, not the root project directory); otherwise, they will be absolute paths. Prior to version 3.5.0, the paths are all absolute paths.

### isReturnDefaultValues

Added in 8.8.0
    
    
    var [isReturnDefaultValues](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest#isReturnDefaultValues\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether unmocked methods from android.jar should throw exceptions or return default values (i.e. zero or null).

See [Test Your App](https://developer.android.com/studio/test/index.html) for details.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
