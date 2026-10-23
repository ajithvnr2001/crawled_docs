---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Replaceable
title: Artifact.Replaceable \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:57:58.497255+00:00
---

# Artifact.Replaceable  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Replaceable

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Artifact.Replaceable

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/Artifact.kt+class:com.android.build.api.artifact.Artifact.Replaceable)

Added in 4.2.0
    
    
    interface [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Replaceable)

Known direct subclasses 

[MultipleArtifact.MULTIDEX_KEEP_PROGUARD](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifact.MULTIDEX_KEEP_PROGUARD), [MultipleArtifact.NATIVE_DEBUG_METADATA](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifact.NATIVE_DEBUG_METADATA), [MultipleArtifact.NATIVE_SYMBOL_TABLES](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifact.NATIVE_SYMBOL_TABLES), [MultipleArtifact.PRE_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifact.PRE_COMPILATION_CLASSES), [ScopedArtifact.CLASSES](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ScopedArtifact.CLASSES), [ScopedArtifact.JAVA_RES](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ScopedArtifact.JAVA_RES), [SingleArtifact.APK](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.APK), [SingleArtifact.ASSETS](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.ASSETS), [SingleArtifact.MERGED_MANIFEST](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.MERGED_MANIFEST), [SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT), [SingleArtifact.OBFUSCATION_MAPPING_FILE](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.OBFUSCATION_MAPPING_FILE)

`[MultipleArtifact.MULTIDEX_KEEP_PROGUARD](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifact.MULTIDEX_KEEP_PROGUARD)` |  Text files with additional ProGuard rules to be used to determine which classes are compiled into the main dex file.  
---|---  
`[MultipleArtifact.NATIVE_DEBUG_METADATA](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifact.NATIVE_DEBUG_METADATA)` |  Directories with native debug metadata  
`[MultipleArtifact.NATIVE_SYMBOL_TABLES](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifact.NATIVE_SYMBOL_TABLES)` |  Directories with debug symbol table  
`[MultipleArtifact.PRE_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/MultipleArtifact.PRE_COMPILATION_CLASSES)` |  Directories containing generated code that will be added to compile classpath for the module.  
`[ScopedArtifact.CLASSES](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ScopedArtifact.CLASSES)` |  .class files, result of sources compilation and/or external dependencies depending on the scope; includes users' transformation, but does not include Jacoco instrumentation  
`[ScopedArtifact.JAVA_RES](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ScopedArtifact.JAVA_RES)` |   
`[SingleArtifact.APK](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.APK)` |  Directory where APK files will be located.  
`[SingleArtifact.ASSETS](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.ASSETS)` |  Assets that will be packaged in the resulting AAR, APK or Bundle.  
`[SingleArtifact.MERGED_MANIFEST](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.MERGED_MANIFEST)` |  Merged manifest file that will be used in the APK, Bundle and InstantApp packages.  
`[SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT)` |  The metadata for the library dependencies.  
`[SingleArtifact.OBFUSCATION_MAPPING_FILE](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/SingleArtifact.OBFUSCATION_MAPPING_FILE)` |   
  
* * *

Denotes an artifact type that can be replaced. Only `[Single](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Single)` artifacts can be replaced, if you want to replace a `[Multiple](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Multiple)` artifact type, you will need to transform it by combining all the inputs into a single output instance.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
