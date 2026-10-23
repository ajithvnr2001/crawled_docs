---
url: https://developer.android.com/develop/background-work/services/fgs/
title: Foreground services overview \u00a0|\u00a0 Background work \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:52.961954+00:00
---

# Foreground services overview  |  Background work  |  Android Developers

> Source: https://developer.android.com/develop/background-work/services/fgs/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ Background work ](https://developer.android.com/develop/background-work)
  * [ Guides ](https://developer.android.com/develop/background-work/background-tasks)



#  Foreground services overview Stay organized with collections  Save and categorize content based on your preferences. 

Foreground services let you asynchronously perform operations that are noticeable to the user. Foreground services show a [status bar notification](https://developer.android.com/develop/ui/views/notifications), to make users aware that your app is performing a task in the foreground and is consuming system resources.

Examples of apps that use foreground services include the following:

  * A music player app that plays music in a foreground service. The notification might show the current song being played.
  * A fitness app that records a user's run in a foreground service, after receiving permission from the user. The notification might show the distance that the user has traveled during the current fitness session.



Only use a foreground service when your app needs to perform a task that is noticeable by the user, even when they're not directly interacting with the app. If the action is of low enough importance that you want to use a minimum-priority notification, you probably want to use a different [background work option](https://developer.android.com/develop/background-work/background-tasks).

This guide explains the following areas:

  * [Declare foreground services and request permissions](https://developer.android.com/develop/background-work/services/fgs/declare)
  * [Launch a foreground service](https://developer.android.com/develop/background-work/services/fgs/launch)
  * [Stop a foreground service](https://developer.android.com/develop/background-work/services/fgs/stop-fgs)
  * [Handle when a user stops an app that has a foreground service](https://developer.android.com/develop/background-work/services/fgs/handle-user-stopping)
  * [Restrictions on starting a foreground service from the background](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start)
  * [Foreground service types](https://developer.android.com/develop/background-work/services/fgs/service-types)
  * [Foreground service timeout behavior](https://developer.android.com/develop/background-work/services/fgs/timeout)
  * [Foreground service troubleshooting](https://developer.android.com/develop/background-work/services/fgs/troubleshooting)
  * [Changes to foreground services](https://developer.android.com/develop/background-work/services/fgs/changes)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
