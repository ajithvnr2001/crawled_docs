---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LibrarySources/
title: LibrarySources \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:01:26.558729+00:00
---

# LibrarySources  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LibrarySources/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# LibrarySources

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/LibrarySources.kt+class:com.android.build.api.variant.LibrarySources)

Added in 9.4.1
    
    
    interface [LibrarySources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LibrarySources) : [Sources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources)

* * *

## Summary

### Public properties  
  
---  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)?` |  `[aarKeepRules](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LibrarySources#aarKeepRules\(\))` KeepRules files for R8 optimization when publishing AAR library.  
  
### Inherited functions  
  
---  
From [com.android.build.api.variant.Sources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources) | `[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)` |  `[getByName](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources#getByName\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Access (and potentially creates) a new `[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)` for a custom source type that can be referenced by its `[name](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources#getByName\(kotlin.String\))`.  
---|---  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.Sources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources) | `[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)?` |  `[aidl](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources#aidl\(\))` Access to the aidl sources folders if `[com.android.build.api.dsl.BuildFeatures.aidl](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/BuildFeatures#aidl\(\))` is true otherwise null  
---|---  
`[SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Layered)?` |  `[assets](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources#assets\(\))` Access to the Android assets sources folders.  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)?` |  `[baselineProfiles](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources#baselineProfiles\(\))` Access to the Baseline profiles source folders.  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)?` |  `[java](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources#java\(\))` Access to the Java source folders.  
`[SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Layered)?` |  `[jniLibs](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources#jniLibs\(\))` Access to the JNI libraries folders  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)?` |  `[keepRules](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources#keepRules\(\))` KeepRules files for R8 configuration  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)?` |  `[kotlin](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources#kotlin\(\))` Access to the Kotlin source folders.  
`[ManifestFiles](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/ManifestFiles)` |  `[manifests](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources#manifests\(\))` Access to all android manifest files.  
`[SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Layered)?` |  `[mlModels](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources#mlModels\(\))` Access to the machine learning models folders if `[com.android.build.api.dsl.ApplicationBuildFeatures.mlModelBinding](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ApplicationBuildFeatures#mlModelBinding\(\))` is true otherwise null  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)?` |  `[renderscript](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources#renderscript\(\))` Access to the renderscript sources folders if `[com.android.build.api.dsl.BuildFeatures.renderScript](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/BuildFeatures#renderScript\(\))` is true otherwise null.  
`[SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Layered)?` |  `[res](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources#res\(\))` Access to the Android resources sources folders if the component supports android resources or if `[com.android.build.api.dsl.LibraryBuildFeatures.androidResources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/LibraryBuildFeatures#androidResources\(\))` is true for library variants, otherwise null.  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)?` |  `[resources](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources#resources\(\))` Access to the Java-style resources sources folders.  
`[SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Layered)?` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/Sources#shaders\(\))` Access to the shaders sources folders if `[com.android.build.api.dsl.BuildFeatures.shaders](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/BuildFeatures#shaders\(\))` is true otherwise null  
  
## Public properties

### aarKeepRules

Added in 9.4.1
    
    
    val [aarKeepRules](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/LibrarySources#aarKeepRules\(\)): [SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SourceDirectories.Flat)?

KeepRules files for R8 optimization when publishing AAR library. These optimization files are used for library own minification process when publishing AAR.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
