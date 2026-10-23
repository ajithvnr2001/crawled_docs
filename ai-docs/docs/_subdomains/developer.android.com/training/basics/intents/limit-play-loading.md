---
url: https://developer.android.com/training/basics/intents/limit-play-loading/
title: Limit loading in on-device Android containers \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:08.968359+00:00
---

# Limit loading in on-device Android containers  |  App architecture  |  Android Developers

> Source: https://developer.android.com/training/basics/intents/limit-play-loading/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  Limit loading in on-device Android containers Stay organized with collections  Save and categorize content based on your preferences. 

_On-device Android containers_ are apps that simulate the Android OS on an Android-powered device. This includes both apps that simulate the Android OS in its entirety and apps that only simulate portions of the Android OS.

If you don't want on-device Android container apps to load in or proxy your Play Store app, you can add a string to your app manifest that declares this restriction.

Create a [property](https://developer.android.com/guide/topics/manifest/property-element) under the [`<application>`](https://developer.android.com/guide/topics/manifest/application-element) in your Android manifest with `android:name` set to `REQUIRE_SECURE_ENV` and `android:value` set to 1:
    
    
    <property android:name="REQUIRE_SECURE_ENV" android:value="1" />
    

For this use case, you can use the `REQUIRE_SECURE_ENV` property regardless of the Android version that your app runs on.

On-device Android container apps are [required](https://support.google.com/googleplay/android-developer/answer/9888379) to respect this declaration.

For more information about on-device Android containers, see the [Help Center](https://support.google.com/googleplay/android-developer/answer/13609005).

[ Previous arrow_back  Allow other apps to start your activity  ](https://developer.android.com/training/basics/intents/filters)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-05 UTC."],[],[]] 
