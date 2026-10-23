---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTestCompilation/
title: KotlinMultiplatformAndroidDeviceTestCompilation \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:33:07.064800+00:00
---

# KotlinMultiplatformAndroidDeviceTestCompilation  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTestCompilation/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# KotlinMultiplatformAndroidDeviceTestCompilation

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTestCompilation.kt+class:com.android.build.api.dsl.KotlinMultiplatformAndroidDeviceTestCompilation)

Added in 8.8.0
    
    
    interface [KotlinMultiplatformAndroidDeviceTestCompilation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTestCompilation) : [KotlinMultiplatformAndroidDeviceTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest), [KotlinMultiplatformAndroidCompilation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation)

* * *

## Summary

### Inherited functions  
  
---  
From [com.android.build.api.dsl.KotlinMultiplatformAndroidCompilation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[kotlinOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#kotlinOptions\(org.gradle.api.Action\))~~(configure: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)>)` **This function is deprecated.** Use compilerOptions instead of kotlinOptions to configure compilations  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[kotlinOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#kotlinOptions\(kotlin.Function1\))~~(configure: [<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` **This function is deprecated.** Use compilerOptions instead of kotlinOptions to configure compilations  
  
From [com.android.build.api.dsl.KotlinMultiplatformAndroidDeviceTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[emulatorControl](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#emulatorControl\(kotlin.Function1\))(action: [EmulatorControl](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/EmulatorControl).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[installation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#installation\(kotlin.Function1\))(action: [Installation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Installation).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[managedDevices](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#managedDevices\(kotlin.Function1\))(action: [ManagedDevices](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedDevices).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures Gradle Managed Devices for use in testing with the Unified test platform.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[multidex](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#multidex\(kotlin.Function1\))(action: [MultiDexConfig](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/MultiDexConfig).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[signing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#signing\(kotlin.Function1\))(action: [ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApkSigningConfig).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#targetSdk\(kotlin.Function1\))(action: [TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TargetSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding target sdk for device tests, see `[TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/TargetSdkSpec)` for available options.  
  
### Inherited properties  
  
---  
From [com.android.build.api.dsl.KotlinMultiplatformAndroidCompilation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation) | `[TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)<[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)>>` |  `[compileTaskProvider](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#compileTaskProvider\(\))`  
---|---  
`[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)<[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)>` |  `[compilerOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#compilerOptions\(\))` **This property is deprecated.** To configure compilation compiler options use 'compileTaskProvider': compilation.compileTaskProvider.configure{ compilerOptions {} }  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[componentName](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#componentName\(\))` The name of the component corresponding to this Android compilation.  
`[<Error class: unknown class>](https://developer.android.com/reference/tools/gradle-api/8.13/\[JVM%20root\]/<Error%20class:%20unknown%20class>)` |  `[kotlinOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidCompilation#kotlinOptions\(\))` **This property is deprecated.** Use compilerOptions instead of kotlinOptions to configure compilations  
  
From [com.android.build.api.dsl.KotlinMultiplatformAndroidDeviceTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest) | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[animationsDisabled](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#animationsDisabled\(\))` Disables animations during instrumented tests you run from the command line.  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[applicationId](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#applicationId\(\))` The test application id.  
`[EmulatorControl](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/EmulatorControl)` |  `[emulatorControl](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#emulatorControl\(\))` Configures Android Emulator Grpc Access  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableCoverage](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#enableCoverage\(\))` Specifies code coverage is enabled for module tests of type AndroidTest.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[execution](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#execution\(\))` Specifies whether to use on-device test orchestration.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[functionalTest](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#functionalTest\(\))` See [instrumentation](http://developer.android.com/guide/topics/manifest/instrumentation-element.html).  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[handleProfiling](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#handleProfiling\(\))` See [instrumentation](http://developer.android.com/guide/topics/manifest/instrumentation-element.html).  
`[Installation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Installation)` |  `[installation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#installation\(\))` Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[instrumentationRunner](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#instrumentationRunner\(\))` Test instrumentation runner class name.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[instrumentationRunnerArguments](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#instrumentationRunnerArguments\(\))` Test instrumentation runner custom arguments.  
`[ManagedDevices](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ManagedDevices)` |  `[managedDevices](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#managedDevices\(\))` Configures Gradle Managed Devices for use in testing with the Unified test platform.  
`[MultiDexConfig](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/MultiDexConfig)` |  `[multidex](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#multidex\(\))`  
`[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/ApkSigningConfig)` |  `[signing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#signing\(\))` Encapsulates signing configurations that you can apply to test APK  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-08-07 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-07 UTC."],[],[]] 
