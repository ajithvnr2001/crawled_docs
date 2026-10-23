---
url: https://developer.android.com/build/r8-execution-profiles/
title: Configure how R8 runs \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:45:27.268945+00:00
---

# Configure how R8 runs  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/build/r8-execution-profiles/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ Gradle build guides ](https://developer.android.com/build/gradle-build-overview)



#  Configure how R8 runs Stay organized with collections  Save and categorize content based on your preferences. 

The settings plugin lets you create execution profiles for the R8 tool, letting you configure how R8 runs so it doesn't slow down your build. Depending on the environment, you can use profiles to run R8 in a separate JVM process and set JVM arguments, such as maximum heap size.

### Declare an execution profile

[Apply the settings plugin](https://developer.android.com/studio/build/android-settings-plugin#apply-settings-plugin), and then add the `android` block to the `settings.gradle` file. In this block, you can define different profiles and then set a default, as shown in the following example:

### Kotlin
    
    
    android {
        execution {
            profiles {
                create("server") {
                    r8 {
                        runInSeparateProcess = true
                        jvmOptions += listOf("-Xms2048m", "-Xmx8192m", "-XX:+HeapDumpOnOutOfMemoryError")
                    }
                }
                create("local") {
                    r8 {
                        runInSeparateProcess = true
                        jvmOptions += listOf("-Xms256m", "-Xmx2048m", "-XX:+HeapDumpOnOutOfMemoryError")
                    }
                }
                defaultProfile = "server"
            }
        }
    }

### Groovy
    
    
    android {
        execution {
            profiles {
                register("server") {
                    r8 {
                        runInSeparateProcess = true
                        jvmOptions += ["-Xms2048m", "-Xmx8192m", "-XX:+HeapDumpOnOutOfMemoryError"]
                    }
                }
                register("local") {
                    r8 {
                        runInSeparateProcess = true
                        jvmOptions += ["-Xms256m", "-Xmx2048m", "-XX:+HeapDumpOnOutOfMemoryError"]
                    }
                }
                defaultProfile = "server"
            }
        }
    }

### Override the default profile

To override the current default execution profile, add the following property to the `gradle.properties` file.
    
    
    android.settings.executionProfile=example-profile
    

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-01-23 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-23 UTC."],[],[]] 
