---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.ASSETS
title: SingleArtifact.ASSETS \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:59:12.877408+00:00
---

# SingleArtifact.ASSETS  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.ASSETS

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# SingleArtifact.ASSETS

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/SingleArtifact.kt+class:com.android.build.api.artifact.SingleArtifact.ASSETS)

Added in 7.3.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    object [SingleArtifact.ASSETS](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.ASSETS) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact), [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Replaceable), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Transformable)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact)  
|  ↳ | [com.android.build.api.artifact.Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Single)  
|  |  ↳ | [com.android.build.api.artifact.SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact)  
|  |  |  ↳ | [com.android.build.api.artifact.SingleArtifact.ASSETS](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.ASSETS)  
  
* * *

Assets that will be packaged in the resulting AAR, APK or Bundle.

When used as an input, the content will be the merged assets. For the APK, the assets will be compressed before packaging.

To add new folders to `[ASSETS](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.ASSETS)`, you must use `[com.android.build.api.variant.Sources.assets](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/variant/Sources#assets\(\))`

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
`[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ArtifactKind)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)>` |  `[kind](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact#kind\(\))`  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
