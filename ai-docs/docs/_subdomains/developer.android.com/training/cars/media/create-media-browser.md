---
url: https://developer.android.com/training/cars/media/create-media-browser/
title: Media browser service overview \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:45:56.721176+00:00
---

# Media browser service overview  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/media/create-media-browser/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Media browser service overview Stay organized with collections  Save and categorize content based on your preferences. 

You create a media browser service by extending the supported [`MediaBrowserServiceCompat`](https://developer.android.com/reference/android/support/v4/media/MediaBrowserCompat) or [`MediaLibraryService`](https://developer.android.com/media/media3/session/serve-content) classes. Android Auto and Android Automotive OS (AAOS) can then use your service to:

  * Browse your app's content hierarchy to present a menu to the user.

  * Get the token for your app's [`MediaSessionCompat`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat) object to control audio playback.




You can also use your media browser service to let other clients access media content from your app. These media clients might be other apps on a user's phone, or they can be other remote clients.

## Contents

These pages detail how to work with the media browser:

  * [Media browser lifecycle](https://developer.android.com/training/cars/media/create-media-browser/lifecycle)
  * [Build content hierarchy](https://developer.android.com/training/cars/media/create-media-browser/content-hierarchy)
  * [Apply content styles](https://developer.android.com/training/cars/media/create-media-browser/content-styles)
  * [Display media artwork](https://developer.android.com/training/cars/media/create-media-browser/media-artwork)
  * [Display browsable search results](https://developer.android.com/training/cars/media/create-media-browser/browsable-search)
  * [Implement custom browse actions](https://developer.android.com/training/cars/media/create-media-browser/custom-browse-actions)



## Design guidelines

To learn more about design guidelines, see:

  * [Plan navigation tabs](https://developer.android.com/design/ui/cars/guides/app-types/plan-navigation-tabs)
  * [Plan browsing views](https://developer.android.com/design/ui/cars/guides/app-types/plan-browsing-views)



[ Next Media browser lifecycle  arrow_forward  ](https://developer.android.com/training/cars/media/create-media-browser/lifecycle)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
