---
url: https://developer.android.com/training/data-storage/shared/
title: Overview of shared storage \u00a0|\u00a0 App data and files \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:44:05.725474+00:00
---

# Overview of shared storage  |  App data and files  |  Android Developers

> Source: https://developer.android.com/training/data-storage/shared/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ App data and files ](https://developer.android.com/training/data-storage)



#  Overview of shared storage Stay organized with collections  Save and categorize content based on your preferences. 

Use shared storage for user data that can or should be accessible to other apps and saved even if the user uninstalls your app.

Android provides APIs for storing and accessing the following types of shareable data:

  * **Media content:** The system provides standard public directories for these kinds of files, so the user has a common location for all their photos, another common location for all their music and audio files, and so on. Your app can access this content using the platform's [`MediaStore`](https://developer.android.com/reference/android/provider/MediaStore) API.
  * **Documents and other files:** The system has a special directory for containing other file types, such as PDF documents and books that use the EPUB format. Your app can access these files using the platform's Storage Access Framework.
  * **Datasets:** On Android 11 (API level 30) and higher, the system caches large datasets that multiple apps might use. These datasets can support use cases like machine learning and media playback. Apps can access these shared datasets using the [`BlobStoreManager`](https://developer.android.com/reference/android/app/blob/BlobStoreManager) API.



For more information about these APIs, see the following guides:

  * [Media content](https://developer.android.com/training/data-storage/shared/media)
  * [Documents and other files](https://developer.android.com/training/data-storage/shared/documents-files)
  * [Datasets](https://developer.android.com/training/data-storage/shared/datasets)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-05 UTC."],[],[]] 
