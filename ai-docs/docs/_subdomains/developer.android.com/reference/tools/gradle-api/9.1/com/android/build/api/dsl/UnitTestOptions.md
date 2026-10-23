---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/UnitTestOptions/
title: UnitTestOptions \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:06:14.720708+00:00
---

# UnitTestOptions  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/UnitTestOptions/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# UnitTestOptions

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/UnitTestOptions.kt+class:com.android.build.api.dsl.UnitTestOptions)

Added in 4.2.0
    
    
    interface [UnitTestOptions](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/UnitTestOptions)

* * *

Options for controlling unit tests execution.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[all](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/UnitTestOptions#all\(kotlin.Function1\))(configAction: ([Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all unit testing tasks.  
  
### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isIncludeAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/UnitTestOptions#isIncludeAndroidResources\(\))` Enables unit tests to use Android resources, assets, and manifests.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isReturnDefaultValues](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/UnitTestOptions#isReturnDefaultValues\(\))` Whether unmocked methods from android.jar should throw exceptions or return default values (i.e. zero or null).  
  
## Public functions

### all

Added in 4.2.0
    
    
    fun [all](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/UnitTestOptions#all\(kotlin.Function1\))(configAction: ([Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures all unit testing tasks.

See `[Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` for available options.

Inside the closure you can check the name of the task to configure only some test tasks, e.g.
    
    
    android {  
        testOptions {  
            unitTests.all {  
                if (it.name == 'testDebug') {  
                    systemProperty 'debug', 'true'  
                }  
            }  
        }  
    }

since 1.2.0

## Public properties

### isIncludeAndroidResources

Added in 4.2.0
    
    
    var [isIncludeAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/UnitTestOptions#isIncludeAndroidResources\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Enables unit tests to use Android resources, assets, and manifests.

If you set this property to `true`, the plugin performs resource, asset, and manifest merging before running your unit tests. Your tests can then inspect a file called `com/android/tools/test_config.properties` on the classpath, which is a Java properties file with the following keys:

`android_resource_apk`: the path to the APK-like zip file containing merged resources, which includes all the resources from the current subproject and all its dependencies.

`android_merged_assets`: the path to the directory containing merged assets. The merged assets directory contains assets from the current subproject and it dependencies.

`android_merged_manifest`: the path to the merged manifest file. Only app subprojects have the manifest merged from their dependencies. Library subprojects do not include manifest components from their dependencies.

`android_custom_package`: the package name (namespace) of the final R class.

Note that the paths above are relative paths (relative to the current project directory, not the root project directory).

since 3.0.0

### isReturnDefaultValues

Added in 4.2.0
    
    
    var [isReturnDefaultValues](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/UnitTestOptions#isReturnDefaultValues\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether unmocked methods from android.jar should throw exceptions or return default values (i.e. zero or null).

See [Test Your App](https://developer.android.com/studio/test/index.html) for details.

since 1.1.0

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
