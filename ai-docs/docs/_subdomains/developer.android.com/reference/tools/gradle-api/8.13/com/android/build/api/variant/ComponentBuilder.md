---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ComponentBuilder/
title: ComponentBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:38:26.091978+00:00
---

# ComponentBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ComponentBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ComponentBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/ComponentBuilder.kt+class:com.android.build.api.variant.ComponentBuilder)

Added in 7.0.0
    
    
    interface [ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ComponentBuilder) : [ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ComponentIdentity)

Known direct subclasses 

[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/VariantBuilder)

`[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/VariantBuilder)` |  Model for variant components that only contains configuration-time properties that impacts the build flow.  
---|---  
  
Known indirect subclasses 

[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ApplicationVariantBuilder), [DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DynamicFeatureVariantBuilder), [KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder), [LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/LibraryVariantBuilder), [TestVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/TestVariantBuilder)

`[ApplicationVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ApplicationVariantBuilder)` |  Model for application components that only contains configuration-time properties that impacts the build flow.  
---|---  
`[DynamicFeatureVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/DynamicFeatureVariantBuilder)` |  Model for dynamic feature components that only contains configuration-time properties that impacts the build flow.  
`[KotlinMultiplatformAndroidVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/KotlinMultiplatformAndroidVariantBuilder)` |  Model for kotlin multiplatform library components that only contains configuration-time properties that impacts the build flow.  
`[LibraryVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/LibraryVariantBuilder)` |  Model for library components that only contains configuration-time properties that impacts the build flow.  
`[TestVariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/TestVariantBuilder)` |  Model for test components that only contains configuration-time properties that impacts the build flow.  
  
* * *

Model for components that only contains configuration-time properties that impacts the build flow.

Components can be APKs, AARs, test APKs, unit tests, test fixtures, ...

This is the parent interface for all objects that can be manipulated by `[AndroidComponentsExtension.beforeVariants](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))`

This type is here to mirror the `[Component](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Component)`/`[Variant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Variant)` hierarchy, which also includes `[TestComponent](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/TestComponent)` (which is not a `[Variant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Variant)`). In this hierarchy however, there isn't a `TestComponentBuilder` and therefore all objects of this type are also `[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/VariantBuilder)`

See `[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/VariantBuilder)` for more information on accessing instances of this type.

The properties exposed by this object have an impact on the build flow. They can add or remove tasks, and change how the tasks consume each other's output. Because of this, they are not using Gradle's `[org.gradle.api.provider.Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)` so that they can be queried during configuration. Because other applied plugins can change these values in their beforeVariants block, it is not safe to read these values in this stage.

This object should only be used to set new values. To read the final values of these properties, find the matching property in `[Component](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Component)`, and its subtypes

See [here](https://developer.android.com/build/extend-agp#variant-api-artifacts-tasks) for more information

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ComponentBuilder#enable\(\))` Set to `true` if the variant is active and should be configured, false otherwise.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enabled](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ComponentBuilder#enabled\(\))` **This property is deprecated.** Will be removed in 9.0  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.ComponentIdentity](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ComponentIdentity) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[buildType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ComponentIdentity#buildType\(\))` Build type name.  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[flavorName](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ComponentIdentity#flavorName\(\))` The multi-flavor name of the variant.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ComponentIdentity#name\(\))` Component's name.  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>>` |  `[productFlavors](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ComponentIdentity#productFlavors\(\))` List of flavor names.  
  
## Public properties

### enable

Added in 7.1.0
    
    
    var [enable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ComponentBuilder#enable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Set to `true` if the variant is active and should be configured, false otherwise.

If set to false, the matching `[Component](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Component)` object for this component will not be created.

### enabled

Added in 7.0.0

Deprecated in 7.1.0
    
    
    var [enabled](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/ComponentBuilder#enabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Will be removed in 9.0

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
