---
url: https://developer.android.com/tools/bmgr/
title: bmgr \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:45:37.554028+00:00
---

# bmgr  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/tools/bmgr/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ SDK tools guides ](https://developer.android.com/tools)



#  bmgr Stay organized with collections  Save and categorize content based on your preferences. 

`bmgr` is a shell tool you can use to interact with the Backup Manager on Android devices version 2.2 (API Level 8) or higher. The tool provides commands to initiate backup and restore operations so that you don't need to repeatedly wipe data or take similar intrusive steps in order to test your application's backup functionality. The `bmgr` tool supports both [Auto Backup](https://developer.android.com/guide/topics/data/autobackup) and [Key/Value Backup](https://developer.android.com/guide/topics/data/keyvaluebackup).

Note: `bmgr restore` does not work for [encrypted backups](https://developer.android.com/guide/topics/data/autobackup#define-device-conditions). 

You run `bmgr` commands on a device via [adb shell](https://developer.android.com/studio/command-line/adb) and then monitor the output of the commands with [logcat](https://developer.android.com/studio/command-line/logcat). For a list and description of available commands, run the `bmgr` tool with no arguments. For information on triggering backup and restore operations, see [Testing Backup and Restore](https://developer.android.com/guide/topics/data/testingbackup). 

For information about adding support for backup in your application, read [Data Backup](https://developer.android.com/guide/topics/data/backup)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2023-04-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2023-04-12 UTC."],[],[]] 
