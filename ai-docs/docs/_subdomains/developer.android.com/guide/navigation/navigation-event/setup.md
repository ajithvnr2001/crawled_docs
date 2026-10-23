---
url: https://developer.android.com/guide/navigation/navigation-event/setup/
title: Set up development environment for Navigation Event \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:47.910182+00:00
---

# Set up development environment for Navigation Event  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/navigation/navigation-event/setup/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  Set up development environment for Navigation Event Stay organized with collections  Save and categorize content based on your preferences. 

To set up your development environment for `NavigationEvent`, follow these steps.

## Declare dependencies

  1. Add the `navigationevent` artifact to your project. This is the core library containing the shared `NavigationEventDispatcher` and `NavigationEventHandler` classes.

For Jetpack Compose integration, you also need to add the corresponding Compose artifact:
         
         [versions]
         navigationevent = "1.0.0"
         
         [libraries]
         # NavigationEvent libraries
         androidx-navigationevent = { module = "androidx.navigationevent:navigationevent", version.ref = "navigationevent" }
         androidx-navigationevent-compose = { module = "androidx.navigationevent:navigationevent-compose", version.ref = "navigationevent" }
         

  2. Update your compile SDK to 36 or above:
         
         [versions]
         compileSdk = "36"
         

  3. Add the following to your app build file, `app/build.gradle.kts`:
         
         dependencies {
           ...
           implementation(libs.androidx.navigationevent)
           implementation(libs.androidx.navigationevent.compose)
         }
         




[ Previous arrow_back  Overview  ](https://developer.android.com/guide/navigation/navigation-event)

[ Next Handle back gestures and animations  arrow_forward  ](https://developer.android.com/guide/navigation/navigation-event/handle-back)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
