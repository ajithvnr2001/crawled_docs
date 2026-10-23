---
url: https://developer.android.com/guide/components/activities/parcelables-and-bundles/
title: Parcelables and bundles \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:32.816485+00:00
---

# Parcelables and bundles  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/components/activities/parcelables-and-bundles/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  Parcelables and bundles Stay organized with collections  Save and categorize content based on your preferences. 

`[Parcelable](https://developer.android.com/reference/kotlin/android/os/Parcelable)` and `[Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle)` objects are intended to be used across process boundaries such as with IPC/Binder transactions, between activities with intents, and to store transient state across configuration changes. This page provides recommendations and best practices for using `[Parcelable](https://developer.android.com/reference/kotlin/android/os/Parcelable)` and `[Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle)` objects. 

**Note:** `[Parcel](https://developer.android.com/reference/kotlin/android/os/Parcel)` is not a general-purpose serialization mechanism, and you should never store any `[Parcel](https://developer.android.com/reference/kotlin/android/os/Parcel)` data on disk or send it over the network. 

## Sending data between activities

When an app creates an `[Intent](https://developer.android.com/reference/kotlin/android/content/Intent)` object to use in `[startActivity()](https://developer.android.com/reference/kotlin/android/app/Activity#startactivity)` in starting a new Activity, the app can pass in parameters using the `[putExtra()](https://developer.android.com/reference/kotlin/android/content/Intent#putextra_18)` method. 

The following code snippet shows an example of how to perform this operation.
    
    
    val intent = Intent(this, MyActivity::class.java).apply {
        putExtra("media_id", "a1b2c3")
        // ...
    }
    startActivity(intent)

The OS parcels the underlying `[Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle)` of the intent. Then, the OS creates the new activity, un-parcels the data, and passes the intent to the new activity. 

We recommend that you use the `[Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle)` class to set primitives known to the OS on `[Intent](https://developer.android.com/reference/kotlin/android/content/Intent)` objects. The `[Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle)` class is highly optimized for marshalling and unmarshalling using parcels. 

In some cases, you may need to pass complex objects across activities or preserve them in UI state. In such cases, the custom class should implement Parcelable. For modern Kotlin and Jetpack Compose apps, the recommended approach is to use the `[@Parcelize](https://developer.android.com/kotlin/parcelize)` annotation. This automatically generates the serialization logic needed to safely handle your data when using Bundles. This is the same approach used to handle your data when using `[rememberSaveable](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/rememberSaveable.composable#rememberSaveable\(kotlin.Array,kotlin.Function0\))`. For more information about using `[@Parcelize](https://developer.android.com/kotlin/parcelize)`, see [Parcelable implementation generator](https://developer.android.com/kotlin/parcelize). 

When sending data via an intent, you should be careful to limit the data size to a few KB. Sending too much data can cause the system to throw a `[TransactionTooLargeException](https://developer.android.com/reference/kotlin/android/os/TransactionTooLargeException)` exception. 

## Sending data between processes

Sending data between processes is similar to doing so between activities. However, when sending between processes, we recommend that you do not use custom parcelables. If you send a custom `[Parcelable](https://developer.android.com/reference/kotlin/android/os/Parcelable)` object from one app to another, you need to be certain that the exact same version of the custom class is present on both the sending and receiving apps. Typically this could be a common library used across both apps. An error can occur if your app tries to send a custom parcelable to the system, because the system cannot unmarshal a class that it has no knowledge of. 

For example, an app might set an alarm using the `[AlarmManager](https://developer.android.com/reference/kotlin/android/app/AlarmManager)` class, and use a custom `[Parcelable](https://developer.android.com/reference/kotlin/android/os/Parcelable)` on the alarm intent. When the alarm goes off, the system modifies the intent's `[Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle)` of extras to add a repeat count. This modification can result in the system's stripping the custom `[Parcelable](https://developer.android.com/reference/kotlin/android/os/Parcelable)` from the extras. This stripping, in turn, can result in the app's crashing when it receives the modified alarm intent, because the app expects to receive extra data that is no longer there. 

The Binder transaction buffer has a limited fixed size, currently 1MB, which is shared by all transactions in progress for the process. Since this limit is at the process level rather than at the per activity level, these transactions include all binder transactions in the app such as `startActivity`, `rememberSaveable` (which uses `onSaveInstanceState` under the hood), and any interaction with the system. When the size limit is exceeded, a `TransactionTooLargeException` is thrown. 

For the specific case of saving state with `rememberSaveable`, the amount of data should be kept small because the system process needs to hold on to the provided data for as long as the user can ever navigate back to that activity (even if the activity's process is killed). We recommend that you keep saved state to less than 50KB of data. 

**Note:** In Android 7.0 (API level 24) and higher, the system throws a `TransactionTooLargeException` as a runtime exception. In lower versions of Android, the system only shows a warning in logcat. 

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
