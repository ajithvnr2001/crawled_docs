---
url: https://developer.android.com/training/wearables/watch-face-push/phone-app/
title: Configure your phone app for Watch Face Push \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:38.291742+00:00
---

# Configure your phone app for Watch Face Push  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/watch-face-push/phone-app/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Configure your phone app for Watch Face Push Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The Watch Face Push library is meant for watch face developers who prefer to publish to their own marketplace stores.  
  
If you publish your watch faces to Google Play, use a tool that supports a less complex publishing process, such as [Watch Face Designer](https://developer.android.com/training/wearables/watch-face-designer/publish) or [Watch Face Studio](https://developer.samsung.com/watch-face-studio/user-guide/build.html).

For the canonical marketplace, the phone app is the predominant way in which the user interacts with the app.

## Set a watch face

When the user selects a watch face in the phone app, there are two parts to the subsequent flow to set the watch face:

  1. **Installation:** Install the watch face using Watch Face Push, initiated through `MessageClient`. This step is straightforward, using either `addWatchFace` or `updateWatchFace`, triggered using `MessageClient` from the phone to the watch.
  2. **Activation:** [Set the installed watch face as active](https://developer.android.com/training/wearables/watch-face-push/wear-os-app#set-watch-face-as-active). This step has several possible paths, depending on the permission state: 
     * There may be **no action needed**. The marketplace may already have control of the active watch face.
     * There may be **no user intervention needed**. The app has the necessary permissions to set the active watch face, and can do so directly using `setWatchFaceAsActive()`.
     * There may be **guidance needed** , either as to how to accept permission requests, or how to manually set the watch face using a long-press gesture or through a companion app.



## Installation response

To facilitate the **Activation** phase, the **Installation** phase should return the following information from the watch to the phone:

  * The outcome of the installation attempt
  * The result of `isWatchFaceActive()` \- to determine whether the app already has the active watch face.
  * Whether `setWatchFaceAsActive()` has already been called in the past - the Wear OS app should track and persist this information locally. _This API call can only be used once._



## Activation

Following the installation, the response may indicate that the app already has the active watch face. However if it does not, then the app may choose to show a button to **set watch face as active**.

### Scenario 1: All attempts to set the active watch face are exhausted

If the response from installation indicated that `setWatchFaceAsActive()` had already been called in the past, then the button should lead to an education screen on the phone, showing the user how to touch & hold on the watch face to manually set it to the one they want.

### Scenario 2 - Try to set the active watch face

The phone should instruct the watch to check for the necessary `SET_PUSHED_WATCH_FACE_AS_ACTIVE` permission:

  * If the user has **already granted it** , proceed to calling setWatchFaceAsActive().
  * If the user has **previously denied the permission** , the watch should communicate this back to the phone, where an education screen can be shown explaining the need for the permission and how to manually grant it.
  * If the **permission has not been requested before** , the watch should instruct the phone to show an educational moment guiding the user on how to accept permissions on the watch, and the watch should proceed to request the permission.

    * If the user grants the permission, the watch should then call `setWatchFaceAsActive()`.
    * Otherwise the watch should instruct the phone to show an education screen explaining the need for the permission and how to manually grant it.



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-05 UTC."],[],[]] 
