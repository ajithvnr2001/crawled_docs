---
url: https://developer.android.com/training/appbar/
title: Add the app bar \u00a0|\u00a0 Views \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:48.775309+00:00
---

# Add the app bar  |  Views  |  Android Developers

> Source: https://developer.android.com/training/appbar/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ UI ](https://developer.android.com/develop/ui)
  * [ Views ](https://developer.android.com/develop/ui/views/layout/declaring-layout)



#  Add the app bar Stay organized with collections  Save and categorize content based on your preferences. 

Try the Compose way 

Jetpack Compose is the recommended UI toolkit for Android. Learn how to add components in Compose. 

[ App Bar → ](https://developer.android.com/develop/ui/compose/components/app-bars)

![](https://developer.android.com/static/images/android-compose-ui-logo.png)

The _app bar_ , also known as the _action bar_ , is one of the most important design elements in your app's activities, because it provides a visual structure and interactive elements that are familiar to users. Using the app bar makes your app consistent with other Android apps, letting users quickly understand how to operate your app and have a great experience.

**Note:** With the release of Android 9.0 (API level 28), there is a version of the Support Library called [AndroidX](https://developer.android.com/jetpack/androidx) that is part of [Jetpack](https://developer.android.com/jetpack). The AndroidX library contains the existing Support Library and includes Jetpack components.   
  
You can continue to use the Support Library. Historical artifacts—those versioned 27 and earlier, and packaged as `android.support.*`—remain available on Google Maven. However, all newer library development occurs in the AndroidX library.   
  
We recommend using the AndroidX libraries in all new projects. Consider [migrating](https://developer.android.com/jetpack/androidx/migrate) existing projects to AndroidX as well. 

The key functions of the app bar are as follows:

  * Dedicated space for giving your app an identity and indicating the user's location in the app.
  * Predictable access to important actions, such as search.
  * Support for navigation and view switching, using tabs or menus.

![An image showing a green app bar, with hamburger menu, and three action icons](https://developer.android.com/static/images/training/appbar/appbar_sheets_2x.png)**Figure 1.** The app bar from the Google Sheets app. 

This documentation section describes how to use the AndroidX `[Toolbar](https://developer.android.com/reference/androidx/appcompat/widget/Toolbar)` widget as an app bar. There are other ways to implement an app bar—for example, some themes set up an `[ActionBar](https://developer.android.com/reference/android/app/ActionBar)` as an app bar by default—but using the AppCompat `Toolbar` makes it easier to set up an app bar that works on the widest range of devices. It also gives you room to customize your app bar later in your app's development.

## Topics

**[Set up the app bar](https://developer.android.com/develop/ui/views/components/appbar/setting-up)**
     Learn how to add a `Toolbar` widget to your activity and set it as the activity's app bar. 
**[Add and handle actions](https://developer.android.com/develop/ui/views/components/appbar/actions)**
     Learn how to add actions to the app bar and its overflow menu, and how to respond when users choose those actions. 
**[Add an Up action](https://developer.android.com/develop/ui/views/components/appbar/up-action)**
     Learn how to add an _Up_ button to your app bar so users can navigate back to the app's home screen. 
**[Use action views and action providers](https://developer.android.com/develop/ui/views/components/appbar/action-views)**
     Learn how to use these widgets to provide advanced functionality in your app bar. 

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-28 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-28 UTC."],[],[]] 
