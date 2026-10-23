---
url: https://developer.android.com/training/cars/apps/library/car-microphone/
title: Record from the car microphone \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:08.233122+00:00
---

# Record from the car microphone  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/library/car-microphone/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Record from the car microphone Stay organized with collections  Save and categorize content based on your preferences. 

You can use your car's [`CarAppService`](https://developer.android.com/reference/androidx/car/app/CarAppService) and [`CarAudioRecord`](https://developer.android.com/reference/androidx/car/app/media/CarAudioRecord) API to grant your app access to the user's car microphone. Users must grant permission to your app to access the car microphone. Your app can record and process user input in your app.

## Declare permission to record

Before recording any audio, you must first declare the permission to record in your `AndroidManifest.xml` and request that the user grant it.
    
    
    <manifest ...>
       ...
       <uses-permission android:name="android.permission.RECORD_AUDIO" />
       ...
    </manifest>
    

You must request the permission to record at runtime. To learn more about how to request permissions in your car, see [Request permissions](https://developer.android.com/training/cars/apps/library/request-permissions).

## Record audio

After the user gives permission to record, you can record the audio and process the recording.
    
    
    val carAudioRecord = CarAudioRecord.create(carContext)
    carAudioRecord.startRecording()
    
    val data = ByteArray(CarAudioRecord.AUDIO_CONTENT_BUFFER_SIZE)
    while (carAudioRecord.read(data, 0, CarAudioRecord.AUDIO_CONTENT_BUFFER_SIZE) >= 0) {
        // Use data array
        // Potentially call carAudioRecord.stopRecording() if your processing finds end of speech
    }
    carAudioRecord.stopRecording()
    
    [CarMicrophone.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/cars/src/main/java/com/example/cars/apps/library/CarMicrophone.kt#L36-L44)

## Acquire audio focus

When recording from the car microphone, you must acquire [audio focus](https://developer.android.com/reference/android/media/AudioFocusRequest#what-is-audio-focus) first. This stops any ongoing media. If you lose audio focus, stop recording. For example, to acquire audio focus:
    
    
    val carAudioRecord = CarAudioRecord.create(carContext)
    
    // Take audio focus so that user's media is not recorded
    val audioAttributes = AudioAttributes.Builder()
        .setContentType(AudioAttributes.CONTENT_TYPE_SPEECH)
        // Use the most appropriate usage type for your use case
        .setUsage(AudioAttributes.USAGE_ASSISTANCE_NAVIGATION_GUIDANCE)
        .build()
    
    val audioFocusRequest =
        AudioFocusRequest.Builder(AudioManager.AUDIOFOCUS_GAIN_TRANSIENT_EXCLUSIVE)
            .setAudioAttributes(audioAttributes)
            .setOnAudioFocusChangeListener { state: Int ->
                if (state == AudioManager.AUDIOFOCUS_LOSS) {
                    // Stop recording if audio focus is lost
                    carAudioRecord.stopRecording()
                }
            }
            .build()
    
    val audioManager = carContext.getSystemService(AudioManager::class.java)
    if (audioManager == null ||
        audioManager.requestAudioFocus(audioFocusRequest)
        != AudioManager.AUDIOFOCUS_REQUEST_GRANTED
    ) {
        // Don't record if the focus isn't granted
        return
    }
    
    carAudioRecord.startRecording()
    // Process the audio and abandon the AudioFocusRequest when done
    
    [CarMicrophone.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/cars/src/main/java/com/example/cars/apps/library/CarMicrophone.kt#L52-L82)

[ Previous arrow_back  Car Hardware APIs  ](https://developer.android.com/training/cars/apps/library/car-hardware-api)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-08 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-08 UTC."],[],[]] 
