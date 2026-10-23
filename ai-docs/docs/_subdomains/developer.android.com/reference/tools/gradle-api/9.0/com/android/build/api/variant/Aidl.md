---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Aidl/
title: Aidl \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:22:33.296688+00:00
---

# Aidl  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Aidl/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Aidl

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/Aidl.kt+class:com.android.build.api.variant.Aidl)

Added in 8.1.0
    
    
    interface [Aidl](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Aidl)

* * *

Provides structured access to various AIDL tools such as the aidl compiler executable and aidl framework.

An instance of `[Aidl](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Aidl)` can be obtained via `[AndroidComponentsExtension.sdkComponents](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/AndroidComponentsExtension#sdkComponents\(\))`

As an example , let's take a Task that runs aidl compiler:
    
    
    abstract class MyTask: DefaultTask() {  
      @get:Nested  
      abstract val aidlInput: Property<com.android.build.api.variant.Aidl>  
      
      @get:Inject  
      abstract val execOperations: ExecOperations  
      
      @TaskAction  
      fun execute() {  
        val aidlExecutable = aidlInput.get().executable.get().asFile  
        val aidlFramework = aidlInput.get().framework.get().asFile  
      
        // execute aidl binary with --help argument  
        execOperations.exec { spec ->  
          spec.commandLine(aidlExecutable)  
          spec.args("--help")  
        }  
      }  
    }  
      
    tasks.register<MyTask>("myTaskName") {  
      // get an instance of Aidl  
      this.aidlInput.set(androidComponents.sdkComponents.aidl)  
    }

## Summary

### Public properties  
  
---  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>` |  `[executable](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Aidl#executable\(\))` Path to the [AIDL](https://developer.android.com/guide/components/aidl) executable file from the Android SDK  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>` |  `[framework](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Aidl#framework\(\))` Path to the [AIDL](https://developer.android.com/guide/components/aidl) framework file from the Android SDK  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[version](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Aidl#version\(\))` Version of build tools.  
  
## Public properties

### executable

Added in 8.1.0
    
    
    val [executable](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Aidl#executable\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>

Path to the [AIDL](https://developer.android.com/guide/components/aidl) executable file from the Android SDK

### framework

Added in 8.1.0
    
    
    val [framework](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Aidl#framework\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>

Path to the [AIDL](https://developer.android.com/guide/components/aidl) framework file from the Android SDK

### version

Added in 8.1.0
    
    
    val [version](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Aidl#version\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Version of build tools. It is used as an input to allow correct build cache behaviour across different platforms

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
