---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/MultipleArtifact.NATIVE_DEBUG_METADATA
title: MultipleArtifact.NATIVE_DEBUG_METADATA \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:42:10.625998+00:00
---

# MultipleArtifact.NATIVE_DEBUG_METADATA  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/MultipleArtifact.NATIVE_DEBUG_METADATA

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# MultipleArtifact.NATIVE_DEBUG_METADATA

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/MultipleArtifact.kt+class:com.android.build.api.artifact.MultipleArtifact.NATIVE_DEBUG_METADATA)

Added in 8.0.2
    
    
    object [MultipleArtifact.NATIVE_DEBUG_METADATA](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/MultipleArtifact.NATIVE_DEBUG_METADATA) : [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/MultipleArtifact), [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Replaceable), [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Appendable), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Transformable)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact)  
|  ↳ | [com.android.build.api.artifact.Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Multiple)  
|  |  ↳ | [com.android.build.api.artifact.MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/MultipleArtifact)  
|  |  |  ↳ | [com.android.build.api.artifact.MultipleArtifact.NATIVE_DEBUG_METADATA](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/MultipleArtifact.NATIVE_DEBUG_METADATA)  
  
* * *

Directories with native debug metadata

If set, the debug metadata files(with extension .dbg) are combined with extracted debug metadata and packaged together.

## Summary

### Inherited functions  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact) | `open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFileSystemLocationName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact#getFileSystemLocationName\(\))()`  
---|---  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFolderName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact#getFolderName\(\))()`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact#name\(\))()` Provide a unique name for the artifact type.  
  
### Inherited properties  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact) | `[Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category)` |  `[category](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact#category\(\))`  
---|---  
`[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ArtifactKind)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)>` |  `[kind](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact#kind\(\))`  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
