---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec/
title: CompileSdkSpec \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:57:25.872856+00:00
---

# CompileSdkSpec  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# CompileSdkSpec

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/CompileSdkSpec.kt+class:com.android.build.api.dsl.CompileSdkSpec)

Added in 8.12.3
    
    
    interface [CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec)

* * *

Specifies the API level to compile your project against, which is required by the Android plugin.

This means your code can use only the Android APIs included in that API level and lower. You can configure the compile sdk version by adding the following block:
    
    
    android {  
      compileSdk {  
        version = release(33) {  
          // this block and its properties are optional  
          minorApiLevel = 1  
          sdkExtension = 18  
        }  
      }  
    }

or to use a preview version:
    
    
    android {  
      compileSdk {  
        version = preview("Tiramisu")  
      }  
    }

You should generally [use the most up-to-date API level](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels) available.

If you are planning to also support older API levels, it's good practice to [use the Lint tool](https://developer.android.com/studio/write/lint.html) to check if you are using APIs that are not available in earlier API levels.

This can be set on all Gradle projects with `[com.android.build.api.dsl.SettingsExtension.compileSdk](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SettingsExtension#compileSdk\(\))`

## Summary

### Public functions  
  
---  
`[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion)` |  `[addon](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec#addon\(kotlin.String,kotlin.String,kotlin.Int\))(vendor: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Specify an SDK add-on to compile your project against.  
`[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion)` |  `[preview](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec#preview\(kotlin.String\))(codeName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` To set compile SDK version with a preview API level, use this function to compute the `[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion)` and assign it to `[CompileSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec#version\(\))` property.  
`[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion)` |  `[release](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec#release\(kotlin.Int\))(version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` To set compile SDK version with a released API level, use this function to compute the `[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion)` and assign it to `[CompileSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec#version\(\))` property.  
`[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion)` |  `[release](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec#release\(kotlin.Int,kotlin.Function1\))(version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), action: [CompileSdkReleaseSpec](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkReleaseSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` To set compile SDK version with a released API level, use this function to compute the `[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion)` and assign it to `[CompileSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec#version\(\))` property.  
  
### Public properties  
  
---  
`[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion)?` |  `[version](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec#version\(\))` The compile SDK version set for this project.  
  
## Public functions

### addon

Added in 8.12.3
    
    
    fun [addon](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec#addon\(kotlin.String,kotlin.String,kotlin.Int\))(vendor: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion)

Specify an SDK add-on to compile your project against.

This can be set on all Gradle projects with `[com.android.build.api.dsl.SettingsExtension.compileSdkAddon](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SettingsExtension#compileSdkAddon\(kotlin.String,kotlin.String,kotlin.Int\))`

Parameters  
---  
`vendor: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the vendor name of the add-on.  
`name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the name of the add-on  
`version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  the integer API level of the add-on  
  
### preview

Added in 8.12.3
    
    
    fun [preview](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec#preview\(kotlin.String\))(codeName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion)

To set compile SDK version with a preview API level, use this function to compute the `[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion)` and assign it to `[CompileSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec#version\(\))` property.

### release

Added in 8.12.3
    
    
    fun [release](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec#release\(kotlin.Int\))(version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion)

To set compile SDK version with a released API level, use this function to compute the `[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion)` and assign it to `[CompileSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec#version\(\))` property.

### release

Added in 8.12.3
    
    
    fun [release](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec#release\(kotlin.Int,kotlin.Function1\))(version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), action: [CompileSdkReleaseSpec](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkReleaseSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion)

To set compile SDK version with a released API level, use this function to compute the `[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion)` and assign it to `[CompileSdkSpec.version](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec#version\(\))` property. When using a released API level, you can also set minor API level and SDK extension level via `[CompileSdkReleaseSpec](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkReleaseSpec)` block.

## Public properties

### version

Added in 8.12.3
    
    
    var [version](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkSpec#version\(\)): [CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileSdkVersion)?

The compile SDK version set for this project.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-09-11 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-11 UTC."],[],[]] 
