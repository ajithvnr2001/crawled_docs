---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/RegisteredArtifactWithQualifiers/
title: RegisteredArtifactWithQualifiers \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:47:22.464044+00:00
---

# RegisteredArtifactWithQualifiers  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/RegisteredArtifactWithQualifiers/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# RegisteredArtifactWithQualifiers

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/RegisteredArtifactWithQualifiers.kt+class:com.android.build.api.artifact.RegisteredArtifactWithQualifiers)

Added in 9.4.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [RegisteredArtifactWithQualifiers](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/RegisteredArtifactWithQualifiers)<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)>

* * *

Encapsulation of a registered `[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)` of `[FileTypeT](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/RegisteredArtifactWithQualifiers)` with qualifiers.

## Summary

### Public properties  
  
---  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<FileTypeT>` |  `[artifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/RegisteredArtifactWithQualifiers#artifact\(\))` Registered artifact's `[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)`.  
`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[qualifiers](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/RegisteredArtifactWithQualifiers#qualifiers\(\))` Qualifiers used when registering the artifact possibly in a different order.  
  
## Public properties

### artifact

Added in 9.4.1
    
    
    val [artifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/RegisteredArtifactWithQualifiers#artifact\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<FileTypeT>

Registered artifact's `[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)`.

### qualifiers

Added in 9.4.1
    
    
    val [qualifiers](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/RegisteredArtifactWithQualifiers#qualifiers\(\)): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Qualifiers used when registering the artifact possibly in a different order.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
