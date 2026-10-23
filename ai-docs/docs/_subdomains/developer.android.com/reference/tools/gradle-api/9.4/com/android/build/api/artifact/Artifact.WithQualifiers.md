---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.WithQualifiers
title: Artifact.WithQualifiers \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:47:01.416817+00:00
---

# Artifact.WithQualifiers  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.WithQualifiers

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Artifact.WithQualifiers

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/Artifact.kt+class:com.android.build.api.artifact.Artifact.WithQualifiers)

Added in 9.4.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [Artifact.WithQualifiers](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.WithQualifiers)

* * *

Denotes a `[Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)` artifact that can have qualifiers attached to each of its `[FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)` instances.

While `[Multiple](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Multiple)` artifacts are stored in a flat namespace, it can be beneficial to attach metadata to each artifact. This allows consumers to filter artifacts of interest and only resolve those particular `[org.gradle.api.provider.Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)` instances, rather than resolving all of them.

## Summary

### Public properties  
  
---  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>?` |  `[qualifierKeys](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.WithQualifiers#qualifierKeys\(\))` The list of attribute keys that can be used to query for specific artifacts.  
  
## Public properties

### qualifierKeys

Added in 9.4.1
    
    
    val [qualifierKeys](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.WithQualifiers#qualifierKeys\(\)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>?

The list of attribute keys that can be used to query for specific artifacts.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
