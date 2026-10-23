---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Publishing/
title: Publishing \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:55:20.110600+00:00
---

# Publishing  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Publishing/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Publishing

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/Publishing.kt+class:com.android.build.api.dsl.Publishing)

Added in 7.1.0
    
    
    interface [Publishing](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Publishing)<SingleVariantT : [SingleVariant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/SingleVariant)>

Known direct subclasses 

[ApplicationPublishing](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationPublishing), [LibraryPublishing](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryPublishing)

`[ApplicationPublishing](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationPublishing)` |  Maven publishing DSL object for configuring options related to publishing APK and AAB.  
---|---  
`[LibraryPublishing](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryPublishing)` |  Maven publishing DSL object for configuring options related to publishing AAR.  
  
* * *

Maven publishing DSL object for configuring options related to publishing Android variants to a Maven repository.

Android Gradle Plugin 7.1.0 and higher allows you to configure which build variants to publish to an Apache Maven repository. Android Gradle Plugin creates components for those variants in your app or library module that you can use to customize a publication to a Maven repository. You are able to publish build variants in two different publishing mechanisms: single variant publishing and multiple variants publishing.

In single variant publishing, Android Gradle Plugin creates a component for the variant you want to publish in your app or library module. The component has the same name as the variant and only contains that single variant. For modules that use the application plugin, Android Gradle Plugin publishes the variant as an Android App Bundle(AAB) by default. You can publish the variant as a ZIP of APK(s) instead by using `[ApplicationSingleVariant.publishApk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationSingleVariant#publishApk\(\))` inside the singleVariant config block. However, publishing the variant as AAB and APK together is not supported.

Multiple variants publishing allows you to publish multiple variants in your library module and choose the name of the component those variants are added to. The component name is set to “default” unless you specify it in the multipleVariants function call. Android Gradle Plugin adds necessary variant specific attributes including buildType and flavorDimensions to disambiguate those variants. Note that multiple variants publishing is not supported in app modules.

`[LibraryPublishing](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryPublishing)` extends this with options for publishing library projects. `[ApplicationPublishing](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationPublishing)` extends this with options for publishing application projects.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[singleVariant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Publishing#singleVariant\(kotlin.String\))(variantName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Publish a variant with single variant publishing mechanism.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[singleVariant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Publishing#singleVariant\(kotlin.String,kotlin.Function1\))(variantName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), action: SingleVariantT.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Publish a variant with single variant publishing options.  
  
## Public functions

### singleVariant

Added in 7.1.0
    
    
    fun [singleVariant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Publishing#singleVariant\(kotlin.String\))(variantName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Publish a variant with single variant publishing mechanism.

### singleVariant

Added in 7.1.0
    
    
    fun [singleVariant](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Publishing#singleVariant\(kotlin.String,kotlin.Function1\))(variantName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), action: SingleVariantT.() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Publish a variant with single variant publishing options.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
