---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest/
title: KotlinMultiplatformAndroidDeviceTest \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:12:04.472877+00:00
---

# KotlinMultiplatformAndroidDeviceTest  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# KotlinMultiplatformAndroidDeviceTest

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest.kt+class:com.android.build.api.dsl.KotlinMultiplatformAndroidDeviceTest)

Added in 8.8.0
    
    
    interface [KotlinMultiplatformAndroidDeviceTest](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest)

Known direct subclasses 

[KotlinMultiplatformAndroidDeviceTestCompilation](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTestCompilation)

`[KotlinMultiplatformAndroidDeviceTestCompilation](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTestCompilation)` |   
---|---  
  
* * *

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[emulatorControl](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#emulatorControl\(kotlin.Function1\))(action: [EmulatorControl](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/EmulatorControl).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[installation](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#installation\(kotlin.Function1\))(action: [Installation](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Installation).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[managedDevices](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#managedDevices\(kotlin.Function1\))(action: [ManagedDevices](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ManagedDevices).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures Gradle Managed Devices for use in testing with the Unified test platform.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[multidex](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#multidex\(kotlin.Function1\))(action: [MultiDexConfig](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MultiDexConfig).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[signing](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#signing\(kotlin.Function1\))(action: [ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ApkSigningConfig).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#targetSdk\(kotlin.Function1\))(action: [TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TargetSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding target sdk for device tests, see `[TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TargetSdkSpec)` for available options.  
  
### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[animationsDisabled](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#animationsDisabled\(\))` Disables animations during instrumented tests you run from the command line.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[applicationId](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#applicationId\(\))` The test application id.  
`[EmulatorControl](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/EmulatorControl)` |  `[emulatorControl](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#emulatorControl\(\))` Configures Android Emulator Grpc Access  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[enableCoverage](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#enableCoverage\(\))` Specifies code coverage is enabled for module tests of type AndroidTest.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[execution](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#execution\(\))` Specifies whether to use on-device test orchestration.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[functionalTest](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#functionalTest\(\))` See [instrumentation](http://developer.android.com/guide/topics/manifest/instrumentation-element.html).  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?` |  `[handleProfiling](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#handleProfiling\(\))` See [instrumentation](http://developer.android.com/guide/topics/manifest/instrumentation-element.html).  
`[Installation](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Installation)` |  `[installation](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#installation\(\))` Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[instrumentationRunner](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#instrumentationRunner\(\))` Test instrumentation runner class name.  
`[MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[instrumentationRunnerArguments](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#instrumentationRunnerArguments\(\))` Test instrumentation runner custom arguments.  
`[ManagedDevices](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ManagedDevices)` |  `[managedDevices](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#managedDevices\(\))` Configures Gradle Managed Devices for use in testing with the Unified test platform.  
`[MultiDexConfig](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MultiDexConfig)` |  `[multidex](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#multidex\(\))`  
`[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ApkSigningConfig)` |  `[signing](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#signing\(\))` Encapsulates signing configurations that you can apply to test APK  
  
## Public functions

### emulatorControl

Added in 8.8.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [emulatorControl](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#emulatorControl\(kotlin.Function1\))(action: [EmulatorControl](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/EmulatorControl).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### installation

Added in 8.8.0
    
    
    fun [installation](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#installation\(kotlin.Function1\))(action: [Installation](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Installation).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.

For more information about the properties you can configure in this block, see `[Installation](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Installation)`.

### managedDevices

Added in 8.8.0
    
    
    fun [managedDevices](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#managedDevices\(kotlin.Function1\))(action: [ManagedDevices](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ManagedDevices).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures Gradle Managed Devices for use in testing with the Unified test platform.

### multidex

Added in 8.8.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [multidex](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#multidex\(kotlin.Function1\))(action: [MultiDexConfig](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MultiDexConfig).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### signing

Added in 8.8.0
    
    
    fun [signing](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#signing\(kotlin.Function1\))(action: [ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ApkSigningConfig).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### targetSdk

Added in 8.12.0
    
    
    fun [targetSdk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#targetSdk\(kotlin.Function1\))(action: [TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TargetSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures all aspects regarding target sdk for device tests, see `[TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TargetSdkSpec)` for available options.

## Public properties

### animationsDisabled

Added in 8.8.0
    
    
    var [animationsDisabled](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#animationsDisabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Disables animations during instrumented tests you run from the command line.

If you set this property to `true`, running instrumented tests with Gradle from the command line executes `am instrument` with the `--no-window-animation` flag. By default, this property is set to `false`.

This property does not affect tests that you run using Android Studio. To learn more about running tests from the command line, see [Test from the Command Line](https://d.android.com/studio/test/command-line.html).

### applicationId

Added in 8.8.0
    
    
    var [applicationId](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#applicationId\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The test application id.

### emulatorControl

Added in 8.8.0
    
    
    val [emulatorControl](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#emulatorControl\(\)): [EmulatorControl](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/EmulatorControl)

Configures Android Emulator Grpc Access

Android Emulator Grpc Access will make it possible to interact with the emulator over gRPC
    
    
    emulatorControl {  
      enable true  
      secondsValid 180  
      allowedEndpoints.addAll(  
          "/android.emulation.control.EmulatorController/getStatus",  
          "/android.emulation.control.EmulatorController/getVmState")  
    }

### enableCoverage

Added in 8.8.0
    
    
    var [enableCoverage](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#enableCoverage\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Specifies code coverage is enabled for module tests of type AndroidTest.

If enabled, prepares module class files for code coverage collection such as instrumenting dependent library classes and module classes. This allows for code coverage reports to be generated.

### execution

Added in 8.8.0
    
    
    var [execution](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#execution\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Specifies whether to use on-device test orchestration.

If you want to [use Android Test Orchestrator](https://developer.android.com/training/testing/junit-runner.html#using-android-test-orchestrator) you need to specify `"ANDROID_TEST_ORCHESTRATOR"`, as shown below. By default, this property is set to `"HOST"`, which disables on-device orchestration.

### functionalTest

Added in 8.8.0
    
    
    var [functionalTest](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#functionalTest\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

See [instrumentation](http://developer.android.com/guide/topics/manifest/instrumentation-element.html).

### handleProfiling

Added in 8.8.0
    
    
    var [handleProfiling](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#handleProfiling\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)?

See [instrumentation](http://developer.android.com/guide/topics/manifest/instrumentation-element.html).

### installation

Added in 8.8.0
    
    
    val [installation](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#installation\(\)): [Installation](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Installation)

Specifies options for the [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb.html), such as APK installation options.

For more information about the properties you can configure in this block, see `[Installation](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Installation)`.

### instrumentationRunner

Added in 8.8.0
    
    
    var [instrumentationRunner](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#instrumentationRunner\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Test instrumentation runner class name. This is a fully qualified class name of the runner See [instrumentation](http://developer.android.com/guide/topics/manifest/instrumentation-element.html).

### instrumentationRunnerArguments

Added in 8.8.0
    
    
    val [instrumentationRunnerArguments](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#instrumentationRunnerArguments\(\)): [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Test instrumentation runner custom arguments.

e.g. `[key: "value"]` will give `adb shell am instrument -w -e key value com.example`...

See [instrumentation](http://developer.android.com/guide/topics/manifest/instrumentation-element.html).

Test runner arguments can also be specified from the command line:
    
    
    ./gradlew connectedAndroidTest -Pandroid.testInstrumentationRunnerArguments.size=medium  
    ./gradlew connectedAndroidTest -Pandroid.testInstrumentationRunnerArguments.foo=bar

### managedDevices

Added in 8.8.0
    
    
    val [managedDevices](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#managedDevices\(\)): [ManagedDevices](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ManagedDevices)

Configures Gradle Managed Devices for use in testing with the Unified test platform.

### multidex

Added in 8.8.0
    
    
    val [multidex](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#multidex\(\)): [MultiDexConfig](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/MultiDexConfig)

### signing

Added in 8.8.0
    
    
    val [signing](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest#signing\(\)): [ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ApkSigningConfig)

Encapsulates signing configurations that you can apply to test APK

For more information about the properties you can configure in this block, see `[ApkSigningConfig](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/ApkSigningConfig)`.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
