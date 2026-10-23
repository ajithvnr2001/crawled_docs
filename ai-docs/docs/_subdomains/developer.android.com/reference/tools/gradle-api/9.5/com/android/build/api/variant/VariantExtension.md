---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantExtension/
title: VariantExtension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:21:21.442944+00:00
---

# VariantExtension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantExtension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# VariantExtension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/VariantExtension.kt+class:com.android.build.api.variant.VariantExtension)

Added in 7.0.0
    
    
    interface [VariantExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantExtension)

* * *

Marker type for `[Variant](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/Variant)` extension objects.

Variant extension must be registered using the `[AndroidComponentsExtension.registerExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidComponentsExtension#registerExtension\(com.android.build.api.variant.DslExtension,kotlin.Function1\))` API and can be retrieved from a `[Variant](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/Variant)` instance using the `[Variant.getExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/Variant#getExtension\(java.lang.Class\))` API.

Since this type will most likely be used as `[org.gradle.api.Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)`'s input, your subtype should also extend `[java.io.Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)`

This variant extension will be passed to all plugins that register a `[AndroidComponentsExtension.onVariants](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` block. In case several plugins modify some of the variant extension fields, it is primordial to define all the fields as a `[org.gradle.api.provider.Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)`. This will ensure that the tasks execution blocks that call `[org.gradle.api.provider.Property.get](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html#get--)` will get the final value, regardless of the order in which plugins are configured.

Example of a sub-type :

` abstract class VariantDslExtension @Inject constructor( // Do not keep a reference on the VariantExtensionConfig as it is not serializable, // use the constructor to extract the values for the BuildType/ProductFlavor extensions // that can be obtained from the VariantExtensionConfig. extensionConfig: VariantExtensionConfig<*> ): VariantExtension, java.io.Serializable { abstract val variantSettingOne: Property abstract val variantSettingTwo: Property`

and this is the corresponding registration and instantiation code : ` androidComponents.registerExtension( DslExtension.Builder("dslExtension") .extendProjectWith(ProjectDslExtension::class.java) .build() ) { config -> project.objects.newInstance( VariantDslExtension::class.java, config ) } `

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
