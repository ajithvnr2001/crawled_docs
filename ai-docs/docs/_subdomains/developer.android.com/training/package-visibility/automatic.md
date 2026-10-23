---
url: https://developer.android.com/training/package-visibility/automatic/
title: Know which packages are visible automatically \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:09.542333+00:00
---

# Know which packages are visible automatically  |  App architecture  |  Android Developers

> Source: https://developer.android.com/training/package-visibility/automatic/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  Know which packages are visible automatically Stay organized with collections  Save and categorize content based on your preferences. 

The system automatically makes some apps visible so that your app can interact with them without needing to declare the [`<queries>`](https://developer.android.com/guide/topics/manifest/queries-element) element. This behavior helps support basic functionality and common use cases.

**Note:** You can start another app's activity using either an [implicit](https://developer.android.com/guide/components/intents-filters#ExampleSend) or [explicit](https://developer.android.com/guide/components/intents-filters#ExampleExplicit) intent regardless of whether that app is visible to your app. Also, if your app targets Android 10 (API level 29) or lower, **all** apps are visible to your app automatically.

## Types of apps that are visible automatically

The following types of apps are always visible to your app, even when your app targets Android 11 (API level 30) or higher:

  * Your own app.
  * Certain system packages, such as the media provider, that implement core Android functionality.
  * The app that installed your app.
  * Any app that launches an activity in your app using the [`startActivityForResult()`](https://developer.android.com/reference/kotlin/android/app/Activity#startactivityforresult) method, as described in the guide about [getting a result from an activity](https://developer.android.com/training/basics/intents/result).
  * Any app that starts or binds to a [service](https://developer.android.com/guide/components/services) in your app.
  * Any app that accesses a [content provider](https://developer.android.com/guide/topics/providers/content-providers) in your app.
  * Any app that has a content provider that your app has been [granted URI permissions](https://developer.android.com/guide/topics/providers/content-provider-basics#getting-access-with-temporary-permissions) to access.
  * Any app that receives input from your app. This case applies only when your app provides input as an [input method editor](https://developer.android.com/guide/topics/text/creating-input-method).



## System packages that are visible automatically

Some system packages that implement core Android functionality are automatically visible to your app, even when your app targets Android 11 or higher. The specific set of packages depends on the device that runs your app.

To view the full list of packages for a specific device, run the following command in a terminal on your development machine:
    
    
    adb shell dumpsys package queries
    

In the command output, find the `forceQueryable` section. This section includes the list of packages that the device has made visible to your app automatically.

[ Previous arrow_back  About package visibility  ](https://developer.android.com/training/package-visibility)

[ Next Declare package visibility needs  arrow_forward  ](https://developer.android.com/training/package-visibility/declaring)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
