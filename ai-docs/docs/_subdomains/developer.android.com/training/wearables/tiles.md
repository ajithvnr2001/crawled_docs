---
url: https://developer.android.com/training/wearables/tiles/
title: Tiles \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:20.745055+00:00
---

# Tiles  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/tiles/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Tiles Stay organized with collections  Save and categorize content based on your preferences. 

Tiles provide quick access to the information and actions users need to get things done. The tiles carousel is revealed by a swipe on the watch face, and additional swipes will switch between tiles. Tiles themselves cannot be scrolled.

Users can choose what tiles they want to see. There are tiles to check the weather, set a timer, track daily fitness progress, quick-start a workout, play a song, scan an upcoming meeting, and send a message to a favorite contact.

![Tiles next to each other.](https://developer.android.com/static/wear/images/tiles/m3-tiles-examples.png)**Figure 1.** : Tiles give users access to information and actions.

Instead of using [Compose](https://developer.android.com/compose) (or [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)), Tiles are defined declaratively using Jetpack's [protolayout](https://developer.android.com/jetpack/androidx/releases/wear-protolayout) and [tiles](https://developer.android.com/jetpack/androidx/releases/wear-tiles) libraries. Because Tiles are rendered in a separate, remote environment, they require different approaches to load, display, and update data within them. Their simplicity makes them straightforward to build, test, and deploy.

## Core principles

Wear OS provides tiles as a way for you to show a small amount of key information, which users can read through after they glance at a tile for a few seconds. To provide this high-quality experience for users, follow these best practices:

  * Don't overcrowd tiles with too much content. Instead, allow users to tap on tiles to learn more and take action on another surface in your app. See [Include (at least) one container](https://developer.android.com/design/ui/wear/guides/surfaces/tiles/bestpractices#include_at_least_one_container).
  * Declaratively define your tile's layout and content. The system is responsible for the final rendering.
  * Don't fetch content frequently or start long-running asynchronous work in your tile service. To perform work which may take some time to complete—such as network calls—use [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/define-work#expedited) to schedule background tasks, and cache or store the results in local storage.



## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [Show dynamic updates in tiles](https://developer.android.com/training/wearables/tiles/dynamic)
  * [Migrate to ProtoLayout namespaces](https://developer.android.com/training/wearables/tiles/migrate-to-protolayout)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-05 UTC."],[],[]] 
