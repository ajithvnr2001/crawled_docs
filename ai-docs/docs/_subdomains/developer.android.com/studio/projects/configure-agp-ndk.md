---
url: https://developer.android.com/studio/projects/configure-agp-ndk/
title: Configure the NDK for the Android Gradle plugin \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:44:34.136619+00:00
---

# Configure the NDK for the Android Gradle plugin  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/studio/projects/configure-agp-ndk/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ IDE guides ](https://developer.android.com/studio/intro)



#  Configure the NDK for the Android Gradle plugin Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to configure the NDK in your project according to the version of the Android Gradle Plugin (AGP) used by the project.

**Note:** If possible, you should try to update the version of AGP in your project to version 4.1 or later. These AGP versions will auto-download the NDK for you in Android Studio.

The steps vary according to the version of AGP used in the project. Find the Android Gradle Plugin version in either of the following locations:

  * **File > Project Structure > Project** menu in Android Studio
  * The top-level `build.gradle` file in the project



Select the version below:

AGP 4.1+ AGP 4.0 AGP 3.6 AGP 3.5 AGP 3.4

## AGP version 4.1+

You have the following options to configure the NDK:

  * (Recommended) Use the [`ndkVersion`](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) property to set the NDK version.
  * Do not set any property. Android Studio will automatically download the [default version of the NDK for that specific AGP version](https://developer.android.com/studio/projects/install-ndk#default-ndk-per-agp) (in this case, NDK version 21.0.6113669) or you can install the NDK from the command line. Android Studio installs all versions of the NDK in the `android-sdk/ndk/` directory. Each version is located in a subdirectory with the version number as its name.
  * For special use cases, use the `ndkPath` property:

### Groovy
        
        android {
          ndkPath "/Users/ndkPath/ndk21"  // Point to your own NDK
        }

### Kotlin
        
        android {
          ndkPath = "/Users/ndkPath/ndk21"  // Point to your own NDK
        }

**Note:** Remove this property before distributing your source code; it should be left outside of your version control system. 



### Install the NDK from the command line

To install the NDK from the command line, do the following:

  1. Use the `sdkmanager` tool to view versions of CMake and NDK packages that are available. Similar to other SDK components, the NDK is released through different channels:
         
         sdkmanager --list [--channel=channel_id]  // NDK channels: 0 (stable),
                                                     // 1 (beta), or 3 (canary)

  2. Pass the `sdkmanager` the strings for the packages that you want to install. For example, to install CMake or the NDK, use the following syntax:
         
         sdkmanager --install
                   ["ndk;major.minor.build[suffix]" | "cmake;major.minor.micro.build"]
                   [--channel=channel_id]

Use the `--channel` option to only install a package if it has been released in a channel _up to and including_ channel_id.




For more information, see [sdkmanager](https://developer.android.com/studio/command-line/sdkmanager).

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-06 UTC."],[],[]] 
