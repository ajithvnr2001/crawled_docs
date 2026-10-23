---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidTestOnJvmCompilation/
title: KotlinMultiplatformAndroidTestOnJvmCompilation \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:00:23.429922+00:00
---

# KotlinMultiplatformAndroidTestOnJvmCompilation  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidTestOnJvmCompilation/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# KotlinMultiplatformAndroidTestOnJvmCompilation

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/KotlinMultiplatformAndroidHostTestCompilation.kt+class:com.android.build.api.dsl.KotlinMultiplatformAndroidTestOnJvmCompilation)

Added in 8.2.0

Deprecated in 8.8.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [KotlinMultiplatformAndroidTestOnJvmCompilation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidTestOnJvmCompilation) : [KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest), [KotlinMultiplatformAndroidCompilation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation)

* * *

**This interface is deprecated.**  
Use KotlinMultiplatformAndroidHostTestCompilation. This interface will be removed in AGP 9.0

## Summary

### Inherited functions  
  
---  
From [com.android.build.api.dsl.KotlinMultiplatformAndroidCompilation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[kotlinOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#kotlinOptions\(org.gradle.api.Action\))~~(configure: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.12/\[JVM%20root\]/<Error%20class:%20unknown%20class>)>)` **This function is deprecated.** Use compilerOptions instead of kotlinOptions to configure compilations  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[kotlinOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#kotlinOptions\(kotlin.Function1\))~~(configure: [<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.12/\[JVM%20root\]/<Error%20class:%20unknown%20class>).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Use compilerOptions instead of kotlinOptions to configure compilations  
  
From [com.android.build.api.dsl.KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest#targetSdk\(kotlin.Function1\))(action: [TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding target sdk for host tests, see `[TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/TargetSdkSpec)` for available options.  
---|---  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.KotlinMultiplatformAndroidCompilation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation) | `[TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.12/\[JVM%20root\]/<Error%20class:%20unknown%20class>)<[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.12/\[JVM%20root\]/<Error%20class:%20unknown%20class>)>>` |  `[compileTaskProvider](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#compileTaskProvider\(\))`  
---|---  
`[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.12/\[JVM%20root\]/<Error%20class:%20unknown%20class>)<[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.12/\[JVM%20root\]/<Error%20class:%20unknown%20class>)>` |  `[compilerOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#compilerOptions\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[componentName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#componentName\(\))` The name of the component corresponding to this Android compilation.  
`[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.12/\[JVM%20root\]/<Error%20class:%20unknown%20class>)` |  `[kotlinOptions](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#kotlinOptions\(\))` **This property is deprecated.** Use compilerOptions instead of kotlinOptions to configure compilations  
  
From [com.android.build.api.dsl.KotlinMultiplatformAndroidHostTest](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableCoverage](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest#enableCoverage\(\))` Specifies unit test code coverage data collection by configuring the JacocoPlugin.  
---|---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isIncludeAndroidResources](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest#isIncludeAndroidResources\(\))` Enables unit tests to use Android resources, assets, and manifests.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isReturnDefaultValues](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest#isReturnDefaultValues\(\))` Whether unmocked methods from android.jar should throw exceptions or return default values (i.e. zero or null).  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-06-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-20 UTC."],[],[]] 
