---
url: https://developer.android.com/training/camera/choose-camera-library/
title: Choose a camera library \u00a0|\u00a0 Android media \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:45.091327+00:00
---

# Choose a camera library  |  Android media  |  Android Developers

> Source: https://developer.android.com/training/camera/choose-camera-library/

  * [ Android Developers ](https://developer.android.com/)
  * [ Essentials ](https://developer.android.com/get-started)
  * [ Camera & media dev center ](https://developer.android.com/media)
  * [ Guides ](https://developer.android.com/media/guides)



#  Choose a camera library Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you want to perform basic camera actions like capturing a photo or video using the device's default camera application, see [Camera intents](https://developer.android.com/training/camera/camera-intents).

If you want to add camera functionality to an Android app, you have three main options:

  * [CameraX](https://developer.android.com/media/camera/camerax)
  * [Camera2](https://developer.android.com/media/camera/camera2)
  * [Camera](https://developer.android.com/media/camera/camera-deprecated) (deprecated)



For most developers, [CameraX](https://developer.android.com/training/camerax) is recommended. CameraX is a Jetpack library that supports the vast majority of Android devices (Android 5.0 and higher) and provides a consistent, high-level API designed around common use cases. CameraX resolves device compatibility issues for you so that you don't have to add device-specific code to your app.

CameraX is built on top of the [Camera2](https://developer.android.com/training/camera2) package. If you need low-level camera control to support complex use cases, Camera2 is a good option, but the API is more complex than CameraX. It requires you to manage device-specific configurations. Like CameraX, Camera2 works on Android 5.0 (API level 21) and higher.

The original Android [Camera](https://developer.android.com/training/camera-deprecated) class is deprecated. New apps should use CameraX (recommended) or Camera2, and existing apps should migrate to take advantage of new features and to avoid losing compatibility with future devices.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2024-04-08 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-04-08 UTC."],[],[]] 
