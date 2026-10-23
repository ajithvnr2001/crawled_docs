---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet/
title: AndroidSourceSet \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:08:26.104369+00:00
---

# AndroidSourceSet  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AndroidSourceSet

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/AndroidSourceSet.kt+class:com.android.build.api.dsl.AndroidSourceSet)

Added in 4.2.0
    
    
    interface [AndroidSourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet) : [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html)

Known direct subclasses 

[AndroidLibrarySourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidLibrarySourceSet)

`[AndroidLibrarySourceSet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidLibrarySourceSet)` |   
---|---  
  
* * *

An AndroidSourceSet represents a logical group of Java, aidl and RenderScript sources as well as Android and non-Android (Java-style) resources.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[aidl](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#aidl\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Android AIDL source directory for this source set.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[assets](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#assets\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Android Assets directory for this source set.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[baselineProfiles](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#baselineProfiles\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Android Baseline Profiles source directory for this source set.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#getName\(\))()` Returns the name of this source set.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[java](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#java\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Java source for this source-set  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[jniLibs](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#jniLibs\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Android JNI libs directory for this source-set  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[keepRules](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#keepRules\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The KeepRules R8 source directory for this source set.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[kotlin](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#kotlin\(org.gradle.api.Action\))(action: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)>)` The Kotlin source for this source-set  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[manifest](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#manifest\(kotlin.Function1\))(action: [AndroidSourceFile](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceFile).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Android Manifest file for this source-set.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[mlModels](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#mlModels\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The machine learning models directory for this source set.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[renderscript](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#renderscript\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Android RenderScript source directory for this source set.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[res](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#res\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Android Resources directory for this source-set.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[resources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#resources\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Java-style resources for this source-set  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` |  `[setRoot](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#setRoot\(kotlin.String\))(path: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Sets the root of the source sets to a given path.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#shaders\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` The Android shaders directory for this source set.  
  
### Public properties  
  
---  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[aidl](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#aidl\(\))` The Android AIDL source directory for this source set.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[annotationProcessorConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#annotationProcessorConfigurationName\(\))` Returns the name of the annotation processing tool classpath for this source set.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[apiConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#apiConfigurationName\(\))` Returns the name of the api configuration for this source set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[assets](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#assets\(\))` The Android Assets directory for this source set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[baselineProfiles](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#baselineProfiles\(\))` The Android Baseline Profiles source directory for this source set.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[compileOnlyApiConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#compileOnlyApiConfigurationName\(\))` Returns the name of the compileOnlyApi configuration for this source set.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[compileOnlyConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#compileOnlyConfigurationName\(\))` Returns the name of the compileOnly configuration for this source set.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[implementationConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#implementationConfigurationName\(\))` Returns the name of the implementation configuration for this source set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[java](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#java\(\))` The Java source for this source-set  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[jniLibs](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#jniLibs\(\))` The Android JNI libs directory for this source-set  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[kaptConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#kaptConfigurationName\(\))` Returns the name of the kapt annotation processing tool classpath for this source set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[keepRules](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#keepRules\(\))` The KeepRules R8 source directory for this source set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[kotlin](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#kotlin\(\))` The Kotlin source for this source-set  
`[AndroidSourceFile](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceFile)` |  `[manifest](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#manifest\(\))` The Android Manifest file for this source-set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[mlModels](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#mlModels\(\))` The machine learning models directory for this source set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[renderscript](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#renderscript\(\))` The Android RenderScript source directory for this source set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[res](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#res\(\))` The Android Resources directory for this source-set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[resources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#resources\(\))` The Java-style resources for this source-set  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[runtimeOnlyConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#runtimeOnlyConfigurationName\(\))` Returns the name of the implementation configuration for this source set.  
`[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)` |  `[shaders](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#shaders\(\))` The Android shaders directory for this source set.  
  
## Public functions

### aidl

Added in 4.2.0
    
    
    fun [aidl](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#aidl\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

The Android AIDL source directory for this source set.

### assets

Added in 4.2.0
    
    
    fun [assets](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#assets\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

The Android Assets directory for this source set.

### baselineProfiles

Added in 8.0.2
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [baselineProfiles](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#baselineProfiles\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

The Android Baseline Profiles source directory for this source set.

### getName
    
    
    fun [getName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#getName\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Returns the name of this source set.

### java

Added in 4.2.0
    
    
    fun [java](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#java\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

The Java source for this source-set

### jniLibs

Added in 4.2.0
    
    
    fun [jniLibs](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#jniLibs\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

The Android JNI libs directory for this source-set

### keepRules

Added in 9.5.0-alpha10
    
    
    fun [keepRules](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#keepRules\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

The KeepRules R8 source directory for this source set.

### kotlin

Added in 7.0.0
    
    
    fun [kotlin](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#kotlin\(org.gradle.api.Action\))(action: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<[AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)>): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

The Kotlin source for this source-set

### manifest

Added in 4.2.0
    
    
    fun [manifest](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#manifest\(kotlin.Function1\))(action: [AndroidSourceFile](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceFile).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

The Android Manifest file for this source-set.

### mlModels

Added in 4.2.0
    
    
    fun [mlModels](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#mlModels\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

The machine learning models directory for this source set.

### renderscript

Added in 4.2.0
    
    
    fun [renderscript](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#renderscript\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

The Android RenderScript source directory for this source set.

### res

Added in 4.2.0
    
    
    fun [res](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#res\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

The Android Resources directory for this source-set.

### resources

Added in 4.2.0
    
    
    fun [resources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#resources\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

The Java-style resources for this source-set

### setRoot

Added in 4.2.0
    
    
    fun [setRoot](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#setRoot\(kotlin.String\))(path: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)

Sets the root of the source sets to a given path.

All entries of the source-set are located under this root directory.

This method has a return value for legacy reasons.

Parameters  
---  
`path: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  the root directory path to use.  
  
### shaders

Added in 4.2.0
    
    
    fun [shaders](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#shaders\(kotlin.Function1\))(action: [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

The Android shaders directory for this source set.

## Public properties

### aidl

Added in 4.2.0
    
    
    val [aidl](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#aidl\(\)): [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)

The Android AIDL source directory for this source set.

### annotationProcessorConfigurationName

Added in 4.2.0
    
    
    val [annotationProcessorConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#annotationProcessorConfigurationName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Returns the name of the annotation processing tool classpath for this source set.

### apiConfigurationName

Added in 4.2.0
    
    
    val [apiConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#apiConfigurationName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Returns the name of the api configuration for this source set.

### assets

Added in 4.2.0
    
    
    val [assets](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#assets\(\)): [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)

The Android Assets directory for this source set.

### baselineProfiles

Added in 8.0.2
    
    
    val [baselineProfiles](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#baselineProfiles\(\)): [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)

The Android Baseline Profiles source directory for this source set.

### compileOnlyApiConfigurationName

Added in 8.4.0
    
    
    val [compileOnlyApiConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#compileOnlyApiConfigurationName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Returns the name of the compileOnlyApi configuration for this source set.

### compileOnlyConfigurationName

Added in 4.2.0
    
    
    val [compileOnlyConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#compileOnlyConfigurationName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Returns the name of the compileOnly configuration for this source set.

### implementationConfigurationName

Added in 4.2.0
    
    
    val [implementationConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#implementationConfigurationName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Returns the name of the implementation configuration for this source set.

### java

Added in 4.2.0
    
    
    val [java](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#java\(\)): [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)

The Java source for this source-set

### jniLibs

Added in 4.2.0
    
    
    val [jniLibs](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#jniLibs\(\)): [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)

The Android JNI libs directory for this source-set

### kaptConfigurationName

Added in 8.7.0
    
    
    val [kaptConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#kaptConfigurationName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Returns the name of the kapt annotation processing tool classpath for this source set.

This configuration is only created when built-in KAPT support is enabled.

### keepRules

Added in 9.5.0-alpha10
    
    
    val [keepRules](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#keepRules\(\)): [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)

The KeepRules R8 source directory for this source set.

### kotlin

Added in 7.0.0
    
    
    val [kotlin](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#kotlin\(\)): [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)

The Kotlin source for this source-set

### manifest

Added in 4.2.0
    
    
    val [manifest](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#manifest\(\)): [AndroidSourceFile](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceFile)

The Android Manifest file for this source-set.

### mlModels

Added in 4.2.0
    
    
    val [mlModels](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#mlModels\(\)): [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)

The machine learning models directory for this source set.

### renderscript

Added in 4.2.0
    
    
    val [renderscript](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#renderscript\(\)): [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)

The Android RenderScript source directory for this source set.

### res

Added in 4.2.0
    
    
    val [res](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#res\(\)): [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)

The Android Resources directory for this source-set.

### resources

Added in 4.2.0
    
    
    val [resources](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#resources\(\)): [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)

The Java-style resources for this source-set

### runtimeOnlyConfigurationName

Added in 4.2.0
    
    
    val [runtimeOnlyConfigurationName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#runtimeOnlyConfigurationName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Returns the name of the implementation configuration for this source set.

### shaders

Added in 4.2.0
    
    
    val [shaders](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceSet#shaders\(\)): [AndroidSourceDirectorySet](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AndroidSourceDirectorySet)

The Android shaders directory for this source set.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
