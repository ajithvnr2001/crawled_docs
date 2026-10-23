---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/package-summary/
title: com.android.build.api.artifact \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:13:11.497553+00:00
---

# com.android.build.api.artifact  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/package-summary/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# com.android.build.api.artifact

## Interfaces

`[Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact.Appendable)` |  Denotes an artifact type that can be appended to.  
---|---  
`[Artifact.ContainsMany](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact.ContainsMany)` |  Denotes a single `[DIRECTORY](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact#DIRECTORY\(\))` that may contain zero to many `[com.android.build.api.variant.BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/BuiltArtifact)`.  
`[Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact.Replaceable)` |  Denotes an artifact type that can be replaced.  
`[Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact.Transformable)` |  Denotes an artifact type that can transformed.  
`[ArtifactTransformationRequest](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ArtifactTransformationRequest)` |  When a `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` contains more than one artifact (for example, consider `[SingleArtifact.APK](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/SingleArtifact.APK)` with multiple APKs for different screen densities), this object will abstract away having to deal with `[BuiltArtifacts](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/BuiltArtifacts)` and manually load and write the metadata files.  
`[Artifacts](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifacts)` |  Access to the artifacts on a Variant object.  
`[CombiningOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/CombiningOperationRequest)` |  Operations performed by a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` with a single `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` or `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` output.  
`[InAndOutDirectoryOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/InAndOutDirectoryOperationRequest)` |  Operations performed by a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` with a single `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` output.  
`[InAndOutFileOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/InAndOutFileOperationRequest)` |  Operations performed by a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` with a single `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` output.  
`[MultipleArtifactTypeOutOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/MultipleArtifactTypeOutOperationRequest)` |  Read-only Operations performed by a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` with a multiple `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` or `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` output.  
`[OutOperationRequest](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/OutOperationRequest)` |  Operations performed by a `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` with a single `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)` or `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)` output.  
`[TaskBasedOperation](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/TaskBasedOperation)` |  Interface with methods to wire input and output method references to `[Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)`-based operations.  
  
## Classes

`[Artifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact)` |  Defines a type of artifact handled by the Android Gradle Plugin.  
---|---  
`[Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact.Multiple)` |  Denotes possible multiple `[FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)` instances for this artifact type.  
`[Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact.Single)` |  Denotes a single `[FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)` instance of this artifact type at a given time.  
`[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ArtifactKind)` |  Exhaustive list of artifact file representations supported by the Android Gradle plugin.  
`[MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/MultipleArtifact)` |  Public `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact)` for Android Gradle plugin.  
`[ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact)` |  List of ScopedArtifacts.Scope artifacts.  
`[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/SingleArtifact)` |  Public `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact)` for Android Gradle plugin.  
  
## Objects

`[ArtifactKind.DIRECTORY](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ArtifactKind.DIRECTORY)` |  A type of artifact file that is a `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)`  
---|---  
`[ArtifactKind.FILE](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ArtifactKind.FILE)` |  A Type of artifact that is a `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)`  
`[MultipleArtifact.MULTIDEX_KEEP_PROGUARD](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/MultipleArtifact.MULTIDEX_KEEP_PROGUARD)` |  Text files with additional ProGuard rules to be used to determine which classes are compiled into the main dex file.  
`[MultipleArtifact.NATIVE_DEBUG_METADATA](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/MultipleArtifact.NATIVE_DEBUG_METADATA)` |  Directories with native debug metadata  
`[MultipleArtifact.NATIVE_SYMBOL_TABLES](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/MultipleArtifact.NATIVE_SYMBOL_TABLES)` |  Directories with debug symbol table  
`[MultipleArtifact.PRE_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/MultipleArtifact.PRE_COMPILATION_CLASSES)` |  Directories containing generated code that will be added to compile classpath for the module.  
`[ScopedArtifact.CLASSES](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact.CLASSES)` |  .class files, result of sources compilation and/or external dependencies depending on the scope; includes users' transformation, but does not include Jacoco instrumentation  
`[ScopedArtifact.JAVA_RES](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact.JAVA_RES)` |   
`[ScopedArtifact.POST_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact.POST_COMPILATION_CLASSES)` |  .class files, result of sources compilation and/or external dependencies depending on the scope  
`[SingleArtifact.AAR](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/SingleArtifact.AAR)` |  The final AAR file as it would be published.  
`[SingleArtifact.APK](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/SingleArtifact.APK)` |  Directory where APK files will be located.  
`[SingleArtifact.APK_FROM_BUNDLE](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/SingleArtifact.APK_FROM_BUNDLE)` |  Universal APK that contains assets for all screen densities.  
`[SingleArtifact.ASSETS](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/SingleArtifact.ASSETS)` |  Assets that will be packaged in the resulting AAR, APK or Bundle.  
`[SingleArtifact.BUNDLE](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/SingleArtifact.BUNDLE)` |  The final Bundle ready for consumption at Play Store.  
`[SingleArtifact.MERGED_MANIFEST](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/SingleArtifact.MERGED_MANIFEST)` |  Merged manifest file that will be used in the APK, Bundle and InstantApp packages.  
`[SingleArtifact.MERGED_NATIVE_LIBS](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/SingleArtifact.MERGED_NATIVE_LIBS)` |  The directory containing all the native library (.so) files that will be packaged in the APK, AAR, or Bundle.  
`[SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT)` |  The metadata for the library dependencies.  
`[SingleArtifact.OBFUSCATION_MAPPING_FILE](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/SingleArtifact.OBFUSCATION_MAPPING_FILE)` |   
`[SingleArtifact.OBFUSCATION_MAPPING_PARTITION_FILE](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/SingleArtifact.OBFUSCATION_MAPPING_PARTITION_FILE)` |   
`[SingleArtifact.PUBLIC_ANDROID_RESOURCES_LIST](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/SingleArtifact.PUBLIC_ANDROID_RESOURCES_LIST)` |  A file containing the list of public resources exported by a library project.  
`[SingleArtifact.RUNTIME_SYMBOL_LIST](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/SingleArtifact.RUNTIME_SYMBOL_LIST)` |  The text symbol output file (R.txt) containing a list of resources and their ids (including of transitive dependencies).  
`[SingleArtifact.VERSION_CONTROL_INFO_FILE](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/SingleArtifact.VERSION_CONTROL_INFO_FILE)` |  Points to the Version control information when VCS tagging is enabled (which is by default in release builds)  
  
## Enums

`[Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact.Category)` |  Defines the kind of artifact type. this will be used to determine the output file location for instance.  
---|---  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-11-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-21 UTC."],[],[]] 
