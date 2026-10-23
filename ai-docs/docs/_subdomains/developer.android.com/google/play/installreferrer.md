---
url: https://developer.android.com/google/play/installreferrer/
title: Google Play Install Referrer \u00a0|\u00a0 Other Play guides \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:21:34.349253+00:00
---

# Google Play Install Referrer  |  Other Play guides  |  Android Developers

> Source: https://developer.android.com/google/play/installreferrer/

  * [ Android Developers ](https://developer.android.com/)
  * [ Google Play ](https://developer.android.com/distribute)
  * [ Other Play guides ](https://developer.android.com/guide/app-bundle)



#  Google Play Install Referrer Stay organized with collections  Save and categorize content based on your preferences. 

You can use the Google Play Store's Install Referrer API to securely retrieve referral content from Google Play, such as:

  * The referrer URL of the installed package.
  * The timestamp, in seconds, of when a referrer click happened (both client- and server-side).
  * The timestamp, in seconds, of when an installation began (both client- and server-side).
  * The app's version at the time when the app was first installed.
  * Whether the user has interacted with your app's [instant experience](https://developer.android.com/topic/google-play-instant/overview) in the past 7 days.



## Requirements

The Install Referrer API is exposed by the Google Play Store app on a device. Devices with a Google Play app version of 8.3.73 or later automatically have access to the API.

You must also have a Google Play Console account to use the Install Referrer API.

## Using the API

The Install Referrer API is implemented as an [Android Interface Definition Language (AIDL)](https://developer.android.com/guide/components/aidl) interface.

  * If you are using the Kotlin programming language or the Java programming language, use the [Play Install Referrer Client Library](https://developer.android.com/google/play/installreferrer/library) to simplify your coding.
  * If you are using another programming language, use the [Play Install Referrer API](https://developer.android.com/google/play/installreferrer/igetinstallreferrerservice). 



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
