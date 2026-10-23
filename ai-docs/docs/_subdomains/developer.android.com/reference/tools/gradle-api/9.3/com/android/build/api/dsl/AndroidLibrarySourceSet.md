---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidLibrarySourceSet/
title: AndroidLibrarySourceSet \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:26:09.870599+00:00
---

# AndroidLibrarySourceSet  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidLibrarySourceSet/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AndroidLibrarySourceSet

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/AndroidLibrarySourceSet.kt+class:com.android.build.api.dsl.AndroidLibrarySourceSet)

Added in 9.3.3
    
    
    interface [AndroidLibrarySourceSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidLibrarySourceSet) : [AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet)

* * *

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[aarKeepRules](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidLibrarySourceSet#aarKeepRules\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The AarKeepRules R8 source directory for this source set.  
  
### Public properties  
  
---  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[aarKeepRules](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidLibrarySourceSet#aarKeepRules\(\))` The AarKeepRules R8 source directory for this source set.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[aidl](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#aidl\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Android AIDL source directory for this source set.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[assets](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#assets\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Android Assets directory for this source set.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[baselineProfiles](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#baselineProfiles\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Android Baseline Profiles source directory for this source set.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#getName\(\))()` Returns the name of this source set.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[java](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#java\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Java source for this source-set  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[jniLibs](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#jniLibs\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Android JNI libs directory for this source-set  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[keepRules](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#keepRules\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The KeepRules R8 source directory for this source set.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[kotlin](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#kotlin\(org.gradle.api.Action\))(action: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet)>)` The Kotlin source for this source-set  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[manifest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#manifest\(kotlin.Function1\))(action: [AndroidSourceFile](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceFile).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Android Manifest file for this source-set.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[mlModels](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#mlModels\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The machine learning models directory for this source set.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[renderscript](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#renderscript\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Android RenderScript source directory for this source set.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[res](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#res\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Android Resources directory for this source-set.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[resources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#resources\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Java-style resources for this source-set  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[setRoot](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#setRoot\(kotlin.String\))(path: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Sets the root of the source sets to a given path.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#shaders\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Android shaders directory for this source set.  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet) | `[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[aidl](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#aidl\(\))` The Android AIDL source directory for this source set.  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[annotationProcessorConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#annotationProcessorConfigurationName\(\))` Returns the name of the annotation processing tool classpath for this source set.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[apiConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#apiConfigurationName\(\))` Returns the name of the api configuration for this source set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[assets](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#assets\(\))` The Android Assets directory for this source set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[baselineProfiles](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#baselineProfiles\(\))` The Android Baseline Profiles source directory for this source set.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[compileOnlyApiConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#compileOnlyApiConfigurationName\(\))` Returns the name of the compileOnlyApi configuration for this source set.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[compileOnlyConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#compileOnlyConfigurationName\(\))` Returns the name of the compileOnly configuration for this source set.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[implementationConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#implementationConfigurationName\(\))` Returns the name of the implementation configuration for this source set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[java](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#java\(\))` The Java source for this source-set  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[jniLibs](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#jniLibs\(\))` The Android JNI libs directory for this source-set  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[kaptConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#kaptConfigurationName\(\))` Returns the name of the kapt annotation processing tool classpath for this source set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[keepRules](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#keepRules\(\))` The KeepRules R8 source directory for this source set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[kotlin](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#kotlin\(\))` The Kotlin source for this source-set  
`[AndroidSourceFile](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceFile)` |  `[manifest](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#manifest\(\))` The Android Manifest file for this source-set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[mlModels](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#mlModels\(\))` The machine learning models directory for this source set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[renderscript](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#renderscript\(\))` The Android RenderScript source directory for this source set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[res](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#res\(\))` The Android Resources directory for this source-set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[resources](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#resources\(\))` The Java-style resources for this source-set  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[runtimeOnlyConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#runtimeOnlyConfigurationName\(\))` Returns the name of the implementation configuration for this source set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceSet#shaders\(\))` The Android shaders directory for this source set.  
  
## Public functions

### aarKeepRules

Added in 9.3.3
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [aarKeepRules](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidLibrarySourceSet#aarKeepRules\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

The AarKeepRules R8 source directory for this source set.

## Public properties

### aarKeepRules

Added in 9.3.3
    
    
    val [aarKeepRules](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidLibrarySourceSet#aarKeepRules\(\)): [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AndroidSourceDirectorySet)

The AarKeepRules R8 source directory for this source set.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
