---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LibraryVariantBuilder/
title: LibraryVariantBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:01:32.337606+00:00
---

# LibraryVariantBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LibraryVariantBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# LibraryVariantBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/LibraryVariantBuilder.kt+class:com.android.build.api.variant.LibraryVariantBuilder)

Added in 4.2.0
    
    
    interface [LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LibraryVariantBuilder) : [VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantBuilder), [HasDeviceTestsBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasDeviceTestsBuilder), [HasAndroidTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidTestBuilder), [HasHostTestsBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasHostTestsBuilder), [HasUnitTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasUnitTestBuilder), [HasTestFixturesBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasTestFixturesBuilder), [HasTestSuitesBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasTestSuitesBuilder), [CanMinifyCodeBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/CanMinifyCodeBuilder)

Known direct subclasses 

[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)

`[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)` |  Model for kotlin multiplatform library components that only contains configuration-time properties that impacts the build flow.  
---|---  
  
* * *

Model for library components that only contains configuration-time properties that impacts the build flow.

See `[ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentBuilder)` and `[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantBuilder)` for more information.

## Summary

### Inherited functions  
  
---  
From [com.android.build.api.variant.VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantBuilder) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<T : [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)> [registerExtension](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantBuilder#registerExtension\(java.lang.Class,kotlin.Any\))(type: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<T>, instance: T)` Registers an extension object to the variant object.  
---|---  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.CanMinifyCodeBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/CanMinifyCodeBuilder) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isMinifyEnabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/CanMinifyCodeBuilder#isMinifyEnabled\(\))` Specifies whether code will be minified  
---|---  
  
From [com.android.build.api.variant.ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentBuilder) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentBuilder#enable\(\))` Set to `true` if the variant is active and should be configured, false otherwise.  
---|---  
  
From [com.android.build.api.variant.ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[buildType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity#buildType\(\))` Build type name.  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[flavorName](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity#flavorName\(\))` The multi-flavor name of the variant.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity#name\(\))` Component's name.  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>>` |  `[productFlavors](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ComponentIdentity#productFlavors\(\))` List of flavor names.  
  
From [com.android.build.api.variant.HasAndroidTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidTestBuilder) | `[AndroidTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidTestBuilder)` |  `[androidTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidTestBuilder#androidTest\(\))` Variant's `[AndroidTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/AndroidTestBuilder)` configuration to turn on or off android tests and set other android test related settings.  
---|---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[androidTestEnabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidTestBuilder#androidTestEnabled\(\))` Set to `true` if the variant's has any android tests, false otherwise.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableAndroidTest](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasAndroidTestBuilder#enableAndroidTest\(\))` Set to `true` if the variant's has any android tests, false otherwise.  
  
From [com.android.build.api.variant.HasDeviceTestsBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasDeviceTestsBuilder) | `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [DeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/DeviceTestBuilder)>` |  `[deviceTests](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasDeviceTestsBuilder#deviceTests\(\))` List of `[DeviceTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/DeviceTestBuilder)` for this variant.  
---|---  
  
From [com.android.build.api.variant.HasHostTestsBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasHostTestsBuilder) | `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [HostTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HostTestBuilder)>` |  `[hostTests](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasHostTestsBuilder#hostTests\(\))` Variant's `[HostTestBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HostTestBuilder)` configuration to turn on or off screenshot tests and set other screenshot test related settings.  
---|---  
  
From [com.android.build.api.variant.HasTestFixturesBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasTestFixturesBuilder) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableTestFixtures](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasTestFixturesBuilder#enableTestFixtures\(\))` Set to `true` if the variant's has test fixtures, `false` otherwise.  
---|---  
  
From [com.android.build.api.variant.HasTestSuitesBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasTestSuitesBuilder) | `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [TestSuiteBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteBuilder)>` |  `[suites](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/HasTestSuitesBuilder#suites\(\))` Variant's `[TestSuiteBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/TestSuiteBuilder)` configuration to configure test suites associated with this variant.  
---|---  
  
From [com.android.build.api.variant.VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantBuilder) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableLint](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantBuilder#enableLint\(\))` Whether lint should be run on this variant.  
---|---  
`[LintBuilder](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LintBuilder)` |  `[lint](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantBuilder#lint\(\))` Access to build-time configuration for lint.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[maxSdk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantBuilder#maxSdk\(\))` Sets the maximum supported SDK Version for this variant.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantBuilder#minSdk\(\))` Sets the minimum supported SDK Version for this variant.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantBuilder#minSdkPreview\(\))` Sets the minimum supported SDK Version for this variant as a Preview codename.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[renderscriptTargetApi](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantBuilder#renderscriptTargetApi\(\))` Specifies the bytecode version to be generated.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-07-23 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-23 UTC."],[],[]] 
