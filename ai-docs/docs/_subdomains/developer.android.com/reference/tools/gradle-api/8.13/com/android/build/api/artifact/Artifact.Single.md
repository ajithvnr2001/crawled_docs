---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Single
title: Artifact.Single \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:29:01.248044+00:00
---

# Artifact.Single  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Single

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Artifact.Single

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/Artifact.kt+class:com.android.build.api.artifact.Artifact.Single)

Added in 7.0.0
    
    
    abstract class [Artifact.Single](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Single)<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> : [Artifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact)  
|  ↳ | [com.android.build.api.artifact.Artifact.Single](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Single)  
  
Known direct subclasses 

[ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/ScopedArtifact), [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact)

`[ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/ScopedArtifact)` |  List of ScopedArtifacts.Scope artifacts.  
---|---  
`[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact)` |  Public `[Artifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact)` for Android Gradle plugin.  
  
Known indirect subclasses 

[ScopedArtifact.CLASSES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/ScopedArtifact.CLASSES), [ScopedArtifact.JAVA_RES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/ScopedArtifact.JAVA_RES), [SingleArtifact.AAR](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.AAR), [SingleArtifact.APK_FROM_BUNDLE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.APK_FROM_BUNDLE), [SingleArtifact.APK](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.APK), [SingleArtifact.ASSETS](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.ASSETS), [SingleArtifact.BUNDLE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.BUNDLE), [SingleArtifact.MERGED_MANIFEST](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.MERGED_MANIFEST), [SingleArtifact.MERGED_NATIVE_LIBS](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.MERGED_NATIVE_LIBS), [SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT), [SingleArtifact.OBFUSCATION_MAPPING_FILE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.OBFUSCATION_MAPPING_FILE), [SingleArtifact.PUBLIC_ANDROID_RESOURCES_LIST](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.PUBLIC_ANDROID_RESOURCES_LIST), [SingleArtifact.RUNTIME_SYMBOL_LIST](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.RUNTIME_SYMBOL_LIST)

`[ScopedArtifact.CLASSES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/ScopedArtifact.CLASSES)` |  .class files, result of sources compilation and/or external dependencies depending on the scope; includes users' transformation, but does not include Jacoco instrumentation  
---|---  
`[ScopedArtifact.JAVA_RES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/ScopedArtifact.JAVA_RES)` |   
`[SingleArtifact.AAR](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.AAR)` |  The final AAR file as it would be published.  
`[SingleArtifact.APK_FROM_BUNDLE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.APK_FROM_BUNDLE)` |  Universal APK that contains assets for all screen densities.  
`[SingleArtifact.APK](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.APK)` |  Directory where APK files will be located.  
`[SingleArtifact.ASSETS](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.ASSETS)` |  Assets that will be packaged in the resulting AAR, APK or Bundle.  
`[SingleArtifact.BUNDLE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.BUNDLE)` |  The final Bundle ready for consumption at Play Store.  
`[SingleArtifact.MERGED_MANIFEST](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.MERGED_MANIFEST)` |  Merged manifest file that will be used in the APK, Bundle and InstantApp packages.  
`[SingleArtifact.MERGED_NATIVE_LIBS](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.MERGED_NATIVE_LIBS)` |  The directory containing all the native library (.so) files that will be packaged in the APK, AAR, or Bundle.  
`[SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT)` |  The metadata for the library dependencies.  
`[SingleArtifact.OBFUSCATION_MAPPING_FILE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.OBFUSCATION_MAPPING_FILE)` |   
`[SingleArtifact.PUBLIC_ANDROID_RESOURCES_LIST](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.PUBLIC_ANDROID_RESOURCES_LIST)` |  A file containing the list of public resources exported by a library project.  
`[SingleArtifact.RUNTIME_SYMBOL_LIST](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/SingleArtifact.RUNTIME_SYMBOL_LIST)` |  The text symbol output file (R.txt) containing a list of resources and their ids (including of transitive dependencies).  
  
* * *

Denotes a single `[FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)` instance of this artifact type at a given time. Single artifact types can be transformed or replaced but never appended.

## Summary

### Public constructors  
  
---  
`<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [Single](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Single#Single\(com.android.build.api.artifact.ArtifactKind,com.android.build.api.artifact.Artifact.Category\))(  
kind: [ArtifactKind](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/ArtifactKind)<FileTypeT>,  
category: [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Category)  
)`  
  
### Inherited functions  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact) | `open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFileSystemLocationName](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact#getFileSystemLocationName\(\))()`  
---|---  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFolderName](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact#getFolderName\(\))()`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact#name\(\))()` Provide a unique name for the artifact type.  
  
### Inherited properties  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact) | `[Artifact.Category](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Category)` |  `[category](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact#category\(\))`  
---|---  
`[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/ArtifactKind)<FileTypeT>` |  `[kind](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact#kind\(\))`  
  
## Public constructors

### Single
    
    
    <FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [Single](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Single#Single\(com.android.build.api.artifact.ArtifactKind,com.android.build.api.artifact.Artifact.Category\))(  
        kind: [ArtifactKind](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/ArtifactKind)<FileTypeT>,  
        category: [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/artifact/Artifact.Category)  
    )

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
