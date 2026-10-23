---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestAndroidComponentsExtension/
title: TestAndroidComponentsExtension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:55:30.994021+00:00
---

# TestAndroidComponentsExtension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestAndroidComponentsExtension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestAndroidComponentsExtension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/TestAndroidComponentsExtension.kt+class:com.android.build.api.variant.TestAndroidComponentsExtension)

Added in 7.0.0
    
    
    interface [TestAndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestAndroidComponentsExtension) : [AndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension)

* * *

Extension for the Android Test Gradle Plugin components.

This is the `androidComponents` block when the `com.android.test` plugin is applied.

Only the Android Gradle Plugin should create instances of interfaces in com.android.build.api.variant.

## Summary

### Inherited functions  
  
---  
From [com.android.build.api.variant.AndroidComponentsExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[addSourceSetConfigurations](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#addSourceSetConfigurations\(kotlin.String\))(suffix: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds a custom configuration for each source set.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,org.gradle.api.Action\))(  
selector: [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantSelector),  
callback: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<[TestVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestVariantBuilder)>  
)` `[Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)` based version of `[beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` above.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))(  
selector: [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantSelector),  
callback: ([TestVariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestVariantBuilder)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
)` Method to register a `[callback](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` to be called with `[VariantBuilderT](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension)` instances that satisfies the `[selector](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))`.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[onVariants](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,org.gradle.api.Action\))(selector: [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantSelector), callback: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<[TestVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestVariant)>)` `[Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)` based version of `[onVariants](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` above.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[onVariants](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))(selector: [VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantSelector), callback: ([TestVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestVariant)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Allow for registration of a `[callback](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` to be called with variant instances of type `[VariantT](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension)` once the list of `[com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact)` has been determined.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[registerExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#registerExtension\(com.android.build.api.variant.DslExtension,kotlin.Function1\))(  
dslExtension: [DslExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DslExtension),  
configurator: (variantExtensionConfig: [VariantExtensionConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantExtensionConfig)<[TestVariant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/TestVariant)>) -> [VariantExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantExtension)  
)` Register an Android Gradle Plugin DSL extension.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[registerSourceType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#registerSourceType\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Register a new source type to all source sets.  
`[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantSelector)` |  `[selector](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#selector\(\))()` Creates a `[VariantSelector](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantSelector)` instance that can be configured to reduce the set of `[ComponentBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/ComponentBuilder)` instances participating in the `[beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` and `[onVariants](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` callback invocation.  
  
From [com.android.build.api.variant.DslLifecycle](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DslLifecycle) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[finalizeDsl](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DslLifecycle#finalizeDsl\(org.gradle.api.Action\))(callback: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<[TestExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestExtension)>)` `[Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)` based version of `[finalizeDsl](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DslLifecycle#finalizeDsl\(kotlin.Function1\))` above.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[finalizeDsl](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/DslLifecycle#finalizeDsl\(kotlin.Function1\))(callback: ([TestExtension](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/TestExtension)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` API to customize the DSL Objects programmatically after they have been evaluated from the build files and before used in the build process next steps like variant or tasks creation.  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.AndroidComponents](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponents) | `[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)` |  `[pluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponents#pluginVersion\(\))` The version of the Android Gradle Plugin currently in use.  
---|---  
`[SdkComponents](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/SdkComponents)` |  `[sdkComponents](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponents#sdkComponents\(\))` Provides access to underlying Android SDK and build-tools components like adb.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
