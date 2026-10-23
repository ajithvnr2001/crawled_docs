---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources/
title: Sources \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:38:03.067513+00:00
---

# Sources  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Sources

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/Sources.kt+class:com.android.build.api.variant.Sources)

Added in 7.2.0
    
    
    interface [Sources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources)

Known direct subclasses 

[LibrarySources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/LibrarySources)

`[LibrarySources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/LibrarySources)` |   
---|---  
  
* * *

Provides access to all source directories for a `[Variant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Variant)`.

## Summary

### Public functions  
  
---  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)` |  `[getByName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#getByName\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Access (and potentially creates) a new `[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)` for a custom source type that can be referenced by its `[name](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#getByName\(kotlin.String\))`.  
  
### Public properties  
  
---  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)?` |  `[aidl](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#aidl\(\))` Access to the aidl sources folders if `[com.android.build.api.dsl.BuildFeatures.aidl](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BuildFeatures#aidl\(\))` is true otherwise null  
`[SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Layered)?` |  `[assets](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#assets\(\))` Access to the Android assets sources folders.  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)?` |  `[baselineProfiles](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#baselineProfiles\(\))` Access to the Baseline profiles source folders.  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)?` |  `[java](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#java\(\))` Access to the Java source folders.  
`[SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Layered)?` |  `[jniLibs](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#jniLibs\(\))` Access to the JNI libraries folders  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)?` |  `[keepRules](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#keepRules\(\))` KeepRules files for R8 configuration  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)?` |  `[kotlin](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#kotlin\(\))` Access to the Kotlin source folders.  
`[ManifestFiles](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ManifestFiles)` |  `[manifests](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#manifests\(\))` Access to all android manifest files.  
`[SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Layered)?` |  `[mlModels](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#mlModels\(\))` Access to the machine learning models folders if `[com.android.build.api.dsl.ApplicationBuildFeatures.mlModelBinding](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApplicationBuildFeatures#mlModelBinding\(\))` is true otherwise null  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)?` |  `[renderscript](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#renderscript\(\))` Access to the renderscript sources folders if `[com.android.build.api.dsl.BuildFeatures.renderScript](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BuildFeatures#renderScript\(\))` is true otherwise null.  
`[SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Layered)?` |  `[res](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#res\(\))` Access to the Android resources sources folders if the component supports android resources or if `[com.android.build.api.dsl.LibraryBuildFeatures.androidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryBuildFeatures#androidResources\(\))` is true for library variants, otherwise null.  
`[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)?` |  `[resources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#resources\(\))` Access to the Java-style resources sources folders.  
`[SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Layered)?` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#shaders\(\))` Access to the shaders sources folders if `[com.android.build.api.dsl.BuildFeatures.shaders](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BuildFeatures#shaders\(\))` is true otherwise null  
  
## Public functions

### getByName

Added in 7.2.0
    
    
    fun [getByName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#getByName\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)

Access (and potentially creates) a new `[SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)` for a custom source type that can be referenced by its `[name](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#getByName\(kotlin.String\))`.

The first caller will create the new instance, other callers with the same `[name](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#getByName\(kotlin.String\))` will get the same instance returned. Any callers can obtain the final list of the folders registered under this custom source type by calling `[SourceDirectories.Flat.all](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat#all\(\))`.

These sources directories are attached to the variant and will be visible to Android Studio.

## Public properties

### aidl

Added in 7.3.0
    
    
    val [aidl](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#aidl\(\)): [SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)?

Access to the aidl sources folders if `[com.android.build.api.dsl.BuildFeatures.aidl](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BuildFeatures#aidl\(\))` is true otherwise null

### assets

Added in 7.3.0
    
    
    val [assets](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#assets\(\)): [SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Layered)?

Access to the Android assets sources folders.

### baselineProfiles

Added in 8.0.2
    
    
    val [baselineProfiles](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#baselineProfiles\(\)): [SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)?

Access to the Baseline profiles source folders.

### java

Added in 7.2.0
    
    
    val [java](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#java\(\)): [SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)?

Access to the Java source folders.

### jniLibs

Added in 7.3.0
    
    
    val [jniLibs](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#jniLibs\(\)): [SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Layered)?

Access to the JNI libraries folders

### keepRules

Added in 9.3.3
    
    
    val [keepRules](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#keepRules\(\)): [SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)?

KeepRules files for R8 configuration

### kotlin

Added in 7.3.0
    
    
    val [kotlin](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#kotlin\(\)): [SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)?

Access to the Kotlin source folders.

### manifests

Added in 8.3.1
    
    
    val [manifests](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#manifests\(\)): [ManifestFiles](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ManifestFiles)

Access to all android manifest files. Main manifest file is always the first one.

### mlModels

Added in 7.3.0
    
    
    val [mlModels](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#mlModels\(\)): [SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Layered)?

Access to the machine learning models folders if `[com.android.build.api.dsl.ApplicationBuildFeatures.mlModelBinding](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/ApplicationBuildFeatures#mlModelBinding\(\))` is true otherwise null

### renderscript

Added in 7.3.0
    
    
    val [renderscript](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#renderscript\(\)): [SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)?

Access to the renderscript sources folders if `[com.android.build.api.dsl.BuildFeatures.renderScript](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BuildFeatures#renderScript\(\))` is true otherwise null. RenderScript APIs are deprecated starting in Android 12 [See more](https://developer.android.com/guide/topics/renderscript/migrate).

### res

Added in 7.3.0
    
    
    val [res](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#res\(\)): [SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Layered)?

Access to the Android resources sources folders if the component supports android resources or if `[com.android.build.api.dsl.LibraryBuildFeatures.androidResources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/LibraryBuildFeatures#androidResources\(\))` is true for library variants, otherwise null.

### resources

Added in 7.4.0
    
    
    val [resources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#resources\(\)): [SourceDirectories.Flat](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Flat)?

Access to the Java-style resources sources folders.

### shaders

Added in 7.3.0
    
    
    val [shaders](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Sources#shaders\(\)): [SourceDirectories.Layered](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/SourceDirectories.Layered)?

Access to the shaders sources folders if `[com.android.build.api.dsl.BuildFeatures.shaders](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/BuildFeatures#shaders\(\))` is true otherwise null

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
