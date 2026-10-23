---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension/
title: PrivacySandboxSdkExtension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:02:40.804966+00:00
---

# PrivacySandboxSdkExtension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# PrivacySandboxSdkExtension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/PrivacySandboxSdkExtension.kt+class:com.android.build.api.dsl.PrivacySandboxSdkExtension)

Added in 7.4.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [PrivacySandboxSdkExtension](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension)

* * *

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[bundle](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#bundle\(kotlin.Function1\))(action: [PrivacySandboxSdkBundle](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkBundle).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[lint](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#lint\(kotlin.Function1\))(action: [Lint](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Lint).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the lint tool.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[optimization](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#optimization\(kotlin.Function1\))(action: [PrivacySandboxSdkOptimization](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkOptimization).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the R8/D8 optimization tool.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[signingConfig](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#signingConfig\(kotlin.Function1\))(action: [SigningConfig](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SigningConfig).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
  
### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#buildToolsVersion\(\))` Specifies the version of the [SDK Build Tools](https://developer.android.com/studio/releases/build-tools.html) to use when building your project.  
`[PrivacySandboxSdkBundle](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkBundle)` |  `[bundle](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#bundle\(\))`  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdk](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#compileSdk\(\))` Specifies the API level to compile your project against.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[compileSdkExtension](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#compileSdkExtension\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[compileSdkPreview](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#compileSdkPreview\(\))`  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>` |  `[experimentalProperties](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#experimentalProperties\(\))`  
`[Lint](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Lint)` |  `[lint](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#lint\(\))` Specifies options for the lint tool.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[minSdk](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#minSdk\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[minSdkPreview](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#minSdkPreview\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[namespace](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#namespace\(\))`  
`[PrivacySandboxSdkOptimization](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkOptimization)` |  `[optimization](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#optimization\(\))` Specifies options for the R8/D8 optimization tool.  
`[SigningConfig](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SigningConfig)` |  `[signingConfig](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#signingConfig\(\))`  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#targetSdk\(\))`  
  
## Public functions

### bundle

Added in 7.4.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [bundle](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#bundle\(kotlin.Function1\))(action: [PrivacySandboxSdkBundle](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkBundle).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### lint

Added in 8.8.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [lint](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#lint\(kotlin.Function1\))(action: [Lint](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Lint).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for the lint tool.

For more information about the properties you can configure in this block, see `[Lint](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Lint)`.

### optimization

Added in 8.4.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [optimization](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#optimization\(kotlin.Function1\))(action: [PrivacySandboxSdkOptimization](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkOptimization).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for the R8/D8 optimization tool.

For more information about the properties you can configure in this block, see `[PrivacySandboxSdkOptimization](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkOptimization)`.

### signingConfig

Added in 8.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [signingConfig](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#signingConfig\(kotlin.Function1\))(action: [SigningConfig](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SigningConfig).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

## Public properties

### buildToolsVersion

Added in 7.4.0
    
    
    var [buildToolsVersion](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#buildToolsVersion\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Specifies the version of the [SDK Build Tools](https://developer.android.com/studio/releases/build-tools.html) to use when building your project.

By default, the plugin uses the minimum version of the build tools required by the [version of the plugin](https://developer.android.com/studio/releases/gradle-plugin.html#revisions) you're using. To specify a different version of the build tools for the plugin to use, specify the version as follows:
    
    
    android {  
        // Specifying this property is optional.  
        buildToolsVersion "26.0.0"  
    }

For a list of build tools releases, read [the release notes](https://developer.android.com/studio/releases/build-tools.html#notes).

Note that the value assigned to this property is parsed and stored in a normalized form, so reading it back may give a slightly different result.

### bundle

Added in 7.4.0
    
    
    val [bundle](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#bundle\(\)): [PrivacySandboxSdkBundle](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkBundle)

### compileSdk

Added in 7.4.0
    
    
    var [compileSdk](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#compileSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Specifies the API level to compile your project against. The Android plugin requires you to configure this property.

This means your code can use only the Android APIs included in that API level and lower. You can configure the compile sdk version by adding the following to the `android` block: `compileSdk = 26`.

You should generally [use the most up-to-date API level](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels) available. If you are planning to also support older API levels, it's good practice to [use the Lint tool](https://developer.android.com/studio/write/lint.html) to check if you are using APIs that are not available in earlier API levels.

The value you assign to this property is parsed and stored in a normalized form, so reading it back may return a slightly different value.

### compileSdkExtension

Added in 7.4.0
    
    
    var [compileSdkExtension](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#compileSdkExtension\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

### compileSdkPreview

Added in 7.4.0
    
    
    var [compileSdkPreview](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#compileSdkPreview\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

### experimentalProperties

Added in 8.2.0
    
    
    val [experimentalProperties](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#experimentalProperties\(\)): [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)>

### lint

Added in 8.8.0
    
    
    val [lint](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#lint\(\)): [Lint](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/Lint)

Specifies options for the lint tool.

Android Studio and the Android SDK provide a code scanning tool called lint that can help you to identify and correct problems with the structural quality of your code without having to execute the app or write test cases. Each problem the tool detects is reported with a description message and a severity level, so that you can quickly prioritize the critical improvements that need to be made.

This property allows you to configure certain lint options, such as which checks to run or ignore. If you're using Android Studio, you can [configure similar lint options](https://developer.android.com/studio/write/lint.html#cis) from the IDE.

To learn more about using and running lint, read [Improve Your Code with Lint](https://developer.android.com/studio/write/lint.html).

See also  
---  
`[LintOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/gradle/internal/dsl/LintOptions)` |   
  
### minSdk

Added in 7.4.0
    
    
    var [minSdk](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#minSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

### minSdkPreview

Added in 7.4.0
    
    
    var [minSdkPreview](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#minSdkPreview\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

### namespace

Added in 7.4.0

Deprecated in 7.4.0
    
    
    var [namespace](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#namespace\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

### optimization

Added in 8.4.0
    
    
    val [optimization](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#optimization\(\)): [PrivacySandboxSdkOptimization](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkOptimization)

Specifies options for the R8/D8 optimization tool.

For more information about the properties you can configure in this block, see `[PrivacySandboxSdkOptimization](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkOptimization)`.

### signingConfig

Added in 8.1.0
    
    
    val [signingConfig](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#signingConfig\(\)): [SigningConfig](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SigningConfig)

### targetSdk

Added in 8.7.0
    
    
    var [targetSdk](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/PrivacySandboxSdkExtension#targetSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
