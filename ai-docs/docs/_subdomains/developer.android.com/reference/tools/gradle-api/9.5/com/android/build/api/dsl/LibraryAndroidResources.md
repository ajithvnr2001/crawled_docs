---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/LibraryAndroidResources/
title: LibraryAndroidResources \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:12:23.058866+00:00
---

# LibraryAndroidResources  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/LibraryAndroidResources/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# LibraryAndroidResources

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/LibraryAndroidResources.kt+class:com.android.build.api.dsl.LibraryAndroidResources)

Added in 8.1.0
    
    
    interface [LibraryAndroidResources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/LibraryAndroidResources) : [AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidResources)

* * *

DSL object for configuring Android resource options for Library plugins. This is accessed via `[LibraryExtension.androidResources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/LibraryExtension#androidResources\(kotlin.Function1\))`

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/LibraryAndroidResources#enable\(\))` Flag to enable Android resource processing in this library module Default value is 'true' for plain android libraries and 'false' for multiplatform libraries.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[resourcePrefix](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/LibraryAndroidResources#resourcePrefix\(\))` Specifies a resource name prefix required for all resources defined in this module.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidResources) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidResources#additionalParameters\(kotlin.String\))~~(params: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property additionalParameters  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidResources#additionalParameters\(kotlin.Array\))~~(vararg params: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property additionalParameters  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[noCompress](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidResources#noCompress\(kotlin.String\))~~(noCompress: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property noCompress  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[noCompress](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidResources#noCompress\(kotlin.Array\))~~(vararg noCompress: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced with property noCompress  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.AndroidResources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidResources) | `[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[additionalParameters](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidResources#additionalParameters\(\))` List of additional parameters to pass to `aapt`.  
---|---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[failOnMissingConfigEntry](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidResources#failOnMissingConfigEntry\(\))` Forces aapt to return an error if it fails to find an entry for a configuration.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[ignoreAssetsPattern](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidResources#ignoreAssetsPattern\(\))` Pattern describing assets to be ignored.  
`[MutableCollection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[ignoreAssetsPatterns](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidResources#ignoreAssetsPatterns\(\))` Patterns describing assets to be ignored.  
`[MutableCollection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[noCompress](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidResources#noCompress\(\))` File extensions of Android resources, assets, and Java resources to be stored uncompressed in the APK.  
  
## Public properties

### enable

Added in 8.11.0
    
    
    var [enable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/LibraryAndroidResources#enable\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Flag to enable Android resource processing in this library module Default value is 'true' for plain android libraries and 'false' for multiplatform libraries.

### resourcePrefix

Added in 9.5.0-alpha10
    
    
    var [resourcePrefix](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/LibraryAndroidResources#resourcePrefix\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Specifies a resource name prefix required for all resources defined in this module.

This setting is used by Android Studio editor features and Android Lint checks (the `ResourceName` detector) to ensure that all resources in this module adhere to the prefix convention.

This property does not automatically prepend the prefix to resources at build time; rather, it validates and enforces that developer-defined resource names begin with the prefix, flagging violations during IDE editing and command-line `./gradlew lint` runs.

Including unique prefixes for module resources helps avoid naming collisions when resources from multiple libraries are merged into a single application namespace.

When specifying a prefix:

  * It is recommended to include a trailing underscore (e.g. `"mylib_"`).

  * XML and file resource names must start with the snake_case prefix (e.g., `mylib_header_icon.xml`, `@string/mylib_button_label`).

  * Styleables and attributes can use the camelCase equivalent (e.g., `<declare-styleable name="MyLibView">` or `myLibAttribute`).




You can specify this prefix as shown below:
    
    
    android {  
        androidResources {  
            resourcePrefix = "mylib_"  
        }  
    }

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
