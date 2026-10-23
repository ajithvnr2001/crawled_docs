---
url: https://developer.android.com/build/sdk-upgrade-assistant/
title: Use the Android SDK Upgrade Assistant \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:45:22.709511+00:00
---

# Use the Android SDK Upgrade Assistant  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/build/sdk-upgrade-assistant/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ Gradle build guides ](https://developer.android.com/build/gradle-build-overview)



#  Use the Android SDK Upgrade Assistant Stay organized with collections  Save and categorize content based on your preferences. 

The Android SDK Upgrade Assistant is a tool in Android Studio that helps you upgrade the [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target), or the API level that your app targets. It's important to keep your `targetSdkVersion` up to date so you can use the platform's latest features. The Android SDK Upgrade Assistant is available in Android Studio Giraffe and higher.

**Important:** Starting August 31, 2023, all apps must target Android 13 (API level 33) or higher to be submitted to Google Play for review and remain discoverable for all Google Play users. Configuring your app to target a recent API level ensures that users benefit from security and performance improvements while your app can still run on lower Android versions (down to the specified `minSdkVersion`). To learn more, see the [Google Play target API level requirement](https://developer.android.com/google/play/requirements/target-sdk).

The Android SDK Upgrade Assistant helps you save time and effort when updating the `targetSdkVersion`:

  * For each migration step, it highlights the major breaking changes and how to address them.
  * It tries to filter the full list of changes to only show steps relevant to your app. It'll show a step if it's not certain though, so you might still see steps that you can skip.

**Note:** If you need to reset the step filters, close and reopen your project or restart the Studio IDE. The SDK Upgrade Assistant filters the migration steps once at the beginning of each project session, so you might want to reset the step filters if you've checked out another version of your project for which previously hidden steps apply. 
  * For some changes, it pinpoints where exactly in your code the changes need to be made.



To open the Android SDK Upgrade Assistant, go to **Tools > Android SDK Upgrade Assistant**. In the **Assistant** panel, select the API level that you want to upgrade to for guidance. For the best experience, you should upgrade `targetSdkVersion` values one level at a time.

![Android SDK Upgrade Assistant](https://developer.android.com/static/studio/images/sdk-upgrade-assistant.png)

## Report bugs

To help us create the best experience for you, please submit feedback and bugs using the [issue tracker](https://issuetracker.google.com/issues/new?component=1267157&template=1750462).

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-26 UTC."],[],[]] 
