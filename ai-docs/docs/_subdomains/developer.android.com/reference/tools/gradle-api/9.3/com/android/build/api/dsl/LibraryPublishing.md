---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryPublishing/
title: LibraryPublishing \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:30:34.988240+00:00
---

# LibraryPublishing  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryPublishing/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# LibraryPublishing

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/LibraryPublishing.kt+class:com.android.build.api.dsl.LibraryPublishing)

Added in 7.1.0
    
    
    interface [LibraryPublishing](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryPublishing) : [Publishing](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Publishing)

* * *

Maven publishing DSL object for configuring options related to publishing AAR.

To publish just one variant, use `[singleVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryPublishing#singleVariant\(kotlin.String\))`. The following sets up publishing of only the fullRelease variant of an android library.
    
    
    android {  
        // This project has four build variants: fullDebug, fullRelease, demoDebug, demoRelease  
        flavorDimensions 'mode'  
        productFlavors {  
            full {}  
            demo {}  
        }  
      
        publishing {  
            // Publishes "fullRelease" build variant with "fullRelease" component created by  
            // Android Gradle plugin  
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

To publish multiple variants, use `[multipleVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryPublishing#multipleVariants\(kotlin.String,kotlin.Function1\))`. The following sets up publishing of both fullDebug and fullRelease variants of an android library.
    
    
    android {  
        publishing {  
            // Published fullDebug and fullRelease build variants with "full" component created by  
            // Android Gradle Plugin. The buildType attribute is added to published build variants.  
            // As only a single flavor from "mode" dimension is included, no flavor attribute is  
            // included.  
            multipleVariants("full") {  
                includeBuildTypeValues("debug", "release")  
                includeFlavorDimensionAndValues("mode", "full")  
            }  
        }  
    }  
      
    afterEvaluate {  
        publishing {  
            publications {  
                full(MavenPublication) {  
                    from components.full  
                    // ......  
                }  
            }  
        }  
    }

To publish all the build variants, you can use `[MultipleVariants.allVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MultipleVariants#allVariants\(\))` as a shortcut instead of filtering variants with `[MultipleVariants.includeBuildTypeValues](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MultipleVariants#includeBuildTypeValues\(kotlin.Array\))` and `[MultipleVariants.includeFlavorDimensionAndValues](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MultipleVariants#includeFlavorDimensionAndValues\(kotlin.String,kotlin.Array\))`.
    
    
    android {  
        publishing {  
            // Publishes all build variants with "default" component  
            multipleVariants {  
                allVariants()  
            }  
        }  
    }  
      
    afterEvaluate {  
        publishing {  
            publications {  
                allVariants(MavenPublication) {  
                    from components.default  
                    // ......  
                }  
            }  
        }  
    }

This following code example shows how to create two publications one for demoRelease build variant, one for fullDebug & fullRelease build variants.
    
    
    android {  
        publishing {  
            // Publish "demoRelease" build variant with "demoRelease" component  
            singleVariant("demoRelease")  
      
            // Publish "fullDebug" and "fullRelease" build variants with "full" component  
            multipleVariants("full") {  
                includeBuildTypeValues("debug", "release")  
                includeFlavorDimensionAndValues("mode", "full")  
            }  
        }  
    }  
      
    afterEvaluate {  
        publishing {  
            publications {  
                // Creates two publications with different artifactIds  
                full(MavenPublication) {  
                    from components.full  
                    groupId = 'com.example.MyLibrary'  
                    artifactId = 'final-full'  
                    version = '1.0'  
                }  
                demoRelease(MavenPublication) {  
                    from components.demoRelease  
                    groupId = 'com.example.MyLibrary'  
                    artifactId = 'final-demo'  
                    version = '1.0'  
                }  
            }  
        }  
    }

The testFixtures component is published by default with its main variant. To disable publishing the testFixtures component, see the following example.
    
    
    afterEvaluate {  
        // Disable publishing test fixtures of release variant  
        components.release.withVariantsFromConfiguration(  
            configurations.releaseTestFixturesVariantReleaseApiPublication) { skip() }  
        components.release.withVariantsFromConfiguration(  
            configurations.releaseTestFixturesVariantReleaseRuntimePublication) { skip() }  
    }

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[multipleVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryPublishing#multipleVariants\(kotlin.Function1\))(action: [MultipleVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MultipleVariants).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Publish multiple variants to the default component.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[multipleVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryPublishing#multipleVariants\(kotlin.String,kotlin.Function1\))(componentName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), action: [MultipleVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MultipleVariants).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Publish multiple variants to a component.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.Publishing](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Publishing) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[singleVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Publishing#singleVariant\(kotlin.String\))(variantName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Publish a variant with single variant publishing mechanism.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[singleVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Publishing#singleVariant\(kotlin.String,kotlin.Function1\))(variantName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), action: [LibrarySingleVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibrarySingleVariant).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Publish a variant with single variant publishing options.  
  
## Public functions

### multipleVariants

Added in 7.1.0
    
    
    fun [multipleVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryPublishing#multipleVariants\(kotlin.Function1\))(action: [MultipleVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MultipleVariants).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Publish multiple variants to the default component.

### multipleVariants

Added in 7.1.0
    
    
    fun [multipleVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryPublishing#multipleVariants\(kotlin.String,kotlin.Function1\))(componentName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), action: [MultipleVariants](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MultipleVariants).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Publish multiple variants to a component.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
