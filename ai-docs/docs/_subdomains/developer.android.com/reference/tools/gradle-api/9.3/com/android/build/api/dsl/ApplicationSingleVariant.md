---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApplicationSingleVariant/
title: ApplicationSingleVariant \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:26:59.023505+00:00
---

# ApplicationSingleVariant  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApplicationSingleVariant/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ApplicationSingleVariant

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ApplicationSingleVariant.kt+class:com.android.build.api.dsl.ApplicationSingleVariant)

Added in 7.1.0
    
    
    interface [ApplicationSingleVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApplicationSingleVariant) : [SingleVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SingleVariant)

* * *

Single variant publishing options for application projects.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[publishApk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApplicationSingleVariant#publishApk\(\))()` Configure to publish this variant as APK artifact.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.PublishingOptions](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/PublishingOptions) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[withJavadocJar](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/PublishingOptions#withJavadocJar\(\))()` Publish javadoc jar generated from java & kotlin source as a secondary artifact to a Maven repository.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[withSourcesJar](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/PublishingOptions#withSourcesJar\(\))()` Publish java & kotlin sources jar as a secondary artifact to a Maven repository.  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.SingleVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SingleVariant) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[variantName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SingleVariant#variantName\(\))`  
---|---  
  
## Public functions

### publishApk

Added in 7.1.0
    
    
    fun [publishApk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApplicationSingleVariant#publishApk\(\))(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configure to publish this variant as APK artifact. Android Gradle Plugin would publish this variant as AAB artifact if this function is not invoked.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
