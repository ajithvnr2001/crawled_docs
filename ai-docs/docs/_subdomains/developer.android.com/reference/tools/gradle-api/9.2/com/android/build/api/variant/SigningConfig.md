---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/SigningConfig/
title: SigningConfig \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:55:12.773622+00:00
---

# SigningConfig  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/SigningConfig/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# SigningConfig

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/SigningConfig.kt+class:com.android.build.api.variant.SigningConfig)

Added in 4.2.0
    
    
    interface [SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/SigningConfig)

* * *

Defines a variant's signing config.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[setConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/SigningConfig#setConfig\(com.android.build.api.dsl.SigningConfig\))(signingConfig: [SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/SigningConfig))` Sets the `[com.android.build.api.dsl.SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/SigningConfig)` with information on how to retrieve the signing configuration.  
  
### Public properties  
  
---  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[enableV1Signing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/SigningConfig#enableV1Signing\(\))` Enable signing using JAR Signature Scheme (aka v1 signing).  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[enableV2Signing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/SigningConfig#enableV2Signing\(\))` Enable signing using APK Signature Scheme v2 (aka v2 signing).  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[enableV3Signing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/SigningConfig#enableV3Signing\(\))` Enable signing using APK Signature Scheme v3 (aka v3 signing).  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[enableV4Signing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/SigningConfig#enableV4Signing\(\))` Enable signing using APK Signature Scheme v4 (aka v4 signing).  
  
## Public functions

### setConfig

Added in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [setConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/SigningConfig#setConfig\(com.android.build.api.dsl.SigningConfig\))(signingConfig: [SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/SigningConfig)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Sets the `[com.android.build.api.dsl.SigningConfig](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/dsl/SigningConfig)` with information on how to retrieve the signing configuration.

## Public properties

### enableV1Signing

Added in 4.2.0
    
    
    val [enableV1Signing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/SigningConfig#enableV1Signing\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>

Enable signing using JAR Signature Scheme (aka v1 signing).

See [Signing Your Applications](http://developer.android.com/tools/publishing/app-signing.html)

This property will override any value set using the corresponding DSL.

### enableV2Signing

Added in 4.2.0
    
    
    val [enableV2Signing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/SigningConfig#enableV2Signing\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>

Enable signing using APK Signature Scheme v2 (aka v2 signing).

See [Signing Your Applications](http://developer.android.com/tools/publishing/app-signing.html)

This property will override any value set using the corresponding DSL.

### enableV3Signing

Added in 4.2.0
    
    
    val [enableV3Signing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/SigningConfig#enableV3Signing\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>

Enable signing using APK Signature Scheme v3 (aka v3 signing).

See [APK Signature Scheme v3](https://source.android.com/security/apksigning/v3)

This property will override any value set using the corresponding DSL.

### enableV4Signing

Added in 4.2.0
    
    
    val [enableV4Signing](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/SigningConfig#enableV4Signing\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>

Enable signing using APK Signature Scheme v4 (aka v4 signing).

This property will override any value set using the corresponding DSL.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
