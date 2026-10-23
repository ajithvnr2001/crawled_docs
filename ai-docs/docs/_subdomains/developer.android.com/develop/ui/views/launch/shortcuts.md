---
url: https://developer.android.com/develop/ui/views/launch/shortcuts/
title: App shortcuts overview \u00a0|\u00a0 Jetpack Compose \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:33.362119+00:00
---

# App shortcuts overview  |  Jetpack Compose  |  Android Developers

> Source: https://developer.android.com/develop/ui/views/launch/shortcuts/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ UI ](https://developer.android.com/develop/ui)
  * [ Docs ](https://developer.android.com/develop/ui/compose/documentation)



#  App shortcuts overview Stay organized with collections  Save and categorize content based on your preferences. 

As a developer, you can define _shortcuts_ to perform specific actions in your app. You can display these shortcuts in a supported launcher or assistant and help your users quickly start common or recommended tasks within your app.

This documentation shows you how to [create](https://developer.android.com/develop/ui/compose/system/shortcuts/creating-shortcuts) and [manage](https://developer.android.com/develop/ui/compose/system/shortcuts/managing-shortcuts) app shortcuts. You can also learn some [best practices](https://developer.android.com/develop/ui/compose/system/shortcuts/best-practices) to improve your shortcuts.

## Shortcut types

![Key actions shown using app shortcuts](https://developer.android.com/static/images/guide/topics/ui/shortcuts_2023.png)**Figure 1.** Using app shortcuts, you can show key actions and instantly take users deep into your app.

Each shortcut references one or more [intents](https://developer.android.com/guide/components/intents-filters), each of which launches a specific action in your app when users select the shortcut. The types of shortcuts you create for your app depend on the app's use case. Examples of actions you can express as shortcuts include the following:

  * Composing a new email in an email app.
  * Navigating users to a particular location in a mapping app.
  * Sending messages to a user's contact in a communication app.
  * Playing the next episode of a TV show in a media app.
  * Loading the last save point in a gaming app.
  * Letting the user order a drink in a delivery app using spoken commands.

**Note:** Only main activities—activities that handle the [`Intent.ACTION_MAIN`](https://developer.android.com/reference/kotlin/android/content/Intent#ACTION_MAIN) action and the [`Intent.CATEGORY_LAUNCHER`](https://developer.android.com/reference/kotlin/android/content/Intent#CATEGORY_LAUNCHER) category—can have shortcuts. If an app has multiple main activities, define the set of shortcuts for each activity.

You can publish the following types of shortcuts for your app:

  * _Static shortcuts_ are defined in a resource file that is packaged into an APK or [app bundle](https://developer.android.com/guide/app-bundle/build).
  * _Dynamic shortcuts_ can be pushed, updated, and removed by your app only at runtime.
  * _Pinned shortcuts_ can be added to supported launchers at runtime if the user grants permission.

**Note:** Users can also create pinned shortcuts by copying your app's static and dynamic shortcuts onto the launcher.



## Display shortcuts in assistants using capabilities

_Capabilities_ in `shortcuts.xml` let you declare the types of actions users can take to launch your app and jump directly to performing a specific task. For more details, see the documentation about [adding capabilities](https://developer.android.com/develop/ui/compose/system/shortcuts/adding-capabilities).

## Shortcut limitations

Most supported launchers display up to four shortcuts at a time, including both static and dynamic shortcuts. When pushing dynamic shortcuts for display on Google's surfaces, use the [Google Shortcuts Integration Library](https://developer.android.com/develop/ui/compose/system/shortcuts/creating-shortcuts#gsi-library) to avoid being subject to the shortcut limit.

If you choose not to use the Google Shortcuts Integration Library, your app is subject to the device's limit for the number of shortcuts it supports at a time. Shortcuts published this way only appear within the Android launchers and aren't discoverable on other Google surfaces.

**Note:** The maximum number of shortcuts a device supports varies. Use the [`getMaxShortcutCountPerActivity()`](https://developer.android.com/reference/kotlin/androidx/core/content/pm/ShortcutManagerCompat#getMaxShortcutCountPerActivity\(android.content.Context\)) method to determine how many shortcuts a particular device supports.

There is no limit to the number of pinned shortcuts users can create to your app. Your app can't remove pinned shortcuts, but it can [disable](https://developer.android.com/develop/ui/compose/system/shortcuts/managing-shortcuts#disable-shortcuts) them.

**Note:** Although other apps can't access the metadata within your shortcuts, the launcher itself can access this data. Therefore, conceal sensitive user information in this metadata.

To start creating shortcuts for your app, refer to the following documentation:

  * [Create shortcuts](https://developer.android.com/develop/ui/compose/system/shortcuts/creating-shortcuts)
  * [Manage shortcuts](https://developer.android.com/develop/ui/compose/system/shortcuts/managing-shortcuts)
  * [Best practices for shortcuts](https://developer.android.com/develop/ui/compose/system/shortcuts/best-practices)



For more details about operations you can perform on shortcuts, see the [`ShortcutManager`](https://developer.android.com/reference/kotlin/android/content/pm/ShortcutManager) API reference documentation.

[ Previous arrow_back  Test predictive back  ](https://developer.android.com/develop/ui/compose/system/predictive-back-test)

[ Next Create shortcuts  arrow_forward  ](https://developer.android.com/develop/ui/compose/system/shortcuts/creating-shortcuts)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
