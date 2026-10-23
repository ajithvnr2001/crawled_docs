---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.RUNTIME_SYMBOL_LIST
title: SingleArtifact.RUNTIME_SYMBOL_LIST \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:29:49.731398+00:00
---

# SingleArtifact.RUNTIME_SYMBOL_LIST  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.RUNTIME_SYMBOL_LIST

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# SingleArtifact.RUNTIME_SYMBOL_LIST

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/SingleArtifact.kt+class:com.android.build.api.artifact.SingleArtifact.RUNTIME_SYMBOL_LIST)

Added in 8.3.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    object [SingleArtifact.RUNTIME_SYMBOL_LIST](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.RUNTIME_SYMBOL_LIST) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact)  
|  ↳ | [com.android.build.api.artifact.Artifact.Single](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Single)  
|  |  ↳ | [com.android.build.api.artifact.SingleArtifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact)  
|  |  |  ↳ | [com.android.build.api.artifact.SingleArtifact.RUNTIME_SYMBOL_LIST](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.RUNTIME_SYMBOL_LIST)  
  
* * *

The text symbol output file (R.txt) containing a list of resources and their ids (including of transitive dependencies).

## Summary

### Inherited functions  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact) | `open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFolderName](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact#getFolderName\(\))()`  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact#name\(\))()` Provide a unique name for the artifact type.  
  
From [com.android.build.api.artifact.SingleArtifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact) | `open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFileSystemLocationName](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact#getFileSystemLocationName\(\))()`  
---|---  
  
### Inherited properties  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact) | `[Artifact.Category](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Category)` |  `[category](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact#category\(\))`  
---|---  
`[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/ArtifactKind)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>` |  `[kind](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact#kind\(\))`  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
