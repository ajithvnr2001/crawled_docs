---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PublishingOptions/
title: PublishingOptions \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:34:49.638505+00:00
---

# PublishingOptions  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PublishingOptions/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# PublishingOptions

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/PublishingOptions.kt+class:com.android.build.api.dsl.PublishingOptions)

Added in 7.1.0
    
    
    interface [PublishingOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PublishingOptions)

Known direct subclasses 

[MultipleVariants](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/MultipleVariants), [SingleVariant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/SingleVariant)

`[MultipleVariants](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/MultipleVariants)` |  Multi variant publishing options.  
---|---  
`[SingleVariant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/SingleVariant)` |  Single variant publishing options.  
  
Known indirect subclasses 

[ApplicationSingleVariant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationSingleVariant), [LibrarySingleVariant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LibrarySingleVariant)

`[ApplicationSingleVariant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApplicationSingleVariant)` |  Single variant publishing options for application projects.  
---|---  
`[LibrarySingleVariant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LibrarySingleVariant)` |  Single variant publishing options for library projects.  
  
* * *

Maven publishing options shared by `[SingleVariant](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/SingleVariant)` and `[MultipleVariants](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/MultipleVariants)`.

To publish sources & javadoc jar apart from AAR, use `[withSourcesJar](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PublishingOptions#withSourcesJar\(\))` and `[withJavadocJar](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PublishingOptions#withJavadocJar\(\))`. The following sets up publishing of sources & javadoc jar in two different publishing mechanisms.
    
    
    android {  
        publishing {  
            singleVariant("release") {  
                withSourcesJar()  
                withJavadocJar()  
            }  
      
            multipleVariants {  
                withSourcesJar()  
                withJavadocJar()  
                allVariants()  
            }  
        }  
    }

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[withJavadocJar](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PublishingOptions#withJavadocJar\(\))()` Publish javadoc jar generated from java & kotlin source as a secondary artifact to a Maven repository.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[withSourcesJar](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PublishingOptions#withSourcesJar\(\))()` Publish java & kotlin sources jar as a secondary artifact to a Maven repository.  
  
## Public functions

### withJavadocJar

Added in 7.1.0
    
    
    fun [withJavadocJar](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PublishingOptions#withJavadocJar\(\))(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Publish javadoc jar generated from java & kotlin source as a secondary artifact to a Maven repository.

### withSourcesJar

Added in 7.1.0
    
    
    fun [withSourcesJar](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/PublishingOptions#withSourcesJar\(\))(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Publish java & kotlin sources jar as a secondary artifact to a Maven repository.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
