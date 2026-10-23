---
url: https://developer.android.com/training/cars/media/errors/
title: Handle errors \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:01.013908+00:00
---

# Handle errors  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/media/errors/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Handle errors Stay organized with collections  Save and categorize content based on your preferences. 

Android Auto and Android Automotive OS (AAOS) set the playback state to `STATE_ERROR` and provide a user-facing, localized error message. The apps can then display the message to the user.

To address an error, you provide an error message with [`setErrorMessage`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.Builder#setErrorMessage\(int,%20java.lang.CharSequence\)).

See [`PlaybackStateCompat`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat) for a list of the error codes you can use when designing the error message to indicate the nature of the error. If a user must interact with their phone to resolve an issue, include this instruction in the error message.

Error messages must be user-facing and targeted to the user's locale. For example, if content is not available in the user's locale, use [`ERROR_CODE_NOT_AVAILABLE_IN_REGION`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#ERROR_CODE_NOT_AVAILABLE_IN_REGION\(\)).

### Kotlin
    
    
    mediaSession.setPlaybackState(
        PlaybackStateCompat.Builder()
            .setState(PlaybackStateCompat.STATE_ERROR)
            .setErrorMessage(PlaybackStateCompat.ERROR_CODE_NOT_AVAILABLE_IN_REGION, getString(R.string.error_unsupported_region))
            // ...and any other setters.
            .build())
    

### Java
    
    
    mediaSession.setPlaybackState(
        new PlaybackStateCompat.Builder()
            .setState(PlaybackStateCompat.STATE_ERROR)
            .setErrorMessage(PlaybackStateCompat.ERROR_CODE_NOT_AVAILABLE_IN_REGION, getString(R.string.error_unsupported_region))
            // ...and any other setters.
            .build())
    

To learn more about error states, see [Using a media session: States and errors](https://developer.android.com/guide/topics/media-apps/working-with-a-media-session#errors).

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-14 UTC."],[],[]] 
