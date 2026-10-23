---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AarMetadata/
title: AarMetadata \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:59:56.927859+00:00
---

# AarMetadata  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AarMetadata/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AarMetadata

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/AarMetadata.kt+class:com.android.build.api.dsl.AarMetadata)

Added in 4.2.0
    
    
    interface [AarMetadata](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AarMetadata)

* * *

DSL object for configuring metadata that is embedded in the AAR.

This metadata is used by consumers of the AAR to control their behavior.

## Summary

### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[minAgpVersion](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AarMetadata#minAgpVersion\(\))` The minimum Android Gradle Plugin version required by any consuming module.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[minCompileSdk](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AarMetadata#minCompileSdk\(\))` The minimum compileSdkVersion required by any consuming module.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[minCompileSdkExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AarMetadata#minCompileSdkExtension\(\))` The minimum compileSdkExtension required by any consuming module.  
  
## Public properties

### minAgpVersion

Added in 7.1.0
    
    
    var [minAgpVersion](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AarMetadata#minAgpVersion\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The minimum Android Gradle Plugin version required by any consuming module.

For example, setting this when the AAR relies on a feature from a new version of AGP will alert consuming projects that they need to update their AGP version to match, rather than getting an ambiguous error from the older version of AGP.

minAgpVersion must be a stable AGP version, and it must be formatted with major, minor, and micro values (for example, "4.0.0").

### minCompileSdk

Added in 4.2.0
    
    
    var [minCompileSdk](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AarMetadata#minCompileSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

The minimum compileSdkVersion required by any consuming module.

For example, setting this when the AAR uses an Android resource from a new version of the Android platform will alert consuming projects that they need to update their compileSdk version to match, rather than getting a 'resource not found' error during resource processing.

### minCompileSdkExtension

Added in 7.4.0
    
    
    var [minCompileSdkExtension](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/AarMetadata#minCompileSdkExtension\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

The minimum compileSdkExtension required by any consuming module.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
