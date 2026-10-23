---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation/
title: KotlinMultiplatformAndroidCompilation \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:32:58.846295+00:00
---

# KotlinMultiplatformAndroidCompilation  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# KotlinMultiplatformAndroidCompilation

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation.kt+class:com.android.build.api.dsl.KotlinMultiplatformAndroidCompilation)

Added in 8.2.0
    
    
    interface [KotlinMultiplatformAndroidCompilation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation)

Known direct subclasses 

[KotlinMultiplatformAndroidDeviceTestCompilation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTestCompilation), [KotlinMultiplatformAndroidHostTestCompilation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTestCompilation), [KotlinMultiplatformAndroidTestOnDeviceCompilation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidTestOnDeviceCompilation), [KotlinMultiplatformAndroidTestOnJvmCompilation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidTestOnJvmCompilation)

`[KotlinMultiplatformAndroidDeviceTestCompilation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTestCompilation)` |   
---|---  
`[KotlinMultiplatformAndroidHostTestCompilation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTestCompilation)` |   
`[KotlinMultiplatformAndroidTestOnDeviceCompilation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidTestOnDeviceCompilation)` |  **This interface is deprecated.** Use KotlinMultiplatformAndroidDeviceTestCompilation.  
`[KotlinMultiplatformAndroidTestOnJvmCompilation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidTestOnJvmCompilation)` |  **This interface is deprecated.** Use KotlinMultiplatformAndroidHostTestCompilation.  
  
* * *

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[kotlinOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#kotlinOptions\(org.gradle.api.Action\))~~(configure: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)>)` **This function is deprecated.** Use compilerOptions instead of kotlinOptions to configure compilations  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[kotlinOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#kotlinOptions\(kotlin.Function1\))~~(configure: [<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Use compilerOptions instead of kotlinOptions to configure compilations  
  
### Public properties  
  
---  
`[TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)<[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)>>` |  `[compileTaskProvider](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#compileTaskProvider\(\))`  
`[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)<[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)>` |  `[compilerOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#compilerOptions\(\))` **This property is deprecated.** To configure compilation compiler options use 'compileTaskProvider': compilation.compileTaskProvider.configure{ compilerOptions {} }  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[componentName](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#componentName\(\))` The name of the component corresponding to this Android compilation.  
`[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)` |  `[kotlinOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#kotlinOptions\(\))` **This property is deprecated.** Use compilerOptions instead of kotlinOptions to configure compilations  
  
## Public functions

### kotlinOptions
    
    
    fun ~~[kotlinOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#kotlinOptions\(org.gradle.api.Action\))~~(configure: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)>): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Use compilerOptions instead of kotlinOptions to configure compilations

### kotlinOptions
    
    
    fun ~~[kotlinOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#kotlinOptions\(kotlin.Function1\))~~(configure: [<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Use compilerOptions instead of kotlinOptions to configure compilations

## Public properties

### compileTaskProvider

Added in 8.13.2
    
    
    val [compileTaskProvider](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#compileTaskProvider\(\)): [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)<[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)>>

### compilerOptions

Added in 8.2.0

Deprecated in 8.13.2
    
    
    val [compilerOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#compilerOptions\(\)): [<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)<[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)>

**This property is deprecated.**  
To configure compilation compiler options use 'compileTaskProvider': compilation.compileTaskProvider.configure{ compilerOptions {} }

### componentName

Added in 8.8.0
    
    
    val [componentName](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#componentName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

The name of the component corresponding to this Android compilation. Consists of the compilation name prefixed by the android target name (e.g "android") The default component names for the default compilations would be:

  * androidMain

  * androidHostTest

  * androidDeviceTest




### kotlinOptions

Added in 8.2.0

Deprecated in 8.2.0
    
    
    val [kotlinOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#kotlinOptions\(\)): [<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)

**This property is deprecated.**  
Use compilerOptions instead of kotlinOptions to configure compilations

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-11 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-11 UTC."],[],[]] 
