---
url: https://developer.android.com/training/wearables/versions/7/changes/
title: Test how your app handles behavior changes \u00a0|\u00a0 Wear OS 7 \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:38.901001+00:00
---

# Test how your app handles behavior changes  |  Wear OS 7  |  Android Developers

> Source: https://developer.android.com/training/wearables/versions/7/changes/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS 7 ](https://developer.android.com/training/wearables/versions/7)



#  Test how your app handles behavior changes Stay organized with collections  Save and categorize content based on your preferences. 

Wear OS 7 is based on Android 17 (API level 37). When you prepare your Wear OS app for use on Wear OS 7, handle the system [behavior changes that affect all apps in Android 17](https://developer.android.com/about/versions/17/behavior-changes-all), as well as the [changes for apps that target Android 17](https://developer.android.com/about/versions/17/behavior-changes-17).

Unless otherwise specified, the changes affect all apps that run on Wear OS 7 or higher, regardless of target SDK version.

**Caution:** Before you upload your app to the Play Store, [target Android 17](https://developer.android.com/training/wearables/versions/7/setup#update-target-sdk) and [configure an emulator](https://developer.android.com/training/wearables/get-started/creating#configure-emulator) to test your app.

The following underlying platform changes warrant particular focus when targeting Wear OS 7:

## Background audio hardening

To ensure background audio interactions are started intentionally by the user, Android 17 enforces restrictions on audio playback and focus requests. Apps interacting with audio while in the background must run a foreground service that is not of type [`SHORT_SERVICE`](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_SHORT_SERVICE). For apps targeting Android 17 (API level 37), this foreground service must typically possess **while-in-use (WIU)** capabilities.

For comprehensive details and mitigation strategies, see the guide on [Background audio hardening](https://developer.android.com/about/versions/17/changes/bg-audio).

## Local network access permissions

Apps targeting Android 17 must declare the `ACCESS_LOCAL_NETWORK` runtime permission to interact with devices on a local area network (LAN). This affects Wear OS apps that communicate directly with smart home devices or casting receivers over Wifi.

For more information, see the [Local network permission](https://developer.android.com/privacy-and-security/local-network-permission) documentation.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-19 UTC."],[],[]] 
