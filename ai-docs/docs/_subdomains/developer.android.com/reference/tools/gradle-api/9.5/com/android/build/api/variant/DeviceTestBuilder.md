---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/DeviceTestBuilder/
title: DeviceTestBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:17:46.801964+00:00
---

# DeviceTestBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/DeviceTestBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DeviceTestBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/DeviceTestBuilder.kt+class:com.android.build.api.variant.DeviceTestBuilder)

Added in 8.4.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [DeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/DeviceTestBuilder) : [GeneratesTestApkBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/GeneratesTestApkBuilder)

Known direct subclasses 

[AndroidTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidTestBuilder)

`[AndroidTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidTestBuilder)` |   
---|---  
  
* * *

Interface to turn tests on devices, `AndroidTest` being an example of device tests.

## Summary

### Constants  
  
---  
`const [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[ANDROID_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/DeviceTestBuilder.Companion#ANDROID_TEST_TYPE\(\))` Host test type for default unit tests.  
  
### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/DeviceTestBuilder#enable\(\))` Set to `true` if the variant's has any device tests, false otherwise.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableCodeCoverage](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/DeviceTestBuilder#enableCodeCoverage\(\))` Specifies device test code coverage data collection by configuring the JacocoPlugin.  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.GeneratesApkBuilder](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/GeneratesApkBuilder) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[debuggable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/GeneratesApkBuilder#debuggable\(\))` Sets the APK debuggable flag.  
---|---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[enableMultiDex](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/GeneratesApkBuilder#enableMultiDex\(\))` Sets whether multi-dex is enabled for this variant.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/GeneratesApkBuilder#targetSdk\(\))` Sets the target SDK Version for this variant as an integer API level.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/GeneratesApkBuilder#targetSdkPreview\(\))` Sets the target SDK Version for this variant as an integer API level.  
  
## Constants

### ANDROID_TEST_TYPE

Added in 8.7.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    const val [ANDROID_TEST_TYPE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/DeviceTestBuilder.Companion#ANDROID_TEST_TYPE\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Host test type for default unit tests.

## Public properties

### enable

Added in 8.4.0
    
    
    var [enable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/DeviceTestBuilder#enable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Set to `true` if the variant's has any device tests, false otherwise. Value is Boolean#True by default.

### enableCodeCoverage

Added in 8.5.0

Deprecated in 8.5.0
    
    
    var [enableCodeCoverage](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/DeviceTestBuilder#enableCodeCoverage\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Specifies device test code coverage data collection by configuring the JacocoPlugin.

When enabled, the Jacoco plugin is applied and coverage data is collected by the Jacoco plugin. This can avoid unwanted build time instrumentation required to collect coverage data from other test types such as unit tests.

If the value is initialized from the DSL `[com.android.build.api.dsl.BuildType.enableAndroidTestCoverage](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BuildType#enableAndroidTestCoverage\(\))`,

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
