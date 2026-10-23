---
url: https://developer.android.com/kotlin/multiplatform/setup/
title: Setup your environment (Kotlin Multiplatform) \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:28.400985+00:00
---

# Setup your environment (Kotlin Multiplatform)  |  Android Developers

> Source: https://developer.android.com/kotlin/multiplatform/setup/

  * [ Android Developers ](https://developer.android.com/)
  * [ Get started ](https://developer.android.com/get-started/overview)
  * [ Kotlin ](https://developer.android.com/kotlin)
  * [ Guides ](https://developer.android.com/kotlin/first)



#  Setup your environment (Kotlin Multiplatform) Stay organized with collections  Save and categorize content based on your preferences. 

[Kotlin Multiplatform](https://kotlinlang.org/lp/mobile/) (KMP) enables sharing Kotlin code across different platforms. Before you start building apps with KMP, you'll need to set up your environment as described in this document. You can also refer to JetBrain's [official documentation](https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform-setup.html).

## Install or update required tools

  * Install or update to the latest stable version of [Android Studio](https://developer.android.com/studio).
  * Update the [Kotlin plugin](https://kotlinlang.org/docs/releases.html#update-to-a-new-release) that is bundled with Android Studio to the latest version to avoid compatibility issues.
  * (Optional) For iOS development, install [Xcode](https://apps.apple.com/us/app/xcode/id497799835) to build the UI and add Swift or Objective-C code as needed.



## Create a Kotlin Multiplatform project

You can use the [Kotlin Multiplatform wizard](https://kmp.jetbrains.com/) from JetBrains to create a new KMP project. Make sure to choose the **Do not share UI** option to keep the UI native.

### Project structure

KMP projects follow a project structure similar to Android projects.

A KMP project contains platform-specific modules along with a shared module. Add your platform-specific code to the relevant module. For example, add your Android app UI in the **androidApp** module and your iOS app UI in **iosApp**. Any code you want to share between platforms goes in the **shared** module.

The shared module uses Gradle as the build system just like the rest of the project. You can declare common and platform-specific dependencies using sourcesets. For example, if your app uses Ktor for networking, you need to add an OkHttp dependency for Android and a darwin dependency for iOS. Note that some libraries require only common dependencies and don't need platform-specific dependencies.
    
    
    sourceSets {
       commonMain.dependencies {
           //put your multiplatform dependencies here
           //...
           implementation(libs.ktor.client.core)
           implementation(libs.ktor.client.content.negotiation)
           implementation(libs.ktor.serialization.kotlinx.json)
           //...
       }
       androidMain.dependencies {
           implementation(libs.ktor.client.okhttp)
       }
       iosMain.dependencies {
           implementation(libs.ktor.client.darwin)
       }
    }
    
    

When you add a new library to your app's shared module, make sure to check for the required dependencies for each platform.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-06 UTC."],[],[]] 
