---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileOptions/
title: CompileOptions \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:57:20.643490+00:00
---

# CompileOptions  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileOptions/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# CompileOptions

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/CompileOptions.kt+class:com.android.build.api.dsl.CompileOptions)

Added in 4.2.0
    
    
    interface [CompileOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileOptions)

* * *

Java compilation options.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[sourceCompatibility](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileOptions#sourceCompatibility\(kotlin.Any\))(sourceCompatibility: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Language level of the java source code.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[targetCompatibility](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileOptions#targetCompatibility\(kotlin.Any\))(targetCompatibility: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Version of the generated Java bytecode.  
  
### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[encoding](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileOptions#encoding\(\))` Java source files encoding.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isCoreLibraryDesugaringEnabled](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileOptions#isCoreLibraryDesugaringEnabled\(\))` Whether core library desugaring is enabled.  
`[JavaVersion](https://docs.gradle.org/current/javadoc/org/gradle/api/JavaVersion.html)` |  `[sourceCompatibility](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileOptions#sourceCompatibility\(\))` Language level of the java source code.  
`[JavaVersion](https://docs.gradle.org/current/javadoc/org/gradle/api/JavaVersion.html)` |  `[targetCompatibility](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileOptions#targetCompatibility\(\))` Version of the generated Java bytecode.  
  
## Public functions

### sourceCompatibility

Added in 4.2.0
    
    
    fun [sourceCompatibility](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileOptions#sourceCompatibility\(kotlin.Any\))(sourceCompatibility: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Language level of the java source code.

Similar to what [Gradle Java plugin](http://www.gradle.org/docs/current/userguide/java_plugin.html) uses. Formats supported are:

  * `"1.6"`

  * `1.6`

  * `JavaVersion.Version_1_6`

  * `"Version_1_6"`




### targetCompatibility

Added in 4.2.0
    
    
    fun [targetCompatibility](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileOptions#targetCompatibility\(kotlin.Any\))(targetCompatibility: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Version of the generated Java bytecode.

Similar to what [Gradle Java plugin](http://www.gradle.org/docs/current/userguide/java_plugin.html) uses. Formats supported are:

  * `"1.6"`

  * `1.6`

  * `JavaVersion.Version_1_6`

  * `"Version_1_6"`




## Public properties

### encoding

Added in 4.2.0
    
    
    var [encoding](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileOptions#encoding\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Java source files encoding.

### isCoreLibraryDesugaringEnabled

Added in 4.2.0
    
    
    var [isCoreLibraryDesugaringEnabled](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileOptions#isCoreLibraryDesugaringEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether core library desugaring is enabled.

### sourceCompatibility

Added in 4.2.0
    
    
    var [sourceCompatibility](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileOptions#sourceCompatibility\(\)): [JavaVersion](https://docs.gradle.org/current/javadoc/org/gradle/api/JavaVersion.html)

Language level of the java source code.

Similar to what [Gradle Java plugin](http://www.gradle.org/docs/current/userguide/java_plugin.html) uses. Formats supported are:

  * `"1.6"`

  * `1.6`

  * `JavaVersion.Version_1_6`

  * `"Version_1_6"`




### targetCompatibility

Added in 4.2.0
    
    
    var [targetCompatibility](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/CompileOptions#targetCompatibility\(\)): [JavaVersion](https://docs.gradle.org/current/javadoc/org/gradle/api/JavaVersion.html)

Version of the generated Java bytecode.

Similar to what [Gradle Java plugin](http://www.gradle.org/docs/current/userguide/java_plugin.html) uses. Formats supported are:

  * `"1.6"`

  * `1.6`

  * `JavaVersion.Version_1_6`

  * `"Version_1_6"`




Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
