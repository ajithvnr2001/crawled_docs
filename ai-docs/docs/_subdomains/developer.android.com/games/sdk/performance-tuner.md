---
url: https://developer.android.com/games/sdk/performance-tuner/
title: Android Performance Tuner (APT) \u00a0|\u00a0 Android game development \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:24.937599+00:00
---

# Android Performance Tuner (APT)  |  Android game development  |  Android Developers

> Source: https://developer.android.com/games/sdk/performance-tuner/

  * [ Android Developers ](https://developer.android.com/)
  * [ Google Play ](https://developer.android.com/distribute)
  * [ Games dev center ](https://developer.android.com/games)
  * [ Guides ](https://developer.android.com/games/guides)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Android Performance Tuner (APT) Part of [Android Game Development Kit](https://developer.android.com/games/agdk/overview).

Android Performance Tuner (APT) enables you to deliver the best possible experience to each of your users by helping you to measure and optimize frame rates, graphical fidelity, loading time and loading abandonment across many Android devices at scale.

It helps you identify performance issues in your game or app, and also highlights opportunities to improve your fidelity. Impact metrics help you to prioritize, and issues are categorized to help you take action. Information at both device model and device spec level enables you to find the most effective way to act.

[Get started for native games](https://developer.android.com/games/sdk/performance-tuner/custom-engine) [Get started for Unity games](https://developer.android.com/games/sdk/performance-tuner/unity)

* * *

## What are the benefits?

Android Performance Tuner (APT) helps you deliver a high-quality experience to more users.

### New! Understand your loading times and their impact on abandonment

APT tracks both your loading time and loading abandonment across multiple types of loading (first loads, cold loads, warm loads and interlevel loads). It shows you the impact that longer loading times has on abandonment for your game, so that you can determine the optimal loading time.

### Measure the quality of your user experience

APT shows you the frame rate and loading time performance of your game on actual user devices in the real world, so you get direct insight into their experience. All metrics are customized to your targets, so you can understand how the game is performing relative to your specific goals.

### Diagnose and prioritise your game performance issues

Frame rate and loading time issues are broken out by your quality levels and your in-game annotations, as well as device model, to help you narrow down the root cause. For each frame rate issue, you can see GPU time as well as CPU time, so you can assess what type of optimization may be needed. The number of affected sessions is also shown, so you can understand what’s affecting your users most, and decide what devices or game scenes to focus on first.

### Get the best out of every device

As well as surfacing performance rate issues, APT highlights opportunities for you to improve your user experience by increasing fidelity on devices which already perform well but that have room to go further. This enables you to ensure that every user gets the best possible experience of your game.

## How does it work?

Android Performance Tuner works with Android vitals.

  * Android Performance Tuner records and aggregates live frame time and loading information from your game or app, alongside game annotations and fidelity parameters that you provide.
  * When you publish a version of your game or app with Android Performance Tuner, this performance data is uploaded to Google Play and unlocks new performance insights in Android vitals.



To get these performance insights, you must integrate Android Performance Tuner into your game or app and then publish it on Google Play:

![](https://developer.android.com/static/images/games/performance-tuner/performance-tuner-integration-paths.png)

## Requirements

For devices:

Android Performance Tuner (APT) works on any Android device (with or without Google Play services) running Android 4.1 (API level 16) or later. This is over 99% of all active Android devices.

For all developers:

  * Access to Android vitals
  * Product only available in the new Google Play Console



Additional requirements for Unity developers:

  * Unity version 2017.4 or later and [.NET version 4.6](https://dotnet.microsoft.com/download/dotnet-framework/net46)
  * To use APK Expansion files, Unity 2018.2 is required
  * For improved frame pacing and GPU measurements, Unity version 2019.3.14 or later is required
  * For Addressables scenes support, Unity 2019.3 or later and [Addressables package 1.19.4](https://docs.unity3d.com/Packages/com.unity.addressables@0.8/manual/index.html) or later are required.



## Learn about Android Performance Tuner

We have codelabs to walk you through integrating Android Performance Tuner into your game for both C/C++ and Unity Engine integrations:

  * [Codelab: Integrating Android Performance Tuner into your C/C++ Android game](https://codelabs.developers.google.com/codelabs/android-performance-tuner-native/)
  * [Codelab: Integrating Android Performance Tuner into your Unity game](https://codelabs.developers.google.com/codelabs/android-performance-tuner-unity/)



References for the C/C++ and Unity Engine SDKs:

  * [Android Performance Tuner C/C++ reference](https://developer.android.com/games/sdk/reference/performance-tuner/custom-engine)
  * [Android Performance Tuner Unity reference](https://developer.android.com/games/sdk/reference/performance-tuner/unity)



## Additional resources

Send feedback 

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-26 UTC."],[],[]] 
