---
url: https://developer.android.com/training/package-visibility/testing/
title: Test package visibility behavior \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:10.728170+00:00
---

# Test package visibility behavior  |  App architecture  |  Android Developers

> Source: https://developer.android.com/training/package-visibility/testing/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  Test package visibility behavior Stay organized with collections  Save and categorize content based on your preferences. 

If your app relies on interactions with other apps to complete its use cases, it's useful to test how [package visibility](https://developer.android.com/training/package-visibility) changes in Android 11 (API level 30) and higher affect your app.

This guide also gives some suggestions on how to test the behavior changes and helps you configure log messages to determine at a more granular level how your app might be affected.

## Test the behavior changes

To test whether this behavior change affects your app, complete the following steps:

  1. Install [Android Studio 3.6.1](https://developer.android.com/studio) or higher.
  2. Install the latest version of Gradle that Android Studio supports.
  3. Set your app's `targetSdkVersion` to `30` or higher.
  4. Don't include the `<queries>` element in your app's manifest file.
  5. Call [`getInstalledApplications()`](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledApplications\(int\)) or [`getInstalledPackages()`](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledPackages\(int\)). Both methods return a filtered list when they are successful.
  6. See which features of your app aren't working.
  7. Introduce appropriate [`<queries>`](https://developer.android.com/guide/topics/manifest/queries-element) entries to fix those features.



## Configure log messages for package filtering

To discover more details about how the default visibility of apps affects your app, you can enable log messages for package filtering. If you're developing a test app or debuggable app in Android Studio, the [system log provides this capability](https://developer.android.com/studio/debug#systemLog) for you. Otherwise, you can run the following command in a terminal window to enable it manually:
    
    
    adb shell pm log-visibility --enable PACKAGE_NAME
    

Then, whenever packages are filtered out of a `PackageManager` object's return values, you see a message similar to the following in Logcat:
    
    
    I/AppsFilter: interaction: PackageSetting{7654321 \
      com.example.myapp/12345} -> PackageSetting{...} BLOCKED
    

**Caution:** Your app's performance is affected when this flag is enabled. Unless you're testing how package visibility affects your app, disable the logging of messages related to package visibility.

[ Previous arrow_back  Fulfill common use cases  ](https://developer.android.com/training/package-visibility/use-cases)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
