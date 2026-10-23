---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestVariantBuilder/
title: TestVariantBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:56:00.481066+00:00
---

# TestVariantBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestVariantBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestVariantBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/TestVariantBuilder.kt+class:com.android.build.api.variant.TestVariantBuilder)

Added in 4.2.0
    
    
    interface [TestVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestVariantBuilder) : [VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder), [GeneratesApkBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesApkBuilder), [CanMinifyCodeBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/CanMinifyCodeBuilder)

* * *

Model for test components that only contains configuration-time properties that impacts the build flow.

This is for components associated with the `com.android.test` plugin. This is not for test components associated with variants. For these see `[TestComponent](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestComponent)` (they currently do not have matching builder interfaces).

See `[ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentBuilder)` and `[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder)` for more information.

## Summary

### Inherited functions  
  
---  
From [com.android.build.api.variant.VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<T : [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)> [registerExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#registerExtension\(java.lang.Class,kotlin.Any\))(type: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<T>, instance: T)` Registers an extension object to the variant object.  
---|---  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.CanMinifyCodeBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/CanMinifyCodeBuilder) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isMinifyEnabled](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/CanMinifyCodeBuilder#isMinifyEnabled\(\))` Specifies whether code will be minified  
---|---  
  
From [com.android.build.api.variant.ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentBuilder) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enable](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentBuilder#enable\(\))` Set to `true` if the variant is active and should be configured, false otherwise.  
---|---  
  
From [com.android.build.api.variant.ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[buildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity#buildType\(\))` Build type name.  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[flavorName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity#flavorName\(\))` The multi-flavor name of the variant.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity#name\(\))` Component's name.  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>>` |  `[productFlavors](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity#productFlavors\(\))` List of flavor names.  
  
From [com.android.build.api.variant.GeneratesApkBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesApkBuilder) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[debuggable](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesApkBuilder#debuggable\(\))` Sets the APK debuggable flag.  
---|---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[enableMultiDex](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesApkBuilder#enableMultiDex\(\))` Sets whether multi-dex is enabled for this variant.  
  
From [com.android.build.api.variant.VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder) | `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[maxSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#maxSdk\(\))` Sets the maximum supported SDK Version for this variant.  
---|---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#minSdk\(\))` Sets the minimum supported SDK Version for this variant.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#minSdkPreview\(\))` Sets the minimum supported SDK Version for this variant as a Preview codename.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[renderscriptTargetApi](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#renderscriptTargetApi\(\))` Specifies the bytecode version to be generated.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
