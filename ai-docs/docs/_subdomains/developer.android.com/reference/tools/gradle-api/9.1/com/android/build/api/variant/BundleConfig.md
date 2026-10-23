---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/BundleConfig/
title: BundleConfig \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:08:00.185183+00:00
---

# BundleConfig  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/BundleConfig/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BundleConfig

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/BundleConfig.kt+class:com.android.build.api.variant.BundleConfig)

Added in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [BundleConfig](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/BundleConfig)

* * *

Information related to the actions creating a bundle (.aab) file for the variant.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[addMetadataFile](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/BundleConfig#addMetadataFile\(kotlin.String,org.gradle.api.provider.Provider\))(metadataDirectory: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), file: [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>)` Add a metadata file to the bundle (.aab) file.  
  
### Public properties  
  
---  
`[CodeTransparency](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/CodeTransparency)` |  `[codeTransparency](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/BundleConfig#codeTransparency\(\))` Settings associated with the code transparency feature in bundles.  
  
## Public functions

### addMetadataFile

Added in 7.2.0
    
    
    fun [addMetadataFile](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/BundleConfig#addMetadataFile\(kotlin.String,org.gradle.api.provider.Provider\))(metadataDirectory: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), file: [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Add a metadata file to the bundle (.aab) file. The file will be added under the BUNDLE-METADATA folder.

Parameters  
---  
`metadataDirectory: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the directory below BUNDLE-METADATA where the file should be stored.  
`file: [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>` |  the `[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)` of `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` that can be wired from a `[org.gradle.api.Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` output or an existing file in the project directory.  
  
## Public properties

### codeTransparency

Added in 7.1.0
    
    
    val [codeTransparency](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/BundleConfig#codeTransparency\(\)): [CodeTransparency](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/CodeTransparency)

Settings associated with the code transparency feature in bundles. Initialized from the corresponding DSL elements.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
