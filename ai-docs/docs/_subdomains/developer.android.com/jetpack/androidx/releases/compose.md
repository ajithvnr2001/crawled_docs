---
url: https://developer.android.com/jetpack/androidx/releases/compose/
title: Compose \u00a0|\u00a0 Jetpack \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:21:29.662201+00:00
---

# Compose  |  Jetpack  |  Android Developers

> Source: https://developer.android.com/jetpack/androidx/releases/compose/

  * [ Android Developers ](https://developer.android.com/)
  * [ Get started ](https://developer.android.com/get-started/overview)
  * [ Jetpack ](https://developer.android.com/jetpack)
  * [ Libraries ](https://developer.android.com/jetpack/androidx/explorer)



Stay organized with collections  Save and categorize content based on your preferences. 

# Compose

[User Guide](https://developer.android.com/jetpack/compose/tutorial) [Code Sample](https://github.com/android/compose-samples)

API Reference  
[androidx.compose](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary)  


Define your UI programmatically with composable functions that describe its shape and data dependencies. 

Compose is combination of 7 Maven Group Ids within `androidx`. Each Group contains a targeted subset of functionality, each with its own set of release notes.

This table explains the groups and links to each set of release notes.

Group| Description  
---|---  
[compose.animation](https://developer.android.com/jetpack/androidx/releases/compose-animation)| Build animations in their Jetpack Compose applications to enrich the user experience.  
[compose.compiler](https://developer.android.com/jetpack/androidx/releases/compose-compiler)| Transform @Composable functions and enable optimizations with a Kotlin compiler plugin.  
[compose.foundation](https://developer.android.com/jetpack/androidx/releases/compose-foundation)| Write Jetpack Compose applications with ready to use building blocks and extend foundation to build your own design system pieces.  
[compose.material](https://developer.android.com/jetpack/androidx/releases/compose-material)| Build Jetpack Compose UIs with ready to use Material Design Components. This is the higher level entry point of Compose, designed to provide components that match those described at www.material.io.  
[compose.material3](https://developer.android.com/jetpack/androidx/releases/compose-material3)| Build Jetpack Compose UIs with Material Design 3 Components, the next evolution of Material Design. Material 3 includes updated theming and components and Material You personalization features like dynamic color, and is designed to be cohesive with the new Android 12 visual style and system UI.  
[compose.runtime](https://developer.android.com/jetpack/androidx/releases/compose-runtime)| Fundamental building blocks of Compose's programming model and state management, and core runtime for the Compose Compiler Plugin to target.  
[compose.ui](https://developer.android.com/jetpack/androidx/releases/compose-ui)| Fundamental components of compose UI needed to interact with the device, including layout, drawing, and input.  
  
## Versions

This table lists the current versions of each group.

Maven Group ID | Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release  
---|---|---|---|---|---  
[compose.animation](https://developer.android.com/jetpack/androidx/releases/compose-animation) | October 07, 2026 | [1.12.1](https://developer.android.com/jetpack/androidx/releases/compose-animation#1.12.1) | - | [1.13.0-beta01](https://developer.android.com/jetpack/androidx/releases/compose-animation#1.13.0-beta01) | -  
[compose.compiler](https://developer.android.com/jetpack/androidx/releases/compose-compiler) | August 7, 2024 | [1.5.15](https://developer.android.com/jetpack/androidx/releases/compose-compiler#1.5.15) | - | - | -  
[compose.foundation](https://developer.android.com/jetpack/androidx/releases/compose-foundation) | October 07, 2026 | [1.12.1](https://developer.android.com/jetpack/androidx/releases/compose-foundation#1.12.1) | - | [1.13.0-beta01](https://developer.android.com/jetpack/androidx/releases/compose-foundation#1.13.0-beta01) | -  
[compose.material](https://developer.android.com/jetpack/androidx/releases/compose-material) | October 07, 2026 | [1.12.1](https://developer.android.com/jetpack/androidx/releases/compose-material#1.12.1) | - | [1.13.0-beta01](https://developer.android.com/jetpack/androidx/releases/compose-material#1.13.0-beta01) | -  
[compose.material3](https://developer.android.com/jetpack/androidx/releases/compose-material3) | October 07, 2026 | [1.4.0](https://developer.android.com/jetpack/androidx/releases/compose-material3#1.4.0) | - | [1.5.0-beta01](https://developer.android.com/jetpack/androidx/releases/compose-material3#1.5.0-beta01) | -  
[compose.runtime](https://developer.android.com/jetpack/androidx/releases/compose-runtime) | October 07, 2026 | [1.12.1](https://developer.android.com/jetpack/androidx/releases/compose-runtime#1.12.1) | - | [1.13.0-beta01](https://developer.android.com/jetpack/androidx/releases/compose-runtime#1.13.0-beta01) | -  
[compose.ui](https://developer.android.com/jetpack/androidx/releases/compose-ui) | October 07, 2026 | [1.12.1](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.12.1) | - | [1.13.0-beta01](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.13.0-beta01) | -  
  
## Declaring dependencies

To add a dependency on Compose, you must add the Google Maven repository to your project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven) for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for your app or module:

### Groovy
    
    
    plugins {
        id 'org.jetbrains.kotlin.plugin.compose'
    }
    
    android {
        buildFeatures {
            compose true
        }
    
        kotlinOptions {
            jvmTarget = "1.8"
        }
    }

### Kotlin
    
    
    plugins {
        kotlin("plugin.compose")
    }
    
    android {
        buildFeatures {
            compose = true
        }
    
        kotlinOptions {
            jvmTarget = "1.8"
        }
    }

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the [existing issues](https://issuetracker.google.com/issues?q=componentid:610764%20status:open) in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=610764&template=1424126)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker) for more information.

## BOMs

For the latest BOM releases, visit [Compose BOM Mapping Page](https://developer.android.com/jetpack/compose/bom/bom-mapping).

## Announcements

Date | Announcement  
---|---  
August 13, 2025 |  The August 2025 Compose Bill of Materials (BOM) has been released, which includes the stable version of Jetpack Compose 1.9! This update for Android's modern UI toolkit introduces several new features, such as advanced shadows, 2D scrolling APIs, and better list performance. If you'd like to learn more about all the new features and improvements, check out the [full blog post!](https://android-developers.googleblog.com/2025/08/whats-new-in-jetpack-compose-august-25-release.html)  
April 23, 2025 |  The Compose 1.8 release is here! This release for Android's modern UI toolkit brings new features like autofill, several text improvements, and visibility tracking. You can also animate a composable's size and location in new ways. We've also stabilized many experimental APIs and fixed a number of bugs. To learn more about all the new features and improvements in this release, check out the full [blog post!](https://android-developers.googleblog.com/2025/04/whats-new-in-jetpack-compose-april-25.html)  
September 4, 2024 |  The 1.7 Jetpack Compose release includes many features to make Android development faster and easier, regardless of the form factor you're building for. [We also shared news ](https://android-developers.googleblog.com/2024/05/whats-new-in-jetpack-compose-at-io-24.html) on expanded Compose support across the Android ecosystem.   
January 24, 2024 |  [Jetpack Compose 1.6](https://android-developers.googleblog.com/2024/01/whats-new-in-jetpack-compose-january-24-release.html) is now stable as part of the Compose January '24 Bill of Materials! This release largely focuses on performance improvements, as we continue to migrate modifiers and improve the efficiency of major parts of our API.  
June 26, 2023 |  Since Compose 1.5.0-beta01 release, Compose aar are located under `*-android` artifacts. With 1.6.0-alpha01, Compose POM files have been updated to point to the `-android` artifact by default for dependency resolution in build systems that don't support Gradle Module Metadata.   
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 

  * [ ![X](https://developer.android.com/_static/android/images/logo-x.svg) X  ](https://x.com/AndroidDev)

Follow @AndroidDev on X

  * [ ![YouTube](https://www.gstatic.com/images/icons/material/product/2x/youtube_48dp.png) YouTube  ](https://www.youtube.com/user/androiddevelopers)

Check out Android Developers on YouTube

  * [ ![LinkedIn](https://developer.android.com/_static/android/images/logo-linkedin.svg) LinkedIn  ](https://www.linkedin.com/showcase/androiddev)

Connect with the Android Developers community on LinkedIn




  * ### More Android

    * [ Android ](https://www.android.com)
    * [ Android for Enterprise ](https://www.android.com/enterprise/)
    * [ Security ](https://www.android.com/security-center/)
    * [ Source ](https://source.android.com)
    * [ News ](https://developer.android.com/news)
    * [ Blog ](https://android-developers.googleblog.com/)
    * [ Podcasts ](https://developer.android.com/podcasts)
  * ### Discover

    * [ Gaming ](https://developer.android.com/games)
    * [ Machine Learning ](https://developer.android.com/ml)
    * [ Health & Fitness ](https://developer.android.com/health-and-fitness)
    * [ Camera & Media ](https://developer.android.com/media)
    * [ Privacy ](https://developer.android.com/privacy)
    * [ 5G ](https://developer.android.com/training/connectivity/5g)
  * ### Android Devices

    * [ Large screens ](https://developer.android.com/large-screens)
    * [ Wear OS ](https://developer.android.com/wear)
    * [ ChromeOS devices ](https://developer.android.com/chrome-os)
    * [ Android for cars ](https://developer.android.com/cars)
    * [ Android TV ](https://developer.android.com/tv)
  * ### Releases

    * [ Android 17 ](https://developer.android.com/about/versions/17)
    * [ Android 16 ](https://developer.android.com/about/versions/16)
    * [ Android 15 ](https://developer.android.com/about/versions/15)
    * [ Android 14 ](https://developer.android.com/about/versions/14)
    * [ Android 13 ](https://developer.android.com/about/versions/13)
    * [ Android 12 ](https://developer.android.com/about/versions/12)
    * [ Android 11 ](https://developer.android.com/about/versions/11)
  * ### Documentation and Downloads

    * [ Android Studio guide ](https://developer.android.com/studio/intro)
    * [ Developers guides ](https://developer.android.com/guide)
    * [ API reference ](https://developer.android.com/reference)
    * [ Download Studio ](https://developer.android.com/studio)
    * [ Android NDK ](https://developer.android.com/ndk)
  * ### Support

    * [ Report platform bug ](https://issuetracker.google.com/issues/new?component=190923&template=841312)
    * [ Report documentation bug ](https://issuetracker.google.com/issues/new?component=192697)
    * [ Google Play support ](https://support.google.com/googleplay/android-developer)
    * [ Join research studies ](https://g.co/userresearch/androiddeveloperfooter)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/android/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com)
  * [ Chrome ](https://developer.chrome.com/home)
  * [ Firebase ](https://firebase.google.com)
  * [ Google Cloud Platform ](https://cloud.google.com)
  * [ All products ](https://developers.google.com/products/)



  * [ Privacy ](https://policies.google.com/privacy)
  * [ License ](https://developer.android.com/license)
  * [ Brand guidelines ](https://developer.android.com/distribute/marketing-tools/brand-guidelines)
  * Manage cookies 
  * Get news and tips by email [ Subscribe ](https://developer.android.com/updates)



  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Polski
  * Português – Brasil
  * Tiếng Việt
  * Türkçe
  * Русский
  * עברית
  * العربيّة
  * فارسی
  * हिंदी
  * বাংলা
  * ภาษาไทย
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


