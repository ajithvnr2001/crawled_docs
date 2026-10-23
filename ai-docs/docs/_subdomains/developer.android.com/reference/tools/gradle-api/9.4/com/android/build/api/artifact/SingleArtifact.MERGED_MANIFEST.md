---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/SingleArtifact.MERGED_MANIFEST
title: SingleArtifact.MERGED_MANIFEST \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:48:43.662566+00:00
---

# SingleArtifact.MERGED_MANIFEST  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/SingleArtifact.MERGED_MANIFEST

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# SingleArtifact.MERGED_MANIFEST

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/SingleArtifact.kt+class:com.android.build.api.artifact.SingleArtifact.MERGED_MANIFEST)

Added in 7.0.0
    
    
    object [SingleArtifact.MERGED_MANIFEST](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/SingleArtifact.MERGED_MANIFEST) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/SingleArtifact), [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Replaceable), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Transformable)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact)  
|  ↳ | [com.android.build.api.artifact.Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Single)  
|  |  ↳ | [com.android.build.api.artifact.SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/SingleArtifact)  
|  |  |  ↳ | [com.android.build.api.artifact.SingleArtifact.MERGED_MANIFEST](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/SingleArtifact.MERGED_MANIFEST)  
  
* * *

Merged manifest file that will be used in the APK, Bundle and InstantApp packages. This will only be available on modules applying one of the following plugins : com.android.application com.android.dynamic-feature com.android.library com.android.test

## Summary

### Inherited functions  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact) | `open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFolderName](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact#getFolderName\(\))()`  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact#name\(\))()` Provide a unique name for the artifact type.  
  
From [com.android.build.api.artifact.SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/SingleArtifact) | `open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFileSystemLocationName](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/SingleArtifact#getFileSystemLocationName\(\))()`  
---|---  
  
### Inherited properties  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact) | `[Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact.Category)` |  `[category](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact#category\(\))`  
---|---  
`[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/ArtifactKind)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>` |  `[kind](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/artifact/Artifact#kind\(\))`  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
