---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions/
title: TestOptions \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:56:25.954362+00:00
---

# TestOptions  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestOptions

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/TestOptions.kt+class:com.android.build.api.dsl.TestOptions)

Added in 4.2.0
    
    
    interface [TestOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions)

* * *

Options for running tests.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[emulatorControl](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#emulatorControl\(kotlin.Function1\))(action: [EmulatorControl](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/EmulatorControl).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[managedDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#managedDevices\(kotlin.Function1\))(action: [ManagedDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedDevices).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures Gradle Managed Devices for use in testing with the Unified test platform.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#targetSdk\(kotlin.Function1\))(action: [TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TargetSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Specifies value that overrides all aspects regarding target sdk for tests in libraries.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[unitTests](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#unitTests\(kotlin.Function1\))(action: [UnitTestOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/UnitTestOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Options for controlling unit tests execution.  
  
### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[animationsDisabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#animationsDisabled\(\))` Disables animations during instrumented tests you run from the command line.  
`[EmulatorControl](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/EmulatorControl)` |  `[emulatorControl](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#emulatorControl\(\))` Configures Android Emulator Grpc Access  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[execution](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#execution\(\))` Specifies whether to use on-device test orchestration.  
`[ManagedDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedDevices)` |  `[managedDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#managedDevices\(\))` Configures Gradle Managed Devices for use in testing with the Unified test platform.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[reportDir](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#reportDir\(\))` Name of the reports' directory.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[resultsDir](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#resultsDir\(\))` Name of the results' directory.  
`[NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ScreenshotTestSuite](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ScreenshotTestSuite)>` |  `[screenshotTests](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#screenshotTests\(\))` Configures the specialized Screenshot TestSuite designed for Compose Preview Screenshot Testing.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#targetSdk\(\))` Specifies value that overrides target sdk version number for tests in libraries.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#targetSdkPreview\(\))` Specifies value that overrides target sdk preview number for tests in libraries.  
`[UnitTestOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/UnitTestOptions)` |  `[unitTests](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#unitTests\(\))` Options for controlling unit tests execution.  
  
## Public functions

### emulatorControl

Added in 8.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [emulatorControl](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#emulatorControl\(kotlin.Function1\))(action: [EmulatorControl](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/EmulatorControl).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### managedDevices

Added in 7.2.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [managedDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#managedDevices\(kotlin.Function1\))(action: [ManagedDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedDevices).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures Gradle Managed Devices for use in testing with the Unified test platform.

### targetSdk

Added in 9.4.1
    
    
    fun [targetSdk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#targetSdk\(kotlin.Function1\))(action: [TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TargetSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies value that overrides all aspects regarding target sdk for tests in libraries.

See `[TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TargetSdkSpec)` for available options. Important: Setting this value will cause an error for application and other module types.

### unitTests

Added in 4.2.0
    
    
    fun [unitTests](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#unitTests\(kotlin.Function1\))(action: [UnitTestOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/UnitTestOptions).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Options for controlling unit tests execution.

## Public properties

### animationsDisabled

Added in 4.2.0
    
    
    var [animationsDisabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#animationsDisabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Disables animations during instrumented tests you run from the command line.

If you set this property to `true`, running instrumented tests with Gradle from the command line executes `am instrument` with the `--no-window-animation` flag. By default, this property is set to `false`.

This property does not affect tests that you run using Android Studio. To learn more about running tests from the command line, see [Test from the Command Line](https://d.android.com/studio/test/command-line.html).

### emulatorControl

Added in 8.1.0
    
    
    val [emulatorControl](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#emulatorControl\(\)): [EmulatorControl](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/EmulatorControl)

Configures Android Emulator Grpc Access

Android Emulator Grpc Access will make it possible to interact with the emulator over gRPC
    
    
    android {  
        emulatorControl {  
          enable true  
          secondsValid 180  
          allowedEndpoints.addAll(  
              "/android.emulation.control.EmulatorController/getStatus",  
              "/android.emulation.control.EmulatorController/getVmState")  
        }  
    }

### execution

Added in 4.2.0
    
    
    var [execution](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#execution\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Specifies whether to use on-device test orchestration.

If you want to [use Android Test Orchestrator](https://developer.android.com/training/testing/junit-runner.html#using-android-test-orchestrator) you need to specify `"ANDROID_TEST_ORCHESTRATOR"`, as shown below. By default, this property is set to `"HOST"`, which disables on-device orchestration.
    
    
    android {  
      testOptions {  
        execution 'ANDROID_TEST_ORCHESTRATOR'  
      }  
    }

since 3.0.0

### managedDevices

Added in 7.2.0
    
    
    val [managedDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#managedDevices\(\)): [ManagedDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedDevices)

Configures Gradle Managed Devices for use in testing with the Unified test platform.

### reportDir

Added in 4.2.0
    
    
    var [reportDir](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#reportDir\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Name of the reports' directory.

### resultsDir

Added in 4.2.0
    
    
    var [resultsDir](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#resultsDir\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Name of the results' directory.

### screenshotTests

Added in 9.4.1
    
    
    val [screenshotTests](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#screenshotTests\(\)): [NamedDomainObjectContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/NamedDomainObjectContainer.html)<[ScreenshotTestSuite](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ScreenshotTestSuite)>

Configures the specialized Screenshot TestSuite designed for Compose Preview Screenshot Testing.

### targetSdk

Added in 8.2.0
    
    
    var [targetSdk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#targetSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

Specifies value that overrides target sdk version number for tests in libraries. Default value is set to minSdk. Important: Setting this value will cause an error for application and other module types.

### targetSdkPreview

Added in 8.2.0
    
    
    var [targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#targetSdkPreview\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Specifies value that overrides target sdk preview number for tests in libraries. Default value is empty. Important: Setting this value will cause an error for application and other module types.

### unitTests

Added in 4.2.0
    
    
    val [unitTests](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/TestOptions#unitTests\(\)): [UnitTestOptions](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/UnitTestOptions)

Options for controlling unit tests execution.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
