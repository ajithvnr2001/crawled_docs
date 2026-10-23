---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension/
title: SettingsExtension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:14:05.979792+00:00
---

# SettingsExtension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# SettingsExtension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/SettingsExtension.kt+class:com.android.build.api.dsl.SettingsExtension)

Added in 7.4.0
    
    
    interface [SettingsExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension)

* * *

Interface used for the `android` DSL in the `settings.gradle[.kts]` file, after the `com.android.settings` plugin is applied.

This allows settings default values that are then applied to all android projects which this build.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#compileSdk\(kotlin.Function1\))(action: [CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CompileSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding compile Sdk version, see `[CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CompileSdkSpec)` for available options.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[compileSdkAddon](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#compileSdkAddon\(kotlin.String,kotlin.String,kotlin.Int\))(vendor: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Specifies an SDK add-on to compile your project against.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[execution](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#execution\(kotlin.Function1\))(action: [Execution](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Execution).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Set execution profiles and options for tools.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[lint](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#lint\(kotlin.Function1\))(action: [Lint](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Lint).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Set Lint options.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#minSdk\(kotlin.Function1\))(action: [MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding minSdk, see `[MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkSpec)` for available options.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#targetSdk\(kotlin.Function1\))(action: [TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TargetSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding target sdk, see `[TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TargetSdkSpec)` for available options.  
  
### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[addOnName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#addOnName\(\))` Value set via `compileSdkAddon`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[addOnVendor](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#addOnVendor\(\))` Value set via `compileSdkAddon`  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[addOnVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#addOnVersion\(\))` Value set via `compileSdkAddon`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#buildToolsVersion\(\))` Specifies the version of the [SDK Build Tools](https://developer.android.com/studio/releases/build-tools.html) to use when building your project.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#compileSdk\(\))` Specifies the API level to compile your project against.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdkExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#compileSdkExtension\(\))` Specifies the SDK Extension level to compile your project against.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[compileSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#compileSdkPreview\(\))` Specify a preview API to compile your project against.  
`[Execution](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Execution)` |  `[execution](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#execution\(\))` Set execution profiles and options for tools.  
`[Lint](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Lint)` |  `[lint](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#lint\(\))` Set Lint options.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#minSdk\(\))` The minimum SDK version.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#minSdkPreview\(\))` The minimum SDK version for preview APIs.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[ndkPath](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#ndkPath\(\))` Requires the specified path to NDK be used.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[ndkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#ndkVersion\(\))` Requires the specified NDK version to be used.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#targetSdk\(\))` The target SDK version.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#targetSdkPreview\(\))` The target SDK version.  
  
## Public functions

### compileSdk

Added in 9.5.0-alpha10
    
    
    fun [compileSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#compileSdk\(kotlin.Function1\))(action: [CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CompileSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures all aspects regarding compile Sdk version, see `[CompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CompileSdkSpec)` for available options.

### compileSdkAddon

Added in 7.4.0
    
    
    fun [compileSdkAddon](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#compileSdkAddon\(kotlin.String,kotlin.String,kotlin.Int\))(vendor: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies an SDK add-on to compile your project against.

Parameters  
---  
`vendor: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  The vendor of the add-on.  
`name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  The name of the add-on.  
`version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  The version of the add-on.  
  
### execution

Added in 7.4.0
    
    
    fun [execution](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#execution\(kotlin.Function1\))(action: [Execution](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Execution).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Set execution profiles and options for tools.

### lint

Added in 9.5.0-alpha10
    
    
    fun [lint](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#lint\(kotlin.Function1\))(action: [Lint](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Lint).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Set Lint options.

### minSdk

Added in 9.5.0-alpha10
    
    
    fun [minSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#minSdk\(kotlin.Function1\))(action: [MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures all aspects regarding minSdk, see `[MinSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MinSdkSpec)` for available options.

### targetSdk

Added in 9.5.0-alpha10
    
    
    fun [targetSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#targetSdk\(kotlin.Function1\))(action: [TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TargetSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures all aspects regarding target sdk, see `[TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TargetSdkSpec)` for available options.

## Public properties

### addOnName

Added in 7.4.0
    
    
    val [addOnName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#addOnName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Value set via `compileSdkAddon`

### addOnVendor

Added in 7.4.0
    
    
    val [addOnVendor](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#addOnVendor\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Value set via `compileSdkAddon`

### addOnVersion

Added in 7.4.0
    
    
    val [addOnVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#addOnVersion\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Value set via `compileSdkAddon`

### buildToolsVersion

Added in 7.4.0
    
    
    var [buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#buildToolsVersion\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Specifies the version of the [SDK Build Tools](https://developer.android.com/studio/releases/build-tools.html) to use when building your project.

See `[com.android.build.api.dsl.CommonExtension.buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CommonExtension#buildToolsVersion\(kotlin.String\))` for more information

### compileSdk

Added in 7.4.0
    
    
    var [compileSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#compileSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Specifies the API level to compile your project against. The Android plugin requires you to configure this property.

This means your code can use only the Android APIs included in that API level and lower. You can configure the compile sdk version by adding the following to the `android` block: `compileSdk = 26`.

You should generally [use the most up-to-date API level](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels) available. If you are planning to also support older API levels, it's good practice to [use the Lint tool](https://developer.android.com/studio/write/lint.html) to check if you are using APIs that are not available in earlier API levels.

The value you assign to this property is parsed and stored in a normalized form, so reading it back may return a slightly different value.

### compileSdkExtension

Added in 7.4.0
    
    
    var [compileSdkExtension](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#compileSdkExtension\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Specifies the SDK Extension level to compile your project against. This value is optional.

When not provided the base extension for the given `compileSdk` API level will be selected.

### compileSdkPreview

Added in 7.4.0
    
    
    var [compileSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#compileSdkPreview\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Specify a preview API to compile your project against.

For example, to try out the Android S preview, rather than `compileSdk = 30` you can use `compileSdkPreview = "S"`

Once the preview APIs are finalized, they will be allocated a stable integer value.

### execution

Added in 7.4.0
    
    
    val [execution](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#execution\(\)): [Execution](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Execution)

Set execution profiles and options for tools.

### lint

Added in 9.5.0-alpha10
    
    
    val [lint](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#lint\(\)): [Lint](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Lint)

Set Lint options.

### minSdk

Added in 7.4.0
    
    
    var [minSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#minSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

The minimum SDK version. Setting this it will override previous calls of `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#minSdk\(kotlin.Function1\))` and `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#minSdkPreview\(\))` setters. Only one of `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#minSdk\(kotlin.Function1\))` and `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#minSdkPreview\(\))` should be set.

See [uses-sdk element documentation](http://developer.android.com/guide/topics/manifest/uses-sdk-element.html).

### minSdkPreview

Added in 7.4.0
    
    
    var [minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#minSdkPreview\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The minimum SDK version for preview APIs. Setting this will override previous calls of `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#minSdk\(kotlin.Function1\))` and `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#minSdkPreview\(\))` setters. Only one of `[minSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#minSdk\(kotlin.Function1\))` and `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#minSdkPreview\(\))` should be set.

See [uses-sdk element documentation](http://developer.android.com/guide/topics/manifest/uses-sdk-element.html).

### ndkPath

Added in 7.4.0
    
    
    var [ndkPath](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#ndkPath\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Requires the specified path to NDK be used.

See `[com.android.build.api.dsl.CommonExtension.ndkPath](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CommonExtension#ndkPath\(\))` for more information

### ndkVersion

Added in 7.4.0
    
    
    var [ndkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#ndkVersion\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Requires the specified NDK version to be used.

See `[com.android.build.api.dsl.CommonExtension.ndkVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/CommonExtension#ndkVersion\(\))` for more information

### targetSdk

Added in 8.8.0
    
    
    var [targetSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#targetSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

The target SDK version. Setting this it will override previous calls of `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#targetSdk\(kotlin.Function1\))` and `[targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#targetSdkPreview\(\))` setters. Only one of `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#targetSdk\(kotlin.Function1\))` and `[targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#targetSdkPreview\(\))` should be set.

See [uses-sdk element documentation](http://developer.android.com/guide/topics/manifest/uses-sdk-element.html).

### targetSdkPreview

Added in 8.8.0
    
    
    var [targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#targetSdkPreview\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The target SDK version. Setting this it will override previous calls of `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#targetSdk\(kotlin.Function1\))` and `[targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#targetSdkPreview\(\))` setters. Only one of `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#targetSdk\(kotlin.Function1\))` and `[targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/SettingsExtension#targetSdkPreview\(\))` should be set.

See [uses-sdk element documentation](http://developer.android.com/guide/topics/manifest/uses-sdk-element.html).

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
