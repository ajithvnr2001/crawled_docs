---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.AAR
title: SingleArtifact.AAR \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:59:06.570799+00:00
---

# SingleArtifact.AAR  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.AAR

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# SingleArtifact.AAR

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/SingleArtifact.kt+class:com.android.build.api.artifact.SingleArtifact.AAR)

Added in 7.0.0
    
    
    object [SingleArtifact.AAR](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.AAR) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Transformable)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact)  
|  ↳ | [com.android.build.api.artifact.Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Single)  
|  |  ↳ | [com.android.build.api.artifact.SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact)  
|  |  |  ↳ | [com.android.build.api.artifact.SingleArtifact.AAR](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.AAR)  
  
* * *

The final AAR file as it would be published.

## Summary

### Inherited functions  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact) | `open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFolderName](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact#getFolderName\(\))()`  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact#name\(\))()` Provide a unique name for the artifact type.  
  
From [com.android.build.api.artifact.SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact) | `open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFileSystemLocationName](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact#getFileSystemLocationName\(\))()`  
---|---  
  
### Inherited properties  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact) | `[Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Category)` |  `[category](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact#category\(\))`  
---|---  
`[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ArtifactKind)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>` |  `[kind](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact#kind\(\))`  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
