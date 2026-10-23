---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApkSigningConfig/
title: ApkSigningConfig \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:54:43.913418+00:00
---

# ApkSigningConfig  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApkSigningConfig/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ApkSigningConfig

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ApkSigningConfig.kt+class:com.android.build.api.dsl.ApkSigningConfig)

Added in 7.0.0
    
    
    interface [ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApkSigningConfig) : [SigningConfig](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SigningConfig), [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html)

* * *

DSL object to configure signing configs.

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[enableV1Signing](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApkSigningConfig#enableV1Signing\(\))` Enable signing using JAR Signature Scheme (aka v1 signing).  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[enableV2Signing](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApkSigningConfig#enableV2Signing\(\))` Enable signing using APK Signature Scheme v2 (aka v2 signing).  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[enableV3Signing](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApkSigningConfig#enableV3Signing\(\))` Enable signing using APK Signature Scheme v3 (aka v3 signing).  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[enableV4Signing](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApkSigningConfig#enableV4Signing\(\))` Enable signing using APK Signature Scheme v4 (aka v4 signing).  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isV1SigningEnabled](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApkSigningConfig#isV1SigningEnabled\(\))` **This property is deprecated.** This property is deprecated  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isV2SigningEnabled](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApkSigningConfig#isV2SigningEnabled\(\))` **This property is deprecated.** This property is deprecated  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
From [com.android.build.api.dsl.SigningConfig](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SigningConfig) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[initWith](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SigningConfig#initWith\(com.android.build.api.dsl.SigningConfig\))(that: [SigningConfig](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SigningConfig))` Copies all properties from the given signing config.  
---|---  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.SigningConfig](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SigningConfig) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[keyAlias](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SigningConfig#keyAlias\(\))` Key alias used when signing.  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[keyPassword](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SigningConfig#keyPassword\(\))` Key password used when signing.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[storeFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SigningConfig#storeFile\(\))` Store file used when signing.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[storePassword](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SigningConfig#storePassword\(\))` Store password used when signing.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[storeType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/SigningConfig#storeType\(\))` Store type used when signing.  
  
## Public properties

### enableV1Signing
    
    
    var [enableV1Signing](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApkSigningConfig#enableV1Signing\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Enable signing using JAR Signature Scheme (aka v1 signing). If null, a default value is used.

See [Signing Your Applications](http://developer.android.com/tools/publishing/app-signing.html)

### enableV2Signing
    
    
    var [enableV2Signing](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApkSigningConfig#enableV2Signing\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Enable signing using APK Signature Scheme v2 (aka v2 signing). If null, a default value is used.

See [Signing Your Applications](http://developer.android.com/tools/publishing/app-signing.html)

### enableV3Signing
    
    
    var [enableV3Signing](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApkSigningConfig#enableV3Signing\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Enable signing using APK Signature Scheme v3 (aka v3 signing). If null, a default value is used.

See [APK Signature Scheme v3](https://source.android.com/security/apksigning/v3)

### enableV4Signing
    
    
    var [enableV4Signing](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApkSigningConfig#enableV4Signing\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

Enable signing using APK Signature Scheme v4 (aka v4 signing). If null, a default value is used.

### isV1SigningEnabled
    
    
    var [isV1SigningEnabled](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApkSigningConfig#isV1SigningEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
This property is deprecated

Whether signing using JAR Signature Scheme (aka v1 signing) is enabled.

See [Signing Your Applications](http://developer.android.com/tools/publishing/app-signing.html)

### isV2SigningEnabled
    
    
    var [isV2SigningEnabled](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/ApkSigningConfig#isV2SigningEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
This property is deprecated

Whether signing using APK Signature Scheme v2 (aka v2 signing) is enabled.

See [Signing Your Applications](http://developer.android.com/tools/publishing/app-signing.html)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
