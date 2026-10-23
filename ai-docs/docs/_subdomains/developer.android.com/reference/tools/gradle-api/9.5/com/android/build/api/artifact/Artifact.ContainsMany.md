---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.ContainsMany
title: Artifact.ContainsMany \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:05:09.958261+00:00
---

# Artifact.ContainsMany  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.ContainsMany

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Artifact.ContainsMany

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/Artifact.kt+class:com.android.build.api.artifact.Artifact.ContainsMany)

Added in 4.2.0
    
    
    interface [Artifact.ContainsMany](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.ContainsMany)

Known direct subclasses 

[SingleArtifact.APK](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.APK)

`[SingleArtifact.APK](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.APK)` |  Directory where APK files will be located.  
---|---  
  
* * *

Denotes a `[DIRECTORY](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact#DIRECTORY\(\))` that may contain zero to many `[com.android.build.api.variant.BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)`.

Artifact types annotated with this marker interface are backed up by a `[DIRECTORY](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact#DIRECTORY\(\))` whose content should be read using the `[com.android.build.api.variant.BuiltArtifactsLoader](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifactsLoader)`.

If producing an artifact type annotated with this marker interface, content should be written using the `[com.android.build.api.variant.BuiltArtifacts.save](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifacts#save\(org.gradle.api.file.Directory\))` methods.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
