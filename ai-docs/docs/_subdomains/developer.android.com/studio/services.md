---
url: https://developer.android.com/studio/services/
title: Service integrations in Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:44:31.090017+00:00
---

# Service integrations in Android Studio  |  Android Developers

> Source: https://developer.android.com/studio/services/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ IDE guides ](https://developer.android.com/studio/intro)



#  Service integrations in Android Studio Stay organized with collections  Save and categorize content based on your preferences. 

Android Studio offers a set of service integrations to increase your productivity as you develop, release, and maintain Android apps. For example, you have access to Cloud services such as Firebase Device Streaming, Firebase Crashlytics, Play Vitals data, and Gemini in Android Studio.

**Note:** Service integrations are only available in the latest stable channel version of Android Studio and major versions (including their patches) released in the previous 10 months. Currently, the oldest supported version is **Panda 1**. If you are using an older version of Android Studio, you will need to update to access Cloud services. For more information, see [Android Studio and Cloud services compatibility](https://developer.android.com/studio/releases#service-compat).

## Admin controls

As an admin, you have the ability to control the Cloud services available to users in your organization. For some Cloud services, this can be done through the [Google Admin Console](https://support.google.com/a/answer/55955?ref_topic=2413312&sjid=9410998059586788964-EU):

  * [Google Cloud](https://support.google.com/a/answer/9197205?sjid=15762865756081758884-EU): If disabled, it would prevent developers in your organization from using services such as Firebase Device Streaming, Firebase Crashlytics, or Gemini Enterprise.



Additionally, you can limit access to Cloud services through permissions. For example, you can limit which developers can access Play Vitals data through [developer account permissions](https://support.google.com/googleplay/android-developer/answer/9844686). Similarly, you can also configure [Google Cloud permissions](https://cloud.google.com/iam/docs/understanding-roles) to limit access to Cloud services and data in Google Cloud and Firebase projects.

## Work account limitations

If you are using Android Studio with a work account, your organization's admin determines what Cloud services and permissions you have access to. Contact your admin to request access to Cloud services.

## Service permissions

When you enable specific cloud service integrations within Android Studio, certain permissions are granted to the IDE to deliver new functionality.

The following table describes the permissions that Android Studio will have when specific cloud services are enabled.

Cloud service integration | Permissions   
---|---  
Android Vitals (Google Play)  | Access metrics and data about your apps in your Google Play Developer account.  
Gemini in Android Studio  | Manage your Google Cloud data.  
  
Submit data to Google for AI-based developer assistance.  
Firebase Device Streaming & Crashlytics  | Manage your Google Cloud data.  
  
Manage all your Firebase data and settings.  
Backup & Sync  | Manage Android Studio configuration data in your Google Drive.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
