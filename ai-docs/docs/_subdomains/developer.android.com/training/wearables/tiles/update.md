---
url: https://developer.android.com/training/wearables/tiles/update/
title: Show periodic updates in tiles \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:23.107370+00:00
---

# Show periodic updates in tiles  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/tiles/update/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Show periodic updates in tiles Stay organized with collections  Save and categorize content based on your preferences. 

Create tiles with content that changes as time passes.

## Work with timelines

A timeline consists of one or more [`TimelineEntry`](https://developer.android.com/reference/androidx/wear/protolayout/TimelineBuilders.TimelineEntry) instances, each of which contain a layout that is displayed during a specific time interval. All tiles need a timeline.

![Tile timeline including two timeline entries, each with a layout.](https://developer.android.com/static/images/training/articles/tiles_timeline.png)Diagram of tile timeline. 

### Single-entry tiles

Often a tile can be described with a single `TimelineEntry`. The layout is fixed, and only the information inside the layout changes. For example, a tile that shows your fitness progress of the day always shows the same progress layout, though you might adjust that layout to show different values. In these cases, you don't know in advance when the content might change.

See the following example of a tile with a single `TimelineEntry`:
    
    
    override fun onTileRequest(
        requestParams: RequestBuilders.TileRequest
    ): ListenableFuture<Tile?> {
        val tile =
            Tile.Builder()
                .setResourcesVersion(RESOURCES_VERSION)
                // We add a single timeline entry when our layout is fixed, and
                // we don't know in advance when its contents might change.
                .setTileTimeline(Timeline.fromLayoutElement(simpleLayout(this)))
                .build()
        return Futures.immediateFuture(tile)
    }
    
    [Tile.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/wear/src/main/java/com/example/wear/snippets/tile/Tile.kt#L118-L129)

### Timebound timeline entries

A `TimelineEntry` can optionally define a validity period, allowing a tile to change its layout at a known time without requiring the app to push a new tile.

The canonical example is an agenda tile whose timeline contains a list of upcoming events. Each upcoming event contains a validity period to indicate when to show it.

The tiles API allows for overlapping validity periods, where the screen with the shortest period of time left is the one shown. Only one event is displayed at a time.

Developers can provide a default fallback entry. For example, the agenda tile could have a tile with an infinite validity period, which is used if no other timeline entry is valid, as shown in the following code sample:
    
    
    override fun onTileRequest(
        requestParams: RequestBuilders.TileRequest
    ): ListenableFuture<Tile?> {
        val timeline = Timeline.Builder()
    
        // Add fallback "no meetings" entry
        // Use the version of TimelineEntry that's in androidx.wear.protolayout.
        timeline.addTimelineEntry(
            TimelineBuilders.TimelineEntry.Builder().setLayout(getNoMeetingsLayout()).build()
        )
    
        // Retrieve a list of scheduled meetings
        val meetings = MeetingsRepo.getMeetings()
        // Add a timeline entry for each meeting
        meetings.forEach { meeting ->
            timeline.addTimelineEntry(
                TimelineBuilders.TimelineEntry.Builder()
                    .setLayout(getMeetingLayout(meeting))
                    .setValidity(
                        // The tile should disappear when the meeting begins
                        // Use the version of TimeInterval that's in
                        // androidx.wear.protolayout.
                        TimelineBuilders.TimeInterval.Builder()
                            .setEndMillis(meeting.dateTimeMillis)
                            .build()
                    )
                    .build()
            )
        }
    
        val tile =
            Tile.Builder()
                .setResourcesVersion(RESOURCES_VERSION)
                .setTileTimeline(timeline.build())
                .build()
        return Futures.immediateFuture(tile)
    }
    
    [Tile.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/wear/src/main/java/com/example/wear/snippets/tile/Tile.kt#L162-L198)

## Refresh a tile

Information shown on a tile might expire after some time. For example, a weather tile that shows the same temperature throughout the day isn't accurate.

To deal with expiring data, set a freshness interval at the time of creating a tile, which specifies how long the tile is valid. In the example of the weather tile, you might update its content every hour, as shown in the following code sample:
    
    
    override fun onTileRequest(
        requestParams: RequestBuilders.TileRequest
    ): ListenableFuture<Tile?> =
        Futures.immediateFuture(
            Tile.Builder()
                .setResourcesVersion(RESOURCES_VERSION)
                .setFreshnessIntervalMillis(60 * 60 * 1000) // 60 minutes
                .setTileTimeline(Timeline.fromLayoutElement(getWeatherLayout()))
                .build()
        )
    
    [Tile.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/wear/src/main/java/com/example/wear/snippets/tile/Tile.kt#L206-L215)

When you set a freshness interval, the system calls [`onTileRequest()`](https://developer.android.com/reference/androidx/wear/tiles/TileService#onTileRequest\(androidx.wear.tiles.RequestBuilders.TileRequest\)) shortly after the interval finishes. If you don't set a freshness interval, the system doesn't call `onTileRequest()`.

A tile can also expire because of an external event. For example, a user might remove a meeting from their calendar, and if the tile wasn't refreshed, then the tile would still show that deleted meeting. In this case, request a refresh from any place in your application code, as shown in the following code sample:
    
    
    fun eventDeletedCallback() {
         TileService.getUpdater(context)
                 .requestUpdate(MyTileService::class.java)
    }

## Choose an update workflow

Use these best practices to determine how to configure your tile updates:

  * If the update is predictable—for example, if it's for the next event in the user's calendar—use a timeline.
  * When you fetch platform data, use data binding so that the system updates the data automatically.
  * If the update can be calculated on-device in a small amount of time—such as updating the position of an image on a sunrise tile—use [`onTileRequest()`](https://developer.android.com/reference/androidx/wear/tiles/TileService#onTileRequest\(androidx.wear.tiles.RequestBuilders.TileRequest\)).

This is particularly useful when you need to generate all images ahead of time. If you need to generate a new image at a future time, call [`setFreshnessIntervalMillis()`](https://developer.android.com/reference/androidx/wear/tiles/TileBuilders.Tile.Builder#setFreshnessIntervalMillis\(long\)).

  * If you're doing more intensive background work repeatedly, such as polling for weather data, use [`WorkManager`](https://developer.android.com/topic/libraries/architecture/workmanager), and push updates to your tile.

  * If the update is in response to an external event—such as the lights turning on, receiving an email, or updating a note—send a [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging) message to make your app active again, then push updates to the tile.

  * If the tile data sync process might be expensive, do the following:

    1. Schedule a data sync.
    2. Start a timer for 1-2 seconds.
    3. If you receive an update from a remote data source before time runs out, show the updated value from the data sync. Otherwise, show a cached local value.



## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [Minimize the effect of regular updates](https://developer.android.com/develop/connectivity/minimize-effect-regular-updates)
  * [Access location in the background](https://developer.android.com/develop/sensors-and-location/location/background)
  * [Getting started with WorkManager](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
