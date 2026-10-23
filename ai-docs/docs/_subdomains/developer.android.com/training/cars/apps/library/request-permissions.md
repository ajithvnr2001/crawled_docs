---
url: https://developer.android.com/training/cars/apps/library/request-permissions/
title: Request permissions \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:07.146909+00:00
---

# Request permissions  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/library/request-permissions/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Request permissions Stay organized with collections  Save and categorize content based on your preferences. 

If your app needs access to restricted data or actions—for example, location—the [standard rules of Android permissions](https://developer.android.com/guide/topics/permissions/overview) apply. To request a permission, you can use the [`CarContext.requestPermissions()`](https://developer.android.com/reference/androidx/car/app/CarContext#requestPermissions\(java.util.List%3Cjava.lang.String%3E,%20java.util.concurrent.Executor,%20androidx.car.app.OnRequestPermissionsListener\)) method.

**Warning:** Update to [`androidx.car.app:1.7.0-rc01`](https://developer.android.com/jetpack/androidx/releases/car-app#1.7.0-rc01) or higher to ensure permission dialogs appear on Android 14 and higher (phone) and to prevent crashes on Android Automotive OS 15 and higher.

The benefit of using `CarContext.requestPermissions()`, as opposed to using [standard Android APIs](https://developer.android.com/training/permissions/requesting#request-permission), is that you needn't launch your own `Activity` to create the permissions dialog. Moreover, you can use the same code on both Android Auto and Android Automotive OS, instead of creating platform-dependent flows.

## Style the permissions dialog on Android Auto

On Android Auto, the permissions dialog for the user appears on the phone. By default, there's no background to the dialog.

To set a custom background:

  1. To declare a [car app theme](https://developer.android.com/training/cars/apps/library/set-up-project#custom-theme) in your `AndroidManifest.xml` file and set the `carPermissionActivityLayout` attribute for your car app theme:
         
         <meta-data
            android:name="androidx.car.app.theme"
            android:resource="@style/<var>MyCarAppTheme</var> />
         

  2. To set the `carPermissionActivityLayout` attribute for your car app theme:
         
         <resources>
          <style name="<var>MyCarAppTheme</var>">
            <item name="carPermissionActivityLayout">@layout/<var>my_custom_background</var></item>
          </style>
         </resources>
         




[ Next Connection API  arrow_forward  ](https://developer.android.com/training/cars/apps/library/connection-api)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
