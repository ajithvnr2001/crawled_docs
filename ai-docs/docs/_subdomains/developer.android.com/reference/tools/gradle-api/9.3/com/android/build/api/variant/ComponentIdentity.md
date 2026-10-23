---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentIdentity/
title: ComponentIdentity \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:35:12.756654+00:00
---

# ComponentIdentity  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentIdentity/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ComponentIdentity

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/ComponentIdentity.kt+class:com.android.build.api.variant.ComponentIdentity)

Added in 7.0.0
    
    
    interface [ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentIdentity)

Known direct subclasses 

[ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentBuilder), [Component](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component)

`[ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentBuilder)` |  Model for components that only contains configuration-time properties that impacts the build flow.  
---|---  
`[Component](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component)` |  Model for components that only contains build-time properties  
  
Known indirect subclasses 

[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidTest), [ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ApplicationVariantBuilder), [ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ApplicationVariant), [DeviceTest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DeviceTest), [DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DynamicFeatureVariantBuilder), [DynamicFeatureVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DynamicFeatureVariant), [HostTest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/HostTest), [KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder), [KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/KotlinMultiplatformAndroidVariant), [LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/LibraryVariantBuilder), [LibraryVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/LibraryVariant), [TestComponent](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestComponent), [TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestFixtures), [TestVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestVariantBuilder), [TestVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestVariant), [UnitTest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/component/UnitTest), [UnitTest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/UnitTest), [VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantBuilder), [Variant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Variant)

`[AndroidTest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidTest)` |  Model for Android Test components that contains build-time properties  
---|---  
`[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ApplicationVariantBuilder)` |  Model for application components that only contains configuration-time properties that impacts the build flow.  
`[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ApplicationVariant)` |  Model for application components that only contains build-time properties.  
`[DeviceTest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DeviceTest)` |  Model for Device Test components that contains build-time properties  
`[DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DynamicFeatureVariantBuilder)` |  Model for dynamic feature components that only contains configuration-time properties that impacts the build flow.  
`[DynamicFeatureVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DynamicFeatureVariant)` |  Model for dynamic feature components that only contains build-time properties.  
`[HostTest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/HostTest)` |  Model for Host Test components that contains build-time properties.  
`[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)` |  Model for kotlin multiplatform library components that only contains configuration-time properties that impacts the build flow.  
`[KotlinMultiplatformAndroidVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)` |  Properties for the main Variant of a kotlin multiplatform android library  
`[LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/LibraryVariantBuilder)` |  Model for library components that only contains configuration-time properties that impacts the build flow.  
`[LibraryVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/LibraryVariant)` |  Model for library components that only contains build-time properties.  
`[TestComponent](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestComponent)` |  Model for test components that contains build-time properties.  
`[TestFixtures](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestFixtures)` |  Model for Test Fixtures components that contains build-time properties  
`[TestVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestVariantBuilder)` |  Model for test components that only contains configuration-time properties that impacts the build flow.  
`[TestVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestVariant)` |  Model for test components that only contains build-time properties.  
`[UnitTest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/component/UnitTest)` |  **This interface is deprecated.** Use the com.android.build.api.variant package  
`[UnitTest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/UnitTest)` |  `[Component](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component)` for unit tests  
`[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/VariantBuilder)` |  Model for variant components that only contains configuration-time properties that impacts the build flow.  
`[Variant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Variant)` |  Model for variant components that only contains build-time properties  
  
* * *

Variant Configuration represents the identify of a variant

This is computed from the list of build types and flavors.

## Summary

### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[buildType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentIdentity#buildType\(\))` Build type name.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[flavorName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentIdentity#flavorName\(\))` The multi-flavor name of the variant.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentIdentity#name\(\))` Component's name.  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>>` |  `[productFlavors](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentIdentity#productFlavors\(\))` List of flavor names.  
  
## Public properties

### buildType

Added in 7.0.0
    
    
    val [buildType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentIdentity#buildType\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Build type name.

### flavorName

Added in 7.0.0
    
    
    val [flavorName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentIdentity#flavorName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The multi-flavor name of the variant.

This does not include the build type. If no flavors are present, this will return null

The full name of the variant is queried via `[name](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentIdentity#name\(\))`.

### name

Added in 7.0.0
    
    
    val [name](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentIdentity#name\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Component's name.

### productFlavors

Added in 7.0.0
    
    
    val [productFlavors](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ComponentIdentity#productFlavors\(\)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>>

List of flavor names.

The order is properly sorted based on the associated dimension order.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
