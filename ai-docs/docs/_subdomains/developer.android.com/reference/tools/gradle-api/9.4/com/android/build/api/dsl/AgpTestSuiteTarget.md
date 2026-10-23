---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AgpTestSuiteTarget/
title: AgpTestSuiteTarget \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:49:36.979562+00:00
---

# AgpTestSuiteTarget  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AgpTestSuiteTarget/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AgpTestSuiteTarget

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/AgpTestSuiteTarget.kt+class:com.android.build.api.dsl.AgpTestSuiteTarget)

Added in 8.12.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [AgpTestSuiteTarget](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AgpTestSuiteTarget) : [TestSuiteTarget](https://docs.gradle.org/current/javadoc/org/gradle/testing/base/TestSuiteTarget.html), [Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html)

* * *

A test suite target is a collection of tests that run in a particular context. The context is defined by the devices they run on when dealing with a device test.

android { // ... other android configurations like compileSdk, defaultConfig, etc.
    
    
    testOptions {
        managedDevices {
            localDevices {
                // First, define your individual managed devices
                create("pixel2api30") {
                    device = "Pixel 2"
                    apiLevel = 30
                    systemImageSource = "aosp-atd" // or "google", "google-atd", "aosp"
                }
                create("pixel6api33") {
                    device = "Pixel 6"
                    apiLevel = 33
                    systemImageSource = "google-atd"
                }
                create("largeScreenApi31") {
                    device = "Nexus 10" // Example of a tablet
                    apiLevel = 31
                    systemImageSource = "aosp"
                }
            }
            groups {
                // Now, define your groups referencing the devices above
                create("phoneGroup") {
                    // This group targets specific phone-like devices
                    targetDevices.add(allDevices.getByName("pixel2api30"))
                    targetDevices.add(allDevices.getByName("pixel6api33"))
                    // You can also set properties for all devices in this group
                    // if they are not already set on the individual device.
                    // For example:
                    // systemImageSource = "aosp-atd" // if all devices in this group should use this
                }
                create("tabletGroup") {
                    // This group targets tablet-like devices
                    targetDevices.add(devices.getByName("largeScreenApi31"))
                }
                create("allMyCiDevices") {
                    // This group could target all devices you use for CI
                    targetDevices.addAll(devices.getByName("pixel2api30"), devices.getByName("pixel6api33"), devices.getByName("largeScreenApi31"))
                }
            }
        }
    }
    testOptions {
        suites {
             create("someTestSuite") {
                  targets {
                      create("tabletRun") {
                         targetDevices += "tabletGroup"
                      }
                  }
             }
        }
    }

}

## Summary

### Public properties  
  
---  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[targetDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AgpTestSuiteTarget#targetDevices\(\))` Defines which group of devices or devices to run the test suite tests against.  
  
### Inherited functions  
  
---  
From [org.gradle.api.Named](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getName](https://docs.gradle.org/current/javadoc/org/gradle/api/Named.html#getName--)()`  
---|---  
  
From [org.gradle.testing.base.TestSuiteTarget](https://docs.gradle.org/current/javadoc/org/gradle/testing/base/TestSuiteTarget.html) | `[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)>` |  `[getBinaryResultsDirectory](https://docs.gradle.org/current/javadoc/org/gradle/testing/base/TestSuiteTarget.html#getBinaryResultsDirectory--)()`  
---|---  
  
## Public properties

### targetDevices

Added in 8.12.0
    
    
    val [targetDevices](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/AgpTestSuiteTarget#targetDevices\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Defines which group of devices or devices to run the test suite tests against. If the test runs on the host machine, this list will be ignored.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
