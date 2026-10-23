---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension/
title: TestedExtension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:50:20.393120+00:00
---

# TestedExtension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestedExtension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/TestedExtension.kt+class:com.android.build.api.dsl.TestedExtension)

Added in 4.2.0
    
    
    interface [TestedExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension)

Known direct subclasses 

[ApplicationExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension), [DynamicFeatureExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DynamicFeatureExtension), [LibraryExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryExtension)

`[ApplicationExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/ApplicationExtension)` |  Extension for the Android Gradle Plugin Application plugin.  
---|---  
`[DynamicFeatureExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/DynamicFeatureExtension)` |  Extension for the Android Dynamic Feature Gradle Plugin.  
`[LibraryExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/LibraryExtension)` |  Extension for the Android Library Gradle Plugin.  
  
* * *

Common extension properties for the Android Application. Library and Dynamic Feature Plugins that relate to testing

Only the Android Gradle Plugin should create instances of this interface.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[testFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension#testFixtures\(kotlin.Function1\))(action: [TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestFixtures).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Options to configure the test fixtures.  
  
### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[testBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension#testBuildType\(\))` Specifies the [build type](https://developer.android.com/studio/build/build-variants.html#build-types) that the plugin should use to test the module.  
`[TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestFixtures)` |  `[testFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension#testFixtures\(\))` Options to configure the test fixtures.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[testNamespace](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension#testNamespace\(\))` The namespace used by the android test and unit test components for the generated R and BuildConfig classes.  
  
## Public functions

### testFixtures

Added in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [testFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension#testFixtures\(kotlin.Function1\))(action: [TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestFixtures).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Options to configure the test fixtures.

## Public properties

### testBuildType

Added in 4.2.0
    
    
    var [testBuildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension#testBuildType\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Specifies the [build type](https://developer.android.com/studio/build/build-variants.html#build-types) that the plugin should use to test the module.

By default, the Android plugin uses the "debug" build type. This means that when you deploy your instrumented tests using `gradlew connectedAndroidTest`, it uses the code and resources from the module's "debug" build type to create the test APK. The plugin then deploys the "debug" version of both the module's APK and the test APK to a connected device, and runs your tests.

To change the test build type to something other than "debug", specify it as follows:
    
    
    android {  
        // Changes the test build type for instrumented tests to "stage".  
        testBuildType "stage"  
    }

If your module configures [product flavors](https://developer.android.com/studio/build/build-variants.html#product-flavors) the plugin creates a test APK and deploys tests for each build variant that uses the test build type. For example, consider if your module configures "debug" and "release" build types, and "free" and "paid" product flavors. By default, when you run your instrumented tests using `gradlew connectedAndroidTest`, the plugin performs executes the following tasks:

  * `connectedFreeDebugAndroidTest`: builds and deploys a `freeDebug` test APK and module APK, and runs instrumented tests for that variant.

  * `connectedPaidDebugAndroidTest`: builds and deploys a `paidDebug` test APK and module APK, and runs instrumented tests for that variant.




To learn more, read [Create instrumented test for a build variant](https://developer.android.com/studio/test/index.html#create_instrumented_test_for_a_build_variant)

**Note:** You can execute `connected<BuildVariant>AndroidTest` tasks only for build variants that use the test build type. So, by default, running `connectedStageAndroidTest` results in the following build error:
    
    
    Task 'connectedStageAndroidTest' not found in root project

You can resolve this issue by changing the test build type to "stage".

### testFixtures

Added in 7.1.0
    
    
    val [testFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension#testFixtures\(\)): [TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestFixtures)

Options to configure the test fixtures.

### testNamespace

Added in 7.0.0
    
    
    var [testNamespace](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestedExtension#testNamespace\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The namespace used by the android test and unit test components for the generated R and BuildConfig classes.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
