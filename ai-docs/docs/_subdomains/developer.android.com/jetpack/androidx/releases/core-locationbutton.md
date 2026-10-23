---
url: https://developer.android.com/jetpack/androidx/releases/core-locationbutton/
title: Core Locationbutton \u00a0|\u00a0 Jetpack \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:36:17.839616+00:00
---

# Core Locationbutton  |  Jetpack  |  Android Developers

> Source: https://developer.android.com/jetpack/androidx/releases/core-locationbutton/

  * [ Android Developers ](https://developer.android.com/)
  * [ Get started ](https://developer.android.com/get-started/overview)
  * [ Jetpack ](https://developer.android.com/jetpack)
  * [ Libraries ](https://developer.android.com/jetpack/androidx/explorer)



Stay organized with collections  Save and categorize content based on your preferences. 

# Core Locationbutton

API Reference  
[androidx.core.locationbutton](https://developer.android.com/reference/kotlin/androidx/core/locationbutton/package-summary)  


Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release  
---|---|---|---|---  
June 17, 2026 | - | - | - | -  
  
## Declaring dependencies

To add a dependency on core locationbutton, you must add the Google Maven repository to your project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven) for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for your app or module:

### Groovy
    
    
    dependencies {
        implementation "androidx.core.locationbutton:locationbutton:"
        implementation "androidx.core.locationbutton:locationbutton-compose:"
        implementation "androidx.core.locationbutton:locationbutton-testing:"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.core.locationbutton:locationbutton:")
        implementation("androidx.core.locationbutton:locationbutton-compose:")
        implementation("androidx.core.locationbutton:locationbutton-testing:")
    }

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the [existing issues](https://issuetracker.google.com/issues?q=componentid:2162367%20status:open) in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=2162367&template=2342253)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker) for more information.

## Version 1.0

### Version 1.0.0-alpha01

June 17, 2026

`androidx.core.locationbutton:locationbutton:1.0.0-alpha01`, `androidx.core.locationbutton:locationbutton-compose:1.0.0-alpha01`, and `androidx.core.locationbutton:locationbutton-testing:1.0.0-alpha01` are released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/refs/heads/androidx-main/core/locationbutton).

**New Features**

The initial alpha release of AndroidX implementations of `LocationButton` that enable both view and compose based applications to easily request one-time precise location permission. For devices running Android 16 (API 36) or below, the library provides automatic backwards compatibility by defaulting to standard location permission prompts.

**API Changes**

  * Added `LocationButton` View as an entry point for View based applications.
  * Added `LocationButton` composable as an entrypoint for Compose based applications.
  * Added `OnPermissionResultListener`, `OnErrorListener`, and `OnRequestPermissionsListener` for callback handling.
  * Added `TestLocationButtonProvider` to allow apps to test flows relying on the secure `LocationButton`.



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-17 UTC."],[],[]] 
