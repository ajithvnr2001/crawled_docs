---
url: https://developer.android.com/training/cars/media/distraction-safeguards/
title: Implement distraction safeguards \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:00.029593+00:00
---

# Implement distraction safeguards  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/media/distraction-safeguards/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Implement distraction safeguards Stay organized with collections  Save and categorize content based on your preferences. 

Because a user's phone is connected to a car's speakers when using Android Auto, you must take additional precautions to prevent driver distraction.

When you develop Android Auto media apps, implement specific safeguards to minimize driver distraction. These safeguards include:

  * Preventing your app from automatically playing audio through car speakers, even for user-scheduled alarms.

  * Managing how Android Auto displays notifications when your app switches between music and ads.




To achieve this, use the `CarConnection` API to detect if a phone projects to a car screen. If it does, disable alarms or provide an on-phone UI to manage them. For ads, set the `METADATA_KEY_IS_ADVERTISEMENT` metadata key to suppress distracting notifications.

## Suppress alarms in the car

Android Auto media apps must not start playing audio through the car speakers unless the user starts playback by, for example, pressing a **Play** button. Even a user-scheduled alarm from your media app must not start playing music through the car speakers.

To fulfill this requirement, your app can use [`CarConnection`](https://developer.android.com/reference/androidx/car/app/connection/CarConnection) as a signal before playing any audio. Your app can check if the phone is projecting to a car screen. Observe the `LiveData` for the [connection type](https://developer.android.com/reference/androidx/car/app/connection/CarConnection#getType\(\)). Confirm the value is equal to [`CONNECTION_TYPE_PROJECTION`](https://developer.android.com/reference/androidx/car/app/connection/CarConnection#CONNECTION_TYPE_PROJECTION\(\)).

If the user's phone is projecting, media apps that support alarms must perform one of these actions:

  * Disable the alarm.

  * Re-play the alarm [`STREAM_ALARM`](https://developer.android.com/reference/android/media/AudioManager#STREAM_ALARM) and provide a UI on the phone screen to disable the alarm.




## Handle media advertisements

By default, Android Auto displays a notification when the media metadata changes during an audio playback session. When a media app switches from playing music to running an advertisement, displaying a notification distracts the user. To prevent Android Auto from displaying a notification, set the media metadata key [`METADATA_KEY_IS_ADVERTISEMENT`](https://github.com/androidx/media/blob/release/libraries/session/src/main/java/androidx/media3/session/legacy/MediaConstants.java) to `METADATA_VALUE_ATTRIBUTE_PRESENT`:

### Kotlin
    
    
    import androidx.media.utils.MediaConstants
    
    override fun onPlayFromMediaId(mediaId: String, extras: Bundle?) {
        MediaMetadataCompat.Builder().apply {
            if (isAd(mediaId)) {
                putLong(
                    MediaConstants.METADATA_KEY_IS_ADVERTISEMENT,
                    MediaConstants.METADATA_VALUE_ATTRIBUTE_PRESENT)
            }
            // ...add any other properties you normally would.
            mediaSession.setMetadata(build())
        }
    }
    

### Java
    
    
    import androidx.media.utils.MediaConstants;
    
    @Override
    public void onPlayFromMediaId(String mediaId, Bundle extras) {
        MediaMetadataCompat.Builder builder = new MediaMetadataCompat.Builder();
        if (isAd(mediaId)) {
            builder.putLong(
                MediaConstants.METADATA_KEY_IS_ADVERTISEMENT,
                MediaConstants.METADATA_VALUE_ATTRIBUTE_PRESENT);
        }
        // ...add any other properties you normally would.
        mediaSession.setMetadata(builder.build());
    }
    

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
