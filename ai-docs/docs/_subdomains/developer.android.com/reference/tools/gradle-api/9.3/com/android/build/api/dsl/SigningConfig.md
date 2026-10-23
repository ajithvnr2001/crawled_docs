---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig/
title: SigningConfig \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:31:46.581872+00:00
---

# SigningConfig  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# SigningConfig

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/SigningConfig.kt+class:com.android.build.api.dsl.SigningConfig)

Added in 4.2.0
    
    
    interface [SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig)

Known direct subclasses 

[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApkSigningConfig)

`[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApkSigningConfig)` |  DSL object to configure signing configs.  
---|---  
  
* * *

DSL object for configuring options related to signing for APKs and bundles.

`[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApkSigningConfig)` extends this with options relating to just APKs

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[initWith](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig#initWith\(com.android.build.api.dsl.SigningConfig\))(that: [SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig))` Copies all properties from the given signing config.  
  
### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[keyAlias](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig#keyAlias\(\))` Key alias used when signing.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[keyPassword](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig#keyPassword\(\))` Key password used when signing.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[storeFile](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig#storeFile\(\))` Store file used when signing.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[storePassword](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig#storePassword\(\))` Store password used when signing.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[storeType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig#storeType\(\))` Store type used when signing.  
  
## Public functions

### initWith

Added in 7.0.0
    
    
    fun [initWith](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig#initWith\(com.android.build.api.dsl.SigningConfig\))(that: [SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Copies all properties from the given signing config.

## Public properties

### keyAlias

Added in 4.2.0
    
    
    var [keyAlias](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig#keyAlias\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Key alias used when signing.

See [Signing Your Applications](http://developer.android.com/tools/publishing/app-signing.html)

### keyPassword

Added in 4.2.0
    
    
    var [keyPassword](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig#keyPassword\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Key password used when signing.

See [Signing Your Applications](http://developer.android.com/tools/publishing/app-signing.html)

### storeFile

Added in 4.2.0
    
    
    var [storeFile](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig#storeFile\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?

Store file used when signing.

See [Signing Your Applications](http://developer.android.com/tools/publishing/app-signing.html)

### storePassword

Added in 4.2.0
    
    
    var [storePassword](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig#storePassword\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Store password used when signing.

See [Signing Your Applications](http://developer.android.com/tools/publishing/app-signing.html)

### storeType

Added in 4.2.0
    
    
    var [storeType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/SigningConfig#storeType\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Store type used when signing.

See [Signing Your Applications](http://developer.android.com/tools/publishing/app-signing.html)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
