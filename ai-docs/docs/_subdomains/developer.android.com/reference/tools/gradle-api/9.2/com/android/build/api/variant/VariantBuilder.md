---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder/
title: VariantBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:56:13.908556+00:00
---

# VariantBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# VariantBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/VariantBuilder.kt+class:com.android.build.api.variant.VariantBuilder)

Added in 4.2.0
    
    
    interface [VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder) : [ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentBuilder)

Known direct subclasses 

[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApplicationVariantBuilder), [DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DynamicFeatureVariantBuilder), [LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/LibraryVariantBuilder), [TestVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestVariantBuilder)

`[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApplicationVariantBuilder)` |  Model for application components that only contains configuration-time properties that impacts the build flow.  
---|---  
`[DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DynamicFeatureVariantBuilder)` |  Model for dynamic feature components that only contains configuration-time properties that impacts the build flow.  
`[LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/LibraryVariantBuilder)` |  Model for library components that only contains configuration-time properties that impacts the build flow.  
`[TestVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestVariantBuilder)` |  Model for test components that only contains configuration-time properties that impacts the build flow.  
  
Known indirect subclasses 

[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)

`[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)` |  Model for kotlin multiplatform library components that only contains configuration-time properties that impacts the build flow.  
---|---  
  
* * *

Model for variant components that only contains configuration-time properties that impacts the build flow.

Variant components are the main output of the plugin (e.g. APKs, AARs). They contain references to optional secondary components (tests, fixtures). Their presence can be controlled in select subtypes of `[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder)`.

It is the object passed to the `[AndroidComponentsExtension.beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` method, like this:
    
    
    androidComponents {  
      beforeVariants(selector().all()) { variant: VariantBuilder ->  
      }  
    }

Note that depending on the actual implementation of `[AndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension)`, the object received may be a subtype. For instance `[ApplicationAndroidComponentsExtension.beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApplicationAndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` will pass `[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ApplicationVariantBuilder)` to the lambda.

See [here](https://developer.android.com/build/extend-agp#variant-api-artifacts-tasks) for more information

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<T : [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)> [registerExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#registerExtension\(java.lang.Class,kotlin.Any\))(type: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<T>, instance: T)` Registers an extension object to the variant object.  
  
### Public properties  
  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[maxSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#maxSdk\(\))` Sets the maximum supported SDK Version for this variant.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#minSdk\(\))` Sets the minimum supported SDK Version for this variant.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#minSdkPreview\(\))` Sets the minimum supported SDK Version for this variant as a Preview codename.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[renderscriptTargetApi](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#renderscriptTargetApi\(\))` Specifies the bytecode version to be generated.  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentBuilder) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enable](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentBuilder#enable\(\))` Set to `true` if the variant is active and should be configured, false otherwise.  
---|---  
  
From [com.android.build.api.variant.ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[buildType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity#buildType\(\))` Build type name.  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[flavorName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity#flavorName\(\))` The multi-flavor name of the variant.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity#name\(\))` Component's name.  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>>` |  `[productFlavors](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentIdentity#productFlavors\(\))` List of flavor names.  
  
## Public functions

### registerExtension

Added in 7.0.0
    
    
    fun <T : [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)> [registerExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#registerExtension\(java.lang.Class,kotlin.Any\))(type: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<T>, instance: T): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Registers an extension object to the variant object. Extension objects can be looked up during the `[AndroidComponentsExtension.onVariants](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` callbacks by using the `[Variant.getExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#getExtension\(java.lang.Class\))` API.

This is very useful for third party plugins that want to attach some variant specific configuration object to the Android Gradle Plugin variant object and make it available to other plugins.

Parameters  
---  
`type: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<T>` |  the registered object type (can be a supertype of `[instance](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#registerExtension\(java.lang.Class,kotlin.Any\))`), this is the type that must be passed to the `[Variant.getExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#getExtension\(java.lang.Class\))` API.  
`instance: T` |  the object to associate to the AGP Variant object.  
  
## Public properties

### maxSdk

Added in 7.0.0
    
    
    var [maxSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#maxSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Sets the maximum supported SDK Version for this variant.

It is not safe to read this value. Use `[Variant.maxSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#maxSdk\(\))` instead.

### minSdk

Added in 7.0.0
    
    
    var [minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#minSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Sets the minimum supported SDK Version for this variant. Setting this it will override previous calls of `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#minSdk\(\))` and `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#minSdkPreview\(\))` setters. Only one of `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#minSdk\(\))` and `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#minSdkPreview\(\))` should be set.

It is not safe to read this value. Use `[Variant.minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#minSdk\(\))` instead.

Returns  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  the minimum supported SDK Version or null if `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#minSdkPreview\(\))` was used to set it.  
  
### minSdkPreview

Added in 7.0.0
    
    
    var [minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#minSdkPreview\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Sets the minimum supported SDK Version for this variant as a Preview codename. Setting this it will override previous calls of `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#minSdk\(\))` and `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#minSdkPreview\(\))` setters. Only one of `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#minSdk\(\))` and `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#minSdkPreview\(\))` should be set.

It is not safe to read this value. Use `[Variant.minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant#minSdk\(\))` instead.

Returns  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  the minimum supported SDK Version or null if `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#minSdk\(\))` was used to set it.  
  
### renderscriptTargetApi

Added in 4.2.0
    
    
    var [renderscriptTargetApi](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder#renderscriptTargetApi\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Specifies the bytecode version to be generated. We recommend you set this value to the lowest API level able to provide all the functionality you are using. -1 means unspecified.

It is not safe to read this value. Use `[GeneratesApk.renderscript](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/GeneratesApk#renderscript\(\))` instead

Returns  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  the renderscript target api or -1 if not specified.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
