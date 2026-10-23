---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesTestApk/
title: GeneratesTestApk \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:00:05.090780+00:00
---

# GeneratesTestApk  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesTestApk/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# GeneratesTestApk

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/GeneratesTestApk.kt+class:com.android.build.api.variant.GeneratesTestApk)

Added in 7.0.0
    
    
    interface [GeneratesTestApk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesTestApk) : [GeneratesApk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApk)

Known direct subclasses 

[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidTest), [DeviceTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/DeviceTest), [TestVariant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestVariant)

`[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidTest)` |  Model for Android Test components that contains build-time properties  
---|---  
`[DeviceTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/DeviceTest)` |  Model for Device Test components that contains build-time properties  
`[TestVariant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestVariant)` |  Model for test components that only contains build-time properties.  
  
Known indirect subclasses 

[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidTest)

`[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidTest)` |  Model for Android Test components that contains build-time properties  
---|---  
  
* * *

Build-time properties for `[Component](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Component)` that produce test APKs.

## Summary

### Public properties  
  
---  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[functionalTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesTestApk#functionalTest\(\))` The functionalTest value to use to run the tests.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[handleProfiling](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesTestApk#handleProfiling\(\))` The handleProfiling value to use to run the tests.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[instrumentationRunner](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesTestApk#instrumentationRunner\(\))` The instrumentationRunner to use to run the tests.  
`[MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[instrumentationRunnerArguments](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesTestApk#instrumentationRunnerArguments\(\))` The instrumentationRunnerArguments to use to run the tests.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[testLabel](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesTestApk#testLabel\(\))` The test label, or "" if none defined.  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.GeneratesApk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApk) | `[AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidResources)` |  `[androidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApk#androidResources\(\))` Variant's android resources processing configuration, initialized by the corresponding global DSL element.  
---|---  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[applicationId](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApk#applicationId\(\))` Variant's application ID as present in the final manifest file of the APK.  
`[Dexing](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Dexing)` |  `[dexing](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApk#dexing\(\))` Variant's specific dexing options  
`[AndroidVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidVersion)` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApk#minSdk\(\))` Min SDK version for this variant  
`[ApkOutputProviders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkOutputProviders)` |  `[outputProviders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApk#outputProviders\(\))` Provides access to built artifacts output(e.g. APK) produced by this Variant.  
`[ApkPackaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ApkPackaging)` |  `[packaging](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApk#packaging\(\))` Variant's packagingOptions, initialized by the corresponding global DSL element.  
`[Renderscript](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Renderscript)?` |  `[renderscript](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApk#renderscript\(\))` Variant specific settings for the renderscript compiler.  
`[AndroidVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidVersion)` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesApk#targetSdk\(\))` Target SDK version for this variant.  
  
## Public properties

### functionalTest

Added in 7.0.0
    
    
    val [functionalTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesTestApk#functionalTest\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>

The functionalTest value to use to run the tests.

### handleProfiling

Added in 7.0.0
    
    
    val [handleProfiling](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesTestApk#handleProfiling\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>

The handleProfiling value to use to run the tests.

### instrumentationRunner

Added in 7.0.0
    
    
    val [instrumentationRunner](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesTestApk#instrumentationRunner\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The instrumentationRunner to use to run the tests.

### instrumentationRunnerArguments

Added in 8.2.0
    
    
    val [instrumentationRunnerArguments](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesTestApk#instrumentationRunnerArguments\(\)): [MapProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The instrumentationRunnerArguments to use to run the tests.

### testLabel

Added in 7.0.0
    
    
    val [testLabel](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/GeneratesTestApk#testLabel\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The test label, or "" if none defined.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
