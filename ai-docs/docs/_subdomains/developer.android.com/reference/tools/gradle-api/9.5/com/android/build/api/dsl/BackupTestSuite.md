---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BackupTestSuite/
title: BackupTestSuite \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:09:15.149596+00:00
---

# BackupTestSuite  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BackupTestSuite/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# BackupTestSuite

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/BackupTestSuite.kt+class:com.android.build.api.dsl.BackupTestSuite)

Added in 9.5.0-alpha10
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [BackupTestSuite](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BackupTestSuite)

* * *

A test suite to configure and run Automated Backup and Restore tests.

A `[BackupTestSuite](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BackupTestSuite)` configures the execution environment, JUnit 5 test engine, instrumentation runners, and dual source container dependency graphs required to execute automated backup and restore tests on a target device or emulator.

Automated Backup and Restore testing uses a hybrid orchestration model:

  1. **Host-side test orchestrator (configured via`[hostJar](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BackupTestSuite#hostJar\(kotlin.Function1\))`)**: Executes on the host machine (JVM) using JUnit 5 (Jupiter), driving device state via ADB, triggering cloud or local backup passes, clearing app data, initiating restores, and verifying broadcast signals.

  2. **On-device test harness (configured via`[testApk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BackupTestSuite#testApk\(kotlin.Function1\))`)**: Runs inside an instrumented Android environment to seed local storage state (SharedPreferences, Room/SQLite, files, Keystore) prior to backup, and asserts post-restore data integrity.




Example usage:
    
    
    android {  
        testOptions {  
            backupTests {  
                create("myBackupTest") {  
                    backupTestLibraryVersion = "1.0.0-alpha01"  
                    targetVariants.add("debug")  
      
                    hostJar {  
                        dependencies {  
                            implementation(project(":custom-backup-test-helpers"))  
                            implementation("com.google.truth:truth:1.4.2")  
                        }  
                    }  
                    testApk {  
                        dependencies {  
                            implementation("androidx.room:room-testing:2.6.1")  
                        }  
                    }  
                }  
            }  
        }  
    }

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[hostJar](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BackupTestSuite#hostJar\(kotlin.Function1\))(action: [TestSuiteHostJarSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TestSuiteHostJarSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures the host-side (JVM) test component for this test suite.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[testApk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BackupTestSuite#testApk\(kotlin.Function1\))(action: [TestSuiteTestApkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TestSuiteTestApkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures the on-device (APK) test component for this test suite.  
  
### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[backupTestLibraryVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BackupTestSuite#backupTestLibraryVersion\(\))` The version of the automated backup test framework.  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[targetVariants](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BackupTestSuite#targetVariants\(\))` Defines which build variants this test suite targets.  
  
## Public functions

### hostJar

Added in 9.5.0-alpha10
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [hostJar](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BackupTestSuite#hostJar\(kotlin.Function1\))(action: [TestSuiteHostJarSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TestSuiteHostJarSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures the host-side (JVM) test component for this test suite.

Dependencies declared inside this block are added to the host JVM test execution classpath. This enables host-side tests to access custom test helpers, assertion libraries (e.g., Google Truth), and mock frameworks.

Parameters  
---  
`action: [TestSuiteHostJarSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TestSuiteHostJarSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  Lambda to configure the `[TestSuiteHostJarSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TestSuiteHostJarSpec)`.  
  
### testApk

Added in 9.5.0-alpha10
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [testApk](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BackupTestSuite#testApk\(kotlin.Function1\))(action: [TestSuiteTestApkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TestSuiteTestApkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures the on-device (APK) test component for this test suite.

Dependencies declared inside this block are compiled into the on-device test helper APK. This enables on-device actions to access application database schemas, Room testing utilities, and custom instrumentation runners.

Parameters  
---  
`action: [TestSuiteTestApkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TestSuiteTestApkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  Lambda to configure the `[TestSuiteTestApkSpec](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/TestSuiteTestApkSpec)`.  
  
## Public properties

### backupTestLibraryVersion

Added in 9.5.0-alpha10
    
    
    var [backupTestLibraryVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BackupTestSuite#backupTestLibraryVersion\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The version of the automated backup test framework.

Specifies the version of the `androidx.test.backup:backup-host` and `androidx.test.backup:backup` artifacts to automatically inject into the test suite's host and device execution classpaths.

This property is optional. If omitted, the Android Gradle Plugin will default to the latest compatible framework version.

### targetVariants

Added in 9.5.0-alpha10
    
    
    val [targetVariants](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/BackupTestSuite#targetVariants\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Defines which build variants this test suite targets.

If left empty, all buildable variants in the module will be tested.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
