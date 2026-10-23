---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AarMetadata/
title: AarMetadata \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:33:46.557622+00:00
---

# AarMetadata  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AarMetadata/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AarMetadata

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/AarMetadata.kt+class:com.android.build.api.variant.AarMetadata)

Added in 7.0.0
    
    
    interface [AarMetadata](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AarMetadata)

* * *

Build-time properties for AAR Metadata inside a `[Component](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component)`

This is accessed via `[GeneratesAar.aarMetadata](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/GeneratesAar#aarMetadata\(\))`

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[minCompileSdk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AarMetadata#minCompileSdk\(kotlin.Function1\))(action: [MinCompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MinCompileSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
  
### Public properties  
  
---  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[minAgpVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AarMetadata#minAgpVersion\(\))` Minimum Android Gradle Plugin version needed to consume this library.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)>` |  `[minCompileSdk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AarMetadata#minCompileSdk\(\))` **This property is deprecated.** Use minCompileSdk() instead.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)>` |  `[minCompileSdkExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AarMetadata#minCompileSdkExtension\(\))` **This property is deprecated.** Use minCompileSdk() instead.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CompileSdkVersion)>` |  `[minCompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AarMetadata#minCompileSdkVersion\(\))` Do not set this property directly.  
  
## Public functions

### minCompileSdk

Added in 9.3.3
    
    
    fun [minCompileSdk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AarMetadata#minCompileSdk\(kotlin.Function1\))(action: [MinCompileSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/MinCompileSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

## Public properties

### minAgpVersion

Added in 7.1.0
    
    
    val [minAgpVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AarMetadata#minAgpVersion\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Minimum Android Gradle Plugin version needed to consume this library. This is the minimum AGP version a module must use in order to import this library.

minAgpVersion must be a stable AGP version, and it must be formatted with major, minor, and micro values (for example, "4.0.0").

### minCompileSdk

Added in 7.0.0

Deprecated in 9.3.3
    
    
    val [minCompileSdk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AarMetadata#minCompileSdk\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)>

**This property is deprecated.**  
Use minCompileSdk() instead. Once minCompileSdk() is set, this property has no effect.

Minimum compileSdkVersion needed to consume this library. This is the minimum sdk version a module must use in order to import this library.

### minCompileSdkExtension

Added in 7.4.0

Deprecated in 9.3.3
    
    
    val [minCompileSdkExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AarMetadata#minCompileSdkExtension\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)>

**This property is deprecated.**  
Use minCompileSdk() instead. Once minCompileSdk() is set, this property has no effect.

Minimum compileSdkExtension needed to consume this library. This is the minimum sdk extension version a module must use in order to import this library.

The default value of `[minCompileSdkExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AarMetadata#minCompileSdkExtension\(\))` is 0 if not set via the DSL.

### minCompileSdkVersion

Added in 9.3.3
    
    
    val [minCompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AarMetadata#minCompileSdkVersion\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[CompileSdkVersion](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/CompileSdkVersion)>

Do not set this property directly. Use `[minCompileSdk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AarMetadata#minCompileSdk\(kotlin.Function1\))` instead.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
