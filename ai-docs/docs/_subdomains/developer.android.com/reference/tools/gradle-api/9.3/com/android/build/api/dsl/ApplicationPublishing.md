---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApplicationPublishing/
title: ApplicationPublishing \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:26:55.974610+00:00
---

# ApplicationPublishing  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApplicationPublishing/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ApplicationPublishing

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ApplicationPublishing.kt+class:com.android.build.api.dsl.ApplicationPublishing)

Added in 7.1.0
    
    
    interface [ApplicationPublishing](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApplicationPublishing) : [Publishing](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Publishing)

* * *

Maven publishing DSL object for configuring options related to publishing APK and AAB.

This following code example creates a publication for the fullRelease build variant, which publish your app as Android App Bundle.
    
    
    android {  
        // This project has four build variants: fullDebug, fullRelease, demoDebug, demoRelease  
        flavorDimensions 'mode'  
        productFlavors {  
            full {}  
            demo {}  
        }  
      
        publishing {  
            // Publish your app as an AAB  
            singleVariant("fullRelease")  
        }  
    }  
      
    afterEvaluate {  
        publishing {  
            publications {  
                fullRelease(MavenPublication) {  
                    from components.fullRelease  
                    // ......  
                }  
            }  
        }  
    }

To publish your app as a ZIP file of APKs, simply use the `[ApplicationSingleVariant.publishApk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApplicationSingleVariant#publishApk\(\))` as shown in the following example.
    
    
    android {  
        publishing {  
            // Publish your app as a ZIP file of APKs  
            singleVariant("fullRelease") {  
                publishApk()  
            }  
        }  
    }

## Summary

### Inherited functions  
  
---  
From [com.android.build.api.dsl.Publishing](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Publishing) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[singleVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Publishing#singleVariant\(kotlin.String\))(variantName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Publish a variant with single variant publishing mechanism.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[singleVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Publishing#singleVariant\(kotlin.String,kotlin.Function1\))(variantName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), action: [ApplicationSingleVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApplicationSingleVariant).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Publish a variant with single variant publishing options.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
