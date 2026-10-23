---
url: https://developer.android.com/work/versions/android-14/
title: What's new for enterprise in Android 14 \u00a0|\u00a0 Android Enterprise \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:35:59.045911+00:00
---

# What's new for enterprise in Android 14  |  Android Enterprise  |  Android Developers

> Source: https://developer.android.com/work/versions/android-14/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Enterprise ](https://developer.android.com/work)



#  What's new for enterprise in Android 14 Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the enterprise APIs, features, and behavior changes introduced in Android 14 (API level 34).

**Note:** Members of our [Enterprise Mobility Management (EMM) partner community](https://www.androidenterprise.dev/) can find more information about EMM-impacting changes in Android 14 in the corresponding [knowledge article](https://emm.androidenterprise.dev/s/article/EMM-impacting-changes-in-Android-14) on the EMM community site.

## Contacts

Android 14 (API level 34) adds the following two fields:

  * [`ContactsContract.Contacts#ENTERPRISE_CONTENT_URI`](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#ENTERPRISE_CONTENT_URI)
  * [`ContactsContract.CommonDataKinds.Phone#ENTERPRISE_CONTENT_URI`](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Phone#ENTERPRISE_CONTENT_URI)



Together, these fields allow personal apps with the [`READ_CONTACTS`](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS) permission to list all work profile contacts and phone numbers as long as the cross-profile contacts policy in `DevicePolicyManager` allows it.

### Cross-profile access to contacts

The policy can be set and queried using the following methods in `DevicePolicyManager`, which specify which packages are allowed to access work contacts from the personal profile:

  * [`setManagedProfileContactsAccessPolicy()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setManagedProfileContactsAccessPolicy\(android.app.admin.PackagePolicy\))
  * [`getManagedProfileContactsAccessPolicy()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getManagedProfileContactsAccessPolicy\(\))



These methods are backward compatible and should be used instead of the following methods that are now deprecated:

  * [`setCrossProfileContactsSearchDisabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setCrossProfileContactsSearchDisabled\(android.content.ComponentName,%20boolean\))
  * [`getCrossProfileContactsSearchDisabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getCrossProfileContactsSearchDisabled\(android.content.ComponentName\))



### Cross-profile caller ID searches

Similarly, Android 14 (API level 34) adds the following methods for cross-profile caller ID searches:

  * [`setManagedProfileCallerIdAccessPolicy()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setManagedProfileCallerIdAccessPolicy\(android.app.admin.PackagePolicy\))
  * [`getManagedProfileCallerIdAccessPolicy()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getManagedProfileCallerIdAccessPolicy\(\))



These methods are backward compatible and should be used instead of the following methods that are now deprecated:

  * [`getCrossProfileCallerIdDisabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getCrossProfileCallerIdDisabled\(android.content.ComponentName\))
  * [`setCrossProfileCallerIdDisabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setCrossProfileCallerIdDisabled\(android.content.ComponentName,%20boolean\))



## Ultra wideband

Ultra wideband (UWB) is a radio technology that can use a very low energy level for short-range, high-bandwidth communications over a large portion of the radio spectrum.

Starting in Android 14 (API level 34), a device or profile owner can disallow UWB on an organization-owned device by applying the [`DISALLOW_ULTRA_WIDEBAND_RADIO`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_ULTRA_WIDEBAND_RADIO) user restriction with [`DevicePolicyManager.addUserRestriction()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#addUserRestriction\(android.content.ComponentName,%20java.lang.String\)).

## Deprecations

Android 14 includes the following notable API deprecations:

  * [`DevicePolicyManager#setCrossProfileCalendarPackages`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setCrossProfileCalendarPackages\(android.content.ComponentName,%20java.util.Set%3Cjava.lang.String%3E\)) and [`DevicePolicyManager#getCrossProfileCalendarPackages`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getCrossProfileCalendarPackages\(android.content.ComponentName\)) are deprecated.

Calendar apps should migrate to [connected apps](https://developers.google.com/android/work/connected-apps) and device policy controllers (DPCs) should use [`DevicePolicyManager#setCrossProfilePackages`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setCrossProfilePackages\(android.content.ComponentName,%20java.util.Set%3Cjava.lang.String%3E\)) instead.

  * The following methods are deprecated:

    * [`DevicePolicyManager#setCrossProfileContactsSearchDisabled`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setCrossProfileContactsSearchDisabled\(android.content.ComponentName,%20boolean\))
    * [`DevicePolicyManager#getCrossProfileContactsSearchDisabled`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getCrossProfileContactsSearchDisabled\(android.content.ComponentName\))
    * [`DevicePolicyManager#setCrossProfileCallerIdDisabled`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setCrossProfileCallerIdDisabled\(android.content.ComponentName,%20boolean\))
    * [`DevicePolicyManager#getCrossProfileCallerIdDisabled`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getCrossProfileCallerIdDisabled\(android.content.ComponentName\))

DPCs should use the alternative methods outlined in the preceding Contacts section.




Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
