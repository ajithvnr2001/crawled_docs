---
url: https://developer.android.com/jetpack/androidx/releases/glance-adaptive/
title: Glance Adaptive \u00a0|\u00a0 Jetpack \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:36:25.277608+00:00
---

# Glance Adaptive  |  Jetpack  |  Android Developers

> Source: https://developer.android.com/jetpack/androidx/releases/glance-adaptive/

  * [ Android Developers ](https://developer.android.com/)
  * [ Get started ](https://developer.android.com/get-started/overview)
  * [ Jetpack ](https://developer.android.com/jetpack)
  * [ Libraries ](https://developer.android.com/jetpack/androidx/explorer)



Stay organized with collections  Save and categorize content based on your preferences. 

# Glance Adaptive

API Reference  
[androidx.glance.adaptive](https://developer.android.com/reference/kotlin/androidx/glance/adaptive/package-summary)  


TODO 

Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release  
---|---|---|---|---  
September 23, 2026 | - | - | - | [1.0.0-alpha03](https://developer.android.com/jetpack/androidx/releases/glance_adaptive#1.0.0-alpha03)  
  
## Declaring dependencies

To add a dependency on glance adaptive, you must add the Google Maven repository to your project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven) for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for your app or module:

<!DOCTYPE html>

glance adaptive deps

### Groovy
    
    
    dependencies {
        implementation "androidx.glance.adaptive:adaptive-appwidget:1.0.0-alpha03"
        implementation "androidx.glance.adaptive:adaptive-core:1.0.0-alpha03"
        implementation "androidx.glance.adaptive:adaptive-wear:1.0.0-alpha03"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.glance.adaptive:adaptive-appwidget:1.0.0-alpha03")
        implementation("androidx.glance.adaptive:adaptive-core:1.0.0-alpha03")
        implementation("androidx.glance.adaptive:adaptive-wear:1.0.0-alpha03")
    }

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the [existing issues](https://issuetracker.google.com/issues?q=componentid:TODO%20status:open) in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=TODO&template=TODO)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker) for more information.

## Version 1.0

### Version 1.0.0-alpha03

September 23, 2026

`androidx.glance.adaptive:adaptive-appwidget:1.0.0-alpha03`, `androidx.glance.adaptive:adaptive-core:1.0.0-alpha03`, and `androidx.glance.adaptive:adaptive-wear:1.0.0-alpha03` are released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e4bd62f853853bf3522ed15681c58ef28b09ed44..b2b5ae7b0fe1bb4eece7018878fe5f18c5967a2f/glance/adaptive).

Internal development to enable building template-first `RemoteCompose` Widgets for multiple surfaces across Android ecosystem. Public APIs to come.

### Version 1.0.0-alpha02

September 09, 2026

`androidx.glance.adaptive:adaptive-appwidget:1.0.0-alpha02`, `androidx.glance.adaptive:adaptive-core:1.0.0-alpha02`, and `androidx.glance.adaptive:adaptive-wear:1.0.0-alpha02` are released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f3ed195f0c9ef9eafe437351d974c9ec49ecc2ea..e4bd62f853853bf3522ed15681c58ef28b09ed44/glance/adaptive).

**Bug Fixes**

  * `compileSdk` for Compose libraries updated to 37.1. This will require transitively updating `compileSdk` for all apps and libraries using Compose. ([I05b0f](https://android-review.googlesource.com/#/q/I05b0f9385d2b99ddcc4041b2ce2d96aea3bd391e))



#### Version 1.0.0-alpha01

August 26, 2026

`androidx.glance.adaptive:adaptive-appwidget:1.0.0-alpha01`, `androidx.glance.adaptive:adaptive-core:1.0.0-alpha01`, and `androidx.glance.adaptive:adaptive-wear:1.0.0-alpha01` are released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f3ed195f0c9ef9eafe437351d974c9ec49ecc2ea/glance/adaptive).

This is the initial release of the Glance Adaptive library - the library for building template-first `RemoteCompose` Widgets for multiple form factors and surfaces across Android ecosystem.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-23 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-23 UTC."],[],[]] 
