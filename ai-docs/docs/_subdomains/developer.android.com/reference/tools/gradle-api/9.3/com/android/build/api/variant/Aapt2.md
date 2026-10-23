---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Aapt2/
title: Aapt2 \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:33:44.209337+00:00
---

# Aapt2  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Aapt2/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Aapt2

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/Aapt2.kt+class:com.android.build.api.variant.Aapt2)

Added in 8.10.1
    
    
    interface [Aapt2](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Aapt2)

* * *

Provides structured access to AAPT2 tool.

An instance of `[Aapt2](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Aapt2)` can be obtained via `[AndroidComponentsExtension.sdkComponents](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/AndroidComponentsExtension#sdkComponents\(\))`

For example, this is the structure of a `[org.gradle.api.Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` that runs aapt2:
    
    
    abstract class MyTaskUsingAapt2: DefaultTask() {  
      @get:Nested  
      abstract val aapt2Input: Property<com.android.build.api.variant.Aapt2>  
      
      @get:Inject  
      abstract val execOperations: ExecOperations  
      
      @TaskAction  
      fun execute() {  
        val aapt2Executable = aapt2Input.get().executable.get().asFile  
      
        // execute aapt2 help  
        execOperations.exec { spec ->  
          spec.commandLine(aapt2Executable)  
          spec.args("-h")  
          spec.isIgnoreExitValue = true // -h returns exit value 1  
        }  
      }  
    }  
      
    tasks.register<MyTaskUsingAapt2>("myTaskUsingAapt2") {  
      // get an instance of Aapt2  
      this.aapt2Input.set(androidComponents.sdkComponents.aapt2)  
    }

## Summary

### Public properties  
  
---  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>` |  `[executable](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Aapt2#executable\(\))` Path to the [AAPT2](https://developer.android.com/tools/aapt2) executable file from the Android SDK  
`[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[version](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Aapt2#version\(\))` Version of build tools.  
  
## Public properties

### executable

Added in 8.10.1
    
    
    val [executable](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Aapt2#executable\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)>

Path to the [AAPT2](https://developer.android.com/tools/aapt2) executable file from the Android SDK

### version

Added in 8.10.1
    
    
    val [version](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Aapt2#version\(\)): [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Version of build tools. It is used as an input to allow correct build cache behaviour across different platforms

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
