---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SingleVariant/
title: SingleVariant \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:14:15.336647+00:00
---

# SingleVariant  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SingleVariant/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# SingleVariant

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/SingleVariant.kt+class:com.android.build.api.dsl.SingleVariant)

Added in 7.1.0
    
    
    interface [SingleVariant](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SingleVariant) : [PublishingOptions](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/PublishingOptions)

Known direct subclasses 

[ApplicationSingleVariant](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ApplicationSingleVariant), [LibrarySingleVariant](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/LibrarySingleVariant)

`[ApplicationSingleVariant](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ApplicationSingleVariant)` |  Single variant publishing options for application projects.  
---|---  
`[LibrarySingleVariant](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/LibrarySingleVariant)` |  Single variant publishing options for library projects.  
  
* * *

Single variant publishing options.

## Summary

### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[variantName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SingleVariant#variantName\(\))`  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.PublishingOptions](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/PublishingOptions) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[withJavadocJar](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/PublishingOptions#withJavadocJar\(\))()` Publish javadoc jar generated from java & kotlin source as a secondary artifact to a Maven repository.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[withSourcesJar](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/PublishingOptions#withSourcesJar\(\))()` Publish java & kotlin sources jar as a secondary artifact to a Maven repository.  
  
## Public properties

### variantName

Added in 7.1.0
    
    
    val [variantName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SingleVariant#variantName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
