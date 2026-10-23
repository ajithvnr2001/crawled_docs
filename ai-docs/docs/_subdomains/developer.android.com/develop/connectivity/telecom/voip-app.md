---
url: https://developer.android.com/develop/connectivity/telecom/voip-app/
title: Build a calling app \u00a0|\u00a0 Connectivity \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:19.248907+00:00
---

# Build a calling app  |  Connectivity  |  Android Developers

> Source: https://developer.android.com/develop/connectivity/telecom/voip-app/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ Connectivity ](https://developer.android.com/develop/connectivity)
  * [ Guides ](https://developer.android.com/develop/connectivity/overview)



#  Build a calling app Stay organized with collections  Save and categorize content based on your preferences. 

Use the Telecom Jetpack library to offer high-quality video and audio experiences to your users. With the Telecom framework, you get call and notification management, foreground support, and more. The Jetpack library adds support for:

  * Call streaming and transfer
  * Android Auto and Wear OS integration
  * [System call log integration (unified call history)](https://developer.android.com/develop/connectivity/telecom/call-log-integration)
  * Backward compatibility



For more information about how to build a calling app with the Telecom library, see [Core-Telecom](https://developer.android.com/develop/connectivity/telecom/voip-app/telecom).

## Supported telecom devices

On Android 5.0 (API level 21) and higher, most phones support the Telecom framework, and they must do so for SIM-based phone calls to work. For devices like tablets, which don't traditionally require a Telephony implementation, Android 14 (API level 34) introduces requirements that mandate a proper Telecom framework implementation for tablets that support VoIP.

Use `PackageManager` to see if the device supports Telecom:
    
    
    packagemanager.hasSystemFeature(PackageManager.FEATURE_TELECOM)
    

**Note:** Non-Telecom based devices don't support other platforms such as Wear OS.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
