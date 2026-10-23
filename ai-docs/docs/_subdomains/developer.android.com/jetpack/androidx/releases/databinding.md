---
url: https://developer.android.com/jetpack/androidx/releases/databinding/
title: Databinding \u00a0|\u00a0 Jetpack \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:36:20.318303+00:00
---

# Databinding  |  Jetpack  |  Android Developers

> Source: https://developer.android.com/jetpack/androidx/releases/databinding/

  * [ Android Developers ](https://developer.android.com/)
  * [ Get started ](https://developer.android.com/get-started/overview)
  * [ Jetpack ](https://developer.android.com/jetpack)
  * [ Libraries ](https://developer.android.com/jetpack/androidx/explorer)



Stay organized with collections  Save and categorize content based on your preferences. 

# Databinding

[User Guide](https://developer.android.com/topic/libraries/data-binding) [Code Sample](https://github.com/android/databinding-samples) [Codelab](https://codelabs.developers.google.com/codelabs/android-databinding)

API Reference  
[android.databinding](https://developer.android.com/reference/android/databinding/package-summary)  


Bind UI components in your layouts to data sources in your app using a declarative format. 

**Caution:** This library is in maintenance mode and will only receive critical fixes; new features are not planned. We recommend using [Jetpack Compose](https://developer.android.com/jetpack/compose) for building Android UIs. See [Compose-first](https://developer.android.com/develop/ui/compose/first) for more information.Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release  
---|---|---|---|---  
September 5, 2019 | [3.5.0](https://developer.android.com/jetpack/androidx/releases/databinding#3.5.0) | - | - | [3.6.0-alpha10](https://developer.android.com/jetpack/androidx/releases/databinding#3.6.0-alpha10)  
  
The databinding library is bundled with [the Android Gradle plugin](https://developer.android.com/studio/releases/gradle-plugin). You do not need to declare a dependency on the library, but you must enable it.

To enable data binding, set the `dataBinding` build option to `true` in your module's `build.gradle` file, as shown below:
    
    
    android {
        ...
        buildFeatures {
            dataBinding true
        }
    }
    

**Note:** You must enable data binding for all modules that depend on libraries that use data binding, even if the module doesn't directly use data binding.

For more information about data binding, see the guide to the [data binding library](https://developer.android.com/topic/libraries/data-binding), and the Android Studio [release notes](https://developer.android.com/studio/releases)

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the [existing issues](https://issuetracker.google.com/issues?q=componentid:192721%20status:open) in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=192721&template=1096850)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker) for more information.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-19 UTC."],[],[]] 
